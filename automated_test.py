import csv

from simulated_power_supply import SimulatedPowerSupply
from dut_model import SimulatedDUT
from config_loader import load_config


# ==========================================
# LOAD CONFIGURATION
# ==========================================

config = load_config()
limits = config["limits"]

MIN_VOLTAGE = limits["voltage"].get("min", 0.0)
MAX_VOLTAGE = limits["voltage"]["max"]

MIN_CURRENT = limits["current"]["min"]
MAX_CURRENT = limits["current"]["max"]

MIN_POWER = limits["power"]["min"]
MAX_POWER = limits["power"]["max"]


# ==========================================
# CREATE TEST EQUIPMENT
# ==========================================

supply = SimulatedPowerSupply()
dut = SimulatedDUT()


# ==========================================
# TEST POINTS
# ==========================================

test_currents = [
    0.5,
    1.0,
    1.5,
    2.0,
    2.5,
    3.0
]

results = []


print("\n==========================================")
print("       AUTOMATED DUT VALIDATION")
print("==========================================")


try:

    # ======================================
    # POWER SUPPLY SETUP
    # ======================================

    supply.set_voltage(12.0)
    supply.set_current(3.0)

    supply.output_on()


    # ======================================
    # AUTOMATED TEST
    # ======================================

    for test_current in test_currents:

        print("\n------------------------------------------")
        print(f"TEST CURRENT: {test_current:.2f} A")
        print("------------------------------------------")

        # Set load current
        supply.set_current(test_current)

        # ----------------------------------
        # DUT MEASUREMENT
        # ----------------------------------

        voltage = dut.measure(test_current)

        current = test_current

        power = voltage * current


        print(f"Voltage: {voltage:.3f} V")
        print(f"Current: {current:.3f} A")
        print(f"Power:   {power:.3f} W")


        # ==================================
        # VALIDATION
        # ==================================

        voltage_pass = (
            MIN_VOLTAGE <= voltage <= MAX_VOLTAGE
        )

        current_pass = (
            MIN_CURRENT <= current <= MAX_CURRENT
        )

        power_pass = (
            MIN_POWER <= power <= MAX_POWER
        )


        if voltage_pass and current_pass and power_pass:

            result = "PASS"

        else:

            result = "FAIL"


        # ==================================
        # FAILURE DETAILS
        # ==================================

        if not voltage_pass:

            print(
                f"FAIL: Voltage outside "
                f"{MIN_VOLTAGE} - {MAX_VOLTAGE} V"
            )

        if not current_pass:

            print(
                f"FAIL: Current outside "
                f"{MIN_CURRENT} - {MAX_CURRENT} A"
            )

        if not power_pass:

            print(
                f"FAIL: Power outside "
                f"{MIN_POWER} - {MAX_POWER} W"
            )


        print(f"RESULT: {result}")


        # ==================================
        # SAVE RESULT
        # ==================================

        results.append(
            [
                test_current,
                voltage,
                current,
                power,
                result
            ]
        )


finally:

    # ======================================
    # SAFETY SHUTDOWN
    # ======================================

    supply.output_off()


# ==========================================
# SAVE CSV
# ==========================================

with open(
    "automated_test_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "Load Current (A)",
            "Voltage (V)",
            "Current (A)",
            "Power (W)",
            "Result"
        ]
    )

    writer.writerows(results)


# ==========================================
# OVERALL RESULT
# ==========================================

overall_result = "PASS"

for row in results:

    if row[4] == "FAIL":

        overall_result = "FAIL"


print("\n==========================================")
print(f"OVERALL RESULT: {overall_result}")
print("==========================================")

print("\nResults saved to:")
print("automated_test_results.csv")