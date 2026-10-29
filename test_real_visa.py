
import pytest

from real_visa_power_supply import RealVisaPowerSupply


def test_real_instrument_identification():
    resource_name = "YOUR_VISA_RESOURCE"

    if resource_name == "YOUR_VISA_RESOURCE":
        pytest.skip("No real VISA instrument configured.")

    instrument = RealVisaPowerSupply(resource_name)

    try:
        identification = instrument.identify()
        assert identification
        print(f"Instrument ID: {identification}")
    finally:
        instrument.close()
