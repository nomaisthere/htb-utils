import time
from api.client import post
from api.active import get_active_machine, NoActiveMachine

class SpawnError(Exception):
    pass

def spawn_machine(machine_id: int) -> None:
    post("/vm/spawn", json={"machine_id": machine_id})

def terminate_machine(machine_id: int) -> None:
    post("/vm/terminate", json={"machine_id": machine_id})

def wait_for_machine(timeout: int = 120, poll_interval: float = 5.0) -> dict:
    start = time.time()

    while time.time() - start < timeout:
        try:
            m = get_active_machine()
        except NoActiveMachine:
            time.sleep(poll_interval)
            continue
        if not m.get("isSpawning") and m.get("ip"):
            return m
        time.sleep(poll_interval)
    raise SpawnError("Machine spawn timeout")
