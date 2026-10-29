import pandas as pd
from config_loader import load_config


# ==========================================
# LOAD TEST CONFIGURATION
# ==========================================

config = load_config()

MIN_VOLTAGE = config["voltage"]["min"]
MAX_VOLTAGE = config["voltage"]["max"]

MIN_CURRENT = config["current"]["min"]
MAX_CURRENT = config["current"]["max"]

MIN_POWER = config["power"]["min"]
MAX_POWER = config["power"]["max"]


# ==========================================
# LOAD MEASUREMENT DATA
# ==========================================

data = pd.read_csv("load_sweep_results.csv")


# ==========================================
# VALIDATION
# ==========================================

print("\n====================================")
print("      DUT AUTOMATED VALIDATION")
print("====================================")

overall_result = "PASS"

for _, row in data.iterrows():

    current = row["Current (A)"]
    voltage = row["Voltage (V)"]
    power = row["Power (W)"]

    voltage_pass = MIN_VOLTAGE <= voltage <= MAX_VOLTAGE
    current_pass = MIN_CURRENT <= current <= MAX_CURRENT
    power_pass = MIN_POWER <= power <= MAX_POWER

    print(f"\nTest Point: {current:.2f} A")
    print(f"Voltage:    {voltage:.2f} V")
    print(f"Power:      {power:.2f} W")

    # Voltage validation
    if not voltage_pass:
        print(
            f"FAIL: Voltage outside limit "
            f"({MIN_VOLTAGE} - {MAX_VOLTAGE} V)"
        )

    # Current validation
    if not current_pass:
        print(
            f"FAIL: Current outside limit "
            f"({MIN_CURRENT} - {MAX_CURRENT} A)"
        )

    # Power validation
    if not power_pass:
        print(
            f"FAIL: Power outside limit "
            f"({MIN_POWER} - {MAX_POWER} W)"
        )

    # Overall test-point result
    if voltage_pass and current_pass and power_pass:
        print("Result: PASS")
    else:
        print("Result: FAIL")
        overall_result = "FAIL"


# ==========================================
# FINAL RESULT
# ==========================================

print("\n====================================")
print(f"OVERALL RESULT: {overall_result}")
print("====================================")