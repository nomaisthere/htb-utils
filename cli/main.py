#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(prog="htb")
    sub = parser.add_subparsers(dest="cmd", required=True)
    up = sub.add_parser("up")
    up.add_argument("box")
    down = sub.add_parser("down")
    submit = sub.add_parser("submit")
    submit.add_argument("flag")
    status = sub.add_parser("status")
    args = parser.parse_args()

    if args.cmd == "up":
        from cli.box import box_up
        box_up(args.box)
    elif args.cmd == "down":
        from cli.box import box_down
        box_down()
    elif args.cmd == "submit":
        from cli.submit import submit
        submit(args.flag)
    elif args.cmd == "status":
        from cli.status import status
        status()

if __name__ == "__main__":
    main()
