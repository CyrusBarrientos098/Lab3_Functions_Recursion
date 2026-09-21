# Appendix 1: Equipment Diagnostic System

LAST_NAME = "BARRIENTOS"
SEED_NUM = 4
FAVORITE_ARTIST = "Mac DeMarco"


def generate_readings():
    """Generate simple equipment readings."""
    base = len(LAST_NAME) + SEED_NUM

    readings = [
        base + 10,
        base + 20,
        base + 30,
        base + 40,
        base + 50
    ]

    return readings


def validate_reading(reading):
    """Check if a reading is valid."""
    return 0 <= reading <= 100


def calculate_average(readings):
    """Calculate the average of valid readings."""
    return sum(readings) / len(readings)


def determine_condition(average):
    """Determine the equipment condition."""
    if average >= 70:
        return "WARNING: High reading"
    elif average <= 30:
        return "WARNING: Low reading"
    else:
        return "NORMAL"


def generate_report():
    """Generate the complete diagnostic report."""

    print("=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    readings = generate_readings()

    print("\nGenerated Equipment Data:")
    print(readings)

    valid_readings = []
    invalid_readings = []

    for reading in readings:
        if validate_reading(reading):
            valid_readings.append(reading)
        else:
            invalid_readings.append(reading)

    print("\nValidation Results:")
    print(f"Valid Readings: {valid_readings}")
    print(f"Invalid Readings: {invalid_readings}")

    if valid_readings:
        average = calculate_average(valid_readings)
        condition = determine_condition(average)

        print("\nDiagnostic Results:")
        print(f"Average Reading: {average:.2f}")
        print(f"Equipment Condition: {condition}")
    else:
        print("\nDiagnostic Results:")
        print("No valid readings available.")


generate_report()