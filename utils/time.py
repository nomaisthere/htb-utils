import time
import datetime

def wait_until_release(release_iso):
    if not release_iso:
        return

    release = datetime.datetime.fromisoformat(
        release_iso.replace("Z", "+00:00")
    )
    now = datetime.datetime.now(datetime.timezone.utc)

    if now < release:
        time.sleep((release - now).total_seconds())
        time.sleep(3)
