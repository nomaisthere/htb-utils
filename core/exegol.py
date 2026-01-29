import os
import subprocess
from pathlib import Path

DOWNLOADS = Path.home() / "Downloads"

def start_exegol(vpn_path, box):
    exegol_bin = os.path.expanduser("~/.local/bin/exegol")
    cmd = (
        f"sudo -E {exegol_bin} start {box['name']} "
        f"--vpn {vpn_path} -V {DOWNLOADS}:/Downloads"
    )
    print("[i] Running:", cmd)
    subprocess.run(cmd, shell=True)
