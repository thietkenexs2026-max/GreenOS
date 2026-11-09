# -*- coding: utf-8 -*-
import csv
import re
import html
import os
from collections import defaultdict

CSV_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv'
CSV_12_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS_12cot.csv'
XLS_PATH = 'Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.xls'
HTML_PATH = 'SHEET_HOANG_THANG_10.html'

# 1. Read existing CSV (12 cols)
with open(CSV_12_PATH, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f))
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
        'row': ['', '2026/10/06', 'Hoàng', '06/10/2026', '2', 'Greenfi', 'Done', 'Cô thuỷ',
                'Thiết kế bộ Slide kinh doanh GreenFi theo yêu cầu cô Thủy', 'Gấp',
                'Tổng hợp sơ đồ giải pháp, mô hình liên kết HTX nông nghiệp và hoàn thiện bản thảo slide gửi cô Thủy review đợt 1.',
                'Slide kinh doanh GreenFi hoàn thiện bản thảo đợt 1 | 📄 Xem slide: https://drive.google.com/file/d/1KIf-iXYA0-v1tVC-k3oXiUigOutQKAW3/view?usp=sharing']
    },
    # 13/10: Slide cô Thủy sửa đợt 1
    {
        'date': '2026/10/13',
        'insert_after_kw': 'gắn nhãn sao ocop',
        'row': ['', '2026/10/13', 'Hoàng', '15/10/2026', '1.5', 'Greenfi', 'Đang làm', 'Cô thuỷ',
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
        'row': ['', '2026/10/14', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Đang làm', 'Cô thuỷ',
                'Hoàn thiện đồ họa và bảng biểu phân tích cho slide kinh doanh cô Thủy', 'Cao',
                'Thiết kế đồ họa các slide quy trình bao tiêu HTX, chuẩn hóa font chữ thương hiệu và đưa hình ảnh thực tế trang trại vào bài.',
                'Bộ slide hoàn thiện 90% các trang đồ họa và sơ đồ luồng HTX']
    },
    # 15/10: Final Slide cô Thủy
    {
        'date': '2026/10/15',
        'insert_after_kw': 'ứng thêm vật tư nông nghiệp',
        'row': ['', '2026/10/15', 'Hoàng', '15/10/2026', '2', 'Greenfi', 'Done', 'Cô thuỷ',
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
combined_12_rows = []
for r in filtered_rows:
    combined_12_rows.append(r)
    task_desc = r[8].lower()
    for at in additional_tasks:
        if at['insert_after_kw'].lower() in task_desc:
            combined_12_rows.append(at['row'])

# Renumber STT & Clean names & Remove [hours] from notes & Sanitize quotes for TSV
for idx, r in enumerate(combined_12_rows, 1):
    r[0] = str(idx)
    for col_i in range(len(r)):
        # Normalize Vinh
        r[col_i] = re.sub(r'(?i)\b(anh\s+vinh|a\.?\s*vinh)\b', 'Vinh', r[col_i])
        # Remove [xh] prefix from notes
        if col_i == 10:
            r[col_i] = re.sub(r'^\[\d+(?:\.\d+)?h\]\s*', '', r[col_i].strip())
        # Replace double quotes with single quotes to prevent TSV copy truncation
        r[col_i] = r[col_i].replace('"', "'")

# Validate daily hours
daily = defaultdict(float)
total_done = 0
total_doing = 0
for r in combined_12_rows:
    daily[r[1]] += float(r[4])
    if r[6].strip() == 'Done':
        total_done += 1
    else:
        total_doing += 1

print(f"Total tasks: {len(combined_12_rows)} | Total hours: {sum(daily.values())}h | Done: {total_done} | In progress: {total_doing}")
for d in sorted(daily.keys()):
    if daily[d] != 8.0:
        print(f"WARNING: {d} total hours is {daily[d]}h (expected 8.0h)")

# 2. Build 11-column rows (matching user's master Google Sheet exactly):
# Col 0: STT
# Col 1: Ngày (yyyy/mm/dd)
# Col 2: Người làm
# Col 3: Dự kiến hoàn thành
# Col 4: Nexs/ Greenfi
# Col 5: Tiến độ
# Col 6: Nguồn
# Col 7: Đầu việc
# Col 8: Thứ tự ưu tiên
# Col 9: Ghi chú
# Col 10: Output/Tài liệu

header_11 = ['STT', 'Ngày (yyyy/mm/dd)', 'Người làm', 'Dự kiến hoàn thành', 'Nexs/ Greenfi', 'Tiến độ', 'Nguồn', 'Đầu việc', 'Thứ tự ưu tiên', 'Ghi chú', 'Output/Tài liệu']
combined_11_rows = []
for r in combined_12_rows:
    stt = r[0]
    date_val = r[1]
    user_val = r[2]
    due_val = r[3]
    hrs_val = r[4]
    proj_val = r[5]
    status_val = r[6]
    src_val = r[7]
    task_val = r[8]
    prio_val = r[9]
    note_val = r[10]
    output_val = r[11]
    
    r_11 = [stt, date_val, user_val, due_val, proj_val, status_val, src_val, task_val, prio_val, note_val, output_val]
    combined_11_rows.append(r_11)

# Write 11-column CSV (Primary standard matching master sheet)
with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header_11)
    writer.writerows(combined_11_rows)

print(f"Updated 11-col CSV {CSV_PATH} successfully.")

# Write 12-column CSV (With hours)
header_12 = ['STT', 'Ngày (yyyy/mm/dd)', 'Người làm', 'Dự kiến hoàn thành', 'Thời lượng (Giờ)', 'Nexs/ Greenfi', 'Tiến độ', 'Nguồn', 'Đầu việc', 'Thứ tự ưu tiên', 'Ghi chú', 'Output/Tài liệu']
with open(CSV_12_PATH, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header_12)
    writer.writerows(combined_12_rows)

print(f"Updated 12-col CSV {CSV_12_PATH} successfully.")

# 3. Build HTML Output
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

tbody_rows = []
for r in combined_12_rows:
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

    # 11 columns in HTML table: STT, Ngày, Người làm, Dự kiến, Nexs/Greenfi, Tiến độ, Nguồn, Đầu việc (kèm badge giờ), Ưu tiên, Ghi chú, Output
    row_html = f'''        <tr>
          <td class="col-stt">{stt}</td>
          <td class="col-date">{html.escape(date_val)}</td>
          <td class="col-user">{html.escape(user_val)}</td>
          <td class="col-due">{html.escape(due_val)}</td>
          <td class="col-proj">{html.escape(proj_val)}</td>
          <td class="col-status"><span class="badge {status_badge_class}">{html.escape(status_val)}</span></td>
          <td class="col-src">{html.escape(src_val)}</td>
          <td class="col-task"><span class="badge-hour" style="margin-right:6px; flex-shrink:0;">{hrs_val}h</span>{html.escape(task_val)}</td>
          <td class="col-prio"><span class="badge {prio_badge_class}">{html.escape(prio_val)}</span></td>
          <td class="col-note">{html.escape(note_val)}</td>
          <td class="col-output">{output_formatted}</td>
        </tr>'''
    tbody_rows.append(row_html)

tbody_new = '<tbody>\n' + '\n'.join(tbody_rows) + '\n      </tbody>'

# Format TSVs for clipboard
tsv_11_text = '\n'.join(['\t'.join(r) for r in combined_11_rows])
tsv_12_text = '\n'.join(['\t'.join(r) for r in combined_12_rows])

# Full modern HTML template
html_template = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[NEXS - GreenFi] Báo Cáo Công Việc Tháng 10 - Hoàng (GreenOS)</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220%22><text y=%2226%22 font-size=%2224%22>📊</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #F8F9FA;
      color: #1F2937;
      line-height: 1.45;
      font-size: 13px;
    }}
    .sheets-header {{
      background: #FFFFFF;
      border-bottom: 1px solid #E5E7EB;
      padding: 12px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .sheets-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .sheets-icon {{
      width: 38px;
      height: 38px;
      background: #E8F5E9;
      color: #1B7A43;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: bold;
    }}
    .sheets-title-box h1 {{
      font-size: 16px;
      font-weight: 700;
      color: #111827;
      margin: 0;
    }}
    .sheets-title-box div {{
      font-size: 12px;
      color: #6B7280;
      margin-top: 2px;
    }}
    .sheets-actions {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .btn-action {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 13px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap !important;
    }}
    .btn-green {{
      background: #1B7A43;
      color: #FFFFFF;
      box-shadow: 0 1px 2px rgba(27,122,67,0.2);
    }}
    .btn-green:hover {{ background: #145E33; }}
    .btn-outline {{
      background: #FFFFFF;
      color: #374151;
      border-color: #D1D5DB;
    }}
    .btn-outline:hover {{ background: #F3F4F6; }}
    .btn-blue {{
      background: #0284C7;
      color: #FFFFFF;
    }}
    .btn-blue:hover {{ background: #0369A1; }}
    .btn-amber {{
      background: #D97706;
      color: #FFFFFF;
    }}
    .btn-amber:hover {{ background: #B45309; }}

    .sheets-toolbar {{
      background: #FFFFFF;
      border-bottom: 1px solid #E5E7EB;
      padding: 10px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }}
    .toolbar-metrics {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .metric-pill {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 4px 10px;
      background: #F3F4F6;
      border: 1px solid #E5E7EB;
      border-radius: 999px;
      font-size: 11.5px;
      color: #374151;
    }}
    .metric-pill strong {{ color: #111827; }}
    .metric-pill.success {{ background: #DEF7EC; border-color: #BCF0DA; color: #03543F; }}
    .metric-pill.warning {{ background: #FEF3C7; border-color: #FDE68A; color: #92400E; }}

    .search-box {{
      display: flex;
      align-items: center;
      background: #F9FAFB;
      border: 1px solid #D1D5DB;
      border-radius: 6px;
      padding: 5px 10px;
      width: 280px;
    }}
    .search-box input {{
      border: none;
      background: transparent;
      outline: none;
      font-size: 12.5px;
      width: 100%;
      color: #111827;
    }}

    .grid-container {{
      width: 100%;
      overflow-x: auto;
      background: #FFFFFF;
      border-bottom: 1px solid #E5E7EB;
    }}
    table {{
      width: 100%;
      min-width: 1550px;
      border-collapse: collapse;
      text-align: left;
    }}
    th {{
      background: #F9FAFB;
      color: #4B5563;
      font-weight: 600;
      font-size: 11.5px;
      padding: 8px 12px;
      border: 1px solid #E5E7EB;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      position: sticky;
      top: 63px;
      z-index: 10;
    }}
    td {{
      padding: 13px 15px;
      border: 1px solid #E5E7EB;
      vertical-align: middle;
      font-size: 13px;
      line-height: 1.55;
    }}
    tr:hover td {{
      background-color: #F8FAFC;
    }}

    /* Column Widths & Alignments (Rộng rãi, thoáng đãng, không bị sát chữ) */
    .col-stt {{ width: 50px; text-align: center; font-weight: 600; color: #6B7280; }}
    .col-date {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; }}
    .col-user {{ width: 95px; text-align: center; font-weight: 500; }}
    .col-due {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; color: #4B5563; }}
    .col-proj {{ width: 130px; font-weight: 600; color: #1E3A8A; }}
    .col-status {{ width: 115px; text-align: center; }}
    .col-src {{ width: 125px; color: #4B5563; }}
    .col-task {{ width: 380px; font-weight: 500; color: #111827; }}
    .col-prio {{ width: 115px; text-align: center; }}
    .col-note {{ width: 400px; color: #374151; }}
    .col-output {{ min-width: 380px; }}

    /* Badges */
    .badge {{
      display: inline-block;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 11.5px;
      font-weight: 600;
      text-align: center;
      white-space: nowrap;
    }}
    .badge-done {{ background: #DEF7EC; color: #03543F; border: 1px solid #BCF0DA; }}
    .badge-inprogress {{ background: #FEF3C7; color: #92400E; border: 1px solid #FDE68A; }}
    .badge-gap {{ background: #FDE8E8; color: #9B1C1C; border: 1px solid #F8B4B4; }}
    .badge-cao {{ background: #FFEDD5; color: #9A3412; border: 1px solid #FDBA74; }}
    .badge-tb {{ background: #E0E7FF; color: #3730A3; border: 1px solid #C7D2FE; }}
    .badge-hour {{
      display: inline-block;
      padding: 1px 6px;
      background: #E8F5E9;
      color: #1B7A43;
      border: 1px solid #C8E6C9;
      border-radius: 4px;
      font-weight: 700;
      font-size: 11px;
    }}

    .output-box {{
      background: #F9FAFB;
      border: 1px solid #E5E7EB;
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 12px;
    }}
    .output-img-link {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      margin-top: 5px;
      margin-right: 5px;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      text-decoration: none;
      transition: opacity 0.15s ease;
    }}
    .output-img-link:hover {{ opacity: 0.85; }}

    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #111827;
      color: #FFFFFF;
      padding: 12px 20px;
      border-radius: 8px;
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
      font-size: 13px;
      font-weight: 500;
      display: none;
      z-index: 10000;
      animation: fadeIn 0.2s ease;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
  </style>
</head>
<body>
  <div class="sheets-header">
    <div class="sheets-left">
      <div class="sheets-icon">📊</div>
      <div class="sheets-title-box">
        <h1>[NEXS - GreenFi] Báo Cáo Công Việc Tháng 10 - Hoàng (GreenOS)</h1>
        <div>Đầy đủ 70 đầu việc cả tháng (01/10/2026 - 30/10/2026) · Chuẩn 11 Cột Khớp 100% Google Sheet Mẫu</div>
      </div>
    </div>
    <div class="sheets-actions">
      <button class="btn-action btn-green" onclick="copyTSV11()">
        📋 Sao Chép 70 Dòng (Chuẩn 11 Cột Mẫu)
      </button>
      <button class="btn-action btn-outline" onclick="copyTSV12()">
        📋 Sao Chép (Kèm Cột Giờ - 12 Cột)
      </button>
      <a class="btn-action btn-blue" href="/Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv" download>
        📥 Tải CSV (11 Cột Mẫu)
      </a>
      <a class="btn-action btn-amber" href="/Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.xls" download>
        📊 Tải Excel (.xls)
      </a>
    </div>
  </div>

  <div class="sheets-toolbar">
    <div class="toolbar-metrics">
      <div class="metric-pill">👤 Người làm: <strong>Hoàng (Frontend Lead)</strong></div>
      <div class="metric-pill">🎯 Dự án: <strong>Green Village · Greenfi · WiseMeal</strong></div>
      <div class="metric-pill">📅 Lịch làm việc: <strong>22 Buổi (01/10 - 30/10)</strong></div>
      <div class="metric-pill success">⏱️ Cân đối giờ: <strong>8.0h/buổi = 176 Giờ cả tháng</strong></div>
      <div class="metric-pill">📋 <strong>{len(combined_11_rows)} Đầu việc cả tháng</strong> ({total_done} Done · {total_doing} Đang làm)</div>
      <div class="metric-pill">📌 Nguồn: <strong>Vinh và BLĐ</strong></div>
    </div>
    <div class="search-box">
      <span style="color:#6B7280; margin-right: 6px;">🔍</span>
      <input type="text" id="searchInput" placeholder="Tìm kiếm nhanh đầu việc, ngày, sản phẩm..." onkeyup="filterTable()">
    </div>
  </div>

  <div class="grid-container">
    <table id="taskTable">
      <thead>
        <tr>
          <th class="col-stt">STT</th>
          <th class="col-date">Ngày<br>(yyyy/mm/dd)</th>
          <th class="col-user">Người làm</th>
          <th class="col-due">Dự kiến hoàn thành</th>
          <th class="col-proj">Nexs/ Greenfi</th>
          <th class="col-status">Tiến độ</th>
          <th class="col-src">Nguồn</th>
          <th class="col-task">Đầu việc</th>
          <th class="col-prio">Thứ tự ưu tiên</th>
          <th class="col-note">Ghi chú</th>
          <th class="col-output">Output / Tài liệu & Link ảnh</th>
        </tr>
      </thead>
      {tbody_new}
    </table>
  </div>

  <!-- Hidden textareas for 1-Click Clipboard Copying -->
  <textarea id="hiddenTsv" style="position:fixed; left:-9999px; top:-9999px;">{tsv_11_text}</textarea>
  <textarea id="hiddenTsv12" style="position:fixed; left:-9999px; top:-9999px;">{tsv_12_text}</textarea>

  <div id="toast" class="toast">
    <span id="toastMsg">✅ Đã sao chép 70 dòng vào bộ nhớ tạm! Bạn chỉ cần dán (Ctrl + V) vào Google Sheets.</span>
  </div>

  <script>
    function copyTSV11() {{
      const area = document.getElementById('hiddenTsv');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã sao chép 70 dòng (Chuẩn 11 Cột Google Sheet Mẫu)! Bạn chỉ cần click ô A2 rồi dán (Ctrl + V).');
    }}

    function copyTSV12() {{
      const area = document.getElementById('hiddenTsv12');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã sao chép 70 dòng (Kèm cột Thời lượng - 12 Cột)! Bạn có thể dán (Ctrl + V).');
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').innerText = msg;
      toast.style.display = 'block';
      setTimeout(() => {{ toast.style.display = 'none'; }}, 4000);
    }}

    function filterTable() {{
      const input = document.getElementById('searchInput').value.toLowerCase();
      const rows = document.querySelectorAll('#taskTable tbody tr');
      rows.forEach(row => {{
        const text = row.innerText.toLowerCase();
        row.style.display = text.includes(input) ? '' : 'none';
      }});
    }}
  </script>
</body>
</html>
'''

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Updated HTML {HTML_PATH} successfully.")

# 4. Generate XLS (11 columns matching master sheet)
xls_header = '''<?xml version="1.0" encoding="UTF-8"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <Styles>
  <Style ss:ID="Default" ss:Name="Normal">
   <Alignment ss:Vertical="Center"/>
   <Borders/>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="10" ss:Color="#000000"/>
   <Interior/>
   <NumberFormat/>
   <Protection/>
  </Style>
  <Style ss:ID="HeaderStyle">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center" ss:WrapText="1"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="10" ss:Color="#374151" ss:Bold="1"/>
   <Interior ss:Color="#F9FAFB" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="CellStyle">
   <Alignment ss:Vertical="Center" ss:WrapText="1"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#111827"/>
  </Style>
  <Style ss:ID="CenterCell">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#374151"/>
  </Style>
  <Style ss:ID="DoneStyle">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#03543F" ss:Bold="1"/>
   <Interior ss:Color="#DEF7EC" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="DoingStyle">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#92400E" ss:Bold="1"/>
   <Interior ss:Color="#FEF3C7" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="PriorityGap">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#9B1C1C" ss:Bold="1"/>
   <Interior ss:Color="#FDE8E8" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="PriorityCao">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#9A3412" ss:Bold="1"/>
   <Interior ss:Color="#FFEDD5" ss:Pattern="Solid"/>
  </Style>
  <Style ss:ID="PriorityTB">
   <Alignment ss:Horizontal="Center" ss:Vertical="Center"/>
   <Borders>
    <Border ss:Position="Bottom" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Left" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Right" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
    <Border ss:Position="Top" ss:LineStyle="Continuous" ss:Weight="1" ss:Color="#E5E7EB"/>
   </Borders>
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="9.5" ss:Color="#3730A3"/>
   <Interior ss:Color="#E0E7FF" ss:Pattern="Solid"/>
  </Style>
 </Styles>
 <Worksheet ss:Name="BaoCaoThang10">
  <Table ss:ExpandedColumnCount="11" x:FullColumns="1" x:FullRows="1" ss:DefaultRowHeight="24">
   <Column ss:Width="45"/>
   <Column ss:Width="90"/>
   <Column ss:Width="75"/>
   <Column ss:Width="95"/>
   <Column ss:Width="105"/>
   <Column ss:Width="85"/>
   <Column ss:Width="105"/>
   <Column ss:Width="260"/>
   <Column ss:Width="85"/>
   <Column ss:Width="280"/>
   <Column ss:Width="300"/>
   <Row ss:Height="28">
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">STT</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Ngày (yyyy/mm/dd)</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Người làm</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Dự kiến hoàn thành</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Nexs/ Greenfi</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Tiến độ</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Nguồn</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Đầu việc</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Thứ tự ưu tiên</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Ghi chú</Data></Cell>
    <Cell ss:StyleID="HeaderStyle"><Data ss:Type="String">Output/Tài liệu</Data></Cell>
   </Row>
'''

xls_rows = []
for r in combined_11_rows:
    stt = r[0].strip()
    date_val = r[1].strip()
    user_val = r[2].strip()
    due_val = r[3].strip()
    proj_val = r[4].strip()
    status_val = r[5].strip()
    src_val = r[6].strip()
    task_val = r[7].strip()
    prio_val = r[8].strip()
    note_val = r[9].strip()
    output_val = r[10].strip()

    status_style = "DoneStyle" if status_val == "Done" else "DoingStyle"
    prio_style = "PriorityGap" if prio_val == "Gấp" else ("PriorityCao" if prio_val == "Cao" else "PriorityTB")

    row_xml = f'''   <Row ss:Height="40">
    <Cell ss:StyleID="CenterCell"><Data ss:Type="Number">{stt}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(date_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(user_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(due_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(proj_val)}</Data></Cell>
    <Cell ss:StyleID="{status_style}"><Data ss:Type="String">{html.escape(status_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(src_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(task_val)}</Data></Cell>
    <Cell ss:StyleID="{prio_style}"><Data ss:Type="String">{html.escape(prio_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(note_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(output_val)}</Data></Cell>
   </Row>'''
    xls_rows.append(row_xml)

xls_footer = '''  </Table>
 </Worksheet>
</Workbook>'''

with open(XLS_PATH, 'w', encoding='utf-8') as f:
    f.write(xls_header + '\n'.join(xls_rows) + '\n' + xls_footer)

print(f"Updated 11-col XLS {XLS_PATH} successfully.")
