"""
BCH Software Inc. | Sprint 2 - Story 2   (SE)
TurnstileGate wraps the decision engine and keeps the day's analytics.
"""
from gate_rules import check_entry, is_granted


class TurnstileGate:
    def __init__(self):
        self.granted_count = 0
        self.denied_count = 0

    def scan(self, ticket_type, height_in, age, has_guardian):
        # TODO 1: result = check_entry(...) with the four inputs
        # TODO 2: if is_granted(result), add 1 to self.granted_count - otherwise add 1 to self.denied_count
        # TODO 3: return result
        return "TODO"

    def total_scans(self):
        # TODO: return granted + denied
        return 0
