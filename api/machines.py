from api.client import get, post

def get_box_profile(name):
    data = get(f"/machine/profile/{name}")
    return data.get("info")

def spawn_box(machine_id, server_id=None):
    payload = {"machine_id": machine_id}
    if server_id:
        payload["server_id"] = server_id
    return post("/vm/spawn", json=payload)
