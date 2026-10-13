#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_orders_and_market.py
Cập nhật hệ thống GreenOS theo yêu cầu của user:
1. Loại bỏ section kho trên bottom nav, thay thế bằng section 'Đơn hàng'
2. Trong màn đơn hàng (panel-orders) có menu tab ở trên: 'Quản lý đơn hàng' và 'Quản lý kho hàng'
3. Ghép Chợ Xanh và Card Đăng Sản Phẩm thành 1 section hợp nhất trên Trang Chủ
"""

import os
import re
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")
BACKUP_PATH = os.path.join(BASE_DIR, "index.html.bak_orders_market")

shutil.copy2(INDEX_PATH, BACKUP_PATH)
print(f"Created backup at {BACKUP_PATH}")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# =========================================================================
# 1. THÊM CSS CHO: TOP SEGMENT TABS, QUẢN LÝ KHO HÀNG & SECTION GHÉP
# =========================================================================
css_to_add = """
    /* =========================================================================
       TOP SEGMENT TABS: QUẢN LÝ ĐƠN HÀNG & QUẢN LÝ KHO HÀNG
       ========================================================================= */
    .orders-top-segment-tabs {
      display: flex;
      background: #F1F5F9;
      border-radius: 14px;
      padding: 4px;
      margin-bottom: 12px;
      gap: 4px;
      border: 1px solid #E2E8F0;
    }
    .ot-segment-btn {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 8px;
      border-radius: 10px;
      border: none;
      background: transparent;
      color: #64748B;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 180ms cubic-bezier(0.16, 1, 0.3, 1);
      font-family: var(--font-sans);
    }
    .ot-segment-btn svg {
      flex-shrink: 0;
    }
    .ot-segment-btn.active {
      background: #FFFFFF;
      color: var(--agri-green);
      box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
      font-weight: 800;
    }
    .ot-badge-pill {
      font-size: 11px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 12px;
      background: #EF4444;
      color: #FFFFFF;
    }
    .ot-badge-pill.secondary {
      background: #E2E8F0;
      color: #334155;
    }
    .ot-segment-btn.active .ot-badge-pill.secondary {
      background: #DCFCE7;
      color: #15803D;
    }

    /* LỐI TẮT IN PHIẾU SOẠN HÀNG (PICK-LIST) TRONG ĐƠN HÀNG */
    .order-picklist-shortcut-card {
      background: linear-gradient(135deg, #ECFDF5 0%, #F0FDF4 100%);
      border: 1.5px solid #A7F3D0;
      border-radius: 14px;
      padding: 10px 14px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.06);
      transition: transform 150ms ease;
    }
    .order-picklist-shortcut-card:active {
      transform: scale(0.99);
    }
    .opsc-left {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }
    .opsc-icon {
      font-size: 22px;
      flex-shrink: 0;
    }
    .opsc-title {
      font-size: 13.5px;
      font-weight: 800;
      color: #065F46;
    }
    .opsc-desc {
      font-size: 12px;
      color: #047857;
      margin-top: 1px;
    }
    .btn-opsc-view {
      background: #059669;
      color: #FFFFFF;
      border: none;
      border-radius: 10px;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
    }

    /* QUẢN LÝ KHO HÀNG SUB-VIEW */
    .warehouse-kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin-bottom: 12px;
    }
    .wh-kpi-card {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 8px 4px;
      text-align: center;
    }
    .wh-kpi-value {
      font-size: 15px;
      font-weight: 900;
      line-height: 1.2;
    }
    .wh-kpi-label {
      font-size: 11px;
      color: #64748B;
      margin-top: 2px;
      font-weight: 600;
    }
    .wh-toolbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
    }
    .wh-filter-chips {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .wh-filter-chips::-webkit-scrollbar {
      display: none;
    }
    .wh-chip {
      padding: 6px 12px;
      border-radius: 20px;
      border: 1px solid #E2E8F0;
      background: #FFFFFF;
      font-size: 12px;
      font-weight: 700;
      color: #475569;
      white-space: nowrap;
      cursor: pointer;
      transition: all 150ms ease;
    }
    .wh-chip.active {
      background: #059669;
      color: #FFFFFF;
      border-color: #059669;
    }
    .btn-wh-add {
      display: flex;
      align-items: center;
      gap: 4px;
      background: #059669;
      color: #FFFFFF;
      border: none;
      border-radius: 12px;
      padding: 7px 12px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(5, 150, 105, 0.2);
    }
    .wh-product-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      padding: 12px 14px;
      margin-bottom: 10px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
    }
    .wh-card-top {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .wh-card-thumb {
      width: 52px;
      height: 52px;
      border-radius: 12px;
      object-fit: cover;
      background: #F1F5F9;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      flex-shrink: 0;
      border: 1px solid #E2E8F0;
    }
    .wh-card-info {
      flex: 1;
      min-width: 0;
    }
    .wh-card-title {
      font-size: 14.5px;
      font-weight: 800;
      color: #0F172A;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .wh-card-meta {
      font-size: 12px;
      color: #64748B;
      margin-top: 2px;
    }
    .wh-card-price {
      font-size: 15px;
      font-weight: 800;
      color: #059669;
      margin-top: 3px;
    }
    .wh-card-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 8px;
      border-top: 1px dashed #E2E8F0;
    }
    .wh-stock-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 8px;
    }
    .wh-stock-pill.low {
      background: #FEE2E2;
      color: #DC2626;
    }
    .wh-stock-pill.good {
      background: #DCFCE7;
      color: #15803D;
    }
    .wh-stock-pill.draft {
      background: #FEF3C7;
      color: #B45309;
    }
    .wh-card-actions {
      display: flex;
      gap: 6px;
    }
    .btn-wh-action {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      padding: 5px 10px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
      transition: background 150ms ease;
    }
    .btn-wh-action:active {
      background: #E2E8F0;
    }

    /* =========================================================================
       SECTION GHÉP: CHỢ XANH & ĐĂNG BÁN NÔNG SẢN (HỢP NHẤT)
       ========================================================================= */
    .home-unified-market-publish-section {
      background: linear-gradient(145deg, #ECFDF5 0%, #FFFFFF 100%);
      border: 1.5px solid #A7F3D0;
      border-radius: 20px;
      padding: 14px 16px;
      margin-bottom: 16px;
      box-shadow: 0 4px 14px rgba(5, 150, 105, 0.08);
    }
    .hump-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid #D1FAE5;
    }
    .hump-header-left {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
    }
    .hump-leaf-badge {
      width: 38px;
      height: 38px;
      border-radius: 12px;
      background: #DCFCE7;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      flex-shrink: 0;
      border: 1px solid #86EFAC;
    }
    .hump-main-title {
      font-size: 15px;
      font-weight: 800;
      color: #065F46;
      letter-spacing: -0.01em;
    }
    .hump-sub-title {
      font-size: 11.5px;
      color: #047857;
      margin-top: 1px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .hump-hot-chip {
      font-size: 11px;
      font-weight: 800;
      background: #DC2626;
      color: #FFFFFF;
      padding: 4px 8px;
      border-radius: 10px;
      cursor: pointer;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(220, 38, 38, 0.25);
    }
    .hump-grid-cards {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 10px;
    }
    .hump-card-action {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 12px 10px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }
    .hump-card-action:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.12);
      border-color: #86EFAC;
    }
    .hump-card-action:active {
      transform: scale(0.98);
    }
    .hump-card-publish {
      border-color: #86EFAC;
      background: linear-gradient(180deg, #FFFFFF 0%, #F0FDF4 100%);
    }
    .hump-card-market {
      border-color: #BFDBFE;
      background: linear-gradient(180deg, #FFFFFF 0%, #EFF6FF 100%);
    }
    .hump-card-icon-wrap {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .hump-card-title {
      font-size: 13.5px;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.25;
    }
    .hump-card-desc {
      font-size: 11.5px;
      color: #64748B;
      margin-top: 3px;
      line-height: 1.3;
    }
    .btn-hump-go {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      width: 100%;
      padding: 7px 10px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 800;
      border: none;
      cursor: pointer;
    }
    .btn-hump-go.primary {
      background: #059669;
      color: #FFFFFF;
    }
    .btn-hump-go.secondary {
      background: #1D4ED8;
      color: #FFFFFF;
    }
    .hump-spotlight-match {
      background: #FEF3C7;
      border: 1px solid #FDE68A;
      border-radius: 12px;
      padding: 8px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      transition: background 150ms ease;
    }
    .hump-spotlight-match:hover {
      background: #FDE68A;
    }
    .hsm-icon {
      font-size: 16px;
      flex-shrink: 0;
    }
    .hsm-info {
      flex: 1;
      min-width: 0;
      font-size: 12px;
      color: #92400E;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .hsm-buyer {
      font-weight: 800;
      color: #78350F;
    }
    .hsm-link {
      font-size: 11.5px;
      font-weight: 800;
      color: #B45309;
      flex-shrink: 0;
      white-space: nowrap;
    }
"""

# Chèn CSS vào trước </style>
if "</style>" in content:
    content = content.replace("</style>", css_to_add + "\n  </style>", 1)
    print("Inserted CSS styles successfully.")

# =========================================================================
# 2. GHÉP CHỢ XANH VÀ CARD ĐĂNG SẢN PHẨM TRÊN PANEL-HOME
# =========================================================================
# Thay thế home-choxanh-banner bằng section ghép
merged_section_html = """<!-- =========================================================================
             SECTION GHÉP: CHỢ XANH & ĐĂNG BÁN NÔNG SẢN (HỢP NHẤT 2 TRONG 1)
             ========================================================================= -->
        <div class="home-unified-market-publish-section">
          <!-- Header của Section Ghép -->
          <div class="hump-header">
            <div class="hump-header-left">
              <div class="hump-leaf-badge">🌿</div>
              <div>
                <div class="hump-main-title">Chợ Xanh & Đăng Bán Nông Sản</div>
                <div class="hump-sub-title">Kết nối thương lái sỉ & Đăng bán đa kênh chuẩn OCOP</div>
              </div>
            </div>
            <span class="hump-hot-chip" onclick="switchNavTab('market')" title="Bấm mở Chợ Xanh">2 Ghép nối mới</span>
          </div>

          <!-- 2 Card hành động song song / lưới trực quan -->
          <div class="hump-grid-cards">
            <!-- Card 1: Đăng Bán Nông Sản Mới (3 Bước Wizard) -->
            <div class="hump-card-action hump-card-publish" onclick="startWizardFlow()">
              <div class="hump-card-icon-wrap" style="background:#DCFCE7;color:#15803D">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
              </div>
              <div class="hump-card-text">
                <div class="hump-card-title">Đăng Bán Nhanh</div>
                <div class="hump-card-desc">3 ảnh + Trợ lý AI định giá OCOP</div>
              </div>
              <button type="button" class="btn-hump-go primary">
                <span>Bắt đầu</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>

            <!-- Card 2: Vào Chợ Xanh Xã (Bản tin Cần / Có & Khớp Lệnh) -->
            <div class="hump-card-action hump-card-market" onclick="switchNavTab('market')">
              <div class="hump-card-icon-wrap" style="background:#DBEAFE;color:#1D4ED8">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
              </div>
              <div class="hump-card-text">
                <div class="hump-card-title">Chợ Xanh Xã</div>
                <div class="hump-card-desc">18 thẻ Có · 7 thẻ Cần thu mua</div>
              </div>
              <button type="button" class="btn-hump-go secondary">
                <span>Vào Chợ</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </button>
            </div>
          </div>

          <!-- Dòng Khớp Nối Nóng (Thương lái đang tìm Bác Ba) -->
          <div class="hump-spotlight-match" onclick="switchNavTab('market')" title="Bấm xem ghép nối này tại Chợ Xanh">
            <div class="hsm-icon">⚡</div>
            <div class="hsm-info">
              <span class="hsm-buyer">Xưởng mứt Hải Hà (3.2km)</span>
              <span class="hsm-need">cần mua gấp <strong>1,2 tấn chuối sấy dẻo</strong></span>
            </div>
            <span class="hsm-link">Khớp đơn ➔</span>
          </div>
        </div>"""

# Tìm block home-choxanh-banner
banner_pattern = re.compile(r'<!--\s*=+\s*CARD LỐI TẮT VÀO CHỢ XANH.*?<div class="home-choxanh-banner".*?</div>\s*</div>', re.DOTALL)
if banner_pattern.search(content):
    content = banner_pattern.sub(merged_section_html, content, count=1)
    print("Replaced home-choxanh-banner with merged section.")
else:
    # Thử thay thế thẻ div trực tiếp
    old_hcb = re.compile(r'<div class="home-choxanh-banner"[^>]*>.*?</div>\s*</div>', re.DOTALL)
    if old_hcb.search(content):
        content = old_hcb.sub(merged_section_html, content, count=1)
        print("Replaced home-choxanh-banner (fallback pattern).")

# Loại bỏ assistant-compact-card vì đã được tích hợp vào section ghép trên
assistant_pattern = re.compile(r'<!--\s*Thẻ Trợ Lý Bán Hàng Thu Gọn.*?<div class="assistant-compact-card".*?</div>\s*</div>', re.DOTALL)
if assistant_pattern.search(content):
    content = assistant_pattern.sub("<!-- Đã tích hợp vào Section Ghép Chợ Xanh & Đăng Bán Nông Sản ở trên -->", content, count=1)
    print("Removed duplicate assistant-compact-card from home.")

# =========================================================================
# 3. CẬP NHẬT BOTTOM NAVIGATION BAR: THAY 'KHO HÀNG' THÀNH 'ĐƠN HÀNG'
# =========================================================================
old_tab_inventory = re.compile(r'<!-- Tab 4: Kho hàng -->\s*<button type="button" class="nav-tab-item" id="tabInventory" onclick="switchNavTab\(\'inventory\'\)">.*?</button>', re.DOTALL)

new_tab_orders = """<!-- Tab 4: Đơn hàng (Thay thế Kho hàng) -->
      <button type="button" class="nav-tab-item" id="tabOrders" onclick="switchNavTab('orders')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        <span class="tab-text">Đơn hàng</span>
        <span class="tab-badge" style="background:#EF4444;color:#fff">44</span>
      </button>"""

if old_tab_inventory.search(content):
    content = old_tab_inventory.sub(new_tab_orders, content, count=1)
    print("Replaced tabInventory with tabOrders in bottom nav.")
else:
    print("WARNING: tabInventory pattern not found in bottom nav!")

# Cập nhật Tab 5 thành Chợ Xanh cho đồng bộ
old_tab_market = re.compile(r'<!-- Tab 5: Chợ Xã \(Nhật ký\) -->\s*<button type="button" class="nav-tab-item" id="tabMarket" onclick="switchNavTab\(\'market\'\)">.*?<span class="tab-text">Chợ Xã</span>\s*</button>', re.DOTALL)
new_tab_market = """<!-- Tab 5: Chợ Xanh -->
      <button type="button" class="nav-tab-item" id="tabMarket" onclick="switchNavTab('market')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>
        <span class="tab-text">Chợ Xanh</span>
        <span class="tab-badge" style="background:#10B981;color:#fff">2</span>
      </button>"""
if old_tab_market.search(content):
    content = old_tab_market.sub(new_tab_market, content, count=1)
    print("Updated tabMarket label to Chợ Xanh.")

# =========================================================================
# 4. TÁI CẤU TRÚC PANEL-ORDERS: MENU TAB QUẢN LÝ ĐƠN HÀNG VÀ QUẢN LÝ KHO HÀNG
# =========================================================================
new_panel_orders = """      <section id="panel-orders" class="view-panel">
        <!-- Top Bar Header -->
        <div class="shopee-order-header">
          <div class="shopee-header-left">
            <button type="button" class="shopee-back-btn" onclick="closeOrdersView()" title="Quay lại">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            </button>
            <span class="shopee-header-title-text" id="orderHeaderTitle">Đơn Hàng & Kho Hàng</span>
            <div class="shopee-open-badge" onclick="toggleStoreOpen(this)">
              <span class="shopee-open-dot"></span>
              <span id="storeOpenText">Mở cửa ›</span>
            </div>
          </div>
          <div class="shopee-header-actions">
            <button type="button" class="shopee-header-btn" onclick="openOrderSearchPrompt()" title="Tìm kiếm"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></button>
            <button type="button" class="shopee-header-btn" onclick="triggerToast('Hỗ trợ HTX Yên Bình: 0988.123.456')" title="Trợ giúp"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg></button>
            <button type="button" class="shopee-header-btn" onclick="triggerToast('Cài đặt thông báo')" title="Cài đặt"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg></button>
          </div>
        </div>

        <!-- MENU TAB Ở TRÊN: QUẢN LÝ ĐƠN HÀNG VÀ QUẢN LÝ KHO HÀNG -->
        <div class="orders-top-segment-tabs">
          <button type="button" class="ot-segment-btn active" id="btnSubtabOrders" onclick="switchOrderSubTab('orders')">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            <span>Quản lý đơn hàng</span>
            <span class="ot-badge-pill" id="subtabOrderBadge">44</span>
          </button>
          <button type="button" class="ot-segment-btn" id="btnSubtabWarehouse" onclick="switchOrderSubTab('warehouse')">
            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="m7.5 4.27 9 5.15"/><path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/></svg>
            <span>Quản lý kho hàng</span>
            <span class="ot-badge-pill secondary">7 SP</span>
          </button>
        </div>

        <!-- SUB-VIEW 1: QUẢN LÝ ĐƠN HÀNG -->
        <div id="ordersSubView_orders" class="orders-sub-view active">
          <!-- Horizontal Scrollable Tabs matching Shopee -->
          <div class="shopee-status-tabs-container">
            <div class="shopee-status-tabs">
              <div class="shopee-tab-item active" data-tab="all" onclick="selectOrderStatusTab('all')">Tất cả</div>
              <div class="shopee-tab-item" data-tab="new" onclick="selectOrderStatusTab('new')">Mới (44)</div>
              <div class="shopee-tab-item" data-tab="preparing" onclick="selectOrderStatusTab('preparing')">Đang làm (9)</div>
              <div class="shopee-tab-item" data-tab="done" onclick="selectOrderStatusTab('done')">Làm xong</div>
              <div class="shopee-tab-item" data-tab="shipping" onclick="selectOrderStatusTab('shipping')">Đang giao</div>
              <div class="shopee-tab-item" data-tab="history" onclick="selectOrderStatusTab('history')">Lịch sử</div>
            </div>
          </div>

          <!-- Lối tắt in Phiếu Soạn Hàng (Pick-list Gom Đơn) -->
          <div class="order-picklist-shortcut-card" onclick="openPickListView()">
            <div class="opsc-left">
              <div class="opsc-icon">📦</div>
              <div>
                <div class="opsc-title">Phiếu Soạn Hàng (Pick-list) · 9 đơn cần đóng</div>
                <div class="opsc-desc">Gom tổng số lượng 4 loại nông sản để đóng gói nhanh</div>
              </div>
            </div>
            <button type="button" class="btn-opsc-view">In phiếu ➔</button>
          </div>

          <!-- Sub-filter Toolbar (Date Dropdown + Status Dropdown) -->
          <div class="shopee-filter-toolbar">
            <button type="button" class="shopee-date-btn" onclick="openOrderDateFilterModal()" title="Bấm chọn khoảng thời gian lọc">
              <span class="shopee-date-check-tag">✓</span>
              <span class="shopee-date-text" id="shopeeDateFilterLabel">01/10/2026 - 31/10/2026</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <button type="button" class="shopee-dropdown-filter" onclick="toggleChannelFilter(this)">
              <span id="shopeeChannelFilterLabel">Tất cả kênh</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
          </div>

          <!-- Order Cards List Container -->
          <div id="shopeeOrdersListContainer">
            <!-- Populated by JavaScript renderOrdersList() -->
          </div>
        </div>

        <!-- SUB-VIEW 2: QUẢN LÝ KHO HÀNG -->
        <div id="ordersSubView_warehouse" class="orders-sub-view" style="display:none">
          <!-- 4 Thẻ Chỉ Số Nhanh Kho Hàng -->
          <div class="warehouse-kpi-grid">
            <div class="wh-kpi-card">
              <div class="wh-kpi-value" style="color:#059669">7</div>
              <div class="wh-kpi-label">Tổng mặt hàng</div>
            </div>
            <div class="wh-kpi-card">
              <div class="wh-kpi-value" style="color:#1D4ED8">1.450</div>
              <div class="wh-kpi-label">Tồn kg/gói</div>
            </div>
            <div class="wh-kpi-card">
              <div class="wh-kpi-value" style="color:#DC2626">2</div>
              <div class="wh-kpi-label">Sắp hết hàng</div>
            </div>
            <div class="wh-kpi-card">
              <div class="wh-kpi-value" style="color:#B45309">48.2 tr</div>
              <div class="wh-kpi-label">Giá trị tồn</div>
            </div>
          </div>

          <!-- Thanh Công Cụ Kho: Thêm SP mới & Lọc danh mục -->
          <div class="wh-toolbar">
            <div class="wh-filter-chips">
              <button type="button" class="wh-chip active" onclick="filterWarehouseCategory('all', this)">Tất cả (7)</button>
              <button type="button" class="wh-chip" onclick="filterWarehouseCategory('active', this)">Đang bán (5)</button>
              <button type="button" class="wh-chip" onclick="filterWarehouseCategory('low', this)">Sắp hết (2)</button>
              <button type="button" class="wh-chip" onclick="filterWarehouseCategory('draft', this)">Bản nháp (2)</button>
            </div>
            <button type="button" class="btn-wh-add" onclick="startWizardFlow()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
              <span>Thêm nông sản</span>
            </button>
          </div>

          <!-- Danh sách Sản Phẩm Kho Hàng -->
          <div id="warehouseProductsListContainer">
            <!-- Populated by JavaScript renderWarehouseList() -->
          </div>
        </div>
      </section>"""

old_panel_orders = re.compile(r'<section id="panel-orders" class="view-panel">.*?</section>', re.DOTALL)
if old_panel_orders.search(content):
    content = old_panel_orders.sub(new_panel_orders, content, count=1)
    print("Replaced panel-orders with dual-tab structure.")
else:
    print("WARNING: panel-orders not found!")

# Chuyển đổi panel-inventory thành fallback container ẩn
old_panel_inventory = re.compile(r'<!--\s*=+\s*PANEL 6: TAB KHO HÀNG.*?<section id="panel-inventory" class="view-panel">.*?</section>', re.DOTALL)
fallback_inventory = """<!-- =========================================================================
           PANEL KHO HÀNG (ĐÃ TÍCH HỢP VÀO TAB QUẢN LÝ KHO HÀNG TRONG ĐƠN HÀNG)
           ========================================================================= -->
      <section id="panel-inventory" class="view-panel" style="display:none"></section>"""
if old_panel_inventory.search(content):
    content = old_panel_inventory.sub(fallback_inventory, content, count=1)
    print("Converted panel-inventory to fallback element.")

# =========================================================================
# 5. CẬP NHẬT JAVASCRIPT: DỮ LIỆU KHO, CHUYỂN TAB & CẬP NHẬT TỒN KHO
# =========================================================================
js_warehouse_and_nav = """
    // =========================================================================
    // DỮ LIỆU KHO NÔNG SẢN BÁC BA & QUẢN LÝ TỒN KHO
    // =========================================================================
    let BAC_BA_WAREHOUSE_PRODUCTS = [
      {
        id: "wh_banana",
        name: "Chuối sấy giòn Đồng Cát",
        category: "active",
        packaging: "Túi zip 250g",
        cert: "OCOP 4 sao",
        stock: 85,
        unit: "gói",
        threshold: 100,
        price: 55000,
        image: "banana_front.jpg",
        isEmoji: false,
        status: "low",
        statusText: "Sắp hết hàng",
        salesToday: 12
      },
      {
        id: "wh_honey",
        name: "Mật ong hoa rừng tự nhiên",
        category: "active",
        packaging: "Hũ thủy tinh 500g",
        cert: "OCOP 4 sao",
        stock: 24,
        unit: "hũ",
        threshold: 30,
        price: 180000,
        image: "honey_front.jpg",
        isEmoji: false,
        status: "low",
        statusText: "Sắp hết hàng",
        salesToday: 4
      },
      {
        id: "wh_tea",
        name: "Trà Bát Tiên Thái Nguyên",
        category: "active",
        packaging: "Túi zip 500g",
        cert: "OCOP 4 sao",
        stock: 120,
        unit: "gói",
        threshold: 40,
        price: 120000,
        image: "tea_front.jpg",
        isEmoji: false,
        status: "active",
        statusText: "Tồn dồi dào",
        salesToday: 8
      },
      {
        id: "wh_rice",
        name: "Gạo Nếp Nương Tú Lệ",
        category: "active",
        packaging: "Bao dệt 5kg",
        cert: "OCOP 4 sao",
        stock: 45,
        unit: "bao",
        threshold: 20,
        price: 210000,
        image: "🌾",
        isEmoji: true,
        status: "active",
        statusText: "Còn 45 bao",
        salesToday: 3
      },
      {
        id: "wh_orange",
        name: "Cam Sành Hàm Yên OCOP",
        category: "active",
        packaging: "Thùng carton 10kg",
        cert: "VietGAP",
        stock: 350,
        unit: "kg",
        threshold: 50,
        price: 35000,
        image: "🍊",
        isEmoji: true,
        status: "active",
        statusText: "Còn 350 kg",
        salesToday: 25
      },
      {
        id: "wh_turmeric",
        name: "Tinh bột nghệ đỏ nguyên chất",
        category: "draft",
        packaging: "Hũ 200g",
        cert: "OCOP 3 sao",
        stock: 40,
        unit: "hũ",
        threshold: 15,
        price: 160000,
        image: "🌿",
        isEmoji: true,
        status: "draft",
        statusText: "Bản nháp",
        salesToday: 2
      },
      {
        id: "wh_plum",
        name: "Mận hậu Mộc Châu sấy dẻo",
        category: "draft",
        packaging: "Túi zip 300g",
        cert: "Đang xét OCOP",
        stock: 15,
        unit: "gói",
        threshold: 20,
        price: 95000,
        image: "🍑",
        isEmoji: true,
        status: "draft",
        statusText: "Bản nháp",
        salesToday: 0
      }
    ];

    let currentOrderSubTab = 'orders';
    function switchOrderSubTab(subTab) {
      currentOrderSubTab = subTab;
      const btnOrders = document.getElementById('btnSubtabOrders');
      const btnWarehouse = document.getElementById('btnSubtabWarehouse');
      const viewOrders = document.getElementById('ordersSubView_orders');
      const viewWarehouse = document.getElementById('ordersSubView_warehouse');
      const headerTitle = document.getElementById('orderHeaderTitle');

      if (subTab === 'warehouse') {
        if (btnOrders) btnOrders.classList.remove('active');
        if (btnWarehouse) btnWarehouse.classList.add('active');
        if (viewOrders) viewOrders.style.display = 'none';
        if (viewWarehouse) viewWarehouse.style.display = 'block';
        if (headerTitle) headerTitle.innerText = 'Kho Nông Sản Bác Ba';
        renderWarehouseList();
      } else {
        if (btnWarehouse) btnWarehouse.classList.remove('active');
        if (btnOrders) btnOrders.classList.add('active');
        if (viewWarehouse) viewWarehouse.style.display = 'none';
        if (viewOrders) viewOrders.style.display = 'block';
        if (headerTitle) headerTitle.innerText = 'Quản Lý Đơn Hàng';
        renderOrdersList();
      }
    }

    let currentWarehouseCategoryFilter = 'all';
    function filterWarehouseCategory(cat, btn) {
      currentWarehouseCategoryFilter = cat;
      document.querySelectorAll('.wh-chip').forEach(c => c.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderWarehouseList(cat);
    }

    function renderWarehouseList(catFilter) {
      const container = document.getElementById('warehouseProductsListContainer');
      if (!container) return;

      const filter = catFilter || currentWarehouseCategoryFilter;
      let list = BAC_BA_WAREHOUSE_PRODUCTS;
      if (filter === 'active') {
        list = list.filter(p => p.category === 'active' || p.status === 'active');
      } else if (filter === 'low') {
        list = list.filter(p => p.status === 'low');
      } else if (filter === 'draft') {
        list = list.filter(p => p.category === 'draft' || p.status === 'draft');
      }

      let html = '';
      list.forEach(p => {
        let pillClass = 'good';
        let pillText = `🟢 ${p.stock} ${p.unit}`;
        if (p.status === 'low') {
          pillClass = 'low';
          pillText = `⚠️ Còn ${p.stock} ${p.unit} (Sắp hết)`;
        } else if (p.status === 'draft') {
          pillClass = 'draft';
          pillText = `📝 Nháp (${p.stock} ${p.unit})`;
        }

        const thumbHtml = p.isEmoji
          ? `<div class="wh-card-thumb">${p.image}</div>`
          : `<img src="${p.image}" alt="${p.name}" class="wh-card-thumb">`;

        html += `
          <div class="wh-product-card" id="whCard_${p.id}">
            <div class="wh-card-top">
              ${thumbHtml}
              <div class="wh-card-info">
                <div class="wh-card-title">${p.name}</div>
                <div class="wh-card-meta">${p.packaging} · <span style="color:#059669;font-weight:700">${p.cert}</span></div>
                <div class="wh-card-price">${Number(p.price).toLocaleString('vi-VN')} đ</div>
              </div>
            </div>
            <div class="wh-card-bottom">
              <span class="wh-stock-pill ${pillClass}">${pillText}</span>
              <div class="wh-card-actions">
                <button type="button" class="btn-wh-action" onclick="promptAdjustStock('${p.id}')">✏️ Tồn kho</button>
                <button type="button" class="btn-wh-action" onclick="promptAdjustPrice('${p.id}')">💰 Đổi giá</button>
                <button type="button" class="btn-wh-action" style="color:#0284C7;border-color:#BAE6FD;background:#F0F9FF" onclick="triggerToast('Mở Zalo: Đã sao chép link đặt hàng ${p.name}')">📤 Zalo</button>
              </div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function promptAdjustStock(productId) {
      const p = BAC_BA_WAREHOUSE_PRODUCTS.find(item => item.id === productId);
      if (!p) return;
      const current = p.stock;
      const input = prompt(`Cập nhật số lượng tồn kho cho "${p.name}" (hiện có ${current} ${p.unit}):`, current);
      if (input !== null) {
        const val = parseInt(input.trim(), 10);
        if (!isNaN(val) && val >= 0) {
          p.stock = val;
          if (val <= p.threshold && p.status !== 'draft') {
            p.status = 'low';
          } else if (p.status !== 'draft') {
            p.status = 'active';
          }
          renderWarehouseList();
          triggerToast(`✅ Đã cập nhật tồn kho: ${p.name} = ${val} ${p.unit}`);
        } else {
          alert('Vui lòng nhập một số hợp lệ (lớn hơn hoặc bằng 0).');
        }
      }
    }

    function promptAdjustPrice(productId) {
      const p = BAC_BA_WAREHOUSE_PRODUCTS.find(item => item.id === productId);
      if (!p) return;
      const current = p.price;
      const input = prompt(`Cập nhật giá bán lẻ cho "${p.name}" (hiện tại: ${Number(current).toLocaleString('vi-VN')} đ):`, current);
      if (input !== null) {
        const val = parseInt(input.replace(/[^0-9]/g, ''), 10);
        if (!isNaN(val) && val > 0) {
          p.price = val;
          renderWarehouseList();
          triggerToast(`✅ Đã cập nhật giá bán: ${p.name} = ${Number(val).toLocaleString('vi-VN')} đ`);
        } else {
          alert('Vui lòng nhập giá bán hợp lệ.');
        }
      }
    }
"""

# Cập nhật switchNavTab
old_switch_nav = re.compile(r'function switchNavTab\(tabName\)\s*\{.*?\n    \}', re.DOTALL)
new_switch_nav = """function switchNavTab(tabName) {
      // Ẩn tất cả panels
      document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-tab-item').forEach(b => b.classList.remove('active'));

      // Đảm bảo hiện bottom nav và ẩn wizard dock
      bottomNav.classList.remove('nav-hidden');
      dockStep1.classList.remove('dock-visible');
      dockStep2.classList.remove('dock-visible');
      dockStep3.classList.remove('dock-visible');

      bodyElem.className = 'has-bottom-nav';

      if (tabName === 'home') {
        document.getElementById('panel-home').classList.add('active');
        document.getElementById('tabHome').classList.add('active');
      } else if (tabName === 'dashboard') {
        document.getElementById('panel-dashboard').classList.add('active');
        if (document.getElementById('tabDashboard')) document.getElementById('tabDashboard').classList.add('active');
      } else if (tabName === 'orders') {
        document.getElementById('panel-orders').classList.add('active');
        if (document.getElementById('tabOrders')) document.getElementById('tabOrders').classList.add('active');
        switchOrderSubTab('orders');
      } else if (tabName === 'inventory') {
        // Tự động chuyển vào tab Quản lý kho hàng bên trong màn Đơn hàng
        document.getElementById('panel-orders').classList.add('active');
        if (document.getElementById('tabOrders')) document.getElementById('tabOrders').classList.add('active');
        switchOrderSubTab('warehouse');
      } else if (tabName === 'market') {
        document.getElementById('panel-market').classList.add('active');
        if (document.getElementById('tabMarket')) document.getElementById('tabMarket').classList.add('active');
      } else if (tabName === 'support') {
        document.getElementById('panel-support').classList.add('active');
        if (document.getElementById('tabSupport')) document.getElementById('tabSupport').classList.add('active');
      }
      document.querySelector('.screen-container').scrollTo(0, 0);
    }"""

if old_switch_nav.search(content):
    content = old_switch_nav.sub(new_switch_nav, content, count=1)
    print("Updated switchNavTab function.")

# Cập nhật openOrdersView để đồng bộ với switchNavTab('orders')
old_open_orders = re.compile(r'function openOrdersView\(\)\s*\{.*?renderOrdersList\(\);\s*\}', re.DOTALL)
new_open_orders = """function openOrdersView(initialSubTab = 'orders') {
      const activePanel = document.querySelector('.view-panel.active');
      if (activePanel && activePanel.id !== 'panel-orders' && activePanel.id !== 'panel-order-detail') {
        previousOrdersPanel = activePanel.id.replace('panel-', '');
      }
      switchNavTab('orders');
      if (initialSubTab === 'warehouse') {
        switchOrderSubTab('warehouse');
      } else {
        switchOrderSubTab('orders');
      }
    }"""
if old_open_orders.search(content):
    content = old_open_orders.sub(new_open_orders, content, count=1)
    print("Updated openOrdersView function.")

# Chèn dữ liệu kho và hàm bổ trợ vào trước </script>
content = content.replace("</script>", js_warehouse_and_nav + "\n  </script>", 1)
print("Inserted JS warehouse logic successfully.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully!")
