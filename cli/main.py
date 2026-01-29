#!/usr/bin/env python3

import argparse
from cli.box import box_cmd
from cli.submit import submit_cmd
from cli.status import status_cmd

def main():
    parser = argparse.ArgumentParser(prog="htb", description="htb utils as cli")
    sub = parser.add_subparsers(dest="command", required=True)
    box_parser = sub.add_parser("box", help="Spawn and prepare a box")
    box_cmd(box_parser)
    submit_parser = sub.add_parser("submit", help="Submit a flag")
    submit_cmd(submit_parser)
    status_parser = sub.add_parser("status", help="Show active machine")
    status_cmd(status_parser)
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
