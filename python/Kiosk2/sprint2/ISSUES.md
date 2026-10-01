# Sprint 2 - Apex Security Turnstile (Python track)
Copy each story below into a GitHub issue (title = the heading line, body = everything under it).
This project lives in the sprint2/ folder of your Sprint 1 repo. Paths below are from the repo root.

---

## [SE] Story 1 - Gate decision engine
**Owner:** SE  **Label:** SE  **File:** `sprint2/gate_rules.py`

As Apex Entertainment, I need the Vortex turnstile to decide who may ride, so that no one unsafe gets on.

**Acceptance criteria**
- [ ] The 5 rules are checked in order (ticket, bad scan, height, guardian, grant)
- [ ] Returns the exact result codes from the spec (GRANTED, GRANTED_VIP, DENIED_NO_TICKET, DENIED_INVALID, DENIED_TOO_SHORT, DENIED_NEEDS_GUARDIAN)
- [ ] VIPs are NOT exempt from the height rule
- [ ] The function does not print or read input - it only returns a code
- [ ] QA tests Q1-Q10 pass

---

## [SE] Story 2 - Turnstile gate, counters and front end
**Owner:** SE  **Label:** SE  **Files:** `sprint2/turnstile_gate.py`, `sprint2/main.py`

As the ride operator, I need to scan riders one after another and see today's granted/denied totals.

**Acceptance criteria**
- [ ] Every scan adds 1 to either the granted count or the denied count - never both, never neither
- [ ] Total = granted + denied
- [ ] Front end shows each result and the running counts
- [ ] Bad input (letters, blank) does not crash the program
- [ ] QA tests Q11-Q12 and CCA test C14 pass

---

## [QA] Story 3 - Boundary test suite
**Owner:** QA  **Label:** QA  **File:** `sprint2/tests/test_qa_boundaries.py`

As QA, I need automated tests at every rule boundary so a bad change is caught the moment it is made.

**Acceptance criteria**
- [ ] Test Matrix: Expected column filled from the spec BEFORE running the code
- [ ] Q1-Q12 written as real pytest tests - none skipped/ignored
- [ ] At least 2 extra edge-case tests of QA's own design
- [ ] Every failure is filed as a bug issue assigned to SE
- [ ] All tests pass against the team's final code

---

## [CCA] Story 4 - Security audit: AI-suggested code vs. our code
**Owner:** CCA  **Label:** CCA  **File:** `sprint2/tests/test_cca_security.py`

As CCA, I need proof - not opinions - that the AI-suggested gate code in `ai_suggested_gate.py` is unsafe, and that our code is safe.

**Acceptance criteria**
- [ ] C1-C13 written as real pytest tests
- [ ] Day 1: run against the AI code; at least 3 bug reports filed (C1 and C2 included)
- [ ] Day 2: tests switched to our GateRules; C14 written; all tests pass
- [ ] Security Audit Checklist completed against our code and signed off
- [ ] `ai_suggested_gate.py` is never called by the real app

---

## Bug report template (QA and CCA)
```
Title: [SAFETY | SECURITY | BUG] <what goes wrong, in plain words>

Test that proves it: <test name, e.g. c1_vipCannotSkipHeightRule>
Input: ticket=..., height=..., age=..., guardian=...
Expected: <code from the spec>
Actual:   <what the code returned>
Severity: Safety (someone could get hurt) / Security (someone could get in) / Bug (wrong but harmless)
```
