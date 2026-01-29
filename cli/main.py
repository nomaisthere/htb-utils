#!/usr/bin/env python3
import argparse

from cli.box import box_up, box_down
from cli.submit import submit_cmd
from cli.status import status_cmd

def main():
    parser = argparse.ArgumentParser(prog="htb")
    sub = parser.add_subparsers(dest="cmd", required=True)
    up = sub.add_parser("up")
    up.add_argument("box")
    up.set_defaults(func=box_up)
    down = sub.add_parser("down")
    down.set_defaults(func=box_down)
    submit = sub.add_parser("submit")
    submit_cmd(submit)
    status = sub.add_parser("status")
    status_cmd(status)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
