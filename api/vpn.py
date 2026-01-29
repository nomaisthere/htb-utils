from pathlib import Path
from api.client import get

DOWNLOADS = Path.home() / "Downloads"

def download_tcp_vpn(server_id):
    content = get(f"/access/ovpnfile/{server_id}/0/1")
    vpn_path = DOWNLOADS / "htb_tcp.ovpn"
    vpn_path.write_text(content if isinstance(content, str) else "")
    with open(vpn_path, "a") as f:
        f.write("\nscript-security 2\n")
        f.write("up /etc/openvpn/update-resolv-conf\n")
        f.write("down /etc/openvpn/update-resolv-conf\n")

    return vpn_path
