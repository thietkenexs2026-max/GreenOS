#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIP_FILE="$(ls "$SCRIPT_DIR"/chat_session_*.zip 2>/dev/null | head -n 1)"

if [ -z "$ZIP_FILE" ]; then
  echo "❌ Không tìm thấy file zip phiên chat trong thư mục này!"
  exit 1
fi

DEST_DIR="$HOME/.gemini/antigravity/brain"
mkdir -p "$DEST_DIR"

echo "📦 Đang bung dữ liệu chat vào: $DEST_DIR ..."
unzip -o "$ZIP_FILE" -d "$DEST_DIR"

echo "✅ ĐÃ KHÔI PHỤC PHIÊN CHAT THÀNH CÔNG!"
echo "👉 Hãy tắt hẳn Antigravity và mở lại để tiếp tục làm việc trên phiên chat này."
