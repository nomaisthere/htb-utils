from api.submit import submit_flag, SubmitError

def submit_cmd(parser):
    parser.add_argument("flag", help="Flag to submit")
    parser.set_defaults(func=submit)

def submit(args):
    try:
        result = submit_flag(args.flag)
    except SubmitError as e:
        print("[-]", (str(e)))
        return

    msg = result["response"].get("message", "OK")
    machine = result["machine"]
    print(msg)
    print("[+] Machine: ", machine["name"])
    print("[+] IP: ", machine["ip"])
