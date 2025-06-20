import pytest
from utils.client_wrapper import AirSimClientWrapper
import time

@pytest.fixture(scope="module")
def client():
    wrapper = AirSimClientWrapper()
    try:
        client = wrapper.connect()
        yield client
    except Exception as e:
        pytest.skip(f"AirSim not reachable: {e}")
    finally:
        wrapper.disconnect()

def test_takeoff_and_hover(client):
    client.takeoffAsync().join()
    time.sleep(2)

    state = client.getMultirotorState()
    altitude = -state.kinematics_estimated.position.z_val
    print(f"Altitude: {altitude:.2f} m")

    assert altitude > 1.5, "Drone should reach at least 1.5m after takeoff"
