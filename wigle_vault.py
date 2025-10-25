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
import requests
import os
import time
from pathlib import Path

# WiGLE API endpoints
TRANSACTIONS_URL = "https://api.wigle.net/api/v2/file/transactions"
CSV_DOWNLOAD_URL = "https://api.wigle.net/api/v2/file/csv/{}"

__version__ = "1.0.0"

def download_wigle_data(token, output_dir=None):
    """Download all WiGLE CSV files for the authenticated user"""

    # Use current directory if not specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        os.chdir(output_dir)

    # Setup authentication
    headers = {
        "Authorization": f"Basic {token}",
        "Accept": "application/json",
        "User-Agent": f"WiGLE-Vault/{__version__}"
    }

    print("=" * 60)
    print("🛰️  WiGLE Vault - Wardriving Data Backup Tool")
    print(f"    Version {__version__}")
    print("=" * 60)
    print(f"📂 Download location: {os.getcwd()}\n")

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
            response = requests.get(TRANSACTIONS_URL, headers=headers, params=params, timeout=30)
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
                csv_response = requests.get(csv_url, headers=headers, timeout=60)
                csv_response.raise_for_status()

                # Save to file
                with open(filename, 'wb') as f:
                    f.write(csv_response.content)

                file_size = len(csv_response.content)
                total_bytes += file_size
                print(f"✅ ({file_size:,} bytes)")
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
    print(f"📂 Location:                   {os.getcwd()}")
    print("\n💡 Next Steps:")
    print("   • Import these CSVs into AirFence or your GIS software")
    print("   • Backup these files to cloud storage")
    print("   • Keep them safe - this is YOUR wardriving history!")
    print()

def main():
    """Main entry point"""

    if len(sys.argv) < 2:
        print("=" * 60)
        print("🛰️  WiGLE Vault - Wardriving Data Backup Tool")
        print(f"    Version {__version__}")
        print("=" * 60)
        print("\n❌ Usage: python wigle_vault.py <your-encoded-token> [output-directory]")
        print("\n📖 How to get your token:")
        print("   1. Visit https://wigle.net/account")
        print("   2. Click 'Show my token'")
        print("   3. Copy the 'Encoded for use' value")
        print("   4. Run: python wigle_vault.py <paste-token-here>")
        print("\n📂 Optional: Specify output directory")
        print("   Example: python wigle_vault.py <token> ./my_wigle_data")
        print()
        sys.exit(1)

    token = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    download_wigle_data(token, output_dir)

if __name__ == "__main__":
    main()
