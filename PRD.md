# PRD - Chợ Xanh: AI Sale OS
### Nền tảng Vận hành Bán hàng Số cho HTX Nông thôn

**Version:** 1.1  
**Ngày cập nhật:** 2026-09-09  
**Thay đổi:** Cập nhật 4 actor rõ ràng theo cấu trúc tổ chức thực tế

---

## 1. Product Overview

### 1.1 Bài học từ thị trường

Các mô hình B2C mua chung (Sendo Farm, Mio) thất bại vì:
- Cạnh tranh trực tiếp với GrabMart, ShopeeFood có hạ tầng khổng lồ
- Chi phí last-mile logistics không thể tối ưu ở mật độ thấp
- Mô hình "chợ bán hàng" tạo gánh nặng vận hành sàn TMĐT

**→ Chợ Xanh KHÔNG làm sàn TMĐT. Chợ Xanh là AI Sale OS.**

### 1.2 Định vị sản phẩm

> **"CX là nơi AI biến người bán chưa biết online thành người bán có thể vận hành được"**

**Mô hình:** SaaS B2B – bán subscription cho HTX/Xã, HTX dùng để bán hàng tốt hơn trên mọi kênh hiện có.

**Doanh thu:**
- Subscription hàng tháng theo HTX (tier: Cơ bản / Pro / Enterprise)
- Commission nhỏ trên giao dịch B2B qua nền tảng
- Gói onboarding & tư vấn số hoá cho HTX lớn

---

## 2. Goals & Objectives

### Mục tiêu MVP (3 tháng)
- Onboard 5–10 HTX thử nghiệm, mỗi HTX bán được hàng trên Shopee/TikTok qua nền tảng
- Onboarding hoàn tất < 30 phút/HTX

### Mục tiêu Scale (6 tháng)
- 50 HTX, subscription revenue > 50 triệu/tháng
- Churn rate < 10%

### KPIs theo actor
| Actor | KPI |
|-------|-----|
| Thành viên HTX | Số sản phẩm đăng thành công / tuần |
| Quản lý HTX | Tỷ lệ đơn xử lý đúng hạn |
| Cán bộ xã | Tần suất login, số báo cáo xuất |
| Người mua/Đối tác | Tỷ lệ chuyển đổi sau scan QR, số đơn B2B |

---

## 3. Target Users — 4 Actors

> **Nguyên tắc phân loại:** Theo vai trò thực tế trong cấu trúc HTX/Xã, không theo hành vi mua hàng.

---

### 🌾 Actor 1: Thành viên HTX
**Là ai:** Nông dân / hộ sản xuất thành viên của HTX. Người trực tiếp trồng trọt, chăn nuôi, sơ chế sản phẩm.

**Đặc điểm:**
- Tuổi: 35–60, trình độ học vấn trung bình
- Dùng điện thoại Android phổ thông, ít dùng máy tính
- Không quen với app, thích giao tiếp qua Zalo/điện thoại
- Không có thời gian ngồi "vận hành" phần mềm

**Nỗi đau chính:**
- Không biết chụp ảnh đẹp, viết mô tả sản phẩm
- Không hiểu cách đăng bán trên Shopee/TikTok
- Không biết giá thị trường để định giá
- Không có kênh để minh bạch hoá sản phẩm của mình

**Quyền truy cập trong hệ thống:**
- Đăng ký sản phẩm của mình (cần Quản lý HTX duyệt)
- Xem đơn hàng liên quan đến lô hàng của mình
- Cập nhật nhật ký canh tác (feeding QRTrace)
- Không có quyền quản lý tài chính HTX

**Feature dành cho actor này:**
| Feature | Mô tả ngắn |
|---------|-----------|
| 📱 AI Product Register | Upload ảnh → AI viết mô tả, gợi ý giá |
| 🗒️ Farm Diary | Ghi nhật ký canh tác (voice/text/ảnh) → feed QR trace |
| 📦 My Batches | Xem trạng thái lô hàng của mình |
| 💬 Zalo Notification | Thông báo khi lô hàng được duyệt / bán được |

---

### 👨‍💼 Actor 2: Quản lý HTX
**Là ai:** Ban Giám đốc / Kế toán / Thủ kho HTX. Người điều hành hoạt động bán hàng và vận hành ngày-ngày của HTX.

**Đặc điểm:**
- Tuổi: 35–55, thường có máy tính bàn/laptop
- Quen làm việc với Excel, thỉnh thoảng Zalo
- Phải báo cáo lên BLĐ xã + Liên minh HTX
- Chịu trách nhiệm doanh thu, tồn kho, giao hàng

**Nỗi đau chính:**
- Nhập liệu thủ công, quản lý đơn hàng trên nhiều nền tảng rất mất thời gian
- Không biết cách tối ưu quảng cáo / content cho Shopee, TikTok
- Khó kiểm soát tồn kho và sản lượng đóng gói
- Thiếu dữ liệu để báo cáo minh bạch lên cấp trên

**Quyền truy cập trong hệ thống:**
- Toàn quyền quản lý HTX của mình
- Duyệt sản phẩm của Thành viên HTX
- Quản lý kênh bán hàng (Shopee/TikTok tokens)
- Xem toàn bộ đơn hàng + tài chính HTX
- Không có quyền xem dữ liệu HTX khác (RLS)

**Feature dành cho actor này:**
| Feature | Mô tả ngắn |
|---------|-----------|
| 🏪 HTX Dashboard | Tổng quan doanh thu, đơn, tồn kho |
| 🤖 AI Onboarding | Setup gian hàng, kết nối Shopee/TikTok nhanh |
| 📋 Order Hub | Tổng hợp đơn mọi kênh, xác nhận, in phiếu |
| 🤖 AI Content Studio | AI viết caption, kịch bản livestream, banner |
| 📦 Inventory | Quản lý tồn kho, cảnh báo hàng sắp hết |
| ✅ Product Approval | Duyệt sản phẩm từ Thành viên |
| 📊 HTX Reports | Báo cáo doanh thu, sản phẩm, xuất Excel/PDF |

---

### 🏛️ Actor 3: Cán bộ xã
**Là ai:** UBND xã, Cán bộ phụ trách HTX, Liên minh HTX cấp huyện/tỉnh. Cơ quan quản lý nhà nước, không trực tiếp bán hàng.

**Đặc điểm:**
- Tuổi: 40–60, môi trường hành chính
- Dùng máy tính, quen với Word/Excel/báo cáo
- Chịu trách nhiệm chính sách, xét duyệt OCOP
- Cần dữ liệu tổng hợp để báo cáo lên tỉnh/TW

**Nỗi đau chính:**
- Không có dữ liệu thực tế về hiệu quả hoạt động HTX
- Báo cáo phải tổng hợp thủ công từ nhiều HTX
- Không giám sát được các HTX đang hoạt động ra sao
- Thiếu công cụ để phát hiện HTX cần hỗ trợ

**Quyền truy cập trong hệ thống:**
- Read-only trên tất cả HTX trong phạm vi quản lý (xã/huyện/tỉnh)
- Không can thiệp vào vận hành của từng HTX
- Xuất báo cáo tổng hợp

**Feature dành cho actor này:**
| Feature | Mô tả ngắn |
|---------|-----------|
| 🗺️ Commune Dashboard | Bản đồ HTX, tổng quan toàn xã/huyện |
| 📊 Aggregate Reports | Báo cáo tổng hợp nhiều HTX, xuất PDF/Excel |
| 🏆 HTX Ranking | Bảng xếp hạng hiệu quả HTX |
| 📈 Trend Analysis | Biểu đồ doanh thu, sản lượng theo mùa vụ |
| 🔔 Alert Center | Cảnh báo HTX hoạt động kém / cần hỗ trợ |
| 📋 OCOP Tracking | Theo dõi sản phẩm OCOP, tiến độ chứng nhận |

---

### 🛒 Actor 4: Người mua / Đối tác
**Là ai:** Hai nhóm con khác nhau về hành vi nhưng có thể share cùng cổng:
- **Người mua lẻ:** Người tiêu dùng đô thị, gia đình, cá nhân
- **Đối tác B2B:** Nhà phân phối, nhà hàng, siêu thị, nhà nhập khẩu

**Đặc điểm Người mua lẻ:**
- Tuổi: 25–45, đô thị, quan tâm thực phẩm sạch
- Tiếp cận qua QR code trên bao bì hoặc link trên Shopee
- Không cần tài khoản để xem thông tin truy xuất

**Đặc điểm Đối tác B2B:**
- Doanh nghiệp, cần đơn sỉ ổn định
- Quan tâm chứng nhận, tồn kho, lịch giao hàng
- Cần hóa đơn, hợp đồng

**Quyền truy cập trong hệ thống:**
- Người mua lẻ: Public page (không cần tài khoản)
- Đối tác B2B: Tài khoản riêng, xem tồn kho, đặt đơn sỉ

**Feature dành cho actor này:**
| Feature | Mô tả ngắn |
|---------|-----------|
| 🔍 QR Trace Page | Public: Scan QR → xem nguồn gốc, chứng nhận, hành trình |
| 🗺️ HTX Discovery | Browse danh sách HTX, sản phẩm OCOP |
| 🏪 B2B Portal | Đặt đơn sỉ, xem tồn kho real-time |
| 📄 Invoice & Docs | Hóa đơn điện tử, hợp đồng |
| 💬 Connect | Chat / liên hệ trực tiếp HTX |

---

## 4. Feature Matrix theo Actor

| Feature | Thành viên HTX | Quản lý HTX | Cán bộ xã | Người mua/ĐT |
|---------|:--------------:|:-----------:|:---------:|:------------:|
| AI Product Register | ✅ (tạo) | ✅ (duyệt) | 👁️ | ❌ |
| Farm Diary | ✅ | 👁️ | ❌ | ❌ |
| Order Hub | 👁️ (batch) | ✅ | 👁️ | ❌ |
| AI Content Studio | ❌ | ✅ | ❌ | ❌ |
| HTX Dashboard | ❌ | ✅ | 👁️ | ❌ |
| Commune Dashboard | ❌ | ❌ | ✅ | ❌ |
| Aggregate Reports | ❌ | ✅ (HTX) | ✅ (toàn xã) | ❌ |
| QR Trace Page | ❌ | ✅ (tạo) | 👁️ | ✅ |
| B2B Portal | ❌ | ✅ (nhận) | 👁️ | ✅ (đặt) |
| Inventory | 👁️ | ✅ | 👁️ | ✅ (tồn kho) |
| Notifications | ✅ | ✅ | ✅ | ✅ |

> **Legend:** ✅ = Toàn quyền | 👁️ = Xem (read-only) | ❌ = Không có quyền

---

## 5. User Flows

### Flow 1: Thành viên HTX — Đăng ký sản phẩm mới
```
[Mở app] → [Chụp ảnh lô hàng]
  → [AI tự điền tên/mô tả] → [Điền giá + số lượng]
  → [Ghi thêm nhật ký (tuỳ chọn)]
  → [Gửi duyệt Quản lý HTX]
  → [Nhận Zalo: "Sản phẩm đã được duyệt, đang bán trên Shopee"] ✓
```

### Flow 2: Quản lý HTX — Xử lý đơn hàng
```
[Zalo: "Bạn có 3 đơn mới từ Shopee!"]
  → [Mở Order Hub] → [Xem danh sách đơn]
  → [Xác nhận đơn] → [In phiếu GHTK tự động]
  → [Bàn giao shipper] → [Hệ thống cập nhật trạng thái tự động]
```

### Flow 3: Quản lý HTX — AI tạo content bán hàng
```
[AI Content Studio] → [Chọn sản phẩm]
  → [AI viết caption TikTok + Facebook]
  → [Review & sửa] → [Lên lịch đăng]
  → [Auto-post theo lịch] ✓
```

### Flow 4: Cán bộ xã — Xem báo cáo tháng
```
[Đăng nhập] → [Commune Dashboard]
  → [Chọn kỳ: Tháng 9/2026]
  → [Xem bảng xếp hạng + biểu đồ doanh thu]
  → [1 click xuất báo cáo PDF gửi Liên minh HTX] ✓
```

### Flow 5: Người mua lẻ — Truy xuất nguồn gốc
```
[Scan QR trên bao bì] → [Trang public (không cần đăng nhập)]
  → [Xem: HTX, ngày thu hoạch, VietGAP/OCOP, hành trình]
  → [Nhấn "Mua thêm"] → [Chuyển đến Shopee / Website HTX]
```

### Flow 6: Đối tác B2B — Đặt đơn sỉ
```
[Đăng ký tài khoản Đối tác] → [Browse HTX / sản phẩm]
  → [Xem tồn kho real-time] → [Đặt đơn sỉ (MOQ)]
  → [HTX xác nhận] → [Hóa đơn điện tử + lịch giao hàng]
```

---

## 6. Wireframes

### Screen 1: Thành viên HTX — Mobile App (AI Product Register)
```
┌──────────────────────────────────┐
│ 🌿 Chợ Xanh         [Zalo 🔔]   │
├──────────────────────────────────┤
│                                  │
│  Xin chào, Chú Năm! 👋          │
│  HTX Hoa Sen • Thành viên        │
│                                  │
│  ┌──────────────────────────┐    │
│  │  📷  CHỤP ẢNH SẢN PHẨM  │    │
│  │    → AI sẽ làm phần còn lại   │
│  └──────────────────────────┘    │
│                                  │
│  Lô hàng của tôi:               │
│  ┌──────────────────────────┐    │
│  │ 🍊 Bưởi Năm Roi • 200kg  │    │
│  │ ✅ Đã duyệt • Đang bán   │    │
│  └──────────────────────────┘    │
│  ┌──────────────────────────┐    │
│  │ 🥭 Xoài Cát • 150kg      │    │
│  │ ⏳ Chờ Quản lý duyệt     │    │
│  └──────────────────────────┘    │
│                                  │
│  🤖 AI đã viết mô tả cho bạn!   │
│  [Xem & chỉnh sửa →]            │
│                                  │
│  [📷 Đăng ký lô mới]            │
└──────────────────────────────────┘
```

### Screen 2: Quản lý HTX — Dashboard chính
```
┌────────────────────────────────────────────────────────┐
│ 🌿 Chợ Xanh          [🔔 3]  [HTX Hoa Sen ▼]  [👤]   │
├──────────────┬─────────────────────────────────────────┤
│              │  Tháng 9/2026         [Hôm nay ▼]       │
│  📦 Sản phẩm │  ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  📋 Đơn hàng │  │ 12 đơn   │ │⚡ 3 mới  │ │▲ 2.4tr  │ │
│  🤖 AI Tools │  │  hôm nay │ │  cần xử  │ │  doanh  │ │
│  📊 Báo cáo  │  └──────────┘ └──────────┘ │  thu    │ │
│  📦 Tồn kho  │                             └─────────┘ │
│  ⚙️ Cài đặt  │  ─────────────────────────────────────  │
│              │  🤖 Gợi ý AI                            │
│  Kênh bán:  │  "Bưởi Năm Roi sắp hết hàng (15kg).    │
│  ✅ Shopee   │   Thành viên Chú Năm có thêm 200kg.    │
│  ✅ TikTok   │   [Duyệt lô hàng mới →]"               │
│  ○  Lazada   │                                          │
│              │  📋 Cần xử lý ngay                      │
│              │  ┌──────────────────────────────────┐   │
│              │  │ ⚡#1234 Bưởi 2kg • Shopee       │   │
│              │  │ Nguyễn A • Q.1 HCM  [Xác nhận]  │   │
│              │  └──────────────────────────────────┘   │
└──────────────┴─────────────────────────────────────────┘
```

### Screen 3: Quản lý HTX — AI Product Manager
```
┌────────────────────────────────────────────────────────┐
│ ← Tạo / Duyệt sản phẩm                   [Lưu nháp]  │
├────────────────────────────────────────────────────────┤
│  Từ: Thành viên Chú Năm  •  Lô BN-2026-09-15         │
│                                                        │
│  📷 Ảnh sản phẩm (3 ảnh từ Chú Năm)                  │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────────┐             │
│  │img1 │ │img2 │ │img3 │ │ + Thêm ảnh  │             │
│  └─────┘ └─────┘ └─────┘ └─────────────┘             │
│                                                        │
│  🤖 AI đã viết sẵn cho bạn                           │
│  ┌──────────────────────────────────────────────────┐ │
│  │ Tên: "Bưởi Năm Roi HTX Hoa Sen - VietGAP"       │ │
│  │ Mô tả: "Bưởi ngọt thanh tự nhiên, trồng theo    │ │
│  │ tiêu chuẩn VietGAP, không hóa chất..."           │ │
│  │                               [Chỉnh sửa ✏️]    │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  💰 Giá  [45,000đ/kg]  AI gợi ý: 42k-48k            │
│  📦 Tồn   [200 kg]  Cảnh báo tối thiểu: [20 kg]     │
│  🔖 Kênh  [✓]Shopee  [✓]TikTok  [ ]Lazada  [✓]Web  │
│  🔍 QR   [✓] Tạo QR truy xuất nguồn gốc             │
│                                                        │
│          [❌ Từ chối]          [✅ Duyệt & Đăng]      │
└────────────────────────────────────────────────────────┘
```

### Screen 4: Cán bộ xã — Commune Dashboard
```
┌────────────────────────────────────────────────────────┐
│ 🏛️ UBND Xã Bình Hòa • Hậu Giang    Tháng 9 [Xuất PDF]│
├────────────────────────────────────────────────────────┤
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│  │ 12 HTX   │ │▲245tr    │ │ 1,234    │ │56 SP     │  │
│  │đang HĐ   │ │doanh thu │ │ đơn hàng │ │OCOP đã   │  │
│  │          │ │          │ │          │ │xét duyệt │  │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │
│                                                        │
│  📈 Doanh thu toàn xã (6 tháng)                       │
│  [===========Recharts Bar Chart===========]           │
│                                                        │
│  🏆 Xếp hạng HTX                                      │
│  ┌──────────────────────────────────────────────────┐ │
│  │ #1  HTX Hoa Sen        ████████▓░ 92% • 85tr    │ │
│  │ #2  HTX Bình Minh      ██████░░░░ 78% • 62tr    │ │
│  │ #3  HTX Thiên Nhiên    █████░░░░░ 65% • 48tr    │ │
│  │ ⚠️  HTX Xuân Mai       ██░░░░░░░░ 28% • Cần HT │ │
│  └──────────────────────────────────────────────────┘ │
│                                                        │
│  🔔 Cảnh báo cần chú ý                               │
│  ⚠️ HTX Xuân Mai: Không có đơn hàng 30 ngày qua     │
└────────────────────────────────────────────────────────┘
```

### Screen 5: Người mua lẻ — Trang QR Truy xuất (Public)
```
┌──────────────────────────────────┐
│ 🌿 Chợ Xanh                     │
├──────────────────────────────────┤
│                                  │
│   🍊 Bưởi Năm Roi               │
│   HTX Hoa Sen                   │
│   Ấp 2, Xã Bình Hòa, Hậu Giang │
│                                  │
│   ┌──────────────────────────┐  │
│   │ ✅ Thu hoạch: 15/09/2026 │  │
│   │ ✅ Chứng nhận: VietGAP   │  │
│   │ ✅ OCOP: 4★              │  │
│   │ ✅ Không tồn dư BVTV     │  │
│   │ 👤 Thành viên: Chú Năm   │  │
│   └──────────────────────────┘  │
│                                  │
│   🗺️ Hành trình sản phẩm       │
│   🌱 → 🌳 → 📦 → 🏷️ → 🚚      │
│   06/01  09/15  09/16  09/16  09/17 │
│                                  │
│   [🛒 Mua trên Shopee]          │
│   [💬 Liên hệ HTX Hoa Sen]     │
└──────────────────────────────────┘
```

### Screen 6: Đối tác B2B — Portal đặt đơn sỉ
```
┌────────────────────────────────────────────────────────┐
│ 🌿 Chợ Xanh B2B           [Đơn của tôi]  [Công ty ▼] │
├────────────────────────────────────────────────────────┤
│  [🔍 Tìm sản phẩm/HTX...]  [Lọc: Tỉnh ▼] [OCOP ▼]   │
├────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐  ┌──────────────────────┐   │
│  │ 🍊 Bưởi Năm Roi      │  │ 🥭 Xoài Cát Hòa Lộc │   │
│  │ HTX Hoa Sen          │  │ HTX Tiền Giang       │   │
│  │ Tồn: 1,200 kg ✅      │  │ Tồn: 800 kg ✅       │   │
│  │ Giá sỉ: 38,000đ/kg   │  │ Giá sỉ: 55,000đ/kg  │   │
│  │ MOQ: 50 kg           │  │ MOQ: 100 kg          │   │
│  │ OCOP 4★ • VietGAP    │  │ OCOP 3★              │   │
│  │ [Đặt hàng →]        │  │ [Đặt hàng →]        │   │
│  └──────────────────────┘  └──────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

## 7. Data Models

```
┌──────────────────────────────────────────────────────────┐
│                    AUTH & USERS                          │
│                                                          │
│  Organization (HTX | Commune | Company)                  │
│  ├── id, name, type, province, address, tax_code         │
│  ├── ocop_stars, verified, tier (basic|pro|enterprise)   │
│  └── created_at                                          │
│                                                          │
│  User                                                    │
│  ├── id, org_id, name, phone, avatar_url                 │
│  ├── role: 'htx_member' | 'htx_manager' |               │
│  │         'commune_officer' | 'buyer' | 'b2b_partner'   │
│  └── status: active | pending | suspended                │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                 PRODUCTS & TRACEABILITY                  │
│                                                          │
│  Product                                                 │
│  ├── id, org_id, created_by (user_id - htx_member)      │
│  ├── name, description (ai_generated: bool)              │
│  ├── images[], category, unit                            │
│  ├── status: draft | pending_approval | active | archived│
│  └── approved_by (user_id - htx_manager)                 │
│                                                          │
│  ProductSKU                                              │
│  ├── id, product_id, variant_name                        │
│  ├── price, b2b_price, min_order_qty                     │
│  └── stock_qty, low_stock_alert                          │
│                                                          │
│  ProductBatch (Lô hàng)                                  │
│  ├── id, product_id, batch_code                          │
│  ├── producer_id (user_id - htx_member)                  │
│  ├── harvest_date, quantity_kg, location                 │
│  └── certifications[] (VietGAP | OCOP | GlobalGAP)      │
│                                                          │
│  QRTrace                                                 │
│  ├── id, batch_id, qr_code (unique)                      │
│  ├── public_url (/trace/[qr_code])                       │
│  └── timeline[]: { stage, date, note, photo_url }        │
│       stages: planting → growing → harvest               │
│               → packaging → shipping → delivered          │
│                                                          │
│  FarmDiary (Nhật ký canh tác)                           │
│  ├── id, batch_id, user_id (htx_member)                  │
│  ├── entry_type: text | voice | photo                    │
│  ├── content, media_url                                  │
│  └── created_at                                          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                   SALES & ORDERS                         │
│                                                          │
│  Channel (Kênh bán hàng)                                │
│  ├── id, org_id, type: shopee|tiktok|lazada|web|zalo    │
│  ├── access_token, refresh_token, shop_id, expires_at    │
│  └── active, last_sync_at                               │
│                                                          │
│  Order                                                   │
│  ├── id, org_id, channel_id                             │
│  ├── external_order_id, order_type: b2c | b2b           │
│  ├── buyer_name, buyer_phone, shipping_address           │
│  ├── status: new|confirmed|packed|shipping|done|cancelled│
│  ├── total_amount, shipping_fee                          │
│  ├── shipping_provider: ghtk|ghn|vnpost                  │
│  ├── tracking_code                                       │
│  └── created_at                                          │
│                                                          │
│  OrderItem                                               │
│  └── order_id, sku_id, batch_id, quantity, unit_price    │
│                                                          │
│  B2BOrder (Đơn hàng sỉ)                                │
│  ├── id, buyer_org_id, seller_org_id                    │
│  ├── status, total_amount, payment_status               │
│  └── invoice_url, contract_url                          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                REPORTING & ANALYTICS                     │
│                                                          │
│  Report (Cached snapshot)                               │
│  ├── id, org_id, report_type: htx_monthly|commune_q      │
│  ├── period_start, period_end                           │
│  ├── data (JSONB): revenue, orders, products, rankings  │
│  └── generated_at, pdf_url                              │
└──────────────────────────────────────────────────────────┘
```

---

## 8. Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│                   FRONTEND (Vercel)                  │
│                                                      │
│  Next.js 14 App Router (TypeScript strict)          │
│  ┌────────────┐ ┌────────────┐ ┌─────────────────┐  │
│  │/app/member │ │/app/manager│ │/app/officer     │  │
│  │(mobile UI) │ │(dashboard) │ │(read-only board)│  │
│  └────────────┘ └────────────┘ └─────────────────┘  │
│  ┌────────────────────┐  ┌───────────────────────┐  │
│  │/app/b2b (partner)  │  │/trace/[qr] (public)   │  │
│  └────────────────────┘  └───────────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                  BACKEND (Supabase)                  │
│  ┌───────────────┐  ┌─────────┐  ┌──────────────┐  │
│  │ PostgreSQL DB │  │  Auth   │  │ Storage (S3) │  │
│  │ + RLS Policy  │  │  JWT    │  │ images/pdfs  │  │
│  └───────────────┘  └─────────┘  └──────────────┘  │
│  ┌───────────────────────────────────────────────┐  │
│  │  Realtime Subscriptions (đơn hàng mới)        │  │
│  └───────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              EXTERNAL INTEGRATIONS                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────────┐ │
│  │ Shopee   │ │ TikTok   │ │ Google Gemini API    │ │
│  │ Open API │ │ Shop API │ │ (Vision + Text gen)  │ │
│  └──────────┘ └──────────┘ └──────────────────────┘ │
│  ┌──────────┐ ┌──────────┐ ┌──────────────────────┐ │
│  │ GHTK API │ │ GHN API  │ │ Zalo OA (notify)     │ │
│  └──────────┘ └──────────┘ └──────────────────────┘ │
└─────────────────────────────────────────────────────┘
```

### RLS Policy Design (Supabase Row Level Security)
| Table | htx_member | htx_manager | commune_officer | b2b_partner |
|-------|:----------:|:-----------:|:---------------:|:-----------:|
| products | Own org (submit) | Own org (full) | All (read) | Public only |
| orders | Own batch | Own org (full) | All (read) | Own orders |
| farm_diary | Own | Own org (read) | ❌ | ❌ |
| reports | ❌ | Own org | Scope (read) | ❌ |
| qr_trace | ❌ | Own org | All (read) | Public |

### Tech Stack
| Layer | Choice | Lý do |
|-------|--------|--------|
| Frontend | Next.js 14 App Router | SSR cho SEO trang public QR, RSC |
| Language | TypeScript strict | Type safety, scale tốt |
| Styling | TailwindCSS + shadcn/ui | Rapid dev, mobile-first |
| State | Zustand + TanStack Query | Lightweight, phù hợp SaaS |
| Auth | Supabase Auth | RLS multi-tenant ngay trong DB |
| Database | Supabase PostgreSQL | Realtime subs, RLS policies |
| Storage | Supabase Storage | Ảnh sản phẩm, PDF báo cáo |
| AI | Google Gemini API | Vision (phân tích ảnh) + Text gen |
| Charts | Recharts | Nhẹ, React-native |
| Forms | react-hook-form + Zod | Type-safe validation |
| PDF | @react-pdf/renderer | Báo cáo + hóa đơn |

### Docker (Development)
| Service | Image | Port |
|---------|-------|------|
| db | postgres:16-alpine | 5432 |
| redis | redis:7-alpine | 6379 |
| minio | minio/minio | 9000 |

---

## 9. UI/UX Guidelines

### Color Scheme (per-role accent)
- **Brand primary:** `#2D7B4F` (xanh lá – thiên nhiên)
- **Brand secondary:** `#F59E0B` (cam vàng – thu hoạch)
- **AI accent:** `#7C3AED` (tím – công nghệ)
- **Member (xanh lá nhạt):** `#ECFDF5`
- **Manager (xanh đậm):** `#064E3B`
- **Officer (xanh navy):** `#1E3A5F`
- **B2B (cam đất):** `#7C2D12`

### UX Principles
1. **Mobile-first** cho Thành viên HTX (chụp ảnh, xem lô hàng)
2. **Desktop-first** cho Quản lý HTX và Cán bộ xã (dashboard phức tạp)
3. **AI visible**: Badge "🤖 AI" ở mọi nơi AI hỗ trợ – người dùng biết AI đang làm gì
4. **Vietnamese-first**: 100% tiếng Việt, không Anh-Việt lẫn lộn
5. **Tối giản**: Mỗi màn hình chỉ có 1 hành động chính (đặc biệt màn hình member)
6. **Offline-aware**: Queue action local khi mất mạng, sync khi có lại
