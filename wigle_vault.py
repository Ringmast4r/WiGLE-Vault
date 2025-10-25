"""
WiGLE Vault - Backup Your Wardriving Data
Download all your uploaded WiGLE data as CSV files

Author: Ringmast4r
Repository: https://github.com/Ringmast4r/WiGLE-Vault
License: MIT

Usage: python wigle_vault.py <your-encoded-token>
Get token from: https://wigle.net/account (click "Show my token" -> copy "Encoded for use")
"""

import sys
import os

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')

import requests
import time
from pathlib import Path

# WiGLE API endpoints
TRANSACTIONS_URL = "https://api.wigle.net/api/v2/file/transactions"
CSV_DOWNLOAD_URL = "https://api.wigle.net/api/v2/file/csv/{}"

__version__ = "1.0.0"

def download_wigle_data(token, output_dir=None):
    """Download all WiGLE CSV files for the authenticated user"""

    # Create download folder if not specified
    if not output_dir:
        output_dir = "vault"

    # Get absolute path before changing directory
    download_path = os.path.abspath(output_dir)

    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)

    # Setup authentication headers
    auth_header = {"Authorization": f"Basic {token}"}

    # Headers for transaction list API (returns JSON)
    json_headers = {
        **auth_header,
        "Accept": "application/json",
        "User-Agent": f"WiGLE-Vault/{__version__}"
    }

    # Headers for CSV download (returns text/csv)
    csv_headers = {
        **auth_header,
        "Accept": "text/csv, text/plain, */*",
        "User-Agent": f"WiGLE-Vault/{__version__}"
    }

    print("=" * 60)
    print("🛰️  WiGLE Vault - Wardriving Data Backup Tool")
    print(f"    Version {__version__}")
    print("=" * 60)
    print(f"📂 Saving to: {download_path}\n")

    # Track statistics
    total_files = 0
    downloaded = 0
    skipped = 0
    failed = 0
    total_bytes = 0

    # Paginate through all transactions
    page = 0
    page_size = 100

    while True:
        print(f"📄 Fetching page {page + 1}...")

        # Get transaction list
        params = {
            "pagestart": page * page_size,
            "pageend": (page + 1) * page_size
        }

        try:
            response = requests.get(TRANSACTIONS_URL, headers=json_headers, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching transactions: {e}")
            if hasattr(e, 'response') and e.response is not None:
                if e.response.status_code == 401:
                    print("\n🔒 Authentication failed! Check your token.")
                    print("Get your token from: https://wigle.net/account")
                    print("Click 'Show my token' and copy 'Encoded for use' value")
            sys.exit(1)

        # Extract transaction IDs
        if "results" not in data or not data["results"]:
            print(f"✅ Reached end of uploads (page {page + 1} is empty)\n")
            break

        transactions = data["results"]
        print(f"   Found {len(transactions)} transaction(s) on this page")

        # Download each CSV
        for transaction in transactions:
            trans_id = transaction.get("transid")
            if not trans_id:
                continue

            total_files += 1
            filename = f"{trans_id}.csv"

            # Skip if already exists
            if os.path.exists(filename):
                file_size = os.path.getsize(filename)
                print(f"   ⏭️  Skipping {filename} (already exists, {file_size:,} bytes)")
                skipped += 1
                total_bytes += file_size
                continue

            # Download CSV
            try:
                print(f"   ⬇️  Downloading {filename}...", end=" ", flush=True)
                csv_url = CSV_DOWNLOAD_URL.format(trans_id)

                # Longer timeout for massive files (10 minutes)
                # Some wardrivers have 100+ MB logs from cross-country trips
                csv_response = requests.get(csv_url, headers=csv_headers, timeout=600, stream=True)
                csv_response.raise_for_status()

                # Save to file with streaming for large files
                file_size = 0
                with open(filename, 'wb') as f:
                    for chunk in csv_response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            file_size += len(chunk)

                total_bytes += file_size

                # Show file size in human-readable format
                if file_size > 1024 * 1024:
                    size_str = f"{file_size / 1024 / 1024:.2f} MB"
                elif file_size > 1024:
                    size_str = f"{file_size / 1024:.2f} KB"
                else:
                    size_str = f"{file_size} bytes"

                print(f"✅ ({size_str})")
                downloaded += 1

                # Be nice to the WiGLE API
                time.sleep(0.5)

            except requests.exceptions.RequestException as e:
                print(f"❌ Failed: {e}")
                failed += 1

        # Check if this was the last page
        if len(transactions) < page_size:
            print(f"✅ Reached end of uploads (final page had {len(transactions)} results)\n")
            break

        page += 1

    # Summary
    print("=" * 60)
    print("🎉 Download Complete!")
    print("=" * 60)
    print(f"📊 Total uploads found:        {total_files:,}")
    print(f"⬇️  Successfully downloaded:   {downloaded:,}")
    print(f"⏭️  Skipped (already existed): {skipped:,}")
    if failed > 0:
        print(f"❌ Failed:                     {failed:,}")
    print(f"💾 Total data size:            {total_bytes:,} bytes ({total_bytes / 1024 / 1024:.2f} MB)")
    print(f"📂 Saved to:                   {download_path}")
    print("\n💡 Next Steps:")
    print("   • Import these CSVs into your GIS software or analysis tools")
    print("   • Backup these files to cloud storage")
    print("   • Keep them safe - this is YOUR wardriving history!")
    print("\n- Love, Ringmast4r <3")
    print()

def main():
    """Main entry point"""

    print("=" * 60)
    print("🛰️  WiGLE Vault - Wardriving Data Backup Tool")
    print(f"    Version {__version__}")
    print("=" * 60)
    print()

    # Check if token provided as argument
    if len(sys.argv) >= 2:
        token = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        # Interactive mode - prompt user for token
        print("📖 How to get your token:")
        print("   1. Visit https://wigle.net/account")
        print("   2. Click 'Show my token'")
        print("   3. Copy the 'Encoded for use' value")
        print()

        token = input("🔑 Paste your WiGLE token here: ").strip()

        if not token:
            print("\n❌ Error: No token provided")
            sys.exit(1)

        output_dir = None
        print()

    download_wigle_data(token, output_dir)

if __name__ == "__main__":
    main()
