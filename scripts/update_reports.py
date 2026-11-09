# -*- coding: utf-8 -*-
import csv
import re
import html
import os
from collections import defaultdict

CSV_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv'
XLS_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.xls'
HTML_PATH = 'SHEET_HOANG_THANG_10.html'

# 1. Read existing CSV
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    header = reader[0]
    old_rows = reader[1:]

# New slide tasks to insert
# Note: insertion based on task content matching so it's idempotent
slide_tasks = [
    {
        'date': '2026/10/06',
        'insert_after_task_kw': 'bàn phím số to', # STT 11
        'row': ['', '2026/10/06', 'Hoàng', '06/10/2026', '2', 'Greenfi', 'Done', 'Vinh và BLĐ',
                'Thiết kế bộ Slide kinh doanh GreenFi theo yêu cầu cô Thủy', 'Gấp',
                'Tổng hợp sơ đồ giải pháp, mô hình liên kết HTX nông nghiệp và hoàn thiện bản thảo slide gửi cô Thủy review đợt 1.',
                'Slide kinh doanh GreenFi hoàn thiện bản thảo đợt 1 | 📄 Xem slide: https://drive.google.com/file/d/1KIf-iXYA0-v1tVC-k3oXiUigOutQKAW3/view?usp=sharing']
    },
    {
        'date': '2026/10/13',
        'insert_after_task_kw': 'gắn nhãn sao OCOP', # STT 25
        'row': ['', '2026/10/13', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Đang làm', 'Vinh và BLĐ',
                'Tiếp nhận phản hồi và chỉnh sửa slide kinh doanh cô Thủy', 'Cao',
                'Cập nhật lại bố cục trang bìa, tinh chỉnh các mốc tiến độ triển khai và bổ sung phần thuyết minh mô hình sàn nông sản.',
                'Bản sửa đổi slide kinh doanh theo góp ý của cô Thủy']
    },
    {
        'date': '2026/10/14',
        'insert_after_task_kw': 'cây giống cấy mô', # STT 27
        'row': ['', '2026/10/14', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Đang làm', 'Vinh và BLĐ',
                'Hoàn thiện đồ họa và bảng biểu phân tích cho slide kinh doanh cô Thủy', 'Cao',
                'Thiết kế đồ họa các slide quy trình bao tiêu HTX, chuẩn hóa font chữ thương hiệu và đưa hình ảnh thực tế trang trại vào bài.',
                'Bộ slide hoàn thiện 90% các trang đồ họa và sơ đồ luồng HTX']
    },
    {
        'date': '2026/10/15',
        'insert_after_task_kw': 'ứng thêm vật tư nông nghiệp', # STT 30
        'row': ['', '2026/10/15', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Done', 'Vinh và BLĐ',
                'Final hoàn tất đóng gói Slide kinh doanh GreenFi gửi cô Thủy duyệt', 'Gấp',
                'Rà soát trang cuối, xuất file trình chiếu hoàn chỉnh chuẩn bị cho buổi báo cáo chiến lược GreenFi.',
                'Bộ Slide kinh doanh GreenFi hoàn chỉnh bản Final | 📄 Xem slide: https://drive.google.com/file/d/12eBOBRx8cq5E1h-ushxr9CmOMqW7ywfl/view?usp=sharing']
    }
]

# Filter out old slide tasks if already present to ensure idempotency
filtered_rows = [r for r in old_rows if 'cô thủy' not in r[8].lower() and 'cô thủy' not in r[10].lower()]

# Adjust hours on those specific days to make room for 2h slide tasks
for r in filtered_rows:
    task = r[8].lower()
    # 2026/10/06
    if 'bấm máy ảnh chụp nông sản' in task or 'cắt ảnh vuông và xóa phông' in task or 'bàn phím số to' in task:
        r[4] = '2'
    # 2026/10/13
    elif 'danh mục 388 sản phẩm' in task or 'thanh nghe ghi âm giọng nói' in task or 'gắn nhãn sao ocop' in task:
        r[4] = '2'
    # 2026/10/14
    elif 'sổ theo dõi tín dụng' in task or 'cây giống cấy mô' in task:
        r[4] = '3'
    # 2026/10/15
    elif 'can thiệp khẩn cấp' in task or 'biểu đồ tiến độ bao tiêu' in task or 'ứng thêm vật tư nông nghiệp' in task:
        r[4] = '2'

# Reconstruct combined list
combined_rows = []
for r in filtered_rows:
    combined_rows.append(r)
    task_desc = r[8].lower()
    for st in slide_tasks:
        if st['insert_after_task_kw'].lower() in task_desc:
            combined_rows.append(st['row'])

# Renumber STT from 1 to N and clean references of anh vinh -> Vinh
for idx, r in enumerate(combined_rows, 1):
    r[0] = str(idx)
    for col_i in range(len(r)):
        r[col_i] = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', r[col_i])

# Check daily hours
daily = defaultdict(float)
total_done = 0
total_doing = 0
for r in combined_rows:
    daily[r[1]] += float(r[4])
    if r[6].strip() == 'Done':
        total_done += 1
    else:
        total_doing += 1

print(f"Total rows: {len(combined_rows)} | Total hours: {sum(daily.values())}h | Done: {total_done} | In progress: {total_doing}")

# Save CSV
with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(combined_rows)

print(f"Updated CSV {CSV_PATH} successfully.")

# 2. Update HTML
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
            is_slide = ('slide' in label.lower() or 'drive' in url.lower())
            is_web = ('web' in label.lower() or 'portal' in label.lower())
            if is_slide:
                bg = '#FEF3C7'
                color = '#92400E'
            elif is_web:
                bg = '#E0F2FE'
                color = '#0369A1'
            else:
                bg = '#E2E8F0'
                color = '#1E293B'
            links_html.append(f'<a class="output-img-link" href="{html.escape(url)}" target="_blank" style="background:{bg}; color:{color};">{html.escape(label)}</a>')
        else:
            links_html.append(f'<span>{html.escape(p)}</span>')
    
    res = f'<div class="output-box"><strong>{html.escape(title)}</strong>'
    if links_html:
        res += '<br>' + ' '.join(links_html)
    res += '</div>'
    return res

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Build table rows HTML
tbody_rows = []
for r in combined_rows:
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
html_content = re.sub(r'<tbody>[\s\S]*?</tbody>', tbody_new, html_content)

# Update metric pill for task count
html_content = re.sub(r'<div class="metric-pill">✅ <strong>[\s\S]*?</strong></div>',
                      f'<div class="metric-pill">📋 <strong>{len(combined_rows)} Đầu việc</strong> ({total_done} Done · {total_doing} Đang làm)</div>',
                      html_content)

# Update toast
html_content = re.sub(r'Đã sao chép \d+ dòng', f'Đã sao chép {len(combined_rows)} dòng', html_content)

# Replace <textarea id="rawTsvData">
raw_tsv_text = '\n'.join(['\t'.join(r) for r in combined_rows])
html_content = re.sub(r'<textarea id="rawTsvData" style="display:none;">[\s\S]*?</textarea>',
                      f'<textarea id="rawTsvData" style="display:none;">{raw_tsv_text}</textarea>',
                      html_content)

html_content = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', html_content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated HTML {HTML_PATH} successfully.")

# 3. Update XLS
xls_rows = []
for r in combined_rows:
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

    status_style = "DoneStyle" if status_val == "Done" else "CellStyle"
    prio_style = "PriorityGap" if prio_val == "Gấp" else ("PriorityCao" if prio_val == "Cao" else "PriorityTB")

    row_xml = f'''    <Row ss:Height="45">
     <Cell ss:StyleID="CenterCell"><Data ss:Type="Number">{stt}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(date_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(user_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(due_val)}</Data></Cell>
     <Cell ss:StyleID="HourCell"><Data ss:Type="Number">{hrs_val}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(proj_val)}</Data></Cell>
     <Cell ss:StyleID="{status_style}"><Data ss:Type="String">{html.escape(status_val)}</Data></Cell>
     <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(src_val)}</Data></Cell>
     <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(task_val)}</Data></Cell>
     <Cell ss:StyleID="{prio_style}"><Data ss:Type="String">{html.escape(prio_val)}</Data></Cell>
     <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(note_val)}</Data></Cell>
     <Cell ss:StyleID="OutputStyle"><Data ss:Type="String">{html.escape(output_val)}</Data></Cell>
    </Row>'''
    xls_rows.append(row_xml)

with open(XLS_PATH, 'r', encoding='utf-8') as f:
    xls_content = f.read()

table_pattern = r'(<Row ss:Height="32">[\s\S]*?</Row>)([\s\S]*?)(</Table>)'
m = re.search(table_pattern, xls_content)
if m:
    header_part = m.group(1)
    new_table_body = header_part + '\n' + '\n'.join(xls_rows) + '\n   '
    xls_content = xls_content[:m.start()] + new_table_body + m.group(3) + xls_content[m.end():]
    xls_content = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', xls_content)
    with open(XLS_PATH, 'w', encoding='utf-8') as f:
        f.write(xls_content)
    print(f"Updated XLS {XLS_PATH} successfully.")
