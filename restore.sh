#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIP_FILES=("$SCRIPT_DIR"/chat_session_*.zip)

if [ ! -e "${ZIP_FILES[0]}" ]; then
  echo "❌ Không tìm thấy file zip phiên chat trong thư mục này!"
  exit 1
fi

DEST_DIR="$HOME/.gemini/antigravity/brain"
mkdir -p "$DEST_DIR"

echo "📦 Đang bung dữ liệu các phiên chat vào: $DEST_DIR ..."
for zip in "${ZIP_FILES[@]}"; do
  if [ -f "$zip" ]; then
    echo " -> Đang giải nén: $(basename "$zip")"
    unzip -qo "$zip" -d "$DEST_DIR"
  fi
done

echo "✅ ĐÃ KHÔI PHỤC TOÀN BỘ PHIÊN CHAT THÀNH CÔNG!"
echo "👉 Hãy tắt hẳn Antigravity và mở lại để tiếp tục làm việc trên các phiên chat này."
