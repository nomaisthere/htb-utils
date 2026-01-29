from api.active import get_active_machine, NoActiveMachine

def status_cmd(parser):
    parser.set_defaults(func=run)

def run(args):
    try:
        m = get_active_machine()
    except NoActiveMachine:
        print("[-] No active machine")
        return

    print("[+] Active machine")
    print(f"    Name: {m['name']}")
    print(f"    IP:   {m['ip']}")
    print(f"    Type: {m['type']}")
    print(f"{m}")
