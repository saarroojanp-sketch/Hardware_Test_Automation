from simulated_power_supply import SimulatedPowerSupply
from dut_model import SimulatedDUT
from config_loader import load_config
from failure_analysis import analyze_measurement

import csv
from datetime import datetime
import time


# ============================================================
# TEST SETUP
# ============================================================

def setup_test():

    print("\n=== TEST SETUP ===")

    # Create simulated test equipment
    supply = SimulatedPowerSupply()

    # Create simulated DUT
    dut = SimulatedDUT()

    # Configure power supply
    supply.set_voltage(12.0)
    supply.set_current(3.0)

    # Turn power supply ON
    supply.output_on()

    print("Test equipment ready.")

    return supply, dut


# ============================================================
# RUN ONE TEST POINT
# ============================================================

def run_test_point(supply, dut, current, config):

    print("\n------------------------------")
    print(f"TEST POINT: {current:.2f} A")
    print("------------------------------")

    # Set electronic load current
    supply.set_current(current)

    # Record timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Start test timer
    start_time = time.perf_counter()

    # --------------------------------------------------------
    # DUT MEASUREMENT
    # --------------------------------------------------------

    voltage = dut.measure(current)

    measured_current = current

    power = voltage * measured_current

    # Stop test timer
    test_duration = time.perf_counter() - start_time

    # --------------------------------------------------------
    # DISPLAY MEASUREMENTS
    # --------------------------------------------------------

    print(f"Timestamp : {timestamp}")
    print(f"Voltage   : {voltage:.3f} V")
    print(f"Current   : {measured_current:.3f} A")
    print(f"Power     : {power:.3f} W")
    print(f"Duration  : {test_duration:.6f} s")

    # --------------------------------------------------------
    # AUTOMATIC FAILURE ANALYSIS
    # --------------------------------------------------------

    result, failures = analyze_measurement(
        voltage,
        measured_current,
        power,
        config
    )

    # --------------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------------

    if result == "PASS":

        print("RESULT    : PASS")

    else:

        print("RESULT    : FAIL")

        for failure in failures:

            print(
                f"FAILURE   : {failure['failure_type']} | "
                f"{failure['parameter']} = "
                f"{failure['measured']:.3f} | "
                f"Limit = {failure['limit']:.3f}"
            )

    # --------------------------------------------------------
    # RETURN TEST RESULT
    # --------------------------------------------------------

    return {

        "timestamp": timestamp,

        "current": measured_current,

        "voltage": voltage,

        "power": power,

        "duration": test_duration,

        "result": result,

        "failures": failures
    }


# ============================================================
# TEST CLEANUP
# ============================================================

def cleanup_test(supply):

    print("\n=== TEST CLEANUP ===")

    # Turn power supply OFF
    supply.output_off()

    print("Power supply OFF.")
    print("Test equipment safely shut down.")


# ============================================================
# MAIN TEST SEQUENCE
# ============================================================

def main():

    print("\n==========================================")
    print("       AUTOMATED DUT VALIDATION")
    print("==========================================")

    # --------------------------------------------------------
    # LOAD YAML CONFIGURATION
    # --------------------------------------------------------

    config = load_config()

    # --------------------------------------------------------
    # SETUP TEST EQUIPMENT
    # --------------------------------------------------------

    supply, dut = setup_test()

    # --------------------------------------------------------
    # READ TEST CURRENTS FROM YAML
    # --------------------------------------------------------

    test_currents = config["test_plan"]["currents"]

    # Store all test results
    results = []

    # --------------------------------------------------------
    # RUN ALL TEST POINTS
    # --------------------------------------------------------

    try:

        for current in test_currents:

            result = run_test_point(
                supply,
                dut,
                current,
                config
            )

            results.append(result)

    finally:

        # Always turn equipment OFF
        cleanup_test(supply)

    # ========================================================
    # SAVE DETAILED CSV REPORT
    # ========================================================

    with open(
        "detailed_validation_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        # ----------------------------------------------------
        # CSV HEADER
        # ----------------------------------------------------

        writer.writerow([
            "Test Point",
            "Timestamp",
            "Current (A)",
            "Voltage (V)",
            "Power (W)",
            "Duration (s)",
            "Result",
            "Failure Type",
            "Deviation (V)"
        ])

        # ----------------------------------------------------
        # WRITE TEST RESULTS
        # ----------------------------------------------------

        for index, result in enumerate(results, start=1):

            # Check whether this test point has failures
            if result["failures"]:

                failure_type = "; ".join(
                    failure["failure_type"]
                    for failure in result["failures"]
                )

                deviation = "; ".join(
                    f"{failure['measured'] - failure['limit']:.3f}"
                    for failure in result["failures"]
                )

            else:

                failure_type = "NONE"

                deviation = "0.000"

            # ------------------------------------------------
            # WRITE ONE CSV ROW
            # ------------------------------------------------

            writer.writerow([

                index,

                result["timestamp"],

                result["current"],

                result["voltage"],

                result["power"],

                result["duration"],

                result["result"],

                failure_type,

                deviation
            ])

    # ========================================================
    # FINAL TEST SUMMARY
    # ========================================================

    print("\nDetailed report saved to:")
    print("detailed_validation_results.csv")

    print("\n==============================")
    print("TEST SEQUENCE COMPLETE")
    print("==============================")

    # --------------------------------------------------------
    # FIND FAILED TESTS
    # --------------------------------------------------------

    failures = [

        result

        for result in results

        if result["result"] == "FAIL"
    ]

    # --------------------------------------------------------
    # COUNT RESULTS
    # --------------------------------------------------------

    total_tests = len(results)

    failed_tests = len(failures)

    passed_tests = total_tests - failed_tests

    print(f"Total Tests : {total_tests}")

    print(f"Passed      : {passed_tests}")

    print(f"Failures    : {failed_tests}")

    # --------------------------------------------------------
    # OVERALL RESULT
    # --------------------------------------------------------

    if failures:

        print("OVERALL     : FAIL")

    else:

        print("OVERALL     : PASS")

    print("==============================")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":

    main()