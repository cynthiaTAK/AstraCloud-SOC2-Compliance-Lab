# AstraCloud AI — Phase 5 Simulated SOC 2 Readiness Assessment

**SIMULATED TRAINING CASE — NOT AN OFFICIAL SOC 2 AUDIT OR ATTESTATION.**  
Assessment as-of: **2026-07-31**. Historical review window: **2026-01-01 through 2026-06-30**. July follow-up deadlines are post-period evidence-collection dates.

## Executive summary

- 12 controls reviewed at the **record/inventory level**, not independently audited.
- 24 evidence requests; 17 marked accepted (70.8%); 6 overdue; 1 evidence exception.
- 8 access-review records; two unresolved access-review alerts (one overdue removal and one overdue review).
- 9 actionable alerts overall. **These are alert records, not nine independently confirmed control failures.**
- No formal Test of Design or Operating Effectiveness conclusion can be reached from the tracking exports alone; actual policies, screenshots, exports, approvals and tickets are not attached.

## Priority observations

1. **AC-03 — Employee offboarding:** EV-006 has an evidence exception. Investigate whether access was revoked on time; document actual timestamps and management response.
2. **AC-02 — Quarterly access reviews:** EV-004 evidence overdue; AR-004 removal overdue; AR-005 review overdue. Confirm privileged access removal and completion of Q2 review.
3. **CL-01 / CL-02 — Cloud configuration and vulnerability remediation:** EV-008 and EV-010 overdue. Collect AWS baseline review and vulnerability remediation proof.
4. **IR-01 / VR-01 / BC-01:** Incident response, vendor review and restoration-test evidence requests overdue (EV-016, EV-020, EV-024).

## Audit testing approach

- **ToD:** Inspect each control's written procedure, owner, trigger, frequency, escalation path, and documented approval; conclude only when actual procedure artifacts are supplied.
- **OE:** Select period-appropriate samples and inspect dated execution evidence; reconcile exceptions to closure records. Missing evidence is a limitation, not automatically a control failure.
- **Period boundary:** Evidence due in July may relate to June operations; distinguish a late submission from failure to execute the control during the six-month period.

## Proposed management actions

- Assign owners to all nine alerts and request missing evidence within five business days (fictional exercise target).
- Prioritize the offboarding exception and privileged-access removal; seek immediate confirmation of account status.
- Re-test affected controls after corrective action and retain dated evidence.
- Present unresolved exceptions and evidence limitations to the fictional Head of Information Security.

## Limitations

All accounts, vendors, evidence paths and outcomes are fictional. Evidence links in the Phase 4 CSV are placeholders, not actual inspected documents. No live AWS, GitHub, Vanta, Drata, or identity-system integration was used. Framework mappings are illustrative.
