"""
QA - Boundary Test Suite (Sprint 2, Story 3)
Run from the project folder with:   pytest -v
Each test = one row of your QA Test Matrix.

HOW TO FINISH A TODO TEST
  1. Delete the pytest.skip(...) line.
  2. Write ONE assert line, copying the pattern from the Q1/Q2 examples.
  3. Run pytest again. Skipped = yellow, passed = green, failed = red.
"""
import pytest
from gate_rules import check_entry
from turnstile_gate import TurnstileGate


# ---------- Height boundary (48 inches) ----------
def test_q1_patron_exactly48_inches_age13_is_granted():
    assert check_entry("PATRON", 48, 13, False) == "GRANTED"

def test_q2_patron47point9_inches_is_too_short():
    assert check_entry("PATRON", 47.9, 30, False) == "DENIED_TOO_SHORT"

def test_q3_patron48point1_inches_is_granted():
    # TODO (Q3): ticket "PATRON", height 48.1, age 30, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")


# ---------- Age boundary (13) ----------
def test_q4_age12_without_guardian_needs_guardian():
    # TODO (Q4): ticket "PATRON", height 60, age 12, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

def test_q5_age12_with_guardian_is_granted():
    # TODO (Q5): ticket "PATRON", height 60, age 12, guardian True  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

def test_q6_age13_without_guardian_is_granted():
    # TODO (Q6): ticket "PATRON", height 60, age 13, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")


# ---------- Ticket types ----------
def test_q7_vip_normal_rider_gets_vip_lane():
    # TODO (Q7): ticket "VIP", height 60, age 30, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

def test_q8_unauthorized_is_denied():
    # TODO (Q8): ticket "UNAUTHORIZED", height 60, age 30, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

def test_q9_top_of_valid_range_is_granted():
    # TODO (Q9): ticket "PATRON", height 96, age 120, guardian False  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

def test_q10_vip_child_with_guardian_gets_vip_lane():
    # TODO (Q10): ticket "VIP", height 60, age 12, guardian True  ->  expect ??? (look it up in the Rules table)
    pytest.skip("TODO - write this test")

# ---------- Analytics counters (runs once SE finishes Story 2) ----------
def test_q11_new_gate_starts_at_zero():
    # TODO (Q11): make a TurnstileGate(), then assert granted_count, denied_count
    #             and total_scans() are all 0
    pytest.skip("TODO - write this test")

def test_q12_counters_after_two_grants_and_one_deny():
    gate = TurnstileGate()
    gate.scan("PATRON", 60, 30, False)   # granted
    gate.scan("VIP", 60, 30, False)      # granted
    gate.scan("PATRON", 40, 30, False)   # denied
    # TODO (Q12): assert granted_count is 2, denied_count is 1, total_scans() is 3
    pytest.skip("TODO - write this test")
