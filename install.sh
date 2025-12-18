#!/usr/bin/env bash
set -euo pipefail

REPO_RAW="https://raw.githubusercontent.com/m0nkeydbus/give-me-the-server-blood-pls/refs/heads/main"

BIN_DIR="$HOME/.local/bin"
CONF_DIR="$HOME/.config/give-me-the-server-blood"
SHARE_DIR="$HOME/.local/share/give-me-the-server-blood"

BIN_NAME="give-me-the-server-blood"

echo "[*] Installing give-me-the-server-blood..."

mkdir -p "$BIN_DIR" "$CONF_DIR" "$SHARE_DIR"

echo "[*] Downloading executable..."
curl -fsSL "$REPO_RAW/give-me-the-server-blood.py" \
  -o "$BIN_DIR/$BIN_NAME"

chmod +x "$BIN_DIR/$BIN_NAME"

if [[ ! -f "$CONF_DIR/config.toml" ]]; then
  echo "[*] Installing default config..."
  curl -fsSL "$REPO_RAW/example_cnf.toml" \
    -o "$CONF_DIR/config.toml"
else
  echo "[i] Config already exists, skipping"
fi

echo
echo "[+] Installation complete!"
echo
echo "Binary installed at:"
echo "  $BIN_DIR/$BIN_NAME"
echo
echo "Config file:"
echo "  $CONF_DIR/config.toml"
echo
echo "Make sure ~/.local/bin is in your PATH:"
echo '  export PATH="$HOME/.local/bin:$PATH"'
echo
echo "Have fun... 🩸"
