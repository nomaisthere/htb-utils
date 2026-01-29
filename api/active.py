from api.client import get

class NoActiveMachine(Exception):
    pass

def get_active_machine() -> dict:
    data = get("/machine/active", api_version="v4")
    info = data.get("info")
    if not info:
        raise NoActiveMachine("No active machine found")

    return info
