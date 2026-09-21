# Appendix 2: Recursive Fault Trace

LAST_NAME = "BARRIENTOS"
SEED_NUM = 4
FAVORITE_ARTIST = "Mac DeMarco"


def generate_fault_code():
    """Generate a student-specific fault code."""
    first_letter = LAST_NAME[0]

    verification_hash = (ord(first_letter) * SEED_NUM) - (SEED_NUM + 3)

    return f"{first_letter}{SEED_NUM}", verification_hash


def trace_fault(level, max_level, trace):
    """Recursively trace the fault until the base condition."""

    trace.append(level)

    # Base case
    if level == max_level:
        return

    # Recursive call
    trace_fault(level + 1, max_level, trace)


def main():
    print("=== RECURSIVE FAULT TRACE ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    fault_code, verification_hash = generate_fault_code()

    print(f"\nGenerated Fault Code: {fault_code}")
    print(f"Verification Hash: {verification_hash}")

    max_level = SEED_NUM + 3
    trace = []

    trace_fault(1, max_level, trace)

    print("\nRecursive Trace:")
    print(trace)

    print(f"\nRecursive Calls: {len(trace)}")
    print("Final Result: Fault trace completed successfully.")


main()