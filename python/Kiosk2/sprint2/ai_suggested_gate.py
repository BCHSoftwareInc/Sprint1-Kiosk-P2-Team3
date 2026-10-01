"""
!!! DO NOT SHIP - CCA AUDIT TARGET !!!

A developer pasted this from an AI chat assistant and said "it works, I ran it
once." Your job (CCA) is to prove whether it is safe with unit tests.
It has the same function name and inputs as gate_rules.check_entry.
"""


def check_entry(ticket_type, height_in, age, has_guardian):
    # VIPs paid extra, so let them straight through
    if ticket_type == "VIP":
        return "GRANTED_VIP"

    if ticket_type == "UNAUTHORIZED":
        return "DENIED_NO_TICKET"

    # Rider must be tall enough or old enough
    if height_in >= 48 or age >= 13:
        return "GRANTED"

    if has_guardian:
        return "GRANTED"

    return "DENIED_TOO_SHORT"
