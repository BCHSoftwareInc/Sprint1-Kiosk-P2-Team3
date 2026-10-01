"""
BCH Software Inc. | Sprint 2 - Apex Security Turnstile   (SE - Story 1)
Client: Apex Entertainment - "The Vortex" coaster

check_entry() is the decision engine. It does NOT print or ask for input -
it only takes facts in and hands a result code back. That is what makes it
unit-testable (QA and CCA are writing tests against it RIGHT NOW).

Result codes (exact strings - tests compare them, spelling matters):
    "GRANTED"                Patron may ride
    "GRANTED_VIP"            VIP may ride (fast lane)
    "DENIED_NO_TICKET"       ticket type is UNAUTHORIZED, missing, or unknown
    "DENIED_INVALID"         height or age is impossible (bad scan)
    "DENIED_TOO_SHORT"       under 48 inches - applies to VIPs too
    "DENIED_NEEDS_GUARDIAN"  under 13 with no guardian present
"""

MIN_HEIGHT_IN = 48
MIN_SOLO_AGE = 13
MAX_HEIGHT_IN = 96
MAX_AGE = 120
VALID_TICKETS = ("PATRON", "VIP")


def check_entry(ticket_type, height_in, age, has_guardian):
    # Check the rules IN THIS ORDER. The first rule that matches wins - return right away.

    # TODO Rule 1: if ticket_type is not one of VALID_TICKETS -> return "DENIED_NO_TICKET"

    # TODO Rule 2: if height_in <= 0, or height_in > MAX_HEIGHT_IN,
    #              or age < 0, or age > MAX_AGE           -> return "DENIED_INVALID"

    # TODO Rule 3: if height_in < MIN_HEIGHT_IN            -> return "DENIED_TOO_SHORT"
    #              (VIPs are NOT exempt - this is a physical safety rule)

    # TODO Rule 4: if age < MIN_SOLO_AGE AND there is no guardian -> return "DENIED_NEEDS_GUARDIAN"

    # TODO Rule 5: if ticket_type is "VIP" -> return "GRANTED_VIP", otherwise return "GRANTED"

    return "TODO"


def is_granted(result_code):
    return result_code.startswith("GRANTED")
