import pandas as pd


data = pd.read_csv("automated_test_results.csv")

total_tests = len(data)

pass_count = (data["Result"] == "PASS").sum()
fail_count = (data["Result"] == "FAIL").sum()

minimum_voltage = data["Voltage (V)"].min()
maximum_voltage = data["Voltage (V)"].max()

minimum_current = data["Current (A)"].min()
maximum_current = data["Current (A)"].max()

minimum_power = data["Power (W)"].min()
maximum_power = data["Power (W)"].max()

failed_tests = data[data["Result"] == "FAIL"]

if fail_count == 0:
    overall_result = "PASS"
else:
    overall_result = "FAIL"


print("\n==========================================")
print("          DUT VALIDATION REPORT")
print("==========================================")

print(f"Total Test Points : {total_tests}")
print(f"PASS              : {pass_count}")
print(f"FAIL              : {fail_count}")

print("\n--- MEASUREMENT SUMMARY ---")

print(f"Voltage Range     : {minimum_voltage:.3f} - {maximum_voltage:.3f} V")
print(f"Current Range     : {minimum_current:.3f} - {maximum_current:.3f} A")
print(f"Power Range       : {minimum_power:.3f} - {maximum_power:.3f} W")

print("\n--- FAILED TESTS ---")

if fail_count == 0:

    print("No failures detected.")

else:

    for _, row in failed_tests.iterrows():

        print(
            f"Current: {row['Current (A)']:.2f} A | "
            f"Voltage: {row['Voltage (V)']:.3f} V | "
            f"Result: {row['Result']}"
        )

print("\n==========================================")
print(f"OVERALL DUT RESULT: {overall_result}")
print("==========================================")