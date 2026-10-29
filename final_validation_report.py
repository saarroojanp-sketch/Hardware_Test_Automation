import pandas as pd


# ==========================================
# LOAD TEST DATA
# ==========================================

detailed_file = "detailed_validation_results.csv"
fine_file = "fine_sweep_results.csv"

detailed = pd.read_csv(detailed_file)
fine = pd.read_csv(fine_file)


# ==========================================
# BASIC SUMMARY
# ==========================================

total_tests = len(detailed)

pass_count = (detailed["Result"] == "PASS").sum()
fail_count = (detailed["Result"] == "FAIL").sum()

pass_rate = (pass_count / total_tests) * 100


# ==========================================
# FAILURE INFORMATION
# ==========================================

failed_tests = detailed[detailed["Result"] == "FAIL"]

if not failed_tests.empty:

    first_failure = failed_tests.iloc[0]

    first_failure_current = first_failure["Current (A)"]
    first_failure_voltage = first_failure["Voltage (V)"]
    first_failure_type = first_failure["Failure Type"]
    first_failure_deviation = first_failure["Deviation (V)"]

else:

    first_failure_current = None
    first_failure_voltage = None
    first_failure_type = "NONE"
    first_failure_deviation = 0


# ==========================================
# FINE SWEEP ANALYSIS
# ==========================================

fine_pass = fine[fine["Result"] == "PASS"]
fine_fail = fine[fine["Result"] == "FAIL"]


if not fine_pass.empty:
    last_pass = fine_pass.iloc[-1]

    last_pass_current = last_pass["Current (A)"]
    last_pass_voltage = last_pass["Voltage (V)"]

else:
    last_pass_current = None
    last_pass_voltage = None


if not fine_fail.empty:
    first_fine_fail = fine_fail.iloc[0]

    first_fine_fail_current = first_fine_fail["Current (A)"]
    first_fine_fail_voltage = first_fine_fail["Voltage (V)"]

else:
    first_fine_fail_current = None
    first_fine_fail_voltage = None


# ==========================================
# GENERATE REPORT
# ==========================================

with open("FINAL_VALIDATION_REPORT.txt", "w") as report:

    report.write("============================================\n")
    report.write("       FINAL DUT VALIDATION REPORT\n")
    report.write("============================================\n\n")

    report.write("DUT INFORMATION\n")
    report.write("------------------------------\n")
    report.write("DUT: 12V Power Module\n")
    report.write("Test Type: Automated Electrical Validation\n")
    report.write("Software: Python\n")
    report.write("Test Framework: pytest / Python automation\n\n")

    report.write("TEST SUMMARY\n")
    report.write("------------------------------\n")
    report.write(f"Total Test Points : {total_tests}\n")
    report.write(f"PASS              : {pass_count}\n")
    report.write(f"FAIL              : {fail_count}\n")
    report.write(f"PASS Rate         : {pass_rate:.1f}%\n\n")

    report.write("FAILURE ANALYSIS\n")
    report.write("------------------------------\n")

    if first_failure_current is not None:

        report.write(
            f"First Failure Current : "
            f"{first_failure_current:.3f} A\n"
        )

        report.write(
            f"Voltage at Failure   : "
            f"{first_failure_voltage:.3f} V\n"
        )

        report.write(
            f"Failure Type         : "
            f"{first_failure_type}\n"
        )

        report.write(
            f"Voltage Deviation    : "
            f"{first_failure_deviation:.3f} V\n\n"
        )

    else:

        report.write("No failures detected.\n\n")


    report.write("FINE SWEEP RESULTS\n")
    report.write("------------------------------\n")

    if last_pass_current is not None:

        report.write(
            f"Last PASS Current : "
            f"{last_pass_current:.3f} A\n"
        )

        report.write(
            f"Voltage at Last PASS : "
            f"{last_pass_voltage:.3f} V\n"
        )

    if first_fine_fail_current is not None:

        report.write(
            f"First FAIL Current : "
            f"{first_fine_fail_current:.3f} A\n"
        )

        report.write(
            f"Voltage at First FAIL : "
            f"{first_fine_fail_voltage:.3f} V\n"
        )

    report.write("\n")


    report.write("ENGINEERING CONCLUSION\n")
    report.write("------------------------------\n")

    if fail_count > 0:

        report.write(
            "The DUT passed the lower-load validation points "
            "but exhibited an undervoltage failure at higher "
            "load current.\n\n"
        )

        report.write(
            "Further investigation is recommended around the "
            "identified failure threshold before the DUT is "
            "considered fully validated.\n"
        )

    else:

        report.write(
            "The DUT passed all defined validation points.\n"
        )


    report.write("\n============================================\n")
    report.write("             END OF REPORT\n")
    report.write("============================================\n")


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n============================================")
print("       FINAL VALIDATION REPORT")
print("============================================")

print(f"\nTotal Test Points : {total_tests}")
print(f"PASS              : {pass_count}")
print(f"FAIL              : {fail_count}")
print(f"PASS Rate         : {pass_rate:.1f}%")

if first_failure_current is not None:

    print("\nFirst Failure")
    print("------------------------------")
    print(f"Current : {first_failure_current:.3f} A")
    print(f"Voltage : {first_failure_voltage:.3f} V")
    print(f"Type    : {first_failure_type}")

print("\nReport generated:")
print("FINAL_VALIDATION_REPORT.txt")