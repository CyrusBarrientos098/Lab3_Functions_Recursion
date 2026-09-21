# telemetry.py
# Handles telemetry data generation


def generate_telemetry(last_name, seed_num):
    """Generate equipment readings one at a time."""

    base = len(last_name) + seed_num

    readings = [
        base + 10,
        base + 20,
        base + 30,
        -5,
        base + 50,
        105
    ]

    for reading in readings:
        yield reading