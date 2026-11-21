# AstraCloud AI — Executive SOC 2 Readiness Report

> **SIMULATED TRAINING CASE — NOT A SOC 2 AUDIT, ATTESTATION, OR CERTIFICATION.**

**Monitoring snapshot:** July 31, 2026  
**Historical control period:** January 1–June 30, 2026  
**Basis:** Phase 3 workbook, Phase 4 deterministic monitoring outputs, Phase 5 preliminary workpapers. No source evidence documents were independently examined.

## Executive assessment

AstraCloud AI's fictional security-control inventory covers **12 controls** across access management, cloud security, change management, incident response, vendor oversight, policy governance, and resilience. The tracking export includes **24 evidence requests**, of which **17 were marked accepted (70.8%)**, **6 overdue**, and **1 exception**. Eight access-review records yielded **two outstanding access-review alerts**: an overdue removal and an overdue review. The monitoring queue contains **9 alerts** in total. These nine alerts are **not nine independently substantiated control failures**.

The snapshot does not support a formal conclusion about control design or operating effectiveness. Accepted records are tracker decisions, not verified audit evidence. The simulated historical period ends June 30, whereas several evidence collection deadlines fall in July; delayed submission alone does not prove that a control failed during the historical period.

## Prioritized observations and actions

| Priority | Control / records | Observation | Recommended management action |
|---|---|---|---|
| High (illustrative) | AC-03 / EV-006 | Offboarding evidence exception | Obtain dated disablement records and HR trigger; establish whether access was revoked within policy; record root cause and remediation |
| High (investigate promptly) | AC-02 / AR-004, AR-005, EV-004 | Privileged access removal and review overdue; supporting evidence overdue | Confirm current account state; obtain Q2 signed review and removal ticket; reconcile timelines and retest |
| Medium | CL-01 / EV-008 | AWS configuration evidence overdue | Collect configuration baseline, exception approvals, and dated review records |
| Medium | CL-02 / EV-010 | Vulnerability remediation evidence overdue | Obtain scan results, tickets, SLA evidence, and rescans |
| Medium | IR-01 / EV-016 | Incident response evidence overdue | Collect approved plan and dated tabletop/exercise records |
| Medium | VR-01 / EV-020 | Vendor review evidence overdue | Obtain due diligence package, risk acceptance and reassessment records |
| Medium | BC-01 / EV-024 | Backup restore testing evidence overdue | Obtain dated restoration test results and exception follow-up |

## Management action plan

1. Request the missing fictional evidence from each assigned owner; preserve submission timestamps and period coverage.
2. Investigate the offboarding and privileged access items first because of potential unauthorized-access exposure.
3. Review actual procedures to establish Test of Design, then select and inspect dated execution samples for Test of Operating Effectiveness.
4. Record validated exceptions, corrective actions, accountable owners, target dates, and retest outcomes. Do not equate missing evidence with a proven control failure.
5. Refresh the dashboard by rerunning the Python monitoring script after updating CSV inputs; regenerate this narrative manually from the validated output.

## Scope and limitations

This portfolio uses entirely fictional organizations, users, vendors, and evidence paths. The dashboard is a **static July 31 snapshot**, not a live connection. The control-to-framework mappings are illustrative. No Vanta, Drata, AWS, identity platform, or auditor integration was used. The Phase 5 ToD/OE conclusions remain pending actual source-document validation. No assurance opinion is expressed.
