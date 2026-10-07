@echo off
chcp 65001 >nul
echo 📦 Đang khôi phục toàn bộ phiên chat vào Antigravity...

set "DEST_DIR=%USERPROFILE%\.gemini\antigravity\brain"
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

set FOUND=0
for %%f in ("%~dp0chat_session_*.zip") do (
    echo  -^> Đang giải nén: %%~nxf
    tar -xf "%%f" -C "%DEST_DIR%"
    set FOUND=1
)

if %FOUND%==0 (
    echo ❌ Không tìm thấy file zip phiên chat!
    pause
    exit /b 1
)

echo ✅ ĐÃ KHÔI PHỤC TOÀN BỘ PHIÊN CHAT THÀNH CÔNG!
echo 👉 Hãy khởi động lại ứng dụng Antigravity để tiếp tục.
pause
