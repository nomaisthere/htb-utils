from api.submit import submit_flag, SubmitError
import sys

def submit_cmd(parser):
    parser.add_argument("flag", nargs="?", help="Flag to submit (optional, will read from stdin if omitted)")
    parser.set_defaults(func=submit)

def handle_submit(flag: str):
    try:
        result = submit_flag(flag)
    except SubmitError as e:
        print("[-]", str(e))
        return

    msg = result["response"].get("message", "OK")
    machine = result["machine"]
    print(msg)

def _handle_submit(flag: str):
    try:
        result = submit_flag(flag)
    except SubmitError as e:
        print("[-]", str(e))
        return
    msg = result["response"].get("message", "OK")
    machine = result["machine"]
    print(msg)
    print("[+] Machine:", machine["name"])
    print("[+] IP:", machine["ip"])
    print()

def submit(args):
    if args.flag:
        handle_submit(args.flag.strip())
        return
    while True:
        try:
            flag = input("Enter flag > ").strip()
        except EOFError:
            print()
            break
        if not flag:
            continue
        handle_submit(flag)