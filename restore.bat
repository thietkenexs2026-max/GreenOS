@echo off
chcp 65001 >nul
echo 📦 Đang khôi phục phiên chat vào Antigravity...

set "DEST_DIR=%USERPROFILE%\.gemini\antigravity\brain"
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

for %%f in ("%~dp0chat_session_*.zip") do (
    tar -xf "%%f" -C "%DEST_DIR%"
    goto :done
)

echo ❌ Không tìm thấy file zip phiên chat!
pause
exit /b 1

:done
echo ✅ ĐÃ KHÔI PHỤC PHIÊN CHAT THÀNH CÔNG!
echo 👉 Hãy khởi động lại ứng dụng Antigravity để tiếp tục.
pause
