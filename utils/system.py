import subprocess

def start_openvpn(vpn_path):
    subprocess.Popen(["sudo", "openvpn", "--config", str(vpn_path)])
