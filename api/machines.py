from api.client import get

def get_box_profile(name: str) -> dict | None:
    data = get(f"/machine/profile/{name}")
    return data.get("info")
