import pandas as pd


data = pd.read_csv("fine_sweep_results.csv")


total_tests = len(data)

pass_count = (data["Result"] == "PASS").sum()

fail_count = (data["Result"] == "FAIL").sum()


print("\n========================================")
print("       FINE SWEEP VALIDATION REPORT")
print("========================================")

print(f"Total Test Points : {total_tests}")
print(f"PASS              : {pass_count}")
print(f"FAIL              : {fail_count}")


# --------------------------------
# LAST PASS
# --------------------------------

passed = data[data["Result"] == "PASS"]

if len(passed) > 0:

    last_pass = passed.iloc[-1]

    print("\n--- LAST PASS ---")

    print(
        f"Current : "
        f"{last_pass['Current (A)']:.2f} A"
    )

    print(
        f"Voltage : "
        f"{last_pass['Voltage (V)']:.3f} V"
    )


# --------------------------------
# FIRST FAILURE
# --------------------------------

failed = data[data["Result"] == "FAIL"]

if len(failed) > 0:

    first_failure = failed.iloc[0]

    print("\n--- FIRST FAILURE ---")

    print(
        f"Current : "
        f"{first_failure['Current (A)']:.2f} A"
    )

    print(
        f"Voltage : "
        f"{first_failure['Voltage (V)']:.3f} V"
    )

    print(
        f"Failure : "
        f"{first_failure['Failure Type']}"
    )

    print(
        f"Deviation : "
        f"{first_failure['Deviation (V)']} V"
    )


# --------------------------------
# FAILURE REGION
# --------------------------------

if len(passed) > 0 and len(failed) > 0:

    last_pass_current = passed.iloc[-1]["Current (A)"]

    first_failure_current = failed.iloc[0]["Current (A)"]

    print("\n--- FAILURE REGION ---")

    print(
        f"{last_pass_current:.2f} A "
        f"< threshold < "
        f"{first_failure_current:.2f} A"
    )


# --------------------------------
# OVERALL RESULT
# --------------------------------

if fail_count == 0:

    overall_result = "PASS"

else:

    overall_result = "FAIL"


print("\n========================================")

print(
    f"OVERALL RESULT: {overall_result}"
)

print("========================================")