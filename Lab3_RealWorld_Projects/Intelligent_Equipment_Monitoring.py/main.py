# Exercise 3: Intelligent Equipment Monitoring Pipeline

from telemetry import generate_telemetry
from diagnostics import process_readings, analyze_fault


LAST_NAME = "BARRIENTOS"
SEED_NUM = 4
FAVORITE_ARTIST = "Mac DeMarco"


def main():

    print("=== INTELLIGENT EQUIPMENT MONITORING PIPELINE ===")
    print(f"Student: {LAST_NAME}")
    print(f"Seed Number: {SEED_NUM}")
    print(f"Favorite Artist: {FAVORITE_ARTIST}")

    # Generator produces readings one at a time
    telemetry_stream = generate_telemetry(LAST_NAME, SEED_NUM)

    readings = []

    print("\nGenerated Telemetry Data:")

    for reading in telemetry_stream:
        print(reading)
        readings.append(reading)

    # Process the readings
    valid, invalid, squared = process_readings(readings)

    print("\nProcessing Results:")
    print(f"Valid Readings: {valid}")
    print(f"Invalid Readings: {invalid}")
    print(f"Squared Valid Readings: {squared}")

    # Analyze abnormal readings recursively
    if invalid:
        print("\nRecursive Fault Analysis:")
        result = analyze_fault(1, 3)
        print(result)

    # Final summary
    print("\n=== FINAL DIAGNOSTIC SUMMARY ===")
    print(f"Number of Processed Readings: {len(readings)}")
    print(f"Valid Readings: {len(valid)}")
    print(f"Invalid Readings: {len(invalid)}")

    if invalid:
        print("Abnormal Conditions Detected: YES")
        print("Overall Equipment Status: WARNING")
    else:
        print("Abnormal Conditions Detected: NO")
        print("Overall Equipment Status: NORMAL")


main()