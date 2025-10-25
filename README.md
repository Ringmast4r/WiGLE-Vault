# WiGLE Vault 🛰️

Download ALL your WiGLE wardriving data in one command.

---

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
- Skips files that already exist (you can resume if interrupted)
- Shows progress as it downloads
- Works on Windows, Mac, Linux

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
   • Import these CSVs into AirFence or your GIS software
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
- **AirFence** - WiFi perimeter security analysis
- **QGIS** - Geographic information system
- **Excel/Google Sheets** - Spreadsheet analysis
- **Python/R** - Custom data science workflows

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

**Can I stop and resume?**
Yes - automatically skips files that already exist.

**How long does it take?**
~1-2 seconds per file. 100 uploads = ~5 minutes.

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
