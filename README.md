# HTB Utils

HTB Utils is a fast CLI tool to interact with the Hack The Box API.
Its primary goal is to **save time** for regular HTB users by automating
machine management and **instant flag submission**.

The tool is designed to be lightweight, scriptable, and competitive.

---

## Features

- Spawn HTB machines by name
- Terminate active machines
- Display active machine status (name, IP, type)
- Submit flags directly to HTB
- Automatic detection of active machine
- Zero configuration after install
- Optimized for fast flag submission

---

## Requirements

- Python **3.10+**
- HTB API token (environment variable)
- `requests` Python package

Optional:
- `openvpn` (if you manage VPN manually)
- `exegol` (if you integrate it later)

---

## Installation

```bash
git clone https://github.com/m0nkeydbus/htb-utils
cd htb-utils
pip install -r requirements.txt
chmod +x htb-utils
```

## HTB API Token Setup (Permanent)

```bash
echo 'export HTB_TOKEN="your_api_token_here"' >> ~/.bashrc
source ~/.bashrc
```

```zsh
echo 'export HTB_TOKEN="your_api_token_here"' >> ~/.zshrc
source ~/.zshrc
```

```sh
echo $HTB_TOKEN
```

## Usage

```bash
htb-utils up <box_name>
htb-utils down
htb-utils status
htb-utils submit <flag>
```

## Speed Aliases (Recommended)

```bash
alias htb=~/htb-utils/htb-utils
alias f='htb submit'
```

Now submit flags instantly:

`f HTB{f4ke_fl4g}`

## Contributors

- Thanks to qu35t, having done the first version of htb-cli, this project is inspired from his idea.
- Big thanks to hunntr, for his ideas on how to upgrade the project.