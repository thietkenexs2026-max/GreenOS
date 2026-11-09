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

# Base GreenOS rows (filter out slide and mealy tasks if re-running)
filtered_rows = [
    r for r in old_rows 
    if 'cô thủy' not in r[8].lower() and 'cô thủy' not in r[10].lower()
    and 'mealy' not in r[8].lower() and 'mealy' not in r[10].lower()
]

# Set balanced hours for GreenOS tasks on the modified dates
for r in filtered_rows:
    task = r[8].lower()
    d = r[1]
    
    # 2026/10/02 (Tổng 6h GreenOS + 2h Mealy = 8h)
    if d == '2026/10/02':
        r[4] = '2'
        
    # 2026/10/05 (Tổng 6h GreenOS + 2h Mealy = 8h)
    elif d == '2026/10/05':
        r[4] = '3'
        
    # 2026/10/06 (Tổng 6h GreenOS + 2h Slide = 8h)
    elif d == '2026/10/06':
        r[4] = '2'
        
    # 2026/10/13 (Tổng 4.5h GreenOS + 1.5h Slide + 2h Mealy = 8h)
    elif d == '2026/10/13':
        r[4] = '1.5'
        
    # 2026/10/14 (Tổng 6h GreenOS + 2h Slide = 8h)
    elif d == '2026/10/14':
        r[4] = '3'
        
    # 2026/10/15 (Tổng 6h GreenOS + 2h Slide = 8h)
    elif d == '2026/10/15':
        r[4] = '2'
        
    # 2026/10/22 (Tổng 6h GreenOS + 2h Mealy = 8h)
    elif d == '2026/10/22':
        r[4] = '3'

# Additional tasks list
additional_tasks = [
    # 02/10: Mealy Home UI/UX Support
    {
        'date': '2026/10/02',
        'insert_after_kw': 'lưu trạng thái đã xem onboarding',
        'row': ['', '2026/10/02', 'Hoàng', '02/10/2026', '2', 'WiseMeal', 'Done', 'Vinh và BLĐ',
                'Hỗ trợ Bảo tinh chỉnh và tối ưu luồng UI/UX Trang chủ ứng dụng Mealy', 'Trong tuần',
                'Rà soát bố cục các khối món ngon gia đình, căn chỉnh khoảng cách các nút gạt chế độ nấu ăn và trải nghiệm lướt mâm cơm 3 món.',
                'Giao diện Trang chủ Mealy mượt mà, đồng bộ luồng công thức nấu ăn cùng Bảo']
    },
    # 05/10: Review Ver 1 Mealy
    {
        'date': '2026/10/05',
        'insert_after_kw': 'cuộn ngang (carousel)',
        'row': ['', '2026/10/05', 'Hoàng', '05/10/2026', '2', 'WiseMeal', 'Done', 'Vinh và BLĐ',
                'Họp review đánh giá phiên bản Ver 1 ứng dụng Mealy cùng Bảo và team', 'Trong tuần',
                'Kiểm tra toàn bộ luồng tạo hộp thoại In-App, từ điển ẩm thực vùng miền và trải nghiệm lọc mâm cơm theo khẩu vị.',
                'Biên bản nghiệm thu Ver 1 Mealy đạt chuẩn trải nghiệm, chốt danh sách tối ưu đợt tiếp theo']
    },
    # 06/10: Slide cô Thủy đợt 1
    {
        'date': '2026/10/06',
        'insert_after_kw': 'bàn phím số to',
        'row': ['', '2026/10/06', 'Hoàng', '06/10/2026', '2', 'Greenfi', 'Done', 'Vinh và BLĐ',
                'Thiết kế bộ Slide kinh doanh GreenFi theo yêu cầu cô Thủy', 'Gấp',
                'Tổng hợp sơ đồ giải pháp, mô hình liên kết HTX nông nghiệp và hoàn thiện bản thảo slide gửi cô Thủy review đợt 1.',
                'Slide kinh doanh GreenFi hoàn thiện bản thảo đợt 1 | 📄 Xem slide: https://drive.google.com/file/d/1KIf-iXYA0-v1tVC-k3oXiUigOutQKAW3/view?usp=sharing']
    },
    # 13/10: Slide cô Thủy sửa đợt 1
    {
        'date': '2026/10/13',
        'insert_after_kw': 'gắn nhãn sao ocop',
        'row': ['', '2026/10/13', 'Hoàng', '15/10/2026', '1.5', 'Greenfi', 'Đang làm', 'Vinh và BLĐ',
                'Tiếp nhận phản hồi và chỉnh sửa slide kinh doanh cô Thủy', 'Cao',
                'Cập nhật lại bố cục trang bìa, tinh chỉnh các mốc tiến độ triển khai và bổ sung phần thuyết minh mô hình sàn nông sản.',
                'Bản sửa đổi slide kinh doanh theo góp ý của cô Thủy']
    },
    # 13/10: Mealy Đi chợ & Phân quyền
    {
        'date': '2026/10/13',
        'insert_after_kw': 'phê duyệt nông sản lên sàn',
        'row': ['', '2026/10/13', 'Hoàng', '13/10/2026', '2', 'WiseMeal', 'Done', 'Vinh và BLĐ',
                'Tối ưu luồng Đi Chợ và phân chia phiên người dùng cho ứng dụng Mealy', 'Gấp',
                'Tách bạch danh sách nguyên liệu cần mua, lược bỏ gia vị nước nêm để user tự thêm khi hết; chia phiên khách vãng lai và tài khoản, khóa tính năng làm tiệc & chia sẻ danh sách đi chợ đối với khách chưa đăng nhập.',
                'Luồng Đi Chợ Mealy thông minh, danh sách nguyên liệu tinh gọn và kiểm soát phân quyền khách chuẩn xác']
    },
    # 14/10: Slide cô Thủy sửa đợt 2
    {
        'date': '2026/10/14',
        'insert_after_kw': 'cây giống cấy mô',
        'row': ['', '2026/10/14', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Đang làm', 'Vinh và BLĐ',
                'Hoàn thiện đồ họa và bảng biểu phân tích cho slide kinh doanh cô Thủy', 'Cao',
                'Thiết kế đồ họa các slide quy trình bao tiêu HTX, chuẩn hóa font chữ thương hiệu và đưa hình ảnh thực tế trang trại vào bài.',
                'Bộ slide hoàn thiện 90% các trang đồ họa và sơ đồ luồng HTX']
    },
    # 15/10: Final Slide cô Thủy
    {
        'date': '2026/10/15',
        'insert_after_kw': 'ứng thêm vật tư nông nghiệp',
        'row': ['', '2026/10/15', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Done', 'Vinh và BLĐ',
                'Final hoàn tất đóng gói Slide kinh doanh GreenFi gửi cô Thủy duyệt', 'Gấp',
                'Rà soát trang cuối, xuất file trình chiếu hoàn chỉnh chuẩn bị cho buổi báo cáo chiến lược GreenFi.',
                'Bộ Slide kinh doanh GreenFi hoàn chỉnh bản Final | 📄 Xem slide: https://drive.google.com/file/d/12eBOBRx8cq5E1h-ushxr9CmOMqW7ywfl/view?usp=sharing']
    },
    # 22/10: Review Ver 2 Mealy
    {
        'date': '2026/10/22',
        'insert_after_kw': 'tự động gán xe tải',
        'row': ['', '2026/10/22', 'Hoàng', '22/10/2026', '2', 'WiseMeal', 'Done', 'Vinh và BLĐ',
                'Họp review đánh giá toàn diện phiên bản Ver 2 ứng dụng Mealy', 'Gấp',
                'Đánh giá toàn bộ UI/UX, kho công thức nấu ăn, luồng xây dựng menu bữa cơm, trải nghiệm đi chợ và tính năng checking đồ ăn lưu trữ trong tủ lạnh trước khi đẩy store.',
                'Nghiệm thu toàn bộ tính năng Ver 2 Mealy cùng Bảo và team, đạt chuẩn phát hành TestFlight/CH Play']
    }
]

# Combine rows sequentially
combined_rows = []
for r in filtered_rows:
    combined_rows.append(r)
    task_desc = r[8].lower()
    for at in additional_tasks:
        if at['insert_after_kw'].lower() in task_desc:
            combined_rows.append(at['row'])

# Renumber STT & Clean names
for idx, r in enumerate(combined_rows, 1):
    r[0] = str(idx)
    for col_i in range(len(r)):
        r[col_i] = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', r[col_i])

# Validate daily hours
daily = defaultdict(float)
total_done = 0
total_doing = 0
for r in combined_rows:
    daily[r[1]] += float(r[4])
    if r[6].strip() == 'Done':
        total_done += 1
    else:
        total_doing += 1

print(f"Total tasks: {len(combined_rows)} | Total hours: {sum(daily.values())}h | Done: {total_done} | In progress: {total_doing}")
for d in sorted(daily.keys()):
    if daily[d] != 8.0:
        print(f"WARNING: {d} total hours is {daily[d]}h (expected 8.0h)")

# 2. Write CSV
with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(combined_rows)

print(f"Updated CSV {CSV_PATH} successfully.")

# 3. Update HTML
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

html_content = re.sub(r'<div class="metric-pill">📋 <strong>[\s\S]*?</strong></div>',
                      f'<div class="metric-pill">📋 <strong>{len(combined_rows)} Đầu việc</strong> ({total_done} Done · {total_doing} Đang làm)</div>',
                      html_content)

html_content = re.sub(r'Đã sao chép \d+ dòng', f'Đã sao chép {len(combined_rows)} dòng', html_content)

raw_tsv_text = '\n'.join(['\t'.join(r) for r in combined_rows])
html_content = re.sub(r'<textarea id="rawTsvData" style="display:none;">[\s\S]*?</textarea>',
                      f'<textarea id="rawTsvData" style="display:none;">{raw_tsv_text}</textarea>',
                      html_content)

html_content = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', html_content)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated HTML {HTML_PATH} successfully.")

# 4. Update XLS
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
