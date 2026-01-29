from api.client import post
from api.active import get_active_machine, NoActiveMachine

class SubmitError(Exception):
    pass

def submit_flag(flag: str) -> dict:
    try:
        machine = get_active_machine()
    except NoActiveMachine as e:
        raise SubmitError(str(e))

    payload = {
        "id": machine["id"],
        "flag": flag
    }
    response = post("/machine/own", json=payload, api_version="v5")

    return {
        "machine": {
            "id": machine["id"],
            "name": machine["name"],
            "ip": machine["ip"],
        },
        "response": response
    }
