import pandas as pd

data = pd.read_csv("detailed_validation_results.csv")

passed = data[data["Result"] == "PASS"]
failed = data[data["Result"] == "FAIL"]

print("\n====================================")
print("       FAILURE THRESHOLD ANALYSIS")
print("====================================")

if len(failed) == 0:

    print("No failure detected.")

else:

    first_failure = failed.iloc[0]

    first_failure_current = first_failure["Current (A)"]
    first_failure_voltage = first_failure["Voltage (V)"]

    print(f"First Failure Current : {first_failure_current:.3f} A")
    print(f"Voltage at Failure   : {first_failure_voltage:.3f} V")

    if len(passed) > 0:

        last_pass = passed.iloc[-1]

        last_pass_current = last_pass["Current (A)"]
        last_pass_voltage = last_pass["Voltage (V)"]

        print(f"Last Passing Current : {last_pass_current:.3f} A")
        print(f"Voltage at Last PASS : {last_pass_voltage:.3f} V")

        print("\nFailure region:")

        print(
            f"{last_pass_current:.3f} A "
            f"< failure threshold < "
            f"{first_failure_current:.3f} A"
        )

print("====================================")