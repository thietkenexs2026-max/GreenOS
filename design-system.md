# GreenVillageOS — Design System & Token Architecture
*Phiên bản: 1.0.0 (Dựa trên tham chiếu Scout Voice-First UI & Đặc tả GreenVillageOS v2.1)*

---

## 1. TỔNG QUAN PHONG CÁCH & DNA THIẾT KẾ

Thiết kế lấy cảm hứng trực tiếp từ **giao diện Scout AI (ảnh tham chiếu)**:
1. **Voice-First & Realtime Entity Chips:** Đặt giọng nói làm kênh giao tiếp tự nhiên hàng đầu; AI vừa nghe vừa bóc tách ngay lập tức các thực thể thành thẻ dạng Pill có thể bấm chỉnh sửa (`Tên sản phẩm ˅`, `Khối lượng ˅`, `Giá bán ˅`).
2. **Card-Driven Minimalism:** Mọi thông tin đều được đóng gói trong các thẻ viền bo tròn mềm mại (`radius: 18px–24px`), đường viền siêu mảnh 1px (`#E5E7EB`), bóng đổ cực nhẹ (`shadow-sm`).
3. **Pill Shapes (Bo tròn hoàn hảo `9999px`):** Dùng xuyên suốt cho thanh ghi âm đáy, các nút bấm CTA chính, thanh input, và các thẻ tag.
4. **Tương phản cao & Dễ đọc cho Người lớn tuổi:** Chữ đen đậm nét trên nền trắng kem ấm, cỡ chữ hiển thị to (24px–32px), các nút bấm có chiều cao tối thiểu 56px–60px để ngón tay to dễ bấm.

---

## 2. HỆ THỐNG DESIGN TOKENS (3-LAYER TOKEN ARCHITECTURE)

### A. Primitive Tokens (Giá trị thô)

```css
:root {
  /* --- Palette Màu Nguyên Bản (Primitives) --- */
  --primitive-black: #0F172A;
  --primitive-charcoal: #1E293B;
  --primitive-slate-900: #0F172A;
  --primitive-slate-800: #1E293B;
  --primitive-slate-700: #334155;
  --primitive-slate-600: #475569;
  --primitive-slate-500: #64748B;
  --primitive-slate-400: #94A3B8;
  --primitive-slate-300: #CBD5E1;
  --primitive-slate-200: #E2E8F0;
  --primitive-slate-100: #F1F5F9;
  --primitive-slate-50:  #F8FAFC;
  --primitive-white:     #FFFFFF;

  /* Xanh lá thương hiệu Nông nghiệp Xã */
  --primitive-green-900: #064E3B;
  --primitive-green-800: #065F46;
  --primitive-green-700: #047857;
  --primitive-green-600: #059669;
  --primitive-green-500: #10B981;
  --primitive-green-100: #D1FAE5;
  --primitive-green-50:  #ECFDF5;

  /* Xanh Voice/AI (Scout Blue) */
  --primitive-blue-600:  #2563EB;
  --primitive-blue-500:  #3B82F6;
  --primitive-blue-100:  #DBEAFE;
  --primitive-blue-50:   #EFF6FF;

  /* Vàng ấm "Tô Vàng" (Amber/Warning) */
  --primitive-amber-600: #D97706;
  --primitive-amber-500: #F59E0B;
  --primitive-amber-100: #FEF3C7;
  --primitive-amber-50:  #FFFBEB;

  /* Zalo & Shopee Brand Colors */
  --primitive-zalo-blue: #0068FF;
  --primitive-shopee-orange: #EE4D2D;

  /* --- Spacing Scale (Hệ khoảng cách 4px) --- */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;

  /* --- Border Radius Scale --- */
  --radius-xs: 6px;
  --radius-sm: 10px;
  --radius-md: 14px;
  --radius-lg: 18px;
  --radius-xl: 24px;
  --radius-pill: 9999px;

  /* --- Typography Scale (Plus Jakarta Sans / SF Pro) --- */
  --font-family-display: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif;
  --font-family-body: 'Plus Jakarta Sans', -apple-system, system-ui, sans-serif;
  --font-family-mono: 'JetBrains Mono', ui-monospace, monospace;

  --font-size-2xs: 11px;
  --font-size-xs:  12px;
  --font-size-sm:  13px;
  --font-size-md:  15px;
  --font-size-lg:  17px;
  --font-size-xl:  20px;
  --font-size-2xl: 24px;
  --font-size-3xl: 30px;
  --font-size-4xl: 36px;
}
```

---

### B. Semantic Tokens (Ý nghĩa & Mục đích sử dụng)

```css
:root {
  /* Surfaces & Backgrounds */
  --color-bg-canvas: #F8F9FA;         /* Nền tổng thể thiết bị */
  --color-bg-surface: #FFFFFF;        /* Mặt thẻ card chính */
  --color-bg-subtle: #F1F3F5;         /* Nền thẻ con, chip nền */
  --color-bg-dark-card: #0F172A;      /* Thẻ nổi bật tone tối như deal card trong Scout */

  /* Text & Foreground */
  --color-text-primary: #0F172A;      /* Chữ tiêu đề, nội dung chính (đen đậm rõ) */
  --color-text-secondary: #475569;    /* Chữ phụ, hướng dẫn */
  --color-text-muted: #94A3B8;        /* Chữ mờ, timestamp */
  --color-text-inverse: #FFFFFF;      /* Chữ trên nền tối */

  /* Borders & Dividers */
  --color-border-subtle: #E2E8F0;     /* Viền thẻ card mảnh */
  --color-border-focused: #0F172A;    /* Viền khi người dùng focus */

  /* Brand Accents */
  --color-accent-ai: #2563EB;         /* Điểm nhấn AI/Voice (Scout Blue) */
  --color-accent-ai-light: #EFF6FF;
  --color-accent-agri: #047857;       /* Điểm nhấn Nông nghiệp xã (GreenVillage) */
  --color-accent-agri-light: #ECFDF5;

  /* Trạng thái nghiệp vụ */
  --color-status-success: #059669;
  --color-status-success-bg: #ECFDF5;

  /* Cơ chế đặc thù: "TÔ VÀNG" (Ảnh mờ, AI nghi vấn) */
  --color-status-to-vang-border: #F59E0B;
  --color-status-to-vang-bg: #FEF3C7;
  --color-status-to-vang-text: #92400E;
}
```

---

### C. Component Tokens & Quy cách thành phần (Component Specs)

#### 1. Thanh Ghi Âm Nổi (Floating Voice Pill Bar)
*Lấy cảm hứng 100% từ thanh Voice bar ở đáy màn hình 1 & 2 trong Scout:*
* **Cấu trúc:** Thanh capsule bo tròn (`radius: 9999px`), trôi cách đáy 20px, có hiệu ứng blur kính mờ (`backdrop-filter: blur(16px)`).
* **Trạng thái Mặc định:** Nền trắng `#FFFFFF`, viền `#E2E8F0`, icon Mic xanh `#2563EB`, text: *"Bác bấm vào đây để nói"* (15px, font-weight 600).
* **Trạng thái Đang nghe (Listening):** Viền xanh `#2563EB`, nền xanh nhạt `#F0F7FF`, sóng âm equalizer 5 vạch nhảy theo nhịp nói, nút dừng đỏ/đen.

#### 2. Thẻ Tag Thực Thể Đã Nghe (Entity Extracted Chips)
*Tương tự cụm "So far Scout heard" ở màn hình 1:*
* **Cấu trúc:** Chip dạng Pill (`radius: 9999px`), viền mảnh 1.5px, padding `6px 14px`.
* **Trạng thái:**
  * Thuộc tính đã trích xuất: `Sản phẩm: Chuối sấy giòn ˅`
  * Khối lượng: `Quy cách: Gói 250g ˅`
  * Giá tiền: `Giá: 55.000 đ ˅`
* **Hành vi:** Bấm vào thẻ để mở popup sửa nhanh bằng giọng nói hoặc phím số to.

#### 3. Khung Chụp 3 Ảnh (Smart Guided Camera Slots)
* **Cấu trúc:** 3 ô hình chữ nhật bo tròn (`radius: 18px`), tỷ lệ 1:1.15.
* **Slot 1 (Mặt trước):** Khung viền nét đứt mảnh, icon sản phẩm, nhãn *"Mặt trước (Tên & Bao bì)"*.
* **Slot 2 (Mặt sau):** Nhãn *"Mặt sau (HSD & Thành phần)"*.
* **Slot 3 (Tem OCOP):** Nhãn *"Tem OCOP / Mã vạch"*.
* **Huy hiệu hoàn thành:** Icon tích tròn xanh góc trên bên phải khi đã chụp đủ nét.
* **Huy hiệu Tô Vàng:** Viền vàng cam nhấp nháy khi ảnh bị lóa đèn flash.

#### 4. Thẻ Trình Bày Bài Viết (Featured Post Card)
*Tương tự Thẻ sản phẩm nổi bật màu đen sang trọng ở màn hình 2:*
* **Biến thể Sáng (Light Card):** Dành cho Hộ nông dân xem lại bài đăng mộc mạc đăng Zalo.
* **Biến thể Tối (Dark Featured Card - `#0F172A`):** Dành cho các khuyến nghị nổi bật, cảnh báo nút thắt kinh tế của xã hoặc gợi ý ghép nối cung cầu Layer 2.

#### 5. Thẻ Thống Kê 3 Cột (Metric Summary Pills)
*Tương tự khối "This week" 3 ô ở màn hình 3:*
* **Cấu trúc:** 3 ô chữ nhật bo tròn đặt ngang nhau (`radius: 16px`), nền `#F1F5F9`.
* **Ô 1:** Icon túi hàng + Số to `25` (Hộ tham gia thí điểm).
* **Ô 2:** Icon giỏ hàng + Số to `48` (Sản phẩm đã số hóa).
* **Ô 3:** Icon nhãn giá + Số to `1.450đ` (Chi phí AI/bộ, đạt ngưỡng $\le 2.000$đ).

#### 6. Nút Hành Động Lớn (Big Action Buttons)
* **Kích thước:** Chiều cao `58px - 60px`, `radius: 9999px` (Pill) hoặc `radius: 18px`.
* **Nút Zalo Primary:** Nền xanh Zalo `#0068FF`, chữ trắng to `17px, font-weight: 700`.
* **Nút Shopee Secondary:** Nền cam Shopee `#EE4D2D`, chữ trắng.
* **Nút Outline:** Nền trắng, viền `#E2E8F0`, chữ `#0F172A`.

---

## 3. CHECKLIST KIỂM ĐỊNH (ACCESSIBILITY & SENIOR GUIDELINE)

- [x] **Mức độ tương phản (Contrast Ratio):** Văn bản chính và nền đạt tối thiểu 7:1 (chuẩn WCAG AAA cho người lớn tuổi).
- [x] **Vùng chạm (Touch Target Size):** Mọi nút bấm và chip tương tác đều có kích thước tối thiểu $48\text{px} \times 48\text{px}$ (khuyến nghị $58\text{px}$).
- [x] **Phản hồi tức thì (Immediate Audio & Visual Feedback):** Khi bấm mic có sóng âm, khi xong có âm thanh tút nhẹ, khi gửi Zalo có modal chuyển giao.
- [x] **Quy tắc Tô Vàng an toàn:** Không bao giờ dùng màu đỏ báo lỗi khiến người già bối rối; chỉ dùng viền vàng ấm `#F59E0B` mời họ bấm để đọc lại.
