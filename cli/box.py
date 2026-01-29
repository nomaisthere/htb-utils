from api.machines import get_box_profile
from api.vm import spawn_machine, terminate_machine, wait_for_machine
from api.active import get_active_machine, NoActiveMachine

def box_up(args):
    box = get_box_profile(args.box)
    if not box:
        print("[-] Box not found")
        return

    print(f"[+] Spawning {box['name']}...")
    spawn_machine(box["id"])
    machine = wait_for_machine()
    print("[/] Machine ready: ", machine["name"])
    print("[+] IP: ", machine["ip"])

def box_down(args):
    try:
        machine = get_active_machine()
    except NoActiveMachine:
        print("[-] No active machine")
        return

    print(f"[+] Terminating {machine['name']}...")
    terminate_machine(machine["id"])
    print("[*] Machine terminated")
