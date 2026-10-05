# 🌿 GreenOS - Lưu trữ & Đồng bộ Phiên Chat Antigravity

Repository này chứa bản sao lưu hoàn chỉnh của phiên chat Antigravity, bảo toàn 100% lịch sử thảo luận, các đoạn code HTML/CSS/JS và dữ liệu session.

---

## 📂 Danh sách tệp trong kho lưu trữ

1. **`chat_history.html`**:
   - Giao diện Web hiển thị toàn bộ nội dung chat, câu hỏi đáp và code có syntax highlighting.
   - **Cách dùng:** Bạn chỉ cần click đúp chuột mở file này bằng bất kỳ trình duyệt nào (Chrome, Edge, Safari...) trên máy tính hoặc điện thoại để xem lại toàn bộ nội dung mà không cần cài Antigravity.

2. **`chat_session_83581842.zip`**:
   - Gói dữ liệu gốc của Antigravity (chứa toàn bộ `transcript.jsonl`, artifacts, task logs).

3. **`restore.sh`** & **`restore.bat`**:
   - Script tự động khôi phục phiên chat vào Antigravity trên Máy 2 chỉ bằng 1 click.

---

## 🚀 Hướng dẫn mở tiếp tục trên Máy 2

### Cách 1: Tự động bằng Script (Khuyên dùng)
1. Trên Máy 2, clone repository này về:
   ```bash
   git clone git@github.com:thietkenexs2026-max/GreenOS.git
   cd GreenOS
   ```
2. Chạy script khôi phục:
   - **Nếu Máy 2 là macOS / Linux:**
     ```bash
     ./restore.sh
     ```
   - **Nếu Máy 2 là Windows:**
     - Click đúp chuột vào file `restore.bat`.
3. Tắt hẳn ứng dụng Antigravity rồi mở lại. Đoạn chat sẽ xuất hiện trong danh sách lịch sử để bạn tiếp tục trao đổi!

---

### Cách 2: Xem nhanh không cần Antigravity
- Mở trực tiếp file `chat_history.html` bằng trình duyệt web.
