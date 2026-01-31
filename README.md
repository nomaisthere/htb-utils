# HTB Utils

HTB Utils is a fast CLI tool to interact with the Hack The Box API.  
Its primary goal is **fast flag submission**.  
The tool is designed to be lightweight and competitive.  
I don't care about it being a full cli, it justs submit flags faster.

## Features

- Spawn HTB machines by name
- Terminate active machines
- Display active machine status (name, IP)
- Submit flags directly to HTB
- Optimized for fast flag submission

## Requirements

- Python
- A machine with linux
- A HTB Account

## Installation

If you're on exegol, put it in the `.exegol/my-resources/bin/` on your machine.  

```bash
cd ~/.exegol/my-resources/bin/
git clone https://github.com/nomaisthere/htb-utils
cd htb-utils
pip install -r requirements.txt
chmod +x htb-utils
```

Then, go into`.exegol/my-resources/bin/`, and create a symlink to `htb-utils` :

```bash
cd ~/.exegol/my-resources/bin/
ln -s htb-utils/htb-utils htb
```

Then you can freely use `htb` as a command in your exegol.

## HTB API Token Setup (Permanent)

### Getting the token

Go on [https://app.hackthebox.com/account-settings](https://app.hackthebox.com/account-settings) and create a token.  

### Putting it in the env

For bash:

```bash
echo 'export HTB_TOKEN="your_api_token_here"' >> ~/.bashrc
source ~/.bashrc
```

Or if you have taste and have zsh:

```zsh
echo 'export HTB_TOKEN="your_api_token_here"' >> ~/.zshrc
source ~/.zshrc
```

then  

```sh
echo $HTB_TOKEN
```

If you have exegol, put it in your `~/.exegol/my-resources/setup/zsh/zshrc`.

## Usage

```bash
htb up <box_name>
htb down
htb status
htb submit <flag>
```

---  

Also, `htb submit` without parameters gives you a stdin in which you can paste the flags.  

```bash
htb submit
           
Enter flag > eeca76c4e4b80d2d6f3e236a6cfc7d62
Darkzero user is now owned.     
Enter flag > 5e75e6432207d047f2fe7ccd2f2ff55b
Darkzero root is now owned.
```

## Aliases (Recommended)

```bash
alias f='htb submit'
```

Now submit flags instantly:

```bash
f HTB{f4ke_fl4g}
```

You can do other ones of course. It's just easier with `f`.  
For persistence, also put the `alias f="htb submit"` into your `~/.exegol/my-resources/setup/zsh/zshrc`.

## Contributors

- Thanks to qu35t, having done the first version of htb-cli, this project is inspired from his.
- Big thanks to hunntr, for his ideas on how to make the tool more accessible.