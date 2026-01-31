from api.active import get_active_machine, NoActiveMachine

def status_cmd(parser):
    parser.set_defaults(func=status)

def status(args):
    try:
        m = get_active_machine()
    except NoActiveMachine:
        print("[-] No active machine")
        return
    print("[+] Active machine:", m["name"])
    print("[+] IP:", m["ip"] or "spawning")