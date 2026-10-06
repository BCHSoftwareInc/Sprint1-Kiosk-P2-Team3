# BCH Software Inc. - Sprint 2: Apex Security Turnstile (Python)

Client: Apex Entertainment - "The Vortex" coaster.
Your role packet tells you exactly what to do on Day 1. Start there.

## Who owns which file
| File | Owner |
|---|---|
| `sprint2/gate_rules.py` | SE (Story 1) |
| `sprint2/turnstile_gate.py` | SE (Story 2) |
| `sprint2/main.py` | SE (Story 2) |
| `sprint2/tests/test_qa_boundaries.py` | QA (Story 3) |
| `sprint2/tests/test_cca_security.py` | CCA (Story 4) |
| `sprint2/ai_suggested_gate.py` | Nobody - AI-suggested code for the CCA to audit. DO NOT use it in the app. |
| `ISSUES.md` | PM - copy into GitHub issues |

Only edit the files you own. If you need a change in someone else's file, open an issue.

## Where this lives
This folder goes into your Sprint 1 repo as  sprint2/ . Open the sprint2 folder itself in VS Code and run every command from inside it.

## Running the tests (pytest (one install, then plain assert statements))
- Everything: python -m pytest -v
- QA only: python -m pytest -v tests/test_qa_boundaries.py
- CCA only: python -m pytest -v tests/test_cca_security.py

Each line ends in PASSED (green), FAILED (red) or SKIPPED (yellow). The last line is the summary, e.g. 2 failed, 10 skipped.

## Running the app
python main.py
