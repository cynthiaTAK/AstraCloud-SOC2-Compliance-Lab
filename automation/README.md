# AstraCloud AI — Phase 4: Python Compliance Automation

**SIMULATED portfolio exercise.** No live Vanta, Drata, AWS, or customer systems are connected. No official SOC 2 audit has been performed.

## Contents

- `data/controls.csv` — 12 controls exported from the Phase 3 workbook
- `data/evidence.csv` — 24 fictional evidence requests
- `data/access_reviews.csv` — 8 fictional access review records
- `compliance_monitor.py` — evidence and access monitoring rules
- `output/compliance_results.json` — machine-readable monitoring results
- `output/compliance_alerts.csv` — actionable issue queue
- `output/management_report.md` — management-ready report

## Run

Requires Python 3.9+; no third-party packages.

```bash
python compliance_monitor.py --as-of 2026-07-31
```

Try another assessment date:

```bash
python compliance_monitor.py --as-of 2026-06-30
```

## Hands-on exercise

1. Open `data/evidence.csv` and locate an overdue item.
2. Set `Submitted Date` to an Excel serial date or `YYYY-MM-DD` and `Review Decision` to `Accepted`.
3. Rerun the script and inspect `output/compliance_alerts.csv` and `output/management_report.md`.
4. Restore the sample file if you want to reproduce the baseline results.

## Logic and limitations

- Evidence is **Pass** when accepted and submitted by the assessment date.
- Rejected, exception, or failed evidence is **Exception**.
- Unaccepted evidence past its due date is **Overdue**.
- Access removal actions have separate pending, overdue, and closed states.
- Results are deterministic based on the CSV inputs and `--as-of` date.
- Acceptance of evidence does **not** establish control operating effectiveness or SOC 2 compliance.
- Dates exported from Excel are interpreted using the standard 1900 date system; ISO dates also work.
- This is a Vanta/Drata-inspired *simulation*, not a claim of platform integration.
