# TEST PLAN — Chợ Xanh AI Sale OS (GreenOS v2.1 — Chuẩn Hóa Direction A, Điều Hướng 6 Vai Trò & Dataset Xã Đồng Lam)

> **Trạng thái hiện tại:** Phase 4 (Test Plan) 📝 **Chờ Human Review & Duyệt** trước khi chạy kiểm thử tự động (theo quy tắc bắt buộc trong `GEMINI.md`).

---

## 1. Phạm Vi Kiểm Thử (Test Scope)

Kiểm thử toàn diện việc chuẩn hóa **Hệ thiết kế Direction A + MD3**, **Logic Điều hướng & Phân quyền 6 vai trò (16 tài khoản mẫu)**, và **Bộ dữ liệu gốc Xã Đồng Lam – Tỉnh Sơn Nguyên** từ `green-village-os` trên:
1. [index.html](file:///Users/hoangminhduc/Downloads/GreenOS/index.html) & [mobile_chu_ba.html](file:///Users/hoangminhduc/Downloads/GreenOS/mobile_chu_ba.html) (Mobile App Hộ Sản Xuất, Hub Xã, Chợ Xanh & Việc làm AnCuJob)
2. [htx-dashboard.html](file:///Users/hoangminhduc/Downloads/GreenOS/htx-dashboard.html) (Web PC: BO Vận hành, BO Chính sách, Số liệu Kinh tế Xã `/xa`, và Cổng Cổ phần `cp.langxanh.vn`)
3. [PORTAL.html](file:///Users/hoangminhduc/Downloads/GreenOS/PORTAL.html) (Cổng trình diễn độc lập nhúng toàn bộ Mobile + Desktop)
4. Mã nguồn gốc `green-village-os/gvos-web` ([App.tsx](file:///Users/hoangminhduc/Downloads/GreenOS/green-village-os/gvos-web/src/App.tsx), [AuthContext.tsx](file:///Users/hoangminhduc/Downloads/GreenOS/green-village-os/gvos-web/src/context/AuthContext.tsx), [account-chips.ts](file:///Users/hoangminhduc/Downloads/GreenOS/green-village-os/gvos-web/src/components/app/account/account-chips.ts))

---

## 2. Danh Sách Ca Kiểm Thử (28 Test Cases — Chờ Duyệt)

### Nhóm 1 — Mở Khóa Mã Nguồn `green-village-os/gvos-web` & Kho Ảnh Gốc `.webp`
| Mã TC | Tên ca kiểm thử | Tiêu chí đạt (Expected Result) | Trạng thái |
| :--- | :--- | :--- | :---: |
| **TC-GVOS-01** | Mở khóa route `/bo/*` và `/xa/*` trong `gvos-web/src/App.tsx` | Không còn `<Navigate to="/app" replace />` chặn cứng `/bo` và `/xa`; render đầy đủ `<BoLayout />` (13 route con) và `<XaShell />` (6 route con). | ⏳ Chờ duyệt |
| **TC-GVOS-02** | Mở khóa 6 vai trò trong `AuthContext.tsx` & `account-chips.ts` | `ALL_ACCOUNTS` chứa đủ `BO_ACCOUNTS` (`vh-1`, `cn-1`, `xa-1`); `ACCOUNT_GROUPS` có đủ 4 tab (`Hộ`, `Hub`, `Người tuyển`, `BO & Xã`). | ⏳ Chờ duyệt |
| **TC-GVOS-03** | Kho ảnh gốc `.webp` & PDF mẫu tại thư mục gốc `GreenOS` | Tồn tại đầy đủ `anh-mau/sp/*.webp` (15 ảnh SP), `anh-mau/nen/bg-home.webp`, `anh-mau/gioi-thieu/slide-1..4.webp`, `anh-mau/nguoi/*.webp`, và `tai-lieu/tai-lieu-mau.pdf`. | ⏳ Chờ duyệt |

---

### Nhóm 2 — Hệ Thiết Kế Direction A ("An Cư Xanh & Đồng Ruộng Bậc Thang") & 5-State AI Field UI (`index.html`)
| Mã TC | Tên ca kiểm thử | Tiêu chí đạt (Expected Result) | Trạng thái |
| :--- | :--- | :--- | :---: |
| **TC-DIRA-01** | Font `Lexend` & Ảnh nền ruộng bậc thang `bg-home.webp` | Nạp font `Lexend`, áp dụng lớp phủ ảnh nền `anh-mau/nen/bg-home.webp` ấm áp trên đầu trang chủ Mobile App. | ⏳ Chờ duyệt |
| **TC-DIRA-02** | Trạng thái 1 — `✓ Chắc` (AutoField) | Vạch trái `6px solid #365F19`, nền `#F3F9EE`, có dòng nguồn trích xuất gạch chân (`từ câu nói: "..."`). | ⏳ Chờ duyệt |
| **TC-DIRA-03** | Trạng thái 2 — `⚠ Ô vàng` (YellowField) | Nền vàng ấm `#FFE066`, viền `3px solid #B18C39`, có đúng 2 nút `[✓ Đúng rồi]` và `[✎ Sửa]`, khi bấm `[✓ Đúng rồi]` tự động chuyển thành `✓ Chắc`. | ⏳ Chờ duyệt |
| **TC-DIRA-04** | Trạng thái 3 — `? Ô thiếu` (MissingField) | Nền xanh lam nhạt `#EAF0FF`, viền nét đứt `2px dashed #2D6FBE`, có ô nhập trực tiếp kèm nút `[🎙 Nói]` và `[Lưu]`. | ⏳ Chờ duyệt |
| **TC-DIRA-05** | Trạng thái 4 — `⊘ Câu bị chặn` (BlockedNotice) | Nền đỏ nhạt `#FFE1DF`, vạch trái `6px solid #C01242`, gạch ngang câu vi phạm, hiển thị câu gợi ý trung tính và **chỉ có 3 nút `[Dùng câu gợi ý]`, `[Sửa]`, `[Bỏ câu]`** (không có nút cho qua). | ⏳ Chờ duyệt |
| **TC-DIRA-06** | Trạng thái 5 — `ConfirmBox` & Bộ chọn 14 Kịch bản AI (`kb-01..kb-08`) | Chuyển đổi được 8 kịch bản AI mẫu của Xã Đồng Lam; khóa nút Chia sẻ Zalo / Sao chép Shopee khi còn Ô thiếu, Câu bị chặn hoặc chưa tích `ConfirmBox`. | ⏳ Chờ duyệt |

---

### Nhóm 3 — Điều Hướng, Route Guards & `SampleAccountDialog` 16 Tài Khoản · 6 Vai Trò (`index.html`)
| Mã TC | Tên ca kiểm thử | Tiêu chí đạt (Expected Result) | Trạng thái |
| :--- | :--- | :--- | :---: |
| **TC-NAV-01** | Hộp chọn Tài khoản mẫu (`SampleAccountDialog` — 4 tab · 16 TK) | Mở modal `#gvosSampleAccountModal`, chuyển đổi 4 tab (`Hộ`, `Hub`, `Người tuyển`, `BO & Xã`), hiển thị đúng tên, thôn, mô tả edge-case từng tài khoản. | ⏳ Chờ duyệt |
| **TC-NAV-02** | Guard `RequireConsent` (`ho-03 Hà Thị Lan`) | Chọn `ho-03 Hà Thị Lan` (chưa đồng ý dữ liệu) → Khi bấm vào tạo sản phẩm tự động chuyển hướng sang màn `/dong-y` (`#panel-consent`). | ⏳ Chờ duyệt |
| **TC-NAV-03** | Guard `RequireActingHousehold` (`hub-1 Đinh Văn Tùng`) | Chọn `hub-1 Đinh Văn Tùng` (chưa chọn hộ) → Tự động mở màn `/ho-duoc-giao` (`#panel-hub-households`); chọn `hub-2 Lý Thị Thắm` hiện ngay thanh vàng đang hỗ trợ `Hộ Hoàng Văn Đức`. | ⏳ Chờ duyệt |
| **TC-NAV-04** | Guard `ForbiddenState` tại chỗ (`ho-21 Giáp Văn Thành` & `ho-23 Mông Văn Sơn`) | Chọn `ho-21` (chỉ Chợ Xanh) bấm Tạo bài AI → Hiện hộp `ForbiddenState` ("Chưa bật quyền cho tài khoản này"); chọn `ho-23` (chỉ Trợ lý AI) bấm Chợ Xanh → Hiện hộp `ForbiddenState`. | ⏳ Chờ duyệt |
| **TC-NAV-05** | Edge-case `0 sản phẩm` (`ho-04`, `ho-10`, `ho-17`) & `Hết lượt 5/5` (`ho-24`) | Chọn `ho-04 Đỗ Thị Hương` hiện thẻ mời tạo sản phẩm đầu tiên; chọn `ho-24 Kiều Thị Liên` hiện cảnh báo đã dùng hết 5/5 lượt gói Cơ bản. | ⏳ Chờ duyệt |
| **TC-NAV-06** | Tự động đổi `BottomNav` theo vai trò & Ẩn khi vào luồng con | Đổi nhãn 4 tab `BottomNav` theo `ho` / `hub` / `nguoi_tuyen`; tự động ẩn `BottomNav` khi vào các màn luồng con (`/dong-y`, `/ho-duoc-giao`, sửa bài 2 giọng, Shopee copy, báo sai). | ⏳ Chờ duyệt |
| **TC-NAV-07** | Chuyển đổi Data Kép (`Xã Đồng Lam` ⇄ `Bác Ba – Xã Yên Bình`) | Nút `#btnDatasetDongLam` và `#btnDatasetGreenOS` chuyển đổi tức thì tên hộ, xã, sản phẩm và ảnh `.webp` gốc. | ⏳ Chờ duyệt |

---

### Nhóm 4 — Khu BO Vận Hành, BO Chính Sách & Số Liệu Kinh Tế Xã `/xa` (`htx-dashboard.html`)
| Mã TC | Tên ca kiểm thử | Tiêu chí đạt (Expected Result) | Trạng thái |
| :--- | :--- | :--- | :---: |
| **TC-BO-01** | Bảng màu Indigo `#1C3DA6`, Viền đậm `2px solid #0D1838` & `border-radius: 6px` | Các bảng và thẻ trong `#view-bo-ops`, `#view-bo-ancujob`, `#view-xa-economy`, `#view-cp-langxanh` áp dụng chuẩn Direction A (`6px` radius, không bóng đổ màu). | ⏳ Chờ duyệt |
| **TC-BO-02** | Phân quyền `BO Vận hành (vh-1)` vs `BO Chính sách (cn-1)` (`ForbiddenState`) | Khi chọn `cn-1 Hoàng Thị Vân` trên `#boRoleSwitcher` và bấm tab `Thanh toán · Khiếu nại · Đối soát` (`cxDisputes`), hệ thống chặn và hiện `#boCnForbiddenBox` (`ForbiddenState`). | ⏳ Chờ duyệt |
| **TC-XA-01** | Bảng `/xa` chuẩn **Xã Đồng Lam – Tỉnh Sơn Nguyên** & Gộp `< 5 hộ` (`Bản Cỏi`) | Hiển thị 6 thôn (`Bãi Sen, Đồng Chè, Khe Trúc, Suối Mây, Nà Liêu` + gộp `Thôn Bản Cỏi — 3 hộ` vào dòng `"🔒 Nhóm nhỏ (< 5 hộ)"`), bộ chọn kỳ `2026-04`, `2026-03`, `2026-02`. | ⏳ Chờ duyệt |
| **TC-XA-02** | Chế độ Trình chiếu `?trinh-chieu=1` cỡ chữ KPI `64px` & Phím `Esc` thoát | Bấm nút Trình chiếu phóng to chữ số KPI `.xa-kpi-big` lên `64px`, ẩn sidebar; bấm phím `Escape` tự động thoát chế độ trình chiếu. | ⏳ Chờ duyệt |

---

### Nhóm 5 — Cổng Cổ Phần `cp.langxanh.vn` (`LNTX`) & Đồng Bộ `PORTAL.html`
| Mã TC | Tên ca kiểm thử | Tiêu chí đạt (Expected Result) | Trạng thái |
| :--- | :--- | :--- | :---: |
| **TC-CP-01** | Lộ trình 3 Đợt phát hành (`DOT-1`, `DOT-2`, `DOT-3`) & 40 Nhà đầu tư mẫu | Hiển thị đúng `DOT-1: Gieo Hạt (12.000đ/CP)`, `DOT-2: Mở Rộng Cụm Xã (15.000đ/CP · 232.000/350.000 CP = 66,3%)`, `DOT-3: Liên Minh Vùng (18.000đ/CP)`, quản trị viên `Lê Thu Hà`, và link tải `tai-lieu/tai-lieu-mau.pdf`. | ⏳ Chờ duyệt |
| **TC-CP-02** | Tuân thủ ngôn ngữ pháp lý & Ký Hợp đồng OTP 6 số + Sổ cái Append-only | 0 lần xuất hiện từ cấm ("ROI" / "cam kết lợi nhuận"); ký OTP 6 số (`signCpContractOtp`), duyệt đơn hàng loạt (`batchApproveCpOrders`) và chuyển nhượng (`recordCpTransferDemo`) hoạt động mượt. | ⏳ Chờ duyệt |
| **TC-SYNC-01** | Đồng bộ 100% giữa `index.html`, `mobile_chu_ba.html`, `htx-dashboard.html` và `PORTAL.html` | `scripts/sync_portal.py` chạy thành công (exit code 0), không có lỗi cú pháp JS trên tất cả các tệp. | ⏳ Chờ duyệt |

---

## 3. Checkpoint Duyệt Kế Hoạch Kiểm Thử (Mandatory Human Review)
> ⛔ **Theo quy tắc `GEMINI.md`, hệ thống đang DỪNG tại bước này chờ bạn duyệt `TEST_PLAN.md` (gõ `"duyệt"` hoặc `"ok"`) để bắt đầu chạy kiểm thử tự động toàn bộ các ca kiểm thử trên.**
