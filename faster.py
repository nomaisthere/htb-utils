#!/usr/bin/env python3

import argparse
import os
import time
import datetime
import requests
import subprocess
import sys
from pathlib import Path

HTB_API = "https://labs.hackthebox.com/api/v4"
TOKEN = os.getenv("HTB_TOKEN")

if not TOKEN:
    print("[-] HTB_TOKEN not set in environment")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "htb-automation/1.0"
}

DOWNLOADS = Path.home() / "Downloads"

def wait_until_release(release_iso):
    if not release_iso:
        return
    release = datetime.datetime.fromisoformat(release_iso.replace("Z", "+00:00"))
    now = datetime.datetime.now(datetime.timezone.utc)
    if now >= release:
        return
    sleep_for = (release - now).total_seconds()
    time.sleep(sleep_for)
    time.sleep(3)

def get_box_profile(name):
    r = requests.get(f"{HTB_API}/machine/profile/{name}", headers=HEADERS)
    if r.status_code != 200:
        return None
    return r.json()["info"]

def get_arena_server():
    r = requests.get(f"{HTB_API}/connections/servers?product=competitive", headers=HEADERS)
    r.raise_for_status()
    data = r.json()["data"]["options"]["EU"]
    if "EU - Release Arena" in data and data["EU - Release Arena"]["servers"]:
        server_id = list(data["EU - Release Arena"]["servers"].keys())[0]
        return int(server_id)
    fallback = list(data["EU - Free"]["servers"].keys())[0]
    return int(fallback)

def spawn_box(machine_id, server_id=None):
    payload = {"machine_id": machine_id}
    if server_id:
        payload["server_id"] = server_id
    r = requests.post(f"{HTB_API}/vm/spawn", headers=HEADERS, json=payload)
    r.raise_for_status()
    print("[+] Spawn response:", r.json()["message"])

def download_tcp_vpn(server_id):
    r = requests.get(f"{HTB_API}/access/ovpnfile/{server_id}/0/1", headers=HEADERS)
    r.raise_for_status()
    vpn_path = DOWNLOADS / "htb_tcp.ovpn"
    vpn_path.write_bytes(r.content)
    with open(vpn_path, "a") as vpn_file:
        vpn_file.write("\nscript-security 2\n")
        vpn_file.write("up /etc/openvpn/update-resolv-conf\n")
        vpn_file.write("down /etc/openvpn/update-resolv-conf\n")
    print("[+] Downloaded vpn at " + str(vpn_path))
    return vpn_path

def start_openvpn(vpn_path):
    subprocess.Popen(["sudo", "openvpn", "--config", str(vpn_path)])

def start_exegol(vpn_path, box):
    exegol_bin = os.path.expanduser("~/.local/bin/exegol")
    cmd = f"sudo -E {exegol_bin} start {box['name']} --vpn {vpn_path} -V {DOWNLOADS}:/Downloads"
    print("[i] Running command:", cmd)
    subprocess.run(cmd, shell=True)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--box")
    parser.add_argument("--chall")
    parser.add_argument("--exegol", action="store_true")
    parser.add_argument("--ovpn", action="store_true")
    args = parser.parse_args()

    if not args.box:
        sys.exit(1)

    #if os.geteuid() != 0:
    #    print("[-] This script must be run with sudo/root privileges.")
    #    print("[i] Please re-run with: sudo faster [args]")
    """   sys.exit(1)"""

    box = get_box_profile(args.box)
    if not box:
        sys.exit(1)

    wait_until_release(box.get("release"))
    print(box)
    if box["playInfo"]["isSpawned"]:
        server_id = None
    else:
        server_id = get_arena_server()
        spawn_box(box["id"], server_id=server_id)

    vpn_path = download_tcp_vpn(server_id if server_id else 0)
    box_ip = print("[+] Spawned box: IP is " + box["ip"])
    if args.ovpn:
        start_openvpn(vpn_path)
        time.sleep(10)

    if args.exegol:
        start_exegol(vpn_path, box)

if __name__ == "__main__":
    main()


# Ecrire dans le /etc/hosts l'ip de la box et le nom de la box .htb.