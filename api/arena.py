from api.client import get

def get_arena_server():
    data = get("/connections/servers?product=competitive")
    options = data["data"]["options"]["EU"]

    if "EU - Release Arena" in options:
        servers = options["EU - Release Arena"]["servers"]
        if servers:
            return int(next(iter(servers)))

    fallback = options["EU - Free"]["servers"]
    return int(next(iter(fallback)))
