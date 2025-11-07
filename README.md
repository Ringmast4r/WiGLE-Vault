# WiGLE Vault 🛰️

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![GitHub stars](https://img.shields.io/github/stars/Ringmast4r/WiGLE-Vault?style=social)
![GitHub forks](https://img.shields.io/github/forks/Ringmast4r/WiGLE-Vault?style=social)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)

Download ALL your WiGLE wardriving data in one command.

---

## 🎯 Quick Start (Choose Your Method)

### Option A: Windows Executable (No Coding Required!)

**Perfect for non-technical users!**

1. Download the latest release from the [Releases page](https://github.com/Ringmast4r/WiGLE-Vault/releases)
2. Extract the ZIP file
3. Double-click `RUN_ME.bat` (or `WiGLE-Vault.exe`)
4. Paste your WiGLE token when prompted
5. Press ENTER and wait for downloads to complete

**Features:**
- ✅ No Python installation needed
- ✅ Single-click execution
- ✅ Automatic progress tracking
- ✅ Resumes interrupted downloads
- ✅ Complete instructions included

📖 See `README_FOR_YOUR_PARTNER.txt` in the download for detailed instructions.

---

### Option B: Python Script (For Developers)

## How to Use (3 Steps)

### Step 1: Run the Script

```bash
python wigle_vault.py
```

### Step 2: Get Your Token When Prompted

The script will ask you to:
1. Visit https://wigle.net/account
2. Click **"Show my token"**
3. Copy the **"Encoded for use"** value
4. Paste it into the command prompt

### Step 3: Done!

All your CSVs download to the `vault` folder.

**💡 Download Interrupted or Failed?**
Just run the script again! It automatically skips files that already exist. Only missing files get downloaded.

**Works for:**
- Network timeouts
- Power loss
- Accidentally closing the window
- Large files that timed out

No wasted bandwidth. No duplicate downloads.

---

**Advanced:** You can also provide the token as an argument:
```bash
python wigle_vault.py YOUR_TOKEN_HERE
```

---

## What You Need

- Python 3.6 or newer
- `requests` library (install: `pip install requests`)

---

## What It Does

- Downloads every CSV file you ever uploaded to WiGLE
- Handles files of ANY size (even 100+ MB cross-country logs)
- Skips files that already exist (fully resumable)
- Shows progress as it downloads
- Works on Windows, Mac, Linux
- Streaming downloads for memory efficiency

---

## Example Output

```
============================================================
🛰️  WiGLE Vault - Wardriving Data Backup Tool
    Version 1.0.0
============================================================
📂 Download location: C:\Users\You\wigle_backup

📄 Fetching page 1...
   Found 43 transaction(s) on this page
   ⬇️  Downloading 12345678.csv... ✅ (1,234,567 bytes)
   ⬇️  Downloading 12345679.csv... ✅ (987,654 bytes)
   ⏭️  Skipping 12345680.csv (already exists, 2,345,678 bytes)
   ...

============================================================
🎉 Download Complete!
============================================================
📊 Total uploads found:        43
⬇️  Successfully downloaded:   42
⏭️  Skipped (already existed): 1
💾 Total data size:            52,345,678 bytes (49.92 MB)
📂 Location:                   C:\Users\You\wigle_backup

💡 Next Steps:
   • Import these CSVs into your GIS software or analysis tools
   • Backup these files to cloud storage
   • Keep them safe - this is YOUR wardriving history!
```

---

## Requirements

- **Python 3.6+**
- **requests library** (install with `pip install requests`)

---

## Use Cases

### 📊 Data Analysis
Import your CSVs into tools like:
- **QGIS** - Geographic information system
- **Excel/Google Sheets** - Spreadsheet analysis
- **Python/R** - Custom data science workflows
- **Wireshark** - Network analysis and mapping

### 💾 Backup Strategy
- Keep local copies of your wardriving history
- Archive data before deleting from WiGLE
- Migrate data to other platforms
- Share datasets with research teams

### 🔒 Privacy & Control
- Your data belongs to you
- No vendor lock-in
- Full offline access
- Complete data portability

---

## Installation

### Option 1: Direct Download
```bash
# Download the script
curl -O https://raw.githubusercontent.com/Ringmast4r/WiGLE-Vault/main/wigle_vault.py

# Install dependencies
pip install requests

# Run it
python wigle_vault.py <your-token>
```

### Option 2: Clone Repository
```bash
git clone https://github.com/Ringmast4r/WiGLE-Vault.git
cd WiGLE-Vault
pip install -r requirements.txt
python wigle_vault.py <your-token>
```

---

## Common Questions

**Is this safe?**
Yes - uses official WiGLE API, read-only access, open source code.

**Can anyone intercept my data?**
NO! Direct HTTPS connection to WiGLE servers. Your data goes straight from WiGLE to your computer - nobody in between.

**Can I stop and resume?**
YES! Just run it again. It will skip every file that already downloaded and only grab what's missing. Works even if:
- Your internet cuts out
- A large file times out
- You accidentally close the window
- Your computer restarts

**How long does it take?**
Depends on file sizes. Small files = 1-2 seconds. Massive 100+ MB logs might take a few minutes each. 100 uploads usually takes 5-10 minutes total.

**Keep token secret?**
YES! Don't share it, don't commit it to git.

---

## Problems?

**401 Error** - Wrong token. Copy "Encoded for use" (not plain token).

**Network Error** - Check internet connection, try again later.

---

## License

MIT License

Created by Ringmast4r for the wardriving community.
