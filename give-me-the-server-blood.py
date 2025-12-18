#!/usr/bin/env python3

import argparse
import os
import sys
import time
import datetime
import subprocess
from pathlib import Path
from hackthebox import HTBClient
import tomllib

CONFIG_PATH = Path.home() / ".config" / "give-me-the-server-blood" / "config.toml"

def load_config():
    if not CONFIG_PATH.exists():
        print(f"[-] Config file not found at {CONFIG_PATH}")
        sys.exit(1)
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)

config = load_config()

TOKEN = config.get("general", {}).get("htb_token")
if not TOKEN:
    print("[-] HTB token not found in config under [general].htb_token")
    sys.exit(1)

DOWNLOADS = Path(os.path.expanduser(config.get("general", {}).get("downloads_dir", "~/Downloads")))
DOWNLOADS.mkdir(exist_ok=True)

EXEGOL_BIN = os.path.expanduser(config.get("paths", {}).get("exegol", "~/.local/bin/exegol"))
VPN_PROTOCOL = config.get("general", {}).get("vpn_protocol", "tcp")

client = HTBClient(token=TOKEN)

def wait_until_release(release_iso: str | None):
    if not release_iso:
        return
    release = datetime.datetime.fromisoformat(release_iso.replace("Z", "+00:00"))
    now = datetime.datetime.now(datetime.timezone.utc)
    if now >= release:
        return
    sleep_for = (release - now).total_seconds()
    print(f"[i] Box not released yet, waiting {int(sleep_for)} seconds…")
    time.sleep(sleep_for + 3)

def get_box_profile(name: str):
    try:
        return client.machines.get(name=name)
    except Exception as e:
        print(f"[-] Failed to fetch box profile: {e}")
        return None

def get_arena_server_id() -> int:
    servers = client.connections.servers(product="competitive")
    eu = servers.data["options"]["EU"] if hasattr(servers, "data") else servers["data"]["options"]["EU"]

    if "EU - Release Arena" in eu and eu["EU - Release Arena"]["servers"]:
        server_id = next(iter(eu["EU - Release Arena"]["servers"]))
        print("[+] Using EU Release Arena server")
        return int(server_id)

    server_id = next(iter(eu["EU - Free"]["servers"]))
    print("[i] Falling back to EU Free server")
    return int(server_id)

def spawn_box(machine):
    if getattr(machine.playInfo, "isSpawned", False):
        print("[i] Box already spawned")
        return None

    server_id = get_arena_server_id()
    client.machines.spawn(machine_id=machine.id, server_id=server_id)
    print("[+] Spawn request sent")
    return server_id

def download_tcp_vpn(server_id: int | None) -> Path:
    server_id = server_id or 0
    vpn_data = client.vpn.download(server_id=server_id, protocol=VPN_PROTOCOL)

    vpn_path = DOWNLOADS / f"htb_{VPN_PROTOCOL}.ovpn"
    if isinstance(vpn_data, str):
        vpn_path.write_text(vpn_data)
    else:
        vpn_path.write_bytes(vpn_data)

    with vpn_path.open("a") as f:
        f.write("\nscript-security 2\n")
        f.write("up /etc/openvpn/update-resolv-conf\n")
        f.write("down /etc/openvpn/update-resolv-conf\n")

    print(f"[+] VPN downloaded to {vpn_path}")
    return vpn_path

def start_openvpn(vpn_path: Path):
    print("[i] Starting OpenVPN")
    subprocess.Popen(
        ["sudo", "openvpn", "--config", str(vpn_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

def start_exegol(vpn_path: Path, box):
    cmd = [
        "sudo", "-E",
        EXEGOL_BIN,
        "start",
        box.name,
        "--vpn", str(vpn_path),
        "-V", f"{DOWNLOADS}:/Downloads",
    ]
    print("[i] Launching Exegol:")
    print(" ".join(cmd))
    subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--box", required=True)
    parser.add_argument("--chall")
    parser.add_argument("--exegol", action="store_true")
    parser.add_argument("--ovpn", action="store_true")
    args = parser.parse_args()

    box = get_box_profile(args.box)
    if not box:
        sys.exit(1)

    wait_until_release(getattr(box, "release", None))

    server_id = spawn_box(box)

    print(f"[+] Box IP: {getattr(box, 'ip', 'Unknown')}")

    vpn_path = download_tcp_vpn(server_id)

    if args.ovpn:
        start_openvpn(vpn_path)
        time.sleep(10)

    if args.exegol:
        start_exegol(vpn_path, box)

if __name__ == "__main__":
    main()
