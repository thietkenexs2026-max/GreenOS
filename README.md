# GreenOS (GreenVillageOS) — Nền Tảng Số Hóa Nông Sản Xã

> **GreenVillageOS** là giải pháp nền tảng hệ điều hành số hóa nông nghiệp nông thôn, kết nối trực tiếp từ **Hộ Nông Dân** $\rightarrow$ **Hợp Tác Xã (HTX)** $\rightarrow$ **Hub Xã / Đoàn Thanh Niên** $\rightarrow$ **Thương Mại & Mạng Xã Hội (Zalo/Facebook)**.

---

## 📱 Điểm Nhấn Thiết Kế Persona: Hộ Nông Dân (Bác Ba - 62 tuổi)

Giao diện được may đo chuyên biệt cho đối tượng **người cao tuổi tại nông thôn**, giải quyết triệt để rào cản công nghệ theo triết lý **Voice-First & Visual-First**:

1. **Font chữ & Typography trợ năng (Inter)**:
   - Toàn bộ hệ thống sử dụng font **Inter** chuẩn quốc tế, sắc nét, hỗ trợ tiếng Việt đầy đủ.
   - Kích thước chữ được phóng to chuẩn trợ năng (chữ thân $15\text{px} - 16\text{px}$, tiêu đề $18\text{px} - 24\text{px}$, số liệu thống kê $20\text{px} - 32\text{px}$).
   - Giãn dòng rộng rãi (`line-height: 1.5 - 1.65`) giúp bà con đọc lướt dễ dàng, không gây mỏi mắt hay dính chữ.
2. **Quy trình 3 bước siêu đơn giản (Wizard Flow)**:
   - **Bước 1 — Chụp ảnh thực tế**: Hỗ trợ bộ sưu tập nhiều ảnh thực tế (Mặt trước bao bì, đĩa sản phẩm thật, mặt sau HSD/dinh dưỡng, tem OCOP).
   - **Bước 2 — Nói giá bán bằng giọng nói (Voice-First)**: Nút micro tròn to bản. Bác Ba chỉ cần nói một câu đời thường (ví dụ: *"Chuối sấy giòn túi 250 gam, bán năm mươi lăm nghìn một gói"*), AI tự động bóc tách khối lượng, giá tiền, hạn sử dụng.
   - **Bước 3 — Tạo bài đăng & Nghe đọc to**: Tự động sinh bài viết thương mại chân thực mộc mạc, có nút loa **"Bấm nghe đọc to bài viết"** để bà con kiểm tra bằng tai.
3. **Mô phỏng thực tế chia sẻ Zalo (Zalo Ecosystem Native)**:
   - Mô phỏng chính xác giao diện Zalo Nhật Ký với Album lưới 3 ảnh ($1\text{ lớn } + 2\text{ nhỏ}$) đạt độ tin cậy cao.
   - Hỗ trợ 1 chạm gửi vào Nhóm Nông Sản Xã (142 thành viên).
4. **Trang chủ Fit Screen (Không cần cuộn phức tạp)**:
   - Profile bác Ba với Avatar thực tế, địa phương hóa (*Xã Yên Bình · HTX Đồng Cát*).
   - Banner khuyến mại tự động trượt (Chiến dịch Tết & OCOP Toàn Quốc).
   - 2 thẻ thống kê tương tác: **Đơn đã bán (18 đơn)** & **Doanh thu tháng (3.850.000 đ)** — bấm vào để mở sổ chi tiết.
   - Thẻ trợ lý giọng nói xanh thương hiệu Green Village.
   - Kho sản phẩm và thanh điều hướng đáy 5 tab đối xứng chuẩn native mobile.

---

## 🗂 Cấu Trúc Dự Án

```
GreenOS/
├── index.html              # Ứng dụng Web di động hoàn chỉnh (CSS + HTML + Vanilla JS)
├── tokens.css              # Design Tokens (màu sắc, spacing, typography, shadow)
├── design-system.md        # Tài liệu đặc tả hệ thống thiết kế GreenVillageOS
├── design-system/          # Các tài liệu thành phần design system chi tiết
├── README.md               # Giới thiệu & hướng dẫn dự án
├── CHAT_HISTORY.md         # Toàn bộ lịch sử thảo luận, yêu cầu và tiến trình phát triển
├── chat_history.html       # Web App xem lại toàn bộ 65+ tin nhắn chat & code syntax
├── chat_session_742f8079.zip # Bản sao lưu đầy đủ session Antigravity (logs, artifacts, transcripts)
├── restore.sh              # Script 1-click khôi phục session trên macOS / Linux
├── restore.bat             # Script 1-click khôi phục session trên Windows
├── bac_ba_avatar.jpg       # Chân dung thực tế Bác Ba (Hộ nông dân)
├── tet_banner.jpg          # Banner panoramic Hội Chợ Tết 2024
├── ocop_banner.jpg         # Banner panoramic Hội Chợ OCOP
├── banana_front.jpg        # Ảnh bao bì mặt trước Chuối sấy giòn OCOP
├── banana_plate.jpg        # Ảnh đĩa chuối sấy thực tế giòn rụm
├── banana_back.jpg         # Ảnh mặt sau bảng thành phần dinh dưỡng & HSD
├── honey_front.jpg         # Ảnh Hũ mật ong hoa rừng tự nhiên OCOP 4 sao
└── tea_front.jpg           # Ảnh Túi Trà Bát Tiên Thái Nguyên OCOP 4 sao
```

---

## 💬 Xem Lại Lịch Sử Đoạn Chat & Khôi Phục Session Antigravity

Repository này lưu trữ đầy đủ 100% cuộc trao đổi và tiến trình xây dựng GreenOS:

### 1. Xem trực tiếp trên trình duyệt (Không cần cài đặt)
Mở file **`chat_history.html`** bằng trình duyệt bất kỳ (Chrome, Safari, Edge) để đọc lại toàn bộ 65+ lượt trao đổi, prompt engineering và code changes.

### 2. Khôi phục phiên làm việc vào Antigravity (1-Click Restore)
Để mở tiếp phiên làm việc này trên máy tính khác trong ứng dụng Antigravity:
- **macOS / Linux:**
  ```bash
  ./restore.sh
  ```
- **Windows:**
  Chạy file `restore.bat`.
- Khởi động lại Antigravity, phiên chat `742f8079` sẽ hiển thị đầy đủ trong lịch sử.

---

## 🚀 Hướng Dẫn Chạy Thử (Quick Start)

Không cần cài đặt framework phức tạp, chỉ cần chạy một máy chủ HTTP tĩnh:

```bash
# Sử dụng Python có sẵn:
python3 -m http.server 8080

# Hoặc dùng Node.js npx:
npx serve .
```

Mở trình duyệt truy cập: **`http://localhost:8080`**

---

## 🌿 Lộ Trình Phát Triển Tiếp Theo

- [x] **Persona 1 — Hộ Nông Dân (Bác Ba)**: Đăng bán bằng giọng nói, chia sẻ Zalo, sổ đơn hàng & doanh thu (`index.html`).
- [x] **Persona 2 — Hợp Tác Xã (HTX Đồng Cát)**: Dashboard Quản lý Web PC (`htx-dashboard.html`), duyệt nông sản Bác Ba (đối chiếu ảnh thật & giọng nói), Order Hub gom đơn sỉ B2B WinMart, kết nối xưởng bao bì & AI Content Studio.
- [ ] **Persona 3 — Hub Xã & Đoàn Thanh Niên**: Hỗ trợ trực tiếp bà con số hóa, thẩm định OCOP, quản lý điểm gom hàng.
- [ ] **Persona 4 — Lãnh Đạo Xã**: Bảng chỉ số điều hành kinh tế số nông nghiệp toàn xã theo thời gian thực.
