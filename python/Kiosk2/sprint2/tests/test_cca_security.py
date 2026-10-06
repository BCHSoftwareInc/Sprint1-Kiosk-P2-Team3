"""
CCA - Security & Safety Test Suite (Sprint 2, Story 4)
Run from the project folder with:   pytest -v tests/test_cca_security.py

DAY 1: you are auditing the AI-suggested code. Leave the import below as-is.
       Every FAILED test is a bug you found - write each one up as a GitHub issue.
DAY 2: change the import to   from gate_rules import check_entry
       and re-run against your team's real code. The goal is all green.

HOW TO FINISH A TODO TEST
  1. Delete the pytest.skip(...) line.
  2. Write ONE assert line, copying the pattern from the C1/C2 examples.
"""
import pytest
from ai_suggested_gate import check_entry   # <- Day 1 audit target. Day 2: from gate_rules import check_entry
from turnstile_gate import TurnstileGate


# ---------- Safety rules nobody can bypass ----------
def test_c1_vip_cannot_skip_height_rule():
    assert check_entry("VIP", 40, 30, False) == "DENIED_TOO_SHORT"

def test_c2_tall_kid_without_guardian_is_denied():
    # The AND/OR trap from Spot the Slop Lab 1
    assert check_entry("PATRON", 60, 10, False) == "DENIED_NEEDS_GUARDIAN"

def test_c3_short_teenager_is_denied():
    # The other half of the AND/OR trap
    # TODO (C3): ticket "PATRON", height 45, age 15, guardian False  ->  expect "DENIED_TOO_SHORT"
    pytest.skip("TODO - write this test")

def test_c4_guardian_cannot_override_height():
    # TODO (C4): ticket "PATRON", height 40, age 8, guardian True  ->  expect "DENIED_TOO_SHORT"
    pytest.skip("TODO - write this test")

def test_c5_unauthorized_with_guardian_still_denied():
    # TODO (C5): ticket "UNAUTHORIZED", height 60, age 30, guardian True  ->  expect "DENIED_NO_TICKET"
    pytest.skip("TODO - write this test")


# ---------- Bad or tampered ticket data ----------
def test_c6_blank_ticket_is_denied():
    # TODO (C6): ticket "", height 60, age 30, guardian False  ->  expect "DENIED_NO_TICKET"
    pytest.skip("TODO - write this test")

def test_c7_missing_ticket_is_denied():
    # TODO (C7): ticket None, height 60, age 30, guardian False  ->  expect "DENIED_NO_TICKET"
    pytest.skip("TODO - write this test")

def test_c8_lowercase_ticket_is_not_a_real_code():
    # TODO (C8): ticket "vip", height 60, age 30, guardian False  ->  expect "DENIED_NO_TICKET"
    pytest.skip("TODO - write this test")


# ---------- Impossible measurements ----------
def test_c9_negative_height_is_invalid():
    # TODO (C9): ticket "PATRON", height -5, age 30, guardian False  ->  expect "DENIED_INVALID"
    pytest.skip("TODO - write this test")

def test_c10_zero_height_is_invalid():
    # TODO (C10): ticket "PATRON", height 0, age 30, guardian False  ->  expect "DENIED_INVALID"
    pytest.skip("TODO - write this test")

def test_c11_giant_height_is_invalid():
    # TODO (C11): ticket "PATRON", height 500, age 30, guardian False  ->  expect "DENIED_INVALID"
    pytest.skip("TODO - write this test")

def test_c12_negative_age_is_invalid():
    # TODO (C12): ticket "PATRON", height 60, age -1, guardian False  ->  expect "DENIED_INVALID"
    pytest.skip("TODO - write this test")

def test_c13_impossible_age_is_invalid():
    # TODO (C13): ticket "PATRON", height 60, age 999, guardian False  ->  expect "DENIED_INVALID"
    pytest.skip("TODO - write this test")

# ---------- Analytics integrity (DAY 2 - uses your team's real gate) ----------
def test_c14_invalid_scan_counts_as_denied_not_granted():
    gate = TurnstileGate()
    gate.scan("PATRON", -5, 30, False)
    # TODO (C14, Day 2): assert granted_count is 0 and denied_count is 1
    pytest.skip("TODO - write this test")
