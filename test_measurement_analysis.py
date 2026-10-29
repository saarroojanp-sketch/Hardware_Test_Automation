from failure_analysis import analyze_measurement
from config_loader import load_config


def test_measurement_analysis():

    config = load_config()

    result, failures = analyze_measurement(
        voltage=11.053,
        current=2.5,
        power=27.631,
        config=config
    )

    print("\n=== AUTOMATED FAILURE ANALYSIS ===")

    print(f"Result: {result}")

    for failure in failures:

        print(
            f"{failure['parameter']} | "
            f"{failure['failure_type']} | "
            f"Measured: {failure['measured']:.3f} | "
            f"Limit: {failure['limit']:.3f}"
        )

    assert result == "FAIL"
    assert failures[0]["failure_type"] == "UNDERVOLTAGE"