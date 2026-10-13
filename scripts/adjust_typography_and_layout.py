#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adjust_typography_and_layout.py
Rà soát và căn chỉnh lại toàn bộ chữ, kích thước, khoảng cách và ngắt dòng
để đảm bảo không bị vỡ layout trên mọi kích thước màn hình điện thoại.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "index.html")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Căn chỉnh .shopee-header-title-text để không bị ép chữ hoặc đẩy tràn các nút trên thanh bar
content = re.sub(
    r'\.shopee-header-title-text\s*\{[^}]*\}',
    """.shopee-header-title-text {
      font-size: 16.5px;
      font-weight: 800;
      color: #0F172A;
      white-space: nowrap;
      letter-spacing: -0.02em;
      overflow: hidden;
      text-overflow: ellipsis;
    }""",
    content
)

# 2. Căn chỉnh .orders-top-segment-tabs và .ot-segment-btn
content = re.sub(
    r'\.orders-top-segment-tabs\s*\{[^}]*\}',
    """.orders-top-segment-tabs {
      display: flex;
      background: #F1F5F9;
      border-radius: 14px;
      padding: 4px;
      margin-bottom: 12px;
      gap: 4px;
      border: 1px solid #E2E8F0;
    }""",
    content
)

content = re.sub(
    r'\.ot-segment-btn\s*\{[^}]*\}',
    """.ot-segment-btn {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      padding: 8px 6px;
      border-radius: 10px;
      border: none;
      background: transparent;
      color: #64748B;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: -0.01em;
      white-space: nowrap;
      cursor: pointer;
      transition: all 180ms cubic-bezier(0.16, 1, 0.3, 1);
      font-family: var(--font-sans);
    }""",
    content
)

content = re.sub(
    r'\.ot-badge-pill\s*\{[^}]*\}',
    """.ot-badge-pill {
      font-size: 10.5px;
      font-weight: 800;
      padding: 2px 6px;
      border-radius: 10px;
      background: #EF4444;
      color: #FFFFFF;
      flex-shrink: 0;
    }""",
    content
)

# 3. Căn chỉnh .order-picklist-shortcut-card
content = re.sub(
    r'\.order-picklist-shortcut-card\s*\{[^}]*\}',
    """.order-picklist-shortcut-card {
      background: linear-gradient(135deg, #ECFDF5 0%, #F0FDF4 100%);
      border: 1.5px solid #A7F3D0;
      border-radius: 14px;
      padding: 10px 12px;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      box-shadow: 0 2px 8px rgba(5, 150, 105, 0.06);
      transition: transform 150ms ease;
    }
    .opsc-left {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 0;
      flex: 1;
    }
    .opsc-left > div {
      min-width: 0;
      flex: 1;
    }
    .opsc-title {
      font-size: 13px;
      font-weight: 800;
      color: #065F46;
      line-height: 1.35;
      word-break: break-word;
    }
    .opsc-desc {
      font-size: 11.5px;
      color: #047857;
      margin-top: 2px;
      line-height: 1.3;
    }
    .btn-opsc-view {
      background: #059669;
      color: #FFFFFF;
      border: none;
      border-radius: 10px;
      padding: 6px 10px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
    }""",
    content
)

# 4. Căn chỉnh .warehouse-kpi-grid & .wh-product-card
content = re.sub(
    r'\.warehouse-kpi-grid\s*\{[^}]*\}',
    """.warehouse-kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin-bottom: 12px;
    }""",
    content
)

content = re.sub(
    r'\.wh-kpi-card\s*\{[^}]*\}',
    """.wh-kpi-card {
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 8px 3px;
      text-align: center;
      min-width: 0;
    }""",
    content
)

content = re.sub(
    r'\.wh-kpi-value\s*\{[^}]*\}',
    """.wh-kpi-value {
      font-size: 14.5px;
      font-weight: 900;
      line-height: 1.2;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }""",
    content
)

content = re.sub(
    r'\.wh-kpi-label\s*\{[^}]*\}',
    """.wh-kpi-label {
      font-size: 10.5px;
      color: #64748B;
      margin-top: 2px;
      font-weight: 600;
      line-height: 1.25;
    }""",
    content
)

content = re.sub(
    r'\.wh-card-bottom\s*\{[^}]*\}',
    """.wh-card-bottom {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      padding-top: 8px;
      border-top: 1px dashed #E2E8F0;
    }
    .wh-card-actions {
      display: flex;
      gap: 5px;
      flex-wrap: wrap;
      align-items: center;
    }
    .btn-wh-action {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      padding: 4px 8px;
      border-radius: 8px;
      font-size: 11.5px;
      font-weight: 700;
      color: #334155;
      cursor: pointer;
      white-space: nowrap;
      transition: background 150ms ease;
    }
    .wh-stock-pill {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 11.5px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 8px;
      white-space: nowrap;
    }""",
    content
)

# 5. Căn chỉnh .home-unified-market-publish-section
content = re.sub(
    r'\.hump-main-title\s*\{[^}]*\}',
    """.hump-main-title {
      font-size: 14.5px;
      font-weight: 800;
      color: #065F46;
      letter-spacing: -0.01em;
      line-height: 1.3;
    }""",
    content
)

content = re.sub(
    r'\.hump-sub-title\s*\{[^}]*\}',
    """.hump-sub-title {
      font-size: 11.5px;
      color: #047857;
      margin-top: 1px;
      line-height: 1.35;
      word-break: break-word;
    }""",
    content
)

content = re.sub(
    r'\.hump-hot-chip\s*\{[^}]*\}',
    """.hump-hot-chip {
      font-size: 11px;
      font-weight: 800;
      background: #DC2626;
      color: #FFFFFF;
      padding: 3px 8px;
      border-radius: 10px;
      cursor: pointer;
      flex-shrink: 0;
      white-space: nowrap;
      box-shadow: 0 2px 6px rgba(220, 38, 38, 0.25);
    }""",
    content
)

content = re.sub(
    r'\.hump-card-action\s*\{[^}]*\}',
    """.hump-card-action {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 14px;
      padding: 10px 8px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 8px;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
      transition: transform 180ms ease, box-shadow 180ms ease, border-color 180ms ease;
    }""",
    content
)

content = re.sub(
    r'\.hump-card-title\s*\{[^}]*\}',
    """.hump-card-title {
      font-size: 13px;
      font-weight: 800;
      color: #0F172A;
      line-height: 1.3;
    }""",
    content
)

content = re.sub(
    r'\.hump-card-desc\s*\{[^}]*\}',
    """.hump-card-desc {
      font-size: 11px;
      color: #64748B;
      margin-top: 3px;
      line-height: 1.3;
    }""",
    content
)

content = re.sub(
    r'\.btn-hump-go\s*\{[^}]*\}',
    """.btn-hump-go {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 4px;
      width: 100%;
      padding: 6px 8px;
      border-radius: 10px;
      font-size: 11.5px;
      font-weight: 800;
      border: none;
      cursor: pointer;
    }""",
    content
)

# 6. Căn chỉnh tiêu đề trong switchOrderSubTab
old_switch_subtab = re.compile(r'function switchOrderSubTab\(subTab\)\s*\{.*?\n    \}', re.DOTALL)
new_switch_subtab = """function switchOrderSubTab(subTab) {
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
        if (headerTitle) headerTitle.innerText = 'Kho hàng';
        renderWarehouseList();
      } else {
        if (btnWarehouse) btnWarehouse.classList.remove('active');
        if (btnOrders) btnOrders.classList.add('active');
        if (viewWarehouse) viewWarehouse.style.display = 'none';
        if (viewOrders) viewOrders.style.display = 'block';
        if (headerTitle) headerTitle.innerText = 'Đơn hàng';
        renderOrdersList();
      }
    }"""
if old_switch_subtab.search(content):
    content = old_switch_subtab.sub(new_switch_subtab, content, count=1)
    print("Updated switchOrderSubTab titles.")

# 7. Căn chỉnh tiêu đề mặc định của panel-orders trong HTML
content = content.replace(
    '<span class="shopee-header-title-text" id="orderHeaderTitle">Đơn Hàng & Kho Hàng</span>',
    '<span class="shopee-header-title-text" id="orderHeaderTitle">Đơn hàng</span>'
)

# 8. Căn chỉnh SVG kích thước trong ot-segment-btn
content = content.replace(
    '<button type="button" class="ot-segment-btn active" id="btnSubtabOrders" onclick="switchOrderSubTab(\'orders\')">\n            <svg width="17" height="17"',
    '<button type="button" class="ot-segment-btn active" id="btnSubtabOrders" onclick="switchOrderSubTab(\'orders\')">\n            <svg width="15" height="15"'
)
content = content.replace(
    '<button type="button" class="ot-segment-btn" id="btnSubtabWarehouse" onclick="switchOrderSubTab(\'warehouse\')">\n            <svg width="17" height="17"',
    '<button type="button" class="ot-segment-btn" id="btnSubtabWarehouse" onclick="switchOrderSubTab(\'warehouse\')">\n            <svg width="15" height="15"'
)

# 9. Thêm bộ quy tắc phòng vệ chống vỡ layout toàn diện (Safeguard CSS)
safeguard_css = """
    /* =========================================================================
       BẢO ĐẢM TẤT CẢ CÁC MÀN HÌNH KHÔNG BỊ VỠ LAYOUT (RESPONSIVE TYPOGRAPHY SAFEGUARDS)
       ========================================================================= */
    *, *::before, *::after {
      box-sizing: border-box;
    }
    .view-panel {
      word-break: break-word;
      overflow-wrap: break-word;
    }
    .step-main-title, .step-sub-desc, .obp-title, .obp-desc {
      word-break: break-word;
      overflow-wrap: break-word;
    }
    .photo-card-info-col {
      min-width: 0;
      flex: 1;
    }
    .product-row-left {
      min-width: 0;
      flex: 1;
    }
    .product-row-left > div {
      min-width: 0;
      flex: 1;
    }
    .product-row-name {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .product-row-badge {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .product-row-price {
      white-space: nowrap;
      flex-shrink: 0;
    }
    .user-profile-meta {
      min-width: 0;
      flex: 1;
    }
    .user-name-text, .user-address-sub {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .hump-header-left {
      min-width: 0;
      flex: 1;
    }
    .obp-item-row > div:last-child {
      min-width: 0;
      flex: 1;
    }
    input, select, textarea {
      max-width: 100%;
    }
"""

if "</style>" in content:
    content = content.replace("</style>", safeguard_css + "\n  </style>", 1)
    print("Appended safeguard CSS rules.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Finished updating typography and layout in index.html!")
