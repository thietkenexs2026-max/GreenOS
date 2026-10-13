# IMPLEMENTATION PLAN - Chợ Xanh AI Sale OS
**Version:** 1.1 — Cập nhật theo 4 actor: Thành viên HTX / Quản lý HTX / Cán bộ xã / Người mua & Đối tác

---

## ⚠️ WORKFLOW CHECKPOINT
**Khi ALL tasks dưới đây là [x]:**
1. ✅ Report "Phase 3 Complete"
2. 📝 Tạo TEST_PLAN.md
3. ⛔ **STOP — chờ Human review TEST_PLAN.md**

---

## Phase 1: Project Setup & Infrastructure
- [ ] Init Next.js 14 với TypeScript strict mode
- [ ] Cấu hình TailwindCSS v4 + shadcn/ui
- [ ] Thiết lập ESLint + Prettier
- [ ] Cấu hình path aliases (@/components, @/lib, @/types, @/hooks)
- [ ] Tạo docker-compose.yml (postgres:16, redis:7, minio)
- [ ] Setup Supabase project (local dev + cloud)
- [ ] Tạo database migrations (schema từ PRD section 7)
- [ ] Cấu hình Supabase RLS policies (5 roles)
- [ ] Setup env variables structure (.env.local template)
- [ ] Folder structure theo feature-based (member/, manager/, officer/, b2b/, public/)

## Phase 2: Auth & Multi-tenant Foundation
- [ ] Supabase Auth: đăng ký qua phone OTP (primary) + email
- [ ] Organization registration flow (HTX / Xã / Công ty)
- [ ] Role assignment (htx_member | htx_manager | commune_officer | buyer | b2b_partner)
- [ ] Middleware bảo vệ route theo role
- [ ] Multi-tenant isolation: RLS đảm bảo HTX A không thấy data HTX B
- [ ] Trang profile Organization + User
- [ ] Invite system: Quản lý HTX mời Thành viên HTX vào

## Phase 3: 🌾 Thành viên HTX — Mobile-first Features

### 3.1 AI Product Register
- [ ] Upload ảnh sản phẩm (camera mobile + gallery)
- [ ] Gọi Gemini Vision API phân tích ảnh → gợi ý tên, mô tả, category
- [ ] Form điền: giá, đơn vị, số lượng lô
- [ ] Submit → status: pending_approval (chờ Quản lý HTX duyệt)
- [ ] Loading state + success screen

### 3.2 Farm Diary (Nhật ký canh tác)
- [ ] Giao diện ghi nhật ký: text / voice-to-text / upload ảnh
- [ ] Liên kết diary entry với ProductBatch
- [ ] Timeline view nhật ký theo lô hàng

### 3.3 My Batches (Lô hàng của tôi)
- [ ] Danh sách lô hàng: draft | pending | active | sold out
- [ ] Xem chi tiết: số lượng, trạng thái đơn hàng, QR code

### 3.4 Zalo Notification
- [ ] Webhook Zalo OA: thông báo lô hàng được duyệt
- [ ] Thông báo khi lô hàng bán được đơn đầu tiên
- [ ] In-app notification center

## Phase 4: 👨‍💼 Quản lý HTX — Dashboard chính

### 4.1 AI Onboarding Wizard
- [ ] Step 1: Nhập thông tin HTX (tên, tỉnh, loại nông sản chủ lực)
- [ ] Step 2: AI tạo profile HTX + mô tả gian hàng
- [ ] Step 3: Upload logo/ảnh cover
- [ ] Step 4: Kết nối kênh (hướng dẫn Shopee OAuth + TikTok OAuth)
- [ ] Step 5: Completed → CTA thêm sản phẩm đầu tiên

### 4.2 HTX Dashboard Overview
- [ ] Stat cards: đơn hôm nay, đơn mới, doanh thu tháng, tồn kho thấp
- [ ] AI insight widget: gợi ý hành động (duyệt lô hàng, tạo content)
- [ ] Quick actions: xác nhận đơn nhanh

### 4.3 Product Approval (Duyệt sản phẩm thành viên)
- [ ] Danh sách sản phẩm pending approval từ thành viên
- [ ] Review: ảnh, mô tả AI, giá
- [ ] Chỉnh sửa mô tả trước khi duyệt
- [ ] Duyệt → tự động sync lên các kênh đã kết nối
- [ ] Từ chối kèm lý do → thông báo về cho thành viên

### 4.4 AI Product Manager (Quản lý tự đăng)
- [ ] Quản lý HTX cũng có thể tự upload sản phẩm
- [ ] Danh sách sản phẩm: filter theo status, kênh, category
- [ ] Edit sản phẩm + đồng bộ lại lên kênh
- [ ] Bulk actions: ẩn nhiều sản phẩm, thay đổi giá

### 4.5 Order Hub
- [ ] Tabs: Tất cả / ⚡ Mới / 🚚 Đang giao / ✅ Hoàn thành / ❌ Hủy
- [ ] Realtime: Supabase subscription nhận đơn mới (không cần F5)
- [ ] Chi tiết đơn: thông tin người mua, sản phẩm, địa chỉ
- [ ] Xác nhận đơn + in phiếu giao hàng (GHTK/GHN API)
- [ ] Cập nhật tracking code
- [ ] Filter theo kênh (Shopee | TikTok | B2B | Web)

### 4.6 AI Content Studio
- [ ] Chọn sản phẩm → AI viết caption Facebook + caption TikTok
- [ ] Template kịch bản livestream (mở đầu, intro SP, CTA, kết)
- [ ] Tạo banner: overlay text lên ảnh sản phẩm
- [ ] Lịch đăng bài (schedule): chọn ngày giờ → queue

### 4.7 Inventory Management
- [ ] Tổng hợp tồn kho theo SKU
- [ ] Cảnh báo tồn kho thấp (low_stock_alert)
- [ ] Điều chỉnh tồn kho thủ công
- [ ] Lịch sử nhập/xuất kho

### 4.8 HTX Reports
- [ ] Báo cáo doanh thu theo tháng/quý
- [ ] Sản phẩm bán chạy nhất
- [ ] Phân tích theo kênh bán
- [ ] Xuất PDF + Excel

## Phase 5: 🏛️ Cán bộ xã — Commune Dashboard

### 5.1 Commune Overview
- [ ] Scope filter: xã / huyện / tỉnh (theo role + org hierarchy)
- [ ] Stats: tổng số HTX, doanh thu tổng, đơn hàng, sản phẩm OCOP
- [ ] Map view: bản đồ HTX theo địa lý (leaflet.js)

### 5.2 HTX Ranking & Analytics
- [ ] Bảng xếp hạng HTX (doanh thu, đơn hàng, sản phẩm mới)
- [ ] Biểu đồ doanh thu toàn xã theo thời gian (Recharts)
- [ ] Biểu đồ sản lượng theo mùa vụ
- [ ] Cảnh báo: HTX không có hoạt động > 30 ngày

### 5.3 Aggregate Reports
- [ ] Báo cáo tổng hợp nhiều HTX trong phạm vi quản lý
- [ ] Xuất PDF báo cáo (định dạng hành chính)
- [ ] Xuất Excel tổng hợp số liệu

### 5.4 OCOP Tracking
- [ ] Danh sách sản phẩm OCOP đã xét duyệt
- [ ] Trạng thái chứng nhận theo HTX
- [ ] Timeline gia hạn chứng nhận

## Phase 6: 🛒 Người mua & Đối tác

### 6.1 QR Trace Page (Public — không cần login)
- [ ] Route: /trace/[qr_code] — SSG + ISR (revalidate 1h)
- [ ] Hiển thị: tên SP, ảnh, HTX, địa chỉ, thành viên sản xuất
- [ ] Chứng nhận badges (VietGAP, OCOP, GlobalGAP)
- [ ] Timeline hành trình (planting → harvest → packaging → delivered)
- [ ] Farm diary entries (public ones)
- [ ] CTA: Mua trên Shopee / Liên hệ HTX
- [ ] SEO: Open Graph, structured data (schema.org/Product)
- [ ] Mobile responsive hoàn hảo

### 6.2 HTX Discovery (Public browse)
- [ ] Trang /htx: danh sách HTX với filter tỉnh/thành, loại SP, OCOP
- [ ] Trang /htx/[slug]: profile HTX + sản phẩm đang bán

### 6.3 B2B Portal (Đối tác — cần login)
- [ ] Đăng ký tài khoản doanh nghiệp (b2b_partner)
- [ ] Browse sản phẩm với giá B2B (b2b_price)
- [ ] Xem tồn kho real-time
- [ ] Đặt đơn sỉ (với MOQ)
- [ ] Workflow: HTX xác nhận → Hóa đơn điện tử PDF
- [ ] Lịch sử đơn hàng B2B

## Phase 7: Integrations

### 7.1 Shopee Open API (Mock → Real)
- [ ] OAuth flow: Quản lý HTX kết nối Shopee shop
- [ ] Sync sản phẩm lên Shopee (push)
- [ ] Pull đơn hàng từ Shopee về Order Hub
- [ ] Cập nhật tồn kho Shopee sau khi có đơn

### 7.2 TikTok Shop API (Mock → Real)
- [ ] OAuth flow TikTok Shop
- [ ] Sync sản phẩm lên TikTok Shop
- [ ] Pull đơn hàng TikTok

### 7.3 GHTK / GHN Logistics
- [ ] Tạo vận đơn GHTK từ Order Hub
- [ ] Track trạng thái vận chuyển
- [ ] Webhook cập nhật khi giao hàng thành công

### 7.4 Zalo OA
- [ ] Gửi thông báo Zalo khi có đơn mới (Quản lý HTX)
- [ ] Gửi thông báo Zalo khi lô hàng được duyệt (Thành viên)
- [ ] Template message Zalo

## Phase 8: UI Polish & PWA

- [ ] Dark mode support (shadcn/ui)
- [ ] Skeleton loading states cho tất cả màn hình
- [ ] Error boundaries + trang 404/500
- [ ] Empty states có hướng dẫn hành động tiếp theo
- [ ] Toast notifications (success/error/warning)
- [ ] Mobile bottom navigation (cho màn hình Thành viên HTX)
- [ ] PWA: manifest.json, service worker, installable
- [ ] Image optimization (next/image, lazy load)
- [ ] Code splitting per route

---

## Progress Log
| Ngày | Phase | Trạng thái | Ghi chú |
|------|-------|-----------|---------|
| 2026-09-09 | Planning | ✅ Done | PRD v1.1 + Implementation Plan v1.1 |
| | Phase 1 | ⏳ Pending | Chờ Human approval |
