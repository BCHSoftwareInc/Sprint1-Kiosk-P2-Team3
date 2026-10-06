"""
BCH Software Inc. | Sprint 2 - Story 2   (SE)
Console front end for the Vortex turnstile. Type END SHIFT as the ticket to stop.
"""
from turnstile_gate import TurnstileGate


def ask_number(prompt):
    # Keeps asking until the user types a real number (a crash here = failed Desk Hack)
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("  Please enter a number.")


def main():
    gate = TurnstileGate()
    print("=== APEX VORTEX TURNSTILE - ONLINE ===")

    # TODO: loop forever:
    #   - ask for the ticket type (.strip().upper() it); if it is "END SHIFT", break
    #   - use ask_number() for height and age (age -> int)
    #   - ask "Guardian present? (y/n)" -> True if they typed y
    #   - result = gate.scan(...)  and print it

    # TODO: after the loop, print a SHIFT REPORT with granted, denied, and total


if __name__ == "__main__":
    main()
