import os
import glob
import shutil
from datetime import datetime
import time
import re
import sys
sys.stdout.flush()
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


# Setup paths
DOWNLOAD_DIR = r"C:\Users\-----\Downloads"
DEST_DIR = r"C:\Users\-----\OneDrive - -----.tech\FSOCIETY\_Data"

# Create destination folder
os.makedirs(DEST_DIR, exist_ok=True)

# Today's date
today_mmdd = datetime.now().strftime("%m%d")

# Match files
pattern = os.path.join(DOWNLOAD_DIR, "------Missouri-DIS*-Packages-Active.xlsx")
time.sleep(2)

files = glob.glob(pattern)
print(f"🗂️ Matched files: {len(files)}")
sys.stdout.flush()

for file_path in files:
    filename = os.path.basename(file_path)
    print(f"📄 Found: {filename}")
    sys.stdout.flush()

    match = re.search(r'DIS\d{6}', filename)
    if match:
        -----_code = match.group()
        new_name = f"{today_mmdd}-{-----_code}.xlsx"
        dest_path = os.path.join(DEST_DIR, new_name)

        # Check for collision and adjust filename if needed
        counter = 1
        while os.path.exists(dest_path):
            new_name = f"{today_mmdd}-{-----_code}-{counter}.xlsx"
            dest_path = os.path.join(DEST_DIR, new_name)
            counter += 1

        shutil.move(file_path, dest_path)
        print(f"✅ Moved: {filename} ➜ {new_name}")
        sys.stdout.flush()
        time.sleep(2)
    else:
        print(f"❌ ----- code not found in: {filename}")
        sys.stdout.flush()

