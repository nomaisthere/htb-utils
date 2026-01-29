import sys
import time

from api.machines import get_box_profile, spawn_box
from api.arena import get_arena_server
from api.vpn import download_tcp_vpn
from utils.time import wait_until_release
from utils.system import start_openvpn
from core.exegol import start_exegol

def box_cmd(parser):
    parser.add_argument("name", help="Box name")
    parser.add_argument("--ovpn", action="store_true")
    parser.add_argument("--exegol", action="store_true")
    parser.set_defaults(func=run)

def run(args):
    box = get_box_profile(args.name)
    if not box:
        print("[-] Box not found")
        sys.exit(1)

    wait_until_release(box.get("release"))

    if not box["playInfo"]["isSpawned"]:
        server_id = get_arena_server()
        print(f"[+] Spawning on server {server_id}")
        spawn_box(box["id"], server_id)
    else:
        server_id = box["playInfo"]["server_id"]

    vpn_path = download_tcp_vpn(server_id)

    print(f"[+] Box IP: {box['ip']}")

    if args.ovpn:
        start_openvpn(vpn_path)
        time.sleep(8)

    if args.exegol:
        start_exegol(vpn_path, box)
