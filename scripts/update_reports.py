# -*- coding: utf-8 -*-
import csv
import re
import html
import os

CSV_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv'
XLS_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.xls'
HTML_PATH = 'SHEET_HOANG_THANG_10.html'

UPDATES = {
    '1': 'Khung sườn Mobile App Bác Ba chạy mượt, không vỡ layout | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '3': 'Bộ màu chuẩn GreenFi và font chữ to rõ toàn app | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '11': 'Ô nhập giá tiền và số lượng to rõ, tự tính thành tiền | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/03_modal_nghe_audio_nong_dan.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '18': 'Màn hình quản lý đơn hàng phân màu rõ ràng | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/09_mobile_tab_don_hang.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '19': 'Popup đơn hàng có nút bấm gọi điện thoại trực tiếp cho người mua | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/09_mobile_tab_don_hang.webp',
    '20': 'Đạt 100% yêu cầu nghiệm thu gói Mobile Bác Ba của anh Vinh | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/10_mobile_thong_ke_doanh_thu.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '31': 'Cột Việc Nên Làm Hôm Nay với các nút Mở, Ghép, Nhắc, Gom | 📸 Xem ảnh: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '32': 'Bảng thẻ chờ duyệt mới nhất kèm nút xanh Duyệt Ngay | 📸 Xem ảnh: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp | 🔗 Link web: https://cho-xanh.vercel.app/mobile',
    '45': 'Trang quét mã QR tem truy xuất nguồn gốc nông sản | 🔗 Link web: https://cho-xanh.vercel.app/portal',
    '54': 'Cổng trình diễn Dark Mode độc lập có mockup iPhone 16 Pro | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/07_mobile_bac_ba_dark_mode.webp | 🔗 Link web: https://cho-xanh.vercel.app/portal',
    '60': 'Bảng thống kê và sổ kho hiển thị chuẩn từng cột trên máy tính bảng | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/10_mobile_thong_ke_doanh_thu.webp | 🔗 Link web: https://cho-xanh.vercel.app/htx-dashboard'
}

# 1. Read & Update CSV
rows = []
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    rows.append(header)
    for r in reader:
        stt = r[0].strip()
        if stt in UPDATES:
            r[11] = UPDATES[stt]
        rows.append(r)

with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Updated CSV {CSV_PATH} with {len(rows)-1} tasks.")

# 2. Update SHEET_HOANG_THANG_10.html
def format_output_html(val):
    parts = val.split(' | ')
    title = parts[0].strip()
    links_html = []
    for p in parts[1:]:
        p = p.strip()
        url_match = re.search(r'(https?://[^\s]+)', p)
        if url_match:
            url = url_match.group(1)
            label = p.replace(url, '').strip()
            if not label:
                label = '🔗 Xem chi tiết'
            is_web = ('web' in label.lower() or 'portal' in label.lower())
            bg = '#E0F2FE' if is_web else '#E2E8F0'
            color = '#0369A1' if is_web else '#1E293B'
            links_html.append(f'<a class="output-img-link" href="{html.escape(url)}" target="_blank" style="background:{bg}; color:{color};">{html.escape(label)}</a>')
        else:
            links_html.append(f'<span>{html.escape(p)}</span>')
    
    res = f'<div class="output-box"><strong>{html.escape(title)}</strong>'
    if links_html:
        res += '<br>' + ' '.join(links_html)
    res += '</div>'
    return res

# Read existing HTML template or parts
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Build table rows HTML
tbody_rows = []
total_hours = 0
for r in rows[1:]:
    stt = r[0].strip()
    date_val = r[1].strip()
    user_val = r[2].strip()
    due_val = r[3].strip()
    hrs_val = r[4].strip()
    try:
        total_hours += float(hrs_val)
    except:
        pass
    proj_val = r[5].strip()
    status_val = r[6].strip()
    src_val = r[7].strip()
    task_val = r[8].strip()
    prio_val = r[9].strip()
    note_val = r[10].strip()
    output_val = r[11].strip()

    status_badge_class = 'badge-done' if status_val == 'Done' else 'badge-inprogress'
    prio_badge_class = 'badge-gap' if prio_val == 'Gấp' else ('badge-cao' if prio_val == 'Cao' else 'badge-tb')

    output_formatted = format_output_html(output_val)

    row_html = f'''        <tr>
          <td class="col-stt">{stt}</td>
          <td class="col-date">{html.escape(date_val)}</td>
          <td class="col-user">{html.escape(user_val)}</td>
          <td class="col-due">{html.escape(due_val)}</td>
          <td class="col-hours"><span class="badge-hour">{hrs_val}h</span></td>
          <td class="col-proj">{html.escape(proj_val)}</td>
          <td class="col-status"><span class="badge {status_badge_class}">{html.escape(status_val)}</span></td>
          <td class="col-src">{html.escape(src_val)}</td>
          <td class="col-task">{html.escape(task_val)}</td>
          <td class="col-prio"><span class="badge {prio_badge_class}">{html.escape(prio_val)}</span></td>
          <td class="col-note">{html.escape(note_val)}</td>
          <td class="col-output">{output_formatted}</td>
        </tr>'''
    tbody_rows.append(row_html)

tbody_new = '<tbody>\n' + '\n'.join(tbody_rows) + '\n      </tbody>'

# Replace <tbody>...</tbody> in HTML
html_content = re.sub(r'<tbody>[\s\S]*?</tbody>', tbody_new, html_content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated HTML {HTML_PATH} successfully.")

# 3. Update XLS (XML Spreadsheet format)
xls_rows = []
for r in rows[1:]:
    stt = r[0].strip()
    date_val = r[1].strip()
    user_val = r[2].strip()
    due_val = r[3].strip()
    hrs_val = r[4].strip()
    proj_val = r[5].strip()
    status_val = r[6].strip()
    src_val = r[7].strip()
    task_val = r[8].strip()
    prio_val = r[9].strip()
    note_val = r[10].strip()
    output_val = r[11].strip()

    prio_style = "PriorityGap" if prio_val == "Gấp" else ("PriorityCao" if prio_val == "Cao" else "PriorityTB")

    row_xml = f'''    <Row ss:Height="45">
     <Cell ss:StyleID="CenterCell"><Data ss:Type="Number">{stt}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(date_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(user_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(due_val)}</Data></Cell>
     <Cell ss:StyleID="HourCell"><Data ss:Type="Number">{hrs_val}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(proj_val)}</Data></Cell>
     <Cell ss:StyleID="DoneStyle"><Data ss:Type="String">{html.escape(status_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(src_val)}</Data></Cell>
     <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(task_val)}</Data></Cell>
     <Cell ss:StyleID="{prio_style}"><Data ss:Type="String">{html.escape(prio_val)}</Data></Cell>
     <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(note_val)}</Data></Cell>
     <Cell ss:StyleID="OutputStyle"><Data ss:Type="String">{html.escape(output_val)}</Data></Cell>
    </Row>'''
    xls_rows.append(row_xml)

with open(XLS_PATH, 'r', encoding='utf-8') as f:
    xls_content = f.read()

# Replace rows in Table
table_pattern = r'(<Row ss:Height="32">[\s\S]*?</Row>)([\s\S]*?)(</Table>)'
m = re.search(table_pattern, xls_content)
if m:
    header_part = m.group(1)
    new_table_body = header_part + '\n' + '\n'.join(xls_rows) + '\n   '
    xls_content = xls_content[:m.start()] + new_table_body + m.group(3) + xls_content[m.end():]
    with open(XLS_PATH, 'w', encoding='utf-8') as f:
        f.write(xls_content)
    print(f"Updated XLS {XLS_PATH} successfully.")
else:
    print("Could not match XLS table pattern.")
