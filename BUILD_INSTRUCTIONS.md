# Building WiGLE-Vault Executable

This guide explains how to build a standalone Windows executable from the Python source code.

## Prerequisites

- Python 3.6 or newer
- PyInstaller (`pip install pyinstaller`)
- requests library (`pip install requests`)

## Build Steps

### 1. Install Dependencies

```bash
pip install pyinstaller requests
```

### 2. Run PyInstaller

```bash
pyinstaller --onefile --console --name "WiGLE-Vault" wigle_vault.py
```

### 3. Find Your Executable

The executable will be created in:
```
dist/WiGLE-Vault.exe
```

## Creating a Distribution Package

### 1. Copy Files to Dist Folder

The following files should be included in the distribution:

```
dist/
├── WiGLE-Vault.exe
├── RUN_ME.bat
├── HOW_TO_USE.txt
└── README_FOR_YOUR_PARTNER.txt
```

### 2. Create RUN_ME.bat

Create a batch file that keeps the console window open after execution:

```batch
@echo off
title WiGLE-Vault - Wardriving Data Backup
color 0A
echo.
echo ========================================
echo    WiGLE-Vault is starting...
echo ========================================
echo.
WiGLE-Vault.exe
echo.
echo.
echo ========================================
echo    Program finished!
echo ========================================
echo.
pause
```

### 3. Create User Documentation

Create `HOW_TO_USE.txt` and `README_FOR_YOUR_PARTNER.txt` with step-by-step instructions for non-technical users.

See the templates in the `docs/` folder for reference.

## Distribution

### Option 1: GitHub Releases

1. Create a new release on GitHub
2. Tag it with a version number (e.g., v1.0.0)
3. Upload the entire `dist/` folder as a ZIP file
4. Users can download and extract without any setup

### Option 2: Direct ZIP

```bash
cd dist
zip -r WiGLE-Vault-Windows.zip *
```

## Troubleshooting

### "Module not found" errors

Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Executable is too large

This is normal. PyInstaller bundles Python and all libraries into a single file. Typical size: 10-15 MB.

### Antivirus false positives

Some antivirus software flags PyInstaller executables. This is a known issue with all PyInstaller builds. The source code is open and auditable.

## Build for Other Platforms

### macOS
```bash
pyinstaller --onefile --console --name "WiGLE-Vault" wigle_vault.py
```

### Linux
```bash
pyinstaller --onefile --console --name "WiGLE-Vault" wigle_vault.py
```

The process is identical on all platforms. PyInstaller will create a native executable for each OS.
