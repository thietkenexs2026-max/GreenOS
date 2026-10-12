#!/usr/bin/env bash
# =============================================================================
# GreenOS - Kịch bản tự động kiểm tra và Push Git định kỳ mỗi 2 tiếng
# Tự động bỏ qua nếu không có thay đổi và đã đồng bộ với GitHub
# =============================================================================

REPO_DIR="/Users/hoangminhduc/Downloads/GreenOS"
LOG_DIR="$REPO_DIR/logs"
LOG_FILE="$LOG_DIR/auto_git_sync.log"

mkdir -p "$LOG_DIR"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

cd "$REPO_DIR" || exit 1

# 1. Đồng bộ bản xuất bản PORTAL và file nén nếu có thay đổi index.html
if [ -f "$REPO_DIR/scripts/sync_portal.py" ]; then
  python3 "$REPO_DIR/scripts/sync_portal.py" >> "$LOG_FILE" 2>&1
fi

if [ -f "$REPO_DIR/index.html" ] && [ -f "$REPO_DIR/PORTAL.html" ]; then
  zip -r "$REPO_DIR/GreenOS_Export_HTML.zip" index.html PORTAL.html >> "$LOG_FILE" 2>&1
fi

# 2. Kiểm tra trạng thái thay đổi trong working directory
CHANGES=$(git status --porcelain)

# 3. Lấy thông tin nhánh hiện tại và kiểm tra commit chưa push
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")
git fetch origin "$CURRENT_BRANCH" --quiet 2>/dev/null

AHEAD_COMMITS=$(git rev-list --count origin/"$CURRENT_BRANCH"..HEAD 2>/dev/null || echo "0")

# 4. Nếu không có thay đổi và không có commit nào cần push -> Dừng lại (không update)
if [ -z "$CHANGES" ] && [ "$AHEAD_COMMITS" -eq 0 ]; then
  log "✓ Git sạch và đã đồng bộ hoàn toàn với GitHub ($CURRENT_BRANCH). Không có gì mới, bỏ qua."
  exit 0
fi

log "⚡ Phát hiện dữ liệu cần đồng bộ (Thay đổi chưa commit: $([ -n "$CHANGES" ] && echo 'Có' || echo 'Không'), Số commit chưa push: $AHEAD_COMMITS)."

# 5. Nếu có thay đổi mới chưa commit -> Tiến hành add và commit
if [ -n "$CHANGES" ]; then
  git add -A
  TIMESTAMP=$(date '+%d/%m/%Y %H:%M:%S')
  COMMIT_MSG="chore(auto): tu dong sao luu va dong bo code luc $TIMESTAMP"
  git commit -m "$COMMIT_MSG" >> "$LOG_FILE" 2>&1
  log "✓ Đã tạo commit mới: $COMMIT_MSG"
fi

# 6. Push lên GitHub
log "🚀 Đang push lên GitHub (nhánh $CURRENT_BRANCH)..."
if git push origin "$CURRENT_BRANCH" >> "$LOG_FILE" 2>&1; then
  log "✓ ĐÃ PUSH THÀNH CÔNG LÊN GITHUB ($CURRENT_BRANCH)."
else
  log "❌ Lỗi trong quá trình push lên GitHub. Bác kiểm tra log tại: $LOG_FILE"
  exit 1
fi
