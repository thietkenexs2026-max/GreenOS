# Lịch Sử Trao Đổi & Tiến Trình Phát Triển GreenOS

Tài liệu này lưu trữ toàn bộ các yêu cầu, phản hồi và quyết định thiết kế xuyên suốt dự án **GreenVillageOS**.

---

## 📅 Dòng Sự Kiện & Các Yêu Cầu Của Người Dùng

### Giai đoạn 1: Khởi tạo ý tưởng & Thiết lập Design System
- **Yêu cầu 1-6**: Phân tích tài liệu gốc, xác định mô hình nền tảng số hóa nông thôn đa tầng (Hộ nông dân $\rightarrow$ HTX $\rightarrow$ Hub Xã $\rightarrow$ Lãnh đạo Xã). Người dùng nhấn mạnh tệp khách hàng nông dân là những người lớn tuổi, đòi hỏi giao diện rõ ràng, cực kỳ đơn giản và dễ thao tác.
- **Yêu cầu 7-12**: Người dùng chia sẻ hình ảnh tham khảo Scout Voice-First UI (`media_1791194189767.png`), yêu cầu thiết lập bộ Design System bài bản với skill `ui-ux-pro-max` trước khi code.
- **Quyết định**: Xây dựng file `design-system.md` và `tokens.css` chuẩn quy cách Figma tokens, màu xanh nông nghiệp đặc trưng (`#15803D`, `#166534`), tỷ lệ cong lớn (`var(--radius-pill)`), cấu trúc giao diện mobile chuẩn iPhone 16 Pro ($414\text{px} \times 870\text{px}$).

---

### Giai đoạn 2: Hiện thực hóa Persona 1 — Hộ Nông Dân (Bác Ba)
- **Yêu cầu 13-14**: "Giao diện nhìn AI quá, tôi muốn làm hiện đại như mấy mẫu tôi gửi".
  - *Giải pháp*: Tái cấu trúc lại layout theo phong cách Scout, chuyển từ form nhập liệu truyền thống sang Voice-First + Card-based.
- **Yêu cầu 15-18**: Bóc tách trải nghiệm người dùng già:
  - Phải có **Giao diện mở đầu (Trang chủ)** khi người dùng mở ứng dụng trước khi vào đăng bán.
  - Phải chia thành **quy trình theo bước (Wizard 3 bước)** rõ ràng, tuyệt đối không gom chung vào 1 màn hình gây bối rối cho người già.
- **Yêu cầu 19**: Tạo ảnh thực tế cho sản phẩm, phóng to ảnh và mô phỏng việc chia sẻ sang Zalo.
  - *Giải pháp*: Tạo ảnh thực tế túi chuối sấy giòn mặt trước, mặt sau bảng dinh dưỡng; xây dựng màn mô phỏng app Zalo native (Nhật Ký & Nhóm chat).

---

### Giai đoạn 3: Tinh chỉnh điều hướng, Banners & Quản lý đơn hàng
- **Yêu cầu 20-21**: "điều chỉnh lại các nút nhé, với cả không có thanh menu ở cho user dùng à" $\rightarrow$ Bổ sung thanh điều hướng đáy Native 5-tab đối xứng (`Trang chủ`, `Kho hàng`, `Đăng bán ➕`, `Chợ Xã`, `Hỗ trợ Hub`).
- **Yêu cầu 22-24**: 
  - Thêm section banner khuyến mại kích cầu nông sản trên cùng với hiệu ứng trượt tự động.
  - Giảm chiều cao banner xuống $112\text{px}$ để đảm bảo vừa vặn màn hình.
  - Tạo lại banner panorama không bị crop chữ (Hội Chợ Tết & Hội Chợ OCOP).
- **Yêu cầu 25-26**:
  - Hỗ trợ đăng nhiều ảnh trong 1 sản phẩm: Thêm ảnh chụp đĩa chuối sấy thật giòn rụm (`banana_plate.jpg`), bộ gallery thumbnail chuyển ảnh nhanh và lưới 3 ảnh chuẩn Zalo.
  - Thu gọn thẻ Trợ lý bán hàng.
  - Bổ sung section 2 thẻ thống kê: **Đơn hàng đã bán (18 đơn)** và **Doanh thu tháng (3.850.000 đ)**, bấm vào chuyển sang màn hình con chi tiết. Toàn bộ nội dung trang chủ phải **Fit Screen (không cuộn)**.
- **Yêu cầu 27-28**:
  - Thẻ CTA đăng bán sản phẩm mới chuyển sang nền xanh lá đồng bộ thương hiệu Green Village.
  - Tạo avatar chân thực cho Bác Ba (`bac_ba_avatar.jpg`), loại bỏ nhãn "Thí điểm 90 ngày".
- **Yêu cầu 29**: Bỏ biểu tượng icon (📦 và 💰) ở 2 thẻ doanh thu và đơn hàng để giao diện thoáng, tinh tế theo phong cách typographic.

---

### Giai đoạn 4: Trợ năng & Typography cho Người Lớn Tuổi
- **Yêu cầu 30**: "dùng tất cả font inter đi"
  - *Giải pháp*: Nhúng Google Font `Inter` đầy đủ trọng số (400, 500, 600, 700, 800, 900), cấu hình biến toàn cục `--font-sans` và ép kế thừa toàn bộ các thẻ nhập liệu, nút bấm.
- **Yêu cầu 31**: "căn chỉnh lại text nhé đang sát nhau, với cả tăng kích thước chữ lên cho người dùng cao tuổi mà"
  - *Giải pháp*:
    - Tăng `line-height` toàn diện lên $1.5 - 1.65$.
    - Mở rộng đệm và khoảng cách giữa các nhãn, số liệu, dòng mô tả.
    - Nâng cấp toàn bộ thang kích thước chữ: loại bỏ chữ nhỏ dưới $12\text{px}$, chữ thân đạt $15\text{px} - 16\text{px}$, tiêu đề $18.5\text{px} - 22.5\text{px}$, số liệu thống kê $20\text{px} - 32\text{px}$.
- **Yêu cầu 32-33**: Đẩy toàn bộ code và lịch sử trao đổi lên GitHub repository GreenOS.

---

### Giai đoạn 5: Hiện thực hóa Persona 2 — Quản Lý Hợp Tác Xã (HTX Đồng Cát) trên Web PC
- **Yêu cầu 34**: "giờ triển khai làm dashboard cho hợp tác xã nhé, build trên web pc"
  - *Giải pháp*:
    - Xây dựng file `htx-dashboard.html` chuẩn Desktop SaaS Web (1440px+ responsive).
    - **Header & Chỉ số đồng bộ**: Kết nối trực tiếp Shopee Mall, TikTok Shop, Zalo OA Nông Sản Xã, Cổng điều hành Xã Yên Bình.
    - **Hệ thống 6 Tab điều hành**:
      1. *Tổng quan chỉ số*: 4 KPI Card (Doanh thu đa kênh 148tr, Sản lượng 12.4 tấn, Hồ sơ chờ duyệt, 685 đơn xuất kho).
      2. *Duyệt nông sản xã viên (Product Approval)*: Xem ảnh chụp thực tế từ vườn của Bác Ba (`banana_front.jpg`, `banana_plate.jpg`, `banana_back.jpg`), đối chiếu đoạn ghi âm giọng nói giá bán (Voice-First), cấu hình tỷ lệ chiết khấu HTX, phê duyệt 1-chạm đẩy thẳng lên sàn TMĐT.
      3. *Order Hub đa kênh*: Gom đơn sỉ B2B WinMart 1.200 túi + đơn lẻ Shopee/TikTok/Zalo, in phiếu vận đơn kèm mã QR Trace.
      4. *Kho hàng & Bao bì*: Theo dõi tồn kho thực tế, kết nối và đặt in 3.000 túi zipper màng nhôm với xưởng in bao bì Tân Á Hưng Yên.
      5. *AI Content & Livestream Studio*: Trợ lý AI tạo kịch bản Livestream TikTok, caption Zalo OA và mô tả Shopee Mall chuẩn SEO & OCOP.
      6. *Báo cáo BLĐ Xã*: Mẫu báo cáo định kỳ kinh tế số, xuất file Excel và PDF gửi UBND Xã Yên Bình.
    - **Liên kết 2 chiều**: Tích hợp nút chuyển đổi nhanh giữa App Mobile Bác Ba (`index.html`) và Dashboard Quản lý HTX (`htx-dashboard.html`).

---

## 💡 Đúc Kết Thiết Kế Cho Nông Dân & Người Lớn Tuổi

1. **Voice-First thay thế bàn phím**: Người già tay run, mắt kém, ngại gõ bàn phím ảo. Nút micro to bản kèm trích dẫn văn bản trực quan giúp họ làm chủ ứng dụng ngay lần đầu.
2. **Âm thanh phản hồi (Loa đọc to bài viết)**: Cho phép bà con nghe kiểm chứng nội dung bằng tai trước khi đăng bán.
3. **Thị giác rõ ràng (High Contrast & Large Font)**: Nền sạch, chữ đậm, độ tương phản cao, phông Inter dễ đọc, không dùng icon rườm rà.
4. **Hệ sinh thái Zalo thân thuộc**: Kết nối thẳng với thói quen bán hàng qua Zalo của nông dân Việt Nam.
