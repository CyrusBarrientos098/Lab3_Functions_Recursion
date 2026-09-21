# diagnostics.py
# Handles validation and diagnosis


def monitor_function(func):
    """Simple decorator for monitoring function execution."""

    def wrapper(*args, **kwargs):
        print("\n[Monitor] Function started.")
        result = func(*args, **kwargs)
        print("[Monitor] Function finished.")
        return result


    return wrapper


def validate_reading(reading):
    """Validate a telemetry reading."""

    if not isinstance(reading, (int, float)):
        raise ValueError("Reading must be numeric.")

    if reading < 0 or reading > 100:
        raise ValueError("Reading is outside the valid range.")

    return True


def analyze_fault(level, max_level):
    """Recursively analyze an abnormal condition."""

    print(f"Fault analysis level {level}")

    # Base case
    if level >= max_level:
        return "Fault analysis completed."

    return analyze_fault(level + 1, max_level)


@monitor_function
def process_readings(readings):
    """Validate and process telemetry readings."""

    valid = []
    invalid = []

    for reading in readings:
        try:
            validate_reading(reading)
            valid.append(reading)
        except ValueError:
            invalid.append(reading)

    # Lambda transformation
    squared = list(map(lambda x: x ** 2, valid))

    return valid, invalid, squared