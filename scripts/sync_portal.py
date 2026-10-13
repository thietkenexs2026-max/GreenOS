#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GreenOS - Script tự động đồng bộ index.html vào PORTAL.html và xuất bản
"""
import os
import shutil
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_FILE = os.path.join(REPO_DIR, "index.html")
PORTAL_FILE = os.path.join(REPO_DIR, "PORTAL.html")

if not os.path.exists(INDEX_FILE) or not os.path.exists(PORTAL_FILE):
    print("Không tìm thấy index.html hoặc PORTAL.html tại repository.")
    exit(0)

# 1. Đọc index.html
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    index_html = f.read()

# 2. Đọc và cập nhật PORTAL.html
with open(PORTAL_FILE, "r", encoding="utf-8") as f:
    portal = f.read()

tag_open = '<template id="rawMobileCode">'
tag_close = '</template>'

start_pos = portal.find(tag_open)
end_pos = portal.find(tag_close, start_pos)

if start_pos != -1 and end_pos != -1:
    new_portal = portal[:start_pos + len(tag_open)] + index_html + portal[end_pos:]
    with open(PORTAL_FILE, "w", encoding="utf-8") as f:
        f.write(new_portal)
    print("✓ Đã đồng bộ index.html vào template PORTAL.html")
else:
    print("Không tìm thấy tag rawMobileCode trong PORTAL.html")

# 3. Đồng bộ sang Desktop và Downloads
dest_desktop = "/Users/hoangminhduc/Desktop/PORTAL_GREENOS.html"
dest_downloads = "/Users/hoangminhduc/Downloads/PORTAL_GREENOS.html"

try:
    if os.path.exists("/Users/hoangminhduc/Desktop"):
        shutil.copyfile(PORTAL_FILE, dest_desktop)
        print(f"✓ Đã sao chép sang: {dest_desktop}")
except Exception as e:
    print(f"Lỗi sao chép Desktop: {e}")

try:
    if os.path.exists("/Users/hoangminhduc/Downloads"):
        shutil.copyfile(PORTAL_FILE, dest_downloads)
        print(f"✓ Đã sao chép sang: {dest_downloads}")
except Exception as e:
    print(f"Lỗi sao chép Downloads: {e}")
