import time
from api.client import post, get
from api.active import get_active_machine, NoActiveMachine

class SpawnError(Exception):
    pass

class TerminateError(Exception):
    pass

def spawn_machine(machine_id: int) -> dict:
    return post(
        "/vm/spawn",
        json={"machine_id": machine_id},
        api_version="v4"
    )

def terminate_machine(machine_id: int) -> dict:
    return post(
        "/vm/terminate",
        json={"machine_id": machine_id},
        api_version="v4"
    )

def wait_for_machine(timeout: int = 60, poll_interval: float = 15.0) -> dict:
    start = time.time()

    while time.time() - start < timeout:
        try:
            machine = get_active_machine()
        except NoActiveMachine:
            time.sleep(poll_interval)
            continue

        if not machine.get("isSpawning") and machine.get("ip"):
            return machine
        time.sleep(poll_interval)
    raise SpawnError("Timeout while waiting for machine to spawn")
