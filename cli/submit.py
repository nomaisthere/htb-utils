import sys
from api.submit import submit_flag, SubmitError

def submit_cmd(parser):
    parser.add_argument("flag", help="Flag to submit")
    parser.set_defaults(func=run)

def run(args):
    try:
        result = submit_flag(args.flag)
    except SubmitError as e:
        print("[-]", e)
        sys.exit(1)

    msg = result["response"].get("message", "Unknown response")
    machine = result["machine"]

    print(f"    {msg}")
    print(f"    Machine: {machine['name']} ({machine['ip']})")
