# -*- coding: utf-8 -*-
import csv
import html
import json
import re

CSV_W1_PATH = 'Bao_Cao_Tuan_1_02_11_den_06_11_Hoang.csv'
CSV_W2_PATH = 'Bao_Cao_Tuan_2_09_11_den_13_11_Hoang.csv'
CSV_ALL_PATH = 'Bao_Cao_Cong_Viec_Tuan_Hoang_GreenOS.csv'
XLS_PATH = 'Bao_Cao_Cong_Viec_Tuan_Hoang_GreenOS.xls'
HTML_PATH = 'SHEET_BAO_CAO_TUAN_HOANG.html'
APPS_SCRIPT_PATH = 'Google_Apps_Script_1Click_Import.js'

HEADER_11 = [
    'STT',
    'Ngày (yyyy/mm/dd)',
    'Người làm',
    'Dự kiến hoàn thành',
    'Nexs/ Greenfi',
    'Tiến độ',
    'Nguồn',
    'Đầu việc',
    'Thứ tự ưu tiên',
    'Ghi chú',
    'Output/Tài liệu'
]

WEEK_1_TASKS = [
    [
        '1', '2026/11/02', 'Hoàng', '02/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Dựng khung trang quản lý cho cán bộ xã Đồng Lam',
        'Gấp',
        'Chia bố cục 2 cột giống bên HTX, cột trái là menu, bên trên để 4 thẻ thống kê số hộ với sản lượng trong xã.',
        'https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png | https://cho-xanh.vercel.app/commune-dashboard'
    ],
    [
        '2', '2026/11/02', 'Hoàng', '02/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Gộp 3 màn hình Bác Ba, HTX với Xã vào chung trang Portal',
        'Gấp',
        'Làm thanh chuyển qua lại giữa 3 màn hình để lúc mở demo cho sếp bấm chuyển tab luôn không phải mở nhiều link.',
        'https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png | https://cho-xanh.vercel.app/portal'
    ],
    [
        '3', '2026/11/02', 'Hoàng', '02/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Chỉnh lại font chữ với màu xanh cho đồng bộ với trang HTX',
        'Trong tuần',
        'Đổi sang font Lexend cho mấy con số nhìn rõ hơn, chỉnh lại tông màu xanh lá đậm.',
        'https://cho-xanh.vercel.app/output_images/01_dashboard_htx_tong_quan.webp'
    ],
    [
        '4', '2026/11/03', 'Hoàng', '03/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm bảng xếp hạng 3 HTX và theo dõi hồ sơ OCOP',
        'Gấp',
        'Liệt kê tiến độ làm hồ sơ OCOP 3-4 sao của từng thôn với bảng chấm điểm các HTX trong xã.',
        'https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'
    ],
    [
        '5', '2026/11/03', 'Hoàng', '03/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm phần ký duyệt báo cáo tháng có đóng dấu đỏ của xã',
        'Gấp',
        'Bấm nút phê duyệt là hiện con dấu đỏ của UBND xã đóng lên góc văn bản để xuất file báo cáo.',
        'https://cho-xanh.vercel.app/output_images/15_ver1_dashboard_xa_ky_so_dong_dau_do.png'
    ],
    [
        '6', '2026/11/03', 'Hoàng', '03/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Vẽ biểu đồ mức số hoá với sản lượng mùa vụ bằng Chart.js',
        'Trong tuần',
        'Vẽ 3 biểu đồ theo dõi số hộ lên sàn, lượt mượn máy nông nghiệp với sản lượng thu hoạch.',
        'https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'
    ],
    [
        '7', '2026/11/04', 'Hoàng', '04/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Thay hết mấy cái icon emoji cũ sang icon SVG',
        'Gấp',
        'Mấy chỗ menu với thẻ số liệu trước để emoji nhìn hơi rối nên thay hết sang icon nét vẽ SVG cho gọn.',
        'https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png'
    ],
    [
        '8', '2026/11/04', 'Hoàng', '04/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm bộ lọc theo thôn và tháng để biểu đồ tự nhảy số',
        'Trong tuần',
        'Chọn thôn hoặc đổi tháng báo cáo ở góc trên là số liệu với biểu đồ bên dưới tự đổi theo.',
        'https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'
    ],
    [
        '9', '2026/11/04', 'Hoàng', '04/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Thêm form nhập nhanh số liệu trực tiếp trên trang xã',
        'Trong tuần',
        'Làm popup để nhập thêm sản lượng mới ngay trên web, bấm lưu là biểu đồ cập nhật luôn.',
        'https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'
    ],
    [
        '10', '2026/11/05', 'Hoàng', '05/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Test lại luồng dữ liệu từ app Bác Ba sang HTX và Xã',
        'Gấp',
        'Kiểm tra từ lúc nông dân đăng bán chuối sấy đến lúc HTX duyệt đơn sỉ WinMart xem số liệu có khớp nhau không.',
        'https://cho-xanh.vercel.app/output_images/05_cong_b2b_dat_don_si.webp'
    ],
    [
        '11', '2026/11/05', 'Hoàng', '05/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Chỉnh lại màn hình Dual Studio để vừa xem điện thoại vừa xem web',
        'Trong tuần',
        'Đặt khung điện thoại Bác Ba cạnh màn hình HTX để lúc demo bấm bên này thì bên kia nhảy thông báo luôn.',
        'https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png'
    ],
    [
        '12', '2026/11/05', 'Hoàng', '05/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Chụp lại toàn bộ màn hình Ver 1 và nén sang đuôi WebP',
        'Trong tuần',
        'Chụp lại 11 màn hình của bản Ver 1 rồi nén nhẹ xuống để mở trên mạng 4G không bị chậm.',
        'https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp'
    ],
    [
        '13', '2026/11/06', 'Hoàng', '06/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Cấu hình lại file vercel.json và đẩy bản Ver 1 lên host',
        'Gấp',
        'Sửa lại đường dẫn ngắn cho các trang mobile, portal, htx-dashboard rồi đẩy code lên Vercel.',
        'https://cho-xanh.vercel.app/output_images/07_mobile_bac_ba_dark_mode.webp | https://cho-xanh.vercel.app/portal'
    ],
    [
        '14', '2026/11/06', 'Hoàng', '06/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Rà soát nghiệm thu xong bản Green Village Ver 1',
        'Gấp',
        'Kiểm tra lại toàn bộ link web và ảnh chụp màn hình bản Ver 1 để chốt giai đoạn 1.',
        'https://cho-xanh.vercel.app/output_images/02_htx_duyet_san_pham.webp'
    ],
    [
        '15', '2026/11/06', 'Hoàng', '06/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Họp với Vinh chốt hướng làm bản Ver 2 sang app G-Xanh',
        'Trong tuần',
        'Thống nhất dừng kiểu nông dân tự đăng lẻ tẻ, chuyển sang làm app G-Xanh bán hàng như sàn thương mại điện tử.',
        'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ]
]

WEEK_2_TASKS = [
    [
        '1', '2026/11/09', 'Hoàng', '09/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Viết tài liệu kế hoạch sản phẩm cho bản Ver 2 (App G-Xanh)',
        'Gấp',
        'Lên khung mô hình chuỗi bán lẻ và sàn G-Xanh Từ Làng Ra Phố: gom hàng từ xã về tổng rồi bán qua cửa hàng và app.',
        'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ],
    [
        '2', '2026/11/09', 'Hoàng', '09/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Vẽ sơ đồ tách 2 dòng tiền và chia 15 phân hệ chức năng',
        'Gấp',
        'Tách riêng tiền khách nạp thẻ mua hàng với tiền cổ đông góp vốn mở điểm, chia 234 tính năng ra 3 giai đoạn làm dần.',
        'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ],
    [
        '3', '2026/11/09', 'Hoàng', '09/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Viết kịch bản xử lý các lỗi hay gặp khi khách mua hàng trên app',
        'Trong tuần',
        'Tính trước mấy trường hợp hết hàng đột xuất tại quầy, khách ngoài bán kính giao lạnh 5km hoặc bấm thanh toán 2 lần.',
        'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '4', '2026/11/10', 'Hoàng', '10/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Dựng khung giao diện điện thoại cho app mua hàng G-Xanh',
        'Gấp',
        'Làm khung màn hình 430px kiểu Shopee, gắn thanh menu 5 tab dưới đáy (Chợ, GF-Track, Giỏ hàng, Thẻ Zalo, Tôi).',
        'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | https://cho-xanh.vercel.app/gxanh'
    ],
    [
        '5', '2026/11/10', 'Hoàng', '10/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm thanh tìm kiếm nông sản và các nút lọc theo nhóm hàng',
        'Gấp',
        'Gõ tên món hoặc tên thôn là lọc ra sản phẩm luôn; thêm các nút lọc Rau củ hữu cơ, Thịt cá bản địa, Đặc sản đóng gói.',
        'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '6', '2026/11/10', 'Hoàng', '10/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm khung Phiên Chợ Sớm đếm ngược giờ và danh sách sản phẩm 2 cột',
        'Trong tuần',
        'Thêm đồng hồ đếm ngược phiên chợ sáng, làm thẻ sản phẩm 2 cột có giá giảm, số lượng đã bán và nút dấu cộng thêm nhanh vào giỏ.',
        'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '7', '2026/11/11', 'Hoàng', '11/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm màn hình xem chi tiết món hàng và chọn quy cách đóng gói',
        'Gấp',
        'Bấm vào sản phẩm hiện ảnh to, đánh giá sao, chọn loại Hũ 500ml hay 1 Lít (hoặc Khay 500g / 1kg) thì giá tiền tự đổi theo.',
        'https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'
    ],
    [
        '8', '2026/11/11', 'Hoàng', '11/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm phần thông tin nguồn gốc nhà vườn và cụm nút Mua Ngay dưới đáy',
        'Trong tuần',
        'Ghi rõ hàng của hộ nào, thôn nào, bảo quản ra sao; dưới đáy gắn nút tăng giảm số lượng, Thêm vào giỏ và Mua Ngay.',
        'https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'
    ],
    [
        '9', '2026/11/11', 'Hoàng', '11/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm màn hình Giỏ hàng gom các món theo từng nhà vườn',
        'Gấp',
        'Món nào cùng một nhà vườn thì gom chung vào 1 khung giống Shopee, chỉnh thêm bớt số lượng hoặc xóa món là tự tính lại tổng tiền.',
        'https://cho-xanh.vercel.app/output_images/23_gxanh_gio_hang_gom_shop.png'
    ],
    [
        '10', '2026/11/12', 'Hoàng', '12/11/2026', '2.5', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm popup chọn mã giảm giá trừ tiền trực tiếp trong giỏ hàng',
        'Trong tuần',
        'Thêm 2 mã giảm 25k với mã miễn phí ship hỏa tốc 50k, bấm áp dụng là trừ thẳng vào số tiền cần thanh toán.',
        'https://cho-xanh.vercel.app/output_images/24_gxanh_modal_voucher.png'
    ],
    [
        '11', '2026/11/12', 'Hoàng', '12/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Dựng màn hình Thẻ thành viên Zalo hiển thị 3 loại điểm',
        'Gấp',
        'Làm thẻ thành viên màu xanh hiện tổng điểm đang có, chia 3 ô: Điểm nạp, Điểm thưởng, Hoa hồng giới thiệu.',
        'https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'
    ],
    [
        '12', '2026/11/12', 'Hoàng', '12/11/2026', '2.5', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm mã QR thanh toán tự đổi mới sau mỗi 60 giây',
        'Gấp',
        'Khách đưa mã QR này cho thu ngân quét trừ điểm, cứ hết 60s hoặc bấm vào là tự đổi mã mới để tránh chụp ảnh màn hình dùng lại.',
        'https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'
    ],
    [
        '13', '2026/11/13', 'Hoàng', '13/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm phần xác nhận đặt đơn, nạp thêm điểm VietQR và lịch sử điểm',
        'Gấp',
        'Bấm đặt hàng thì trừ điểm trong thẻ và lưu mã đơn; nếu thiếu điểm thì mở form nạp 200k/500k/1tr qua VietQR và ghi lại lịch sử cộng trừ điểm.',
        'https://cho-xanh.vercel.app/output_images/25_gxanh_modal_xac_nhan_dat_don.png | https://cho-xanh.vercel.app/output_images/27_gxanh_modal_nap_diem_vietqr.png | https://cho-xanh.vercel.app/output_images/28_gxanh_modal_lich_su_diem.png'
    ],
    [
        '14', '2026/11/13', 'Hoàng', '13/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Làm màn hình tra cứu tem GF-Track 6 chặng và gửi đánh giá sao',
        'Gấp',
        'Hiện thông tin nhật ký vùng trồng, nhiệt độ xe lạnh 3.2 độ C, giấy kiểm nghiệm VietGAP, hành trình 6 chặng từ ruộng lên kệ và form chấm 5 sao.',
        'https://cho-xanh.vercel.app/output_images/29_gxanh_tra_cuu_tem_gf_track.png | https://cho-xanh.vercel.app/output_images/30_gxanh_modal_danh_gia_5sao.png'
    ],
    [
        '15', '2026/11/13', 'Hoàng', '13/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        'Test lại toàn bộ các màn hình app G-Xanh và đẩy code lên nhánh hoang-dev',
        'Gấp',
        'Kiểm tra lại hết các nút thêm giỏ, áp mã, nạp điểm, đặt hàng trên khung điện thoại rồi commit đẩy lên nhánh hoang-dev.',
        'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | https://cho-xanh.vercel.app/gxanh'
    ]
]


def to_11_cols(rows_12):
    res = []
    for idx, r in enumerate(rows_12, 1):
        clean_r = [x.replace('"', "'").strip() for x in r]
        clean_r[0] = str(idx)
        out_val = clean_r[11].replace(' | ', '\n')
        r_11 = [
            clean_r[0], clean_r[1], clean_r[2], clean_r[3],
            clean_r[5], clean_r[6], clean_r[7], clean_r[8],
            clean_r[9], clean_r[10], out_val
        ]
        res.append(r_11)
    return res


w1_11 = to_11_cols(WEEK_1_TASKS)
w2_11 = to_11_cols(WEEK_2_TASKS)
all_12 = WEEK_1_TASKS + WEEK_2_TASKS
all_11 = to_11_cols(all_12)

for path, rows in [
    (CSV_W1_PATH, w1_11),
    (CSV_W2_PATH, w2_11),
    (CSV_ALL_PATH, all_11),
]:
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(HEADER_11)
        writer.writerows(rows)


def format_output_html(val):
    urls = [u.strip() for u in val.replace('\n', ' | ').split(' | ') if u.strip()]
    links_html = []
    for u in urls:
        links_html.append(
            f'<div><a href="{html.escape(u)}" target="_blank" style="color:#0284C7; text-decoration:underline; word-break:break-all;">{html.escape(u)}</a></div>'
        )
    return '\n'.join(links_html)


def build_tbody_html(rows_12):
    tbody_rows = []
    for idx, r in enumerate(rows_12, 1):
        _, date_val, user_val, due_val, hrs_val, proj_val, status_val, src_val, task_val, prio_val, note_val, output_val = [
            x.replace('"', "'").strip() for x in r
        ]
        status_badge_class = 'badge-done' if status_val == 'Done' else 'badge-inprogress'
        prio_badge_class = 'badge-gap' if prio_val == 'Gấp' else ('badge-cao' if prio_val == 'Cao' else 'badge-tb')
        output_formatted = format_output_html(output_val)

        row_html = f'''        <tr>
          <td class="col-stt">{idx}</td>
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
    return '\n'.join(tbody_rows)


def make_tsv(rows_11, include_header=True):
    lines = []
    if include_header:
        lines.append('\t'.join(HEADER_11))
    for r in rows_11:
        r_single_line = [col.replace('\n', ' | ') for col in r]
        lines.append('\t'.join(r_single_line))
    return '\n'.join(lines)


with open(APPS_SCRIPT_PATH, 'r', encoding='utf-8') as f:
    apps_script_code = f.read()

WEEKS_META = {
    'w1': {
        'tab_title': 'Tuần 1 - 2/11 - 6/11',
        'subtitle': 'Thứ 2 (02/11) → Thứ 6 (06/11) · Hoàn thiện Green Village Ver 1',
        'date_range': '02/11/2026 - 06/11/2026 (5 buổi · 40 giờ)',
        'count': len(w1_11),
        'csv_file': CSV_W1_PATH,
        'tbody': build_tbody_html(WEEK_1_TASKS),
        'tsv_with_header': make_tsv(w1_11, True),
        'tsv_data_only': make_tsv(w1_11, False),
    },
    'w2': {
        'tab_title': 'Tuần 2 - 9/11 - 13/11',
        'subtitle': 'Thứ 2 (09/11) → Thứ 6 (13/11) · Phát triển Ver 2 App G-Xanh (nhánh hoang-dev)',
        'date_range': '09/11/2026 - 13/11/2026 (5 buổi · 40 giờ)',
        'count': len(w2_11),
        'csv_file': CSV_W2_PATH,
        'tbody': build_tbody_html(WEEK_2_TASKS),
        'tsv_with_header': make_tsv(w2_11, True),
        'tsv_data_only': make_tsv(w2_11, False),
    },
    'all': {
        'tab_title': 'Gộp cả 2 Tuần (Tuần 1 + Tuần 2)',
        'subtitle': 'Tổng hợp 30 đầu việc của 2 tuần đầu tháng 11 (02/11 - 13/11/2026)',
        'date_range': '02/11/2026 - 13/11/2026 (10 buổi · 80 giờ)',
        'count': len(all_11),
        'csv_file': CSV_ALL_PATH,
        'tbody': build_tbody_html(all_12),
        'tsv_with_header': make_tsv(all_11, True),
        'tsv_data_only': make_tsv(all_11, False),
    }
}

weeks_json = json.dumps(WEEKS_META, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[NEXS - GreenFi] Báo Cáo Tuần Tháng 11 - Hoàng</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><text y=%2226%22 font-size=%2224%22>📊</text></svg>">
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
      padding-bottom: 52px;
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
    .sheets-left {{ display: flex; align-items: center; gap: 12px; }}
    .sheets-icon {{
      width: 38px; height: 38px; background: #E8F5E9; color: #1B7A43;
      border-radius: 8px; display: flex; align-items: center; justify-content: center;
      font-size: 20px; font-weight: bold;
    }}
    .sheets-title-box h1 {{ font-size: 16px; font-weight: 700; color: #111827; margin: 0; }}
    .sheets-title-box div {{ font-size: 12px; color: #6B7280; margin-top: 2px; }}
    .sheets-actions {{ display: flex; align-items: center; flex-wrap: wrap; gap: 8px; }}
    .btn-action {{
      display: inline-flex; align-items: center; gap: 6px; padding: 8px 14px;
      border-radius: 6px; font-size: 12.5px; font-weight: 600; cursor: pointer;
      border: 1px solid transparent; text-decoration: none; transition: all 0.15s ease;
      white-space: nowrap !important;
    }}
    .btn-purple {{ background: #7C3AED; color: #FFFFFF; }}
    .btn-purple:hover {{ background: #6D28D9; }}
    .btn-green {{ background: #1B7A43; color: #FFFFFF; }}
    .btn-green:hover {{ background: #145E33; }}
    .btn-outline {{ background: #FFFFFF; color: #374151; border-color: #D1D5DB; }}
    .btn-outline:hover {{ background: #F3F4F6; }}
    .btn-blue {{ background: #0284C7; color: #FFFFFF; }}
    .btn-blue:hover {{ background: #0369A1; }}
    .btn-amber {{ background: #D97706; color: #FFFFFF; }}
    .btn-amber:hover {{ background: #B45309; }}

    .week-switcher-banner {{
      background: #ECFDF5; border-bottom: 1px solid #A7F3D0; padding: 10px 20px;
      display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px;
    }}
    .week-tabs-top {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .week-tab-btn {{
      padding: 7px 14px; border-radius: 8px; font-size: 12.5px; font-weight: 700;
      cursor: pointer; border: 1px solid #6EE7B7; background: #FFFFFF; color: #065F46;
      display: inline-flex; align-items: center; gap: 6px;
    }}
    .week-tab-btn.active {{ background: #1B7A43; color: #FFFFFF; border-color: #1B7A43; }}

    .sheets-toolbar {{
      background: #FFFFFF; border-bottom: 1px solid #E5E7EB; padding: 10px 20px;
      display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px;
    }}
    .toolbar-metrics {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .metric-pill {{
      display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px;
      background: #F3F4F6; border: 1px solid #E5E7EB; border-radius: 999px;
      font-size: 11.5px; color: #374151;
    }}
    .metric-pill strong {{ color: #111827; }}
    .metric-pill.success {{ background: #DEF7EC; border-color: #BCF0DA; color: #03543F; }}

    .search-box {{
      display: flex; align-items: center; background: #F9FAFB; border: 1px solid #D1D5DB;
      border-radius: 6px; padding: 5px 10px; width: 280px;
    }}
    .search-box input {{ border: none; background: transparent; outline: none; font-size: 12.5px; width: 100%; }}

    .grid-container {{ width: 100%; overflow-x: auto; background: #FFFFFF; border-bottom: 1px solid #E5E7EB; }}
    table {{ width: 100%; min-width: 1550px; border-collapse: collapse; text-align: left; }}
    th {{
      background: #1B7A43; color: #FFFFFF; font-weight: 600; font-size: 11.5px;
      padding: 10px 12px; border: 1px solid #145E33; text-transform: uppercase;
      position: sticky; top: 63px; z-index: 10;
    }}
    td {{ padding: 12px 14px; border: 1px solid #E5E7EB; vertical-align: middle; font-size: 13px; line-height: 1.5; }}
    tr:hover td {{ background-color: #F8FAFC; }}

    .col-stt {{ width: 50px; text-align: center; font-weight: 600; color: #6B7280; }}
    .col-date {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; }}
    .col-user {{ width: 95px; text-align: center; font-weight: 500; }}
    .col-due {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; color: #4B5563; }}
    .col-proj {{ width: 130px; font-weight: 600; color: #1E3A8A; text-align: center; }}
    .col-status {{ width: 115px; text-align: center; }}
    .col-src {{ width: 125px; color: #4B5563; }}
    .col-task {{ width: 350px; font-weight: 500; color: #111827; }}
    .col-prio {{ width: 115px; text-align: center; }}
    .col-note {{ width: 390px; color: #374151; }}
    .col-output {{ min-width: 420px; font-size: 12px; }}

    .badge {{
      display: inline-block; padding: 2px 8px; border-radius: 4px;
      font-size: 11.5px; font-weight: 600; text-align: center; white-space: nowrap;
    }}
    .badge-done {{ background: #DEF7EC; color: #03543F; border: 1px solid #BCF0DA; }}
    .badge-gap {{ background: #FDE8E8; color: #9B1C1C; border: 1px solid #F8B4B4; }}
    .badge-tb {{ background: #E0E7FF; color: #3730A3; border: 1px solid #C7D2FE; }}
    .badge-hour {{
      display: inline-block; padding: 1px 6px; background: #E8F5E9; color: #1B7A43;
      border: 1px solid #C8E6C9; border-radius: 4px; font-weight: 700; font-size: 11px;
    }}

    .gsheet-bottom-bar {{
      position: fixed; bottom: 0; left: 0; right: 0; height: 42px;
      background: #F1F3F4; border-top: 1px solid #DADCE0; display: flex; align-items: center;
      padding: 0 16px; gap: 4px; z-index: 200;
    }}
    .gsheet-tab {{
      height: 100%; padding: 0 16px; display: inline-flex; align-items: center; gap: 6px;
      font-size: 12.5px; font-weight: 600; color: #5F6368; background: transparent;
      border: none; border-right: 1px solid #DADCE0; cursor: pointer;
    }}
    .gsheet-tab.active {{ background: #FFFFFF; color: #1B7A43; border-top: 3px solid #1B7A43; font-weight: 700; }}

    .toast {{
      position: fixed; bottom: 56px; right: 24px; background: #111827; color: #FFFFFF;
      padding: 12px 20px; border-radius: 8px; font-size: 13px; font-weight: 500;
      display: none; z-index: 10000;
    }}
  </style>
</head>
<body>
  <div class="sheets-header">
    <div class="sheets-left">
      <div class="sheets-icon">📊</div>
      <div class="sheets-title-box">
        <h1 id="header-title">Báo Cáo Công Việc Theo Tuần — Tuần 2 - 9/11 - 13/11</h1>
        <div id="header-subtitle">Văn phong ngắn gọn tự nhiên · Chỉ gắn link trực tiếp ở cột Output</div>
      </div>
    </div>
    <div class="sheets-actions">
      <button class="btn-action btn-purple" onclick="copyAppsScript()">
        ⚡ Copy Mã Apps Script (Tự Động Điền Cả 2 Tuần)
      </button>
      <button class="btn-action btn-green" onclick="copyWithHeader()">
        📋 Copy Kèm Tiêu Đề (Dán vào ô A1)
      </button>
      <button class="btn-action btn-outline" onclick="copyDataOnly()">
        📋 Copy Chỉ Dữ Liệu (Dán vào ô A2)
      </button>
      <a class="btn-action btn-blue" id="btn-download-csv" href="./{CSV_W2_PATH}" download>
        📥 Tải CSV Tuần Này
      </a>
      <a class="btn-action btn-amber" href="./{XLS_PATH}" download>
        📊 Tải Excel (.xls 2 Tuần)
      </a>
    </div>
  </div>

  <div class="week-switcher-banner">
    <div class="week-tabs-top">
      <button class="week-tab-btn" id="top-btn-w1" onclick="selectWeek('w1')">
        📅 Tuần 1 - 2/11 - 6/11 (Ver 1 Green Village)
      </button>
      <button class="week-tab-btn active" id="top-btn-w2" onclick="selectWeek('w2')">
        🛒 Tuần 2 - 9/11 - 13/11 (Ver 2 App G-Xanh)
      </button>
      <button class="week-tab-btn" id="top-btn-all" onclick="selectWeek('all')">
        📚 Gộp Cả 2 Tuần (30 việc)
      </button>
    </div>
  </div>

  <div class="sheets-toolbar">
    <div class="toolbar-metrics">
      <div class="metric-pill">👤 Người làm: <strong>Hoàng</strong></div>
      <div class="metric-pill">🎯 Dự án: <strong>Green Village</strong></div>
      <div class="metric-pill">📅 Lịch làm việc: <strong id="metric-date-range">09/11/2026 - 13/11/2026 (5 buổi · 40 giờ)</strong></div>
      <div class="metric-pill success">⏱️ Định mức: <strong>8.0h/ngày · Done</strong></div>
      <div class="metric-pill">📋 Số lượng: <strong id="metric-count">15 Đầu việc</strong></div>
    </div>
    <div class="search-box">
      <span style="color:#6B7280; margin-right: 6px;">🔍</span>
      <input type="text" id="searchInput" placeholder="Tìm kiếm nhanh..." onkeyup="filterTable()">
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
          <th class="col-output">Output/Tài liệu</th>
        </tr>
      </thead>
      <tbody id="table-body">
      </tbody>
    </table>
  </div>

  <div class="gsheet-bottom-bar">
    <span style="font-size: 12px; color: #5F6368; margin-right: 8px;">📑 Tabs:</span>
    <button class="gsheet-tab" id="bot-btn-w1" onclick="selectWeek('w1')">Tuần 1 - 2/11 - 6/11</button>
    <button class="gsheet-tab active" id="bot-btn-w2" onclick="selectWeek('w2')">Tuần 2 - 9/11 - 13/11</button>
    <button class="gsheet-tab" id="bot-btn-all" onclick="selectWeek('all')">Tổng hợp 2 Tuần</button>
  </div>

  <textarea id="hiddenTsvHeader" style="position:fixed; left:-9999px; top:-9999px;"></textarea>
  <textarea id="hiddenTsvData" style="position:fixed; left:-9999px; top:-9999px;"></textarea>
  <textarea id="hiddenAppsScript" style="position:fixed; left:-9999px; top:-9999px;">{html.escape(apps_script_code)}</textarea>

  <div id="toast" class="toast">
    <span id="toastMsg">✅ Đã sao chép!</span>
  </div>

  <script>
    const WEEKS_DATA = {weeks_json};
    let currentWeekKey = 'w2';

    function selectWeek(weekKey) {{
      currentWeekKey = weekKey;
      const info = WEEKS_DATA[weekKey];
      if (!info) return;

      document.getElementById('header-title').innerText = 'Báo Cáo Công Việc Theo Tuần — ' + info.tab_title;
      document.getElementById('header-subtitle').innerText = info.subtitle;
      document.getElementById('metric-date-range').innerText = info.date_range;
      document.getElementById('metric-count').innerText = info.count + ' Đầu việc';
      document.getElementById('btn-download-csv').href = './' + info.csv_file;
      document.getElementById('table-body').innerHTML = info.tbody;

      document.getElementById('hiddenTsvHeader').value = info.tsv_with_header;
      document.getElementById('hiddenTsvData').value = info.tsv_data_only;

      ['w1', 'w2', 'all'].forEach(k => {{
        document.getElementById('top-btn-' + k)?.classList.toggle('active', k === weekKey);
        document.getElementById('bot-btn-' + k)?.classList.toggle('active', k === weekKey);
      }});

      filterTable();
    }}

    function copyAppsScript() {{
      const area = document.getElementById('hiddenAppsScript');
      area.select();
      document.execCommand('copy');
      showToast('⚡ Đã copy mã Google Apps Script!');
    }}

    function copyWithHeader() {{
      const info = WEEKS_DATA[currentWeekKey];
      const area = document.getElementById('hiddenTsvHeader');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã copy kèm tiêu đề (' + info.count + ' dòng)!');
    }}

    function copyDataOnly() {{
      const info = WEEKS_DATA[currentWeekKey];
      const area = document.getElementById('hiddenTsvData');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã copy ' + info.count + ' dòng dữ liệu!');
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

    selectWeek('w2');
  </script>
</body>
</html>
'''

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_content)


def build_worksheet_xml(sheet_name, rows_11):
    ws_rows = []
    for r in rows_11:
        stt, date_val, user_val, due_val, proj_val, status_val, src_val, task_val, prio_val, note_val, output_val = [
            x.strip() for x in r
        ]
        prio_style = "PriorityGap" if prio_val == "Gấp" else "PriorityTB"
        ws_rows.append(f'''   <Row ss:Height="44">
    <Cell ss:StyleID="CenterCell"><Data ss:Type="Number">{stt}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(date_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(user_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(due_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(proj_val)}</Data></Cell>
    <Cell ss:StyleID="DoneStyle"><Data ss:Type="String">{html.escape(status_val)}</Data></Cell>
    <Cell ss:StyleID="CenterCell"><Data ss:Type="String">{html.escape(src_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(task_val)}</Data></Cell>
    <Cell ss:StyleID="{prio_style}"><Data ss:Type="String">{html.escape(prio_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(note_val)}</Data></Cell>
    <Cell ss:StyleID="CellStyle"><Data ss:Type="String">{html.escape(output_val)}</Data></Cell>
   </Row>''')
    rows_str = '\n'.join(ws_rows)
    return f''' <Worksheet ss:Name="{sheet_name}">
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
   <Column ss:Width="340"/>
   <Row ss:Height="32">
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
{rows_str}
  </Table>
 </Worksheet>'''


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
   <Font ss:FontName="Segoe UI" x:Family="Swiss" ss:Size="10" ss:Color="#FFFFFF" ss:Bold="1"/>
   <Interior ss:Color="#1B7A43" ss:Pattern="Solid"/>
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
'''

ws1 = build_worksheet_xml("Tuan 1 - 2_11 - 6_11", w1_11)
ws2 = build_worksheet_xml("Tuan 2 - 9_11 - 13_11", w2_11)

with open(XLS_PATH, 'w', encoding='utf-8') as f:
    f.write(xls_header + ws1 + '\n' + ws2 + '\n</Workbook>')

print("Updated all files with short natural text and bare links!")
