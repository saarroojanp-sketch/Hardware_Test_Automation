def analyze_measurement(voltage, current, power, config):

    failures = []

    voltage_min = config["limits"]["voltage"]["min"]
    voltage_max = config["limits"]["voltage"]["max"]

    current_min = config["limits"]["current"]["min"]
    current_max = config["limits"]["current"]["max"]

    power_min = config["limits"]["power"]["min"]
    power_max = config["limits"]["power"]["max"]

    # Voltage
    if voltage < voltage_min:
        failures.append({
            "parameter": "Voltage",
            "failure_type": "UNDERVOLTAGE",
            "measured": voltage,
            "limit": voltage_min
        })

    elif voltage > voltage_max:
        failures.append({
            "parameter": "Voltage",
            "failure_type": "OVERVOLTAGE",
            "measured": voltage,
            "limit": voltage_max
        })

    # Current
    if current < current_min:
        failures.append({
            "parameter": "Current",
            "failure_type": "UNDERCURRENT",
            "measured": current,
            "limit": current_min
        })

    elif current > current_max:
        failures.append({
            "parameter": "Current",
            "failure_type": "OVERCURRENT",
            "measured": current,
            "limit": current_max
        })

    # Power
    if power < power_min:
        failures.append({
            "parameter": "Power",
            "failure_type": "LOW_POWER",
            "measured": power,
            "limit": power_min
        })

    elif power > power_max:
        failures.append({
            "parameter": "Power",
            "failure_type": "OVERPOWER",
            "measured": power,
            "limit": power_max
        })

    if failures:
        result = "FAIL"
    else:
        result = "PASS"

    return result, failures