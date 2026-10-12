#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GreenOS - Tiến trình chạy ngầm tự động kiểm tra và Push Git mỗi 2 tiếng (7200 giây).
Nếu đã push rồi và không có thay đổi mới -> Tự động bỏ qua không cập nhật.
"""
import os
import subprocess
import time
from datetime import datetime

INTERVAL_SECONDS = 7200  # 2 tiếng = 7200s
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNC_SCRIPT = os.path.join(REPO_DIR, "scripts", "auto_git_sync.sh")
LOG_FILE = os.path.join(REPO_DIR, "logs", "auto_git_daemon.log")

def log(msg):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] [DAEMON] {msg}\n"
    print(line, end="", flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass

def run_sync():
    log("Bắt đầu chu kỳ kiểm tra Git tự động...")
    try:
        res = subprocess.run(
            ["/bin/bash", SYNC_SCRIPT],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            timeout=120
        )
        if res.stdout:
            for l in res.stdout.strip().splitlines():
                log(f"> {l}")
        if res.returncode == 0:
            log("Hoàn thành chu kỳ kiểm tra.")
        else:
            log(f"Lỗi (code {res.returncode}): {res.stderr}")
    except Exception as e:
        log(f"Ngoại lệ khi thực thi sync: {e}")

if __name__ == "__main__":
    log("Khởi động Daemon tự động Push Git GreenOS (Chu kỳ 2 tiếng = 7200s).")
    # Chạy lần đầu tiên để xác nhận trạng thái hiện tại
    run_sync()
    while True:
        time.sleep(INTERVAL_SECONDS)
        run_sync()
