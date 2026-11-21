"""AstraCloud AI simulated compliance monitor. No live services or real audit evidence."""
import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent

def load_csv(filename):
    with (BASE / 'data' / filename).open(newline='', encoding='utf-8-sig') as file:
        return list(csv.DictReader(file))

def as_date(value):
    value = str(value or '').strip()
    if not value:
        return None
    try:
        return date(1899, 12, 30) + timedelta(days=float(value))
    except ValueError:
        return date.fromisoformat(value[:10])

def evidence_status(record, as_of):
    decision = (record.get('Review Decision') or '').strip().lower()
    due = as_date(record.get('Due Date'))
    submitted = as_date(record.get('Submitted Date'))
    if decision in ('rejected', 'exception', 'failed'):
        return 'Exception'
    if decision == 'accepted' and submitted and submitted <= as_of:
        return 'Pass'
    if due and due < as_of:
        return 'Overdue'
    if submitted and submitted <= as_of:
        return 'Pending Review'
    return 'Pending Evidence'

def access_status(record, as_of):
    reviewed = as_date(record.get('Reviewed On'))
    due = as_date(record.get('Review Due'))
    removal_due = as_date(record.get('Removal Due'))
    closed = as_date(record.get('Closed On'))
    decision = (record.get('Decision') or '').strip().lower()
    if decision == 'remove':
        if closed and closed <= as_of:
            return 'Closed' if not removal_due or closed <= removal_due else 'Closed Late'
        return 'Removal Overdue' if removal_due and removal_due < as_of else 'Removal Pending'
    if reviewed and reviewed <= as_of:
        return 'Approved' if decision == 'retain' else 'Reviewed'
    return 'Review Overdue' if due and due < as_of else 'Review Pending'

def run(as_of):
    controls, evidence, access = (load_csv(x) for x in ('controls.csv', 'evidence.csv', 'access_reviews.csv'))
    alerts = []
    statuses = Counter()
    by_control = defaultdict(list)
    for record in evidence:
        status = evidence_status(record, as_of)
        statuses[status] += 1
        by_control[record['Control ID']].append(status)
        if status in ('Overdue', 'Exception'):
            alerts.append({'type': 'Evidence', 'id': record['Evidence ID'], 'control': record['Control ID'], 'status': status, 'owner': record['Control Owner'], 'due': str(as_date(record['Due Date']) or '')})
    access_counts = Counter()
    for record in access:
        status = access_status(record, as_of)
        access_counts[status] += 1
        if status in ('Removal Overdue', 'Review Overdue', 'Closed Late'):
            alerts.append({'type': 'Access Review', 'id': record['Review ID'], 'control': 'AC-02', 'status': status, 'owner': record['Reviewer'], 'due': str(as_date(record['Removal Due'] if status != 'Review Overdue' else record['Review Due']) or '')})
    control_health = {}
    for control in controls:
        id_ = control['Control ID']
        results = by_control[id_]
        if not results:
            health = 'No Evidence'
        elif 'Exception' in results:
            health = 'Exception'
        elif 'Overdue' in results:
            health = 'Overdue'
        elif all(s == 'Pass' for s in results):
            health = 'Pass'
        else:
            health = 'Pending'
        if id_ == 'AC-02' and any(s in ('Removal Overdue', 'Review Overdue', 'Closed Late') for s in access_counts):
            health = 'Attention Required'
        control_health[id_] = health
    total = len(evidence)
    result = {'notice': 'SIMULATED DATA — NOT A SOC 2 AUDIT OR LIVE VANTA/DRATA INTEGRATION', 'as_of': str(as_of), 'controls': len(controls), 'evidence_requests': total, 'accepted_evidence': statuses['Pass'], 'evidence_acceptance_pct': round(100 * statuses['Pass'] / total, 1) if total else 0, 'evidence_statuses': dict(statuses), 'access_review_statuses': dict(access_counts), 'control_health': control_health, 'alerts': alerts}
    out = BASE / 'output'
    out.mkdir(exist_ok=True)
    (out / 'compliance_results.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    with (out / 'compliance_alerts.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['type', 'id', 'control', 'status', 'owner', 'due'])
        writer.writeheader()
        writer.writerows(alerts)
    lines = ['# AstraCloud AI — Simulated Compliance Monitoring Report', '', f'**As-of date:** {as_of}', '', '**SIMULATED TRAINING DATA. Not an official SOC 2 audit, certification, or live Vanta/Drata integration.**', '', '## Executive summary', '', f'- Controls in scope: **{len(controls)}**', f'- Evidence requests: **{total}**', f'- Accepted evidence: **{statuses["Pass"]} ({result["evidence_acceptance_pct"]}%)**', f'- Overdue evidence: **{statuses["Overdue"]}**', f'- Evidence exceptions: **{statuses["Exception"]}**', f'- Alerts requiring follow-up: **{len(alerts)}**', '', '## Control health', '', '| Control | Status |', '|---|---|']
    lines.extend(f'| {k} | {v} |' for k, v in control_health.items())
    lines += ['', '## Action queue', '', '| Record | Control | Issue | Owner | Due |', '|---|---|---|---|---|']
    lines.extend(f'| {a["id"]} | {a["control"]} | {a["status"]} | {a["owner"]} | {a["due"]} |' for a in alerts)
    lines += ['', '## Analyst interpretation', '', 'Evidence acceptance is not the same as control effectiveness or SOC 2 compliance. Review source records, verify exceptions, and obtain owner sign-off before making conclusions.', '', 'All evidence references are fictional placeholders.']
    (out / 'management_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'As of {as_of}: {statuses["Pass"]}/{total} accepted; {statuses["Overdue"]} overdue; {len(alerts)} alerts.')
    print(f'Files written to {out}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulated SOC 2 continuous compliance monitoring')
    parser.add_argument('--as-of', default='2026-07-31', help='Assessment date, YYYY-MM-DD')
    args = parser.parse_args()
    run(date.fromisoformat(args.as_of))
