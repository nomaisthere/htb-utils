# give me the server blood pls

This script automates spawning Hack The Box (HTB) machines, downloading the VPN profile, and optionally launching Exegol for lab interaction. It uses the official [`hackthebox`](https://pypi.org/project/hackthebox/) Python client (`HTBClient`) instead of raw API calls, making the code cleaner and more maintainable.

---

## Features

- Fetch HTB machine profile by name.
- Wait until the box release time if not yet available.
- Automatically select an arena server (Release Arena preferred, fallback to Free server).
- Spawn a machine if not already spawned.
- Download the TCP VPN profile for the selected server.
- Start OpenVPN to connect to the HTB lab.
- Optionally start Exegol with the machine and VPN setup.

---

## Requirements

- Python 3.10+
- `hackthebox` Python package:  

```sh
pip install hackthebox
```

- HTB API token stored in the environment:

```sh
export HTB_TOKEN="your_api_token_here"
```

- openvpn installed if using --ovpn.
- exegol installed locally if using --exegol.

## Install

```sh
curl -fsSL https://example.com/install.sh | bash
```

## Usage

```sh
give-me-the-server-blood.py --box <box_name> [--ovpn] [--exegol]
```

## Options

- --box <box_name>: Required. The name of the HTB machine to spawn.
- --ovpn: Optional. Start OpenVPN automatically with the downloaded profile.
- --exegol: Optional. Launch Exegol to interact with the box.
- --chall: Placeholder for challenges (future support).

## Example

```sh
give-me-the-server-blood.py --box "Hercules" --ovpn --exegol
```

This will:

Check if Hercules is released.

Spawn it if not already running.

Download the TCP VPN file.

Start OpenVPN.

Launch Exegol for lab interaction.

## Notes

The script automatically waits until the box release time.

VPN is saved in ~/Downloads/htb_tcp.ovpn.

The script will ask you for sudo privileges for OpenVPN and Exegol.