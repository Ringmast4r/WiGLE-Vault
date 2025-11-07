#!/bin/bash
#
# WiGLE-Vault for macOS - One-Click Runner
# No installation or building required!
#
# Usage:
#   1. Download this file
#   2. Open Terminal
#   3. Run: bash wigle-vault-mac.sh
#

clear
echo "=========================================="
echo "  🛰️  WiGLE Vault - macOS Runner"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed."
    echo ""
    echo "Please install Python 3 from:"
    echo "https://www.python.org/downloads/"
    echo ""
    read -p "Press ENTER to exit..."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check/install requests library
echo "📦 Checking dependencies..."
python3 -c "import requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing requests library..."
    pip3 install --user requests --quiet
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install requests library"
        echo "Try running: pip3 install requests"
        read -p "Press ENTER to exit..."
        exit 1
    fi
fi

echo "✅ Dependencies ready"
echo ""

# Download the latest script if not present
if [ ! -f "wigle_vault.py" ]; then
    echo "📥 Downloading WiGLE-Vault script..."
    curl -sL https://raw.githubusercontent.com/Ringmast4r/WiGLE-Vault/main/wigle_vault.py -o wigle_vault.py
    if [ $? -ne 0 ]; then
        echo "❌ Failed to download script"
        read -p "Press ENTER to exit..."
        exit 1
    fi
    echo "✅ Script downloaded"
    echo ""
fi

# Run the script
echo "=========================================="
echo "  Starting WiGLE-Vault..."
echo "=========================================="
echo ""

python3 wigle_vault.py

# Keep window open after completion
echo ""
echo "=========================================="
echo "  Program finished!"
echo "=========================================="
echo ""
read -p "Press ENTER to close..."
