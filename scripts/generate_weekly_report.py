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

# ==============================================================================
# TUẦN 1: 02/11/2026 - 06/11/2026 (Thứ 2 -> Thứ 6) — GREEN VILLAGE VER 1
# ==============================================================================
WEEK_1_TASKS = [
    [
        '1', '2026/11/02', 'Hoàng', '02/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Dựng khung giao diện Bảng điều khiển Kinh tế & Lao động Cấp Xã (Actor 3 - UBND Xã Đồng Lam)',
        'Gấp',
        'Thiết kế bố cục 2 cột đồng bộ hệ sinh thái Green Village Ver 1: menu điều hướng cấp xã bên trái, đỉnh trang hiển thị thông tin lãnh đạo UBND xã và 4 thẻ KPI kinh tế nông thôn.',
        'Khung giao diện Dashboard Cán bộ Xã Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png | 🔗 Link web: https://cho-xanh.vercel.app/commune-dashboard'
    ],
    [
        '2', '2026/11/02', 'Hoàng', '02/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Tích hợp Cổng trình diễn 3 nền tảng (Portal) và bàn làm việc đối sánh Dual Studio Workbench',
        'Gấp',
        'Đấu nối liên thông đủ 3 phân hệ của Green Village Ver 1 (Mobile Bác Ba, Dashboard HTX Yên Bình, Dashboard Cán bộ Xã) trên cùng một cổng trình diễn phục vụ báo cáo.',
        'Cổng trình diễn 3 nền tảng Green Village Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png | 🔗 Link web: https://cho-xanh.vercel.app/portal'
    ],
    [
        '3', '2026/11/02', 'Hoàng', '02/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Đồng bộ phông chữ Lexend & Inter kèm bảng màu Emerald chuẩn nhận diện giữa Dashboard Xã và HTX',
        'Trong tuần',
        'Chuẩn hóa bộ biến màu Emerald (#064E3B, #10B981) kết hợp phông chữ Lexend đậm rõ cho các con số thống kê sản lượng và ngân sách, đảm bảo đồng nhất toàn bản Ver 1.',
        'Hệ thống Typography & Bảng màu đồng bộ | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/01_dashboard_htx_tong_quan.webp | 🔗 Link web: https://cho-xanh.vercel.app/htx-dashboard'
    ],
    [
        '4', '2026/11/03', 'Hoàng', '03/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Xây dựng phân hệ theo dõi hồ sơ OCOP (OCOP Pipeline) và Ma trận xếp hạng các HTX trong xã',
        'Gấp',
        'Hiển thị tiến độ thẩm định từng sản phẩm OCOP 3 sao - 4 sao của các thôn và bảng chấm điểm xếp hạng năng lực vận hành của các HTX nông nghiệp trên địa bàn.',
        'Bảng OCOP Pipeline & Ma trận xếp hạng HTX | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png | 🔗 Link web: https://cho-xanh.vercel.app/commune-dashboard'
    ],
    [
        '5', '2026/11/03', 'Hoàng', '03/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Lập trình tính năng Ký duyệt báo cáo điện tử và đóng dấu đỏ UBND Xã trực tiếp trên màn hình',
        'Gấp',
        'Làm cửa sổ xem trước công văn báo cáo tổng hợp kinh tế xã, tích hợp nút bấm ký số hiển thị con dấu đỏ chính thức của UBND xã và xuất biên bản nghiệm thu.',
        'Luồng ký duyệt điện tử đóng dấu đỏ cấp xã | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/15_ver1_dashboard_xa_ky_so_dong_dau_do.png'
    ],
    [
        '6', '2026/11/03', 'Hoàng', '03/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Tích hợp thư viện Chart.js vẽ biểu đồ tăng trưởng sản lượng và cơ cấu lao động nông thôn',
        'Trong tuần',
        'Vẽ biểu đồ cột và biểu đồ đường thể hiện sản lượng tiêu thụ nông sản qua các tháng của Green Village Ver 1, tự động co giãn mượt mà trên cả PC và iPad.',
        'Biểu đồ Chart.js mức số hoá & sản lượng mùa vụ | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'
    ],
    [
        '7', '2026/11/04', 'Hoàng', '04/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Thay thế toàn bộ ký tự Emoji rời rạc bằng hệ thống Icon SVG vector sắc nét trên toàn bộ Ver 1',
        'Gấp',
        'Thiết kế và gắn mới bộ icon SVG đồng nhất độ dày nét vẽ cho toàn bộ thanh menu, thẻ KPI, nút hành động và bảng xếp hạng trên Dashboard Xã và Cổng Portal.',
        '100% icon trên Dashboard Xã & Portal chuyển sang SVG | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png'
    ],
    [
        '8', '2026/11/04', 'Hoàng', '04/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Lập trình bộ lọc phạm vi Thôn/Bản và Tháng báo cáo tự động cập nhật lại biểu đồ thời gian thực',
        'Trong tuần',
        'Khi cán bộ xã chọn từng thôn hoặc đổi tháng báo cáo trên thanh công cụ, toàn bộ thẻ KPI và biểu đồ Chart.js tự động tính toán và vẽ lại số liệu ngay lập tức.',
        'Bộ lọc Thôn/Tháng phản hồi tức thì (Reactive Charts) | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'
    ],
    [
        '9', '2026/11/04', 'Hoàng', '04/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Làm cửa sổ Modal nhập số liệu thực tế tại cuộc họp cập nhật thẳng vào biểu đồ cấp xã',
        'Trong tuần',
        'Cho phép cán bộ nhập nhanh sản lượng thu hoạch mới hoặc số hộ tham gia ngay trong lúc họp giao ban, bấm lưu là biểu đồ trên màn hình chiếu nhảy số theo.',
        'Modal nhập số liệu trực tiếp trên Dashboard Xã | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'
    ],
    [
        '10', '2026/11/05', 'Hoàng', '05/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Rà soát và kiểm thử chéo toàn bộ luồng liên thông 4 Actor của phiên bản Green Village Ver 1',
        'Gấp',
        'Kiểm tra sự ăn khớp số liệu giữa Mobile Bác Ba đăng bán chuối sấy -> HTX Yên Bình duyệt đơn sỉ WinMart -> Cổng B2B -> Báo cáo tổng hợp tại UBND Xã.',
        'Luồng dữ liệu 4 Actor của Ver 1 chạy thông suốt | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/05_cong_b2b_dat_don_si.webp'
    ],
    [
        '11', '2026/11/05', 'Hoàng', '05/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Tối ưu giao diện Dual Studio Workbench (studio-10.html) đặt song song Mobile và Desktop',
        'Trong tuần',
        'Tinh chỉnh khung trình diễn song song giúp Ban Lãnh Đạo vừa bấm thao tác trên máy Bác Ba bên trái vừa xem kết quả nhảy tức thì trên màn hình HTX/Xã bên phải.',
        'Bàn làm việc đối sánh Dual Studio Ver 1 mượt mà | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png'
    ],
    [
        '12', '2026/11/05', 'Hoàng', '05/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Chụp và xử lý bộ 11 ảnh minh chứng giao diện thực tế (PNG & WebP) cho toàn bộ các màn hình Ver 1',
        'Trong tuần',
        'Chụp màn hình thực tế độ phân giải cao các phân hệ Dashboard HTX, duyệt sản phẩm, nghe audio nông dân, thẻ tài nguyên, cổng B2B, app Bác Ba và nén WebP dưới 100KB.',
        'Bộ ảnh minh chứng Ver 1 chuẩn WebP | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp'
    ],
    [
        '13', '2026/11/06', 'Hoàng', '06/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Cấu hình định tuyến máy chủ Vercel (vercel.json) và đóng gói phát hành bản Green Village Ver 1',
        'Gấp',
        'Cập nhật đường dẫn tĩnh cho mobile.html, portal.html, htx-dashboard.html, commune-dashboard.html và thư mục ảnh minh chứng; kiểm tra mở link qua Zalo mượt 100%.',
        'Bản Green Village Ver 1 vận hành trên Vercel | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/07_mobile_bac_ba_dark_mode.webp | 🔗 Link: https://cho-xanh.vercel.app/portal.html'
    ],
    [
        '14', '2026/11/06', 'Hoàng', '06/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1] Tổng hợp hồ sơ nghiệm thu kết quả Green Village Ver 1 và chuẩn hóa công cụ báo cáo tự động',
        'Gấp',
        'Đóng gói toàn bộ link sản phẩm, hình ảnh kết quả thực tế của giai đoạn Ver 1 vào hệ thống báo cáo chuẩn 11 cột để bàn giao hoàn tất giai đoạn 1.',
        'Hoàn tất bàn giao gói giao diện Green Village Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/02_htx_duyet_san_pham.webp'
    ],
    [
        '15', '2026/11/06', 'Hoàng', '06/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 1 -> Ver 2] Họp tổng kết Ver 1 cùng Vinh & BLĐ, nhận đề bài phát triển Ver 2 (App G-Xanh Sàn TMĐT)',
        'Trong tuần',
        'Đánh giá kết quả Ver 1 và chốt định hướng chuyển sang làm Ver 2 từ tuần kế tiếp: xây dựng App G-Xanh (Từ Làng Ra Phố) hoạt động như sàn thương mại điện tử khép kín.',
        'Chốt định hướng phát triển Ver 2 — App G-Xanh | 📸 Xem ảnh mockup: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ]
]

# ==============================================================================
# TUẦN 2: 09/11/2026 - 13/11/2026 (Thứ 2 -> Thứ 6) — VER 2 APP G-XANH (SÀN TMĐT)
# ==============================================================================
WEEK_2_TASKS = [
    [
        '1', '2026/11/09', 'Hoàng', '09/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Xây dựng Kế hoạch Phát triển Sản phẩm G-Xanh — Từ Làng Ra Phố (Mô hình Sàn TMĐT & Chuỗi bán lẻ)',
        'Gấp',
        'Lập tài liệu chiến lược Ver 2: chuyển từ mô hình đăng bán lẻ tẻ sang Sàn TMĐT & Chuỗi bán lẻ nông sản khép kín G-Xanh (Thu mua vùng trồng -> Tổng điều phối -> Cửa hàng & App Người mua).',
        'Kế hoạch Sản phẩm G-Xanh Ver 2 (GXANH_PRODUCT_PLAN.md) | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ],
    [
        '2', '2026/11/09', 'Hoàng', '09/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Thiết kế kiến trúc 3 tầng, tách biệt tuyệt đối 2 vòng tiền và lập ma trận 15 phân hệ (234 tính năng)',
        'Gấp',
        'Thiết kế luồng tách bạch Vòng tiền thẻ thành viên mua sắm TMĐT (nạp VietQR về Tổng, đối soát bù trừ T+1 trước 06:00 sáng) và Vòng vốn góp cổ đông; phân bổ 234 tính năng vào 3 giai đoạn P0/P1/P2.',
        'Sơ đồ 2 vòng tiền & Ma trận 15 phân hệ Ver 2 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'
    ],
    [
        '3', '2026/11/09', 'Hoàng', '09/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Đặc tả chi tiết User Flow & Kịch bản xử lý lỗi (Error Cases) cho Sàn TMĐT App G-Xanh',
        'Trong tuần',
        'Viết đặc tả kỹ thuật UX phục hồi sự cố cho Ver 2 (320 dòng): khóa giữ tồn kho tạm thời 10 phút chống hết hàng đột xuất (OOS), kiểm tra bán kính giao hỏa tốc 5km giữ chuỗi lạnh 2-4 độ C và chống trừ điểm trùng.',
        'Tài liệu Kiến trúc Chức năng & UX/UI G-Xanh Ver 2 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '4', '2026/11/10', 'Hoàng', '10/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Dựng khung Mobile Viewport 430px, thanh chuyển nhanh 5 màn hình và Bottom Tab Bar chuẩn Shopee UI',
        'Gấp',
        'Khởi tạo kiến trúc giao diện App G-Xanh Ver 2 (consumer-prototype.html): bộ màu xanh lá - cam Shopee (#15803d / #ee4d2d), thanh điều hướng đáy 5 tab (Chợ, GF-Track, Giỏ hàng, Thẻ Zalo, Tôi) có bong bóng đếm giỏ hàng.',
        'Khung App Sàn TMĐT G-Xanh Ver 2 chuẩn Shopee UI | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | 🔗 Link web: https://cho-xanh.vercel.app/gxanh'
    ],
    [
        '5', '2026/11/10', 'Hoàng', '10/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Lập trình Header tìm kiếm nông sản thời gian thực, thanh cam kết chất lượng và dải lọc danh mục',
        'Gấp',
        'Làm ô tìm kiếm lọc tức thì theo tên nông sản hoặc tên thôn làng (handleSearch); dải cam kết 3 cột (100% Nguồn gốc, Đổi trả 24h, Chuỗi lạnh 2-4 độ C) và thanh tag lọc (Rau củ hữu cơ, Thịt cá bản địa, Đặc sản đóng gói).',
        'Thanh tìm kiếm & Bộ lọc danh mục nông sản G-Xanh | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '6', '2026/11/10', 'Hoàng', '10/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Làm Banner Phiên Chợ Sớm (Flash Sale) đếm ngược từng giây và lưới sản phẩm 2 cột chuẩn sàn TMĐT',
        'Trong tuần',
        'Lập trình đồng hồ đếm ngược phiên chợ chạy thực tế; thiết kế thẻ sản phẩm 2 cột (shopee-card) có nhãn GF-Track/OCOP góc trái, tem giảm giá (-15%, -21%) góc phải, nguồn gốc thôn, giá gạch ngang, đã bán và nút (+) thêm nhanh vào giỏ.',
        'Màn 1: Sàn TMĐT Chợ G-Xanh Flash Sale & Lưới 2 cột | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'
    ],
    [
        '7', '2026/11/11', 'Hoàng', '11/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Phát triển màn hình Chi tiết món hàng TMĐT với bộ chọn phân loại quy cách đóng gói tự động nhảy giá',
        'Gấp',
        'Hiển thị ảnh lớn sản phẩm, dải giá khuyến mãi nổi bật, điểm đánh giá sao, số lượng đã bán; làm bộ nút chọn quy cách (Hũ 500ml / Hũ 1 Lít, Khay 500g / Khay 1kg) bấm vào tự động cập nhật giá bán tương ứng.',
        'Màn 2: Chi tiết sản phẩm TMĐT chọn quy cách động | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'
    ],
    [
        '8', '2026/11/11', 'Hoàng', '11/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Làm bảng thông số nguồn gốc hộ sản xuất và thanh công cụ mua hàng cố định đáy (Sticky Bottom CTA)',
        'Trong tuần',
        'Hiển thị rõ nguồn gốc thôn/nhà vườn, tiêu chuẩn tem GF-Track, hướng dẫn bảo quản; gắn thanh cố định đáy gồm cụm tăng giảm số lượng (stepper), nút Thêm vào giỏ (38px) và nút Mua Ngay cam Shopee (48px).',
        'Thanh Sticky Bottom CTA Thêm vào giỏ & Mua Ngay | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'
    ],
    [
        '9', '2026/11/11', 'Hoàng', '11/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Lập trình màn hình Giỏ hàng TMĐT tự động gom nhóm theo từng Gian hàng/Thôn làng (CRUD đầy đủ)',
        'Gấp',
        'Tự động gom các món trong giỏ theo từng gian hàng/thôn (Đặc sản nhà chị Hoa, Mật ong nhà Khánh - Thôn Gò Mít); hỗ trợ tăng giảm số lượng từng món, xóa từng món, xóa toàn bộ giỏ và tự tính lại tổng tiền.',
        'Màn 3: Giỏ hàng thông minh gom theo gian hàng/thôn | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/23_gxanh_gio_hang_gom_shop.png'
    ],
    [
        '10', '2026/11/12', 'Hoàng', '12/11/2026', '2.5', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Xây dựng cửa sổ chọn mã giảm giá G-Xanh Voucher tự động khấu trừ vào đơn hàng',
        'Trong tuần',
        'Làm Bottom Sheet chọn mã giảm giá (VOUCHER25K giảm 25.000đ cho đơn từ 200k, GXANHFREESHIP miễn phí vận chuyển hỏa tốc 50.000đ), bấm Áp dụng tự động trừ thẳng vào tổng thanh toán giỏ hàng.',
        'Cửa sổ chọn và áp dụng mã giảm giá G-Xanh Voucher | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/24_gxanh_modal_voucher.png'
    ],
    [
        '11', '2026/11/12', 'Hoàng', '12/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Phát triển màn hình Thẻ thành viên Zalo Mini App và lưới 3 thẻ số dư điểm ngang song song',
        'Gấp',
        'Thiết kế thẻ thành viên điện tử (Digital Pass) hiển thị tổng điểm khả dụng (565.000 điểm) và lưới 3 cột ngang bằng nhau (Điểm nạp: 505.000, Điểm thưởng: 0, Hoa hồng: 60.000) kèm nút Nạp điểm & Lịch sử.',
        'Màn 4: Ví & Thẻ thành viên Zalo Mini App 3 nguồn điểm | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'
    ],
    [
        '12', '2026/11/12', 'Hoàng', '12/11/2026', '2.5', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Lập trình khối Mã QR Thanh Toán Dùng 1 Lần tự động làm mới sau mỗi 60 giây chống gian lận',
        'Gấp',
        'Vẽ ma trận QR SVG sắc nét kèm đồng hồ đếm ngược 60s tự động tái tạo mã mới khi hết giờ hoặc khi khách bấm đổi mã trực tiếp, ngăn chặn hoàn toàn việc dùng ảnh chụp màn hình tĩnh tại quầy.',
        'Bộ sinh mã QR thanh toán động 60s dùng 1 lần | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'
    ],
    [
        '13', '2026/11/13', 'Hoàng', '13/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Lập trình luồng Xác nhận đặt hàng (Checkout trừ điểm thẻ), Nạp điểm VietQR và Sổ lịch sử điểm',
        'Gấp',
        'Kiểm tra số dư điểm khi đặt đơn, tự động trừ điểm thẻ, sinh mã đơn DH-xxxx; làm modal nạp điểm 3 gói (200k/500k/1tr) tự sinh nội dung chuyển khoản NAP CX-302401 và tự động ghi vào lịch sử biến động điểm.',
        '3 Modal Đặt đơn, Nạp VietQR & Lịch sử điểm | 📸 Xem ảnh đặt đơn: https://cho-xanh.vercel.app/output_images/25_gxanh_modal_xac_nhan_dat_don.png | 📸 Ảnh nạp điểm: https://cho-xanh.vercel.app/output_images/27_gxanh_modal_nap_diem_vietqr.png | 📸 Ảnh lịch sử: https://cho-xanh.vercel.app/output_images/28_gxanh_modal_lich_su_diem.png'
    ],
    [
        '14', '2026/11/13', 'Hoàng', '13/11/2026', '3', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Xây dựng màn hình Tra cứu Tem GF-Track (3 tầng bằng chứng, 6 chặng) và Form đánh giá chất lượng',
        'Gấp',
        'Hiển thị huy hiệu Chính hãng GF-Track, 3 tầng bằng chứng (Nhật ký vùng trồng GPS, Chuỗi lạnh 3.2 độ C, Hồ sơ VietGAP), hành trình 6 chặng từ Xã Quy Đức đến kệ hàng và modal chấm sao + gắn tag nhận xét nhanh.',
        'Màn 5: Tra cứu GF-Track & Đánh giá 5 sao | 📸 Xem ảnh GF-Track: https://cho-xanh.vercel.app/output_images/29_gxanh_tra_cuu_tem_gf_track.png | 📸 Ảnh đánh giá: https://cho-xanh.vercel.app/output_images/30_gxanh_modal_danh_gia_5sao.png'
    ],
    [
        '15', '2026/11/13', 'Hoàng', '13/11/2026', '2', 'Green Village', 'Done', 'Vinh và BLĐ',
        '[Ver 2 - G-Xanh] Kiểm thử toàn diện 5 màn hình & 6 modal (2.374 dòng code) và đẩy toàn bộ bản Ver 2 lên nhánh hoang-dev',
        'Gấp',
        'Test kỹ toàn bộ thao tác CRUD giỏ hàng, áp voucher, nạp điểm, đặt đơn, chống tràn chữ trên màn hình 375px-430px và đẩy commit c875d503 (2.845 dòng) lên kho Git nhánh origin/hoang-dev.',
        'Đồng bộ hoàn tất App Sàn TMĐT G-Xanh Ver 2 lên nhánh hoang-dev | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | 🔗 Link web: https://cho-xanh.vercel.app/gxanh'
    ]
]


def to_11_cols(rows_12):
    res = []
    for idx, r in enumerate(rows_12, 1):
        clean_r = [x.replace('"', "'").strip() for x in r]
        clean_r[0] = str(idx)
        r_11 = [
            clean_r[0], clean_r[1], clean_r[2], clean_r[3],
            clean_r[5], clean_r[6], clean_r[7], clean_r[8],
            clean_r[9], clean_r[10], clean_r[11]
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
    parts = val.split(' | ')
    title = parts[0].strip()
    links_html = []
    for p in parts[1:]:
        p = p.strip()
        url_match = re.search(r'(https?://[^\s]+)', p)
        if url_match:
            url = url_match.group(1)
            label = p.replace(url, '').strip() or '🔗 Xem chi tiết'
            is_img = ('output_images/' in url)
            bg = '#DEF7EC' if is_img else '#E0F2FE'
            color = '#03543F' if is_img else '#0369A1'
            links_html.append(
                f'<a class="output-img-link" href="{html.escape(url)}" target="_blank" style="background:{bg}; color:{color};">{html.escape(label)}</a>'
            )
        else:
            links_html.append(f'<span>{html.escape(p)}</span>')
    res = f'<div class="output-box"><strong>{html.escape(title)}</strong>'
    if links_html:
        res += '<br>' + ' '.join(links_html)
    res += '</div>'
    return res


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
        lines.append('\t'.join(r))
    return '\n'.join(lines)


with open(APPS_SCRIPT_PATH, 'r', encoding='utf-8') as f:
    apps_script_code = f.read()

WEEKS_META = {
    'w1': {
        'tab_title': 'Tuần 1 - 2/11 - 6/11',
        'subtitle': 'Thứ 2 (02/11) → Thứ 6 (06/11) · Hoàn thiện & Nghiệm thu Green Village Ver 1 (Dashboard Xã Actor 3, Portal 3 nền tảng, Dual Studio)',
        'date_range': '02/11/2026 - 06/11/2026 (5 buổi · 40 giờ)',
        'count': len(w1_11),
        'csv_file': CSV_W1_PATH,
        'tbody': build_tbody_html(WEEK_1_TASKS),
        'tsv_with_header': make_tsv(w1_11, True),
        'tsv_data_only': make_tsv(w1_11, False),
    },
    'w2': {
        'tab_title': 'Tuần 2 - 9/11 - 13/11',
        'subtitle': 'Thứ 2 (09/11) → Thứ 6 (13/11) · Phát triển Ver 2 App G-Xanh — Sàn Thương Mại Điện Tử Shopee UI & Master Plan 15 Phân hệ (nhánh hoang-dev)',
        'date_range': '09/11/2026 - 13/11/2026 (5 buổi · 40 giờ)',
        'count': len(w2_11),
        'csv_file': CSV_W2_PATH,
        'tbody': build_tbody_html(WEEK_2_TASKS),
        'tsv_with_header': make_tsv(w2_11, True),
        'tsv_data_only': make_tsv(w2_11, False),
    },
    'all': {
        'tab_title': 'Gộp cả 2 Tuần (Tuần 1 Ver 1 + Tuần 2 Ver 2 G-Xanh)',
        'subtitle': 'Tổng hợp 30 đầu việc của 2 tuần đầu tháng 11 (02/11 - 13/11/2026) · Chuẩn 11 Cột Google Sheet',
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
  <title>[NEXS - GreenFi] Báo Cáo Tuần Tháng 11 (Ver 1 GreenVillage & Ver 2 App G-Xanh) - Hoàng</title>
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
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      border: 1px solid transparent;
      text-decoration: none;
      transition: all 0.15s ease;
      white-space: nowrap !important;
    }}
    .btn-purple {{
      background: #7C3AED;
      color: #FFFFFF;
      box-shadow: 0 2px 4px rgba(124,58,237,0.25);
    }}
    .btn-purple:hover {{ background: #6D28D9; }}
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

    .week-switcher-banner {{
      background: #ECFDF5;
      border-bottom: 1px solid #A7F3D0;
      padding: 10px 20px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}
    .week-tabs-top {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .week-tab-btn {{
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      border: 1px solid #6EE7B7;
      background: #FFFFFF;
      color: #065F46;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .week-tab-btn:hover {{ background: #D1FAE5; }}
    .week-tab-btn.active {{
      background: #1B7A43;
      color: #FFFFFF;
      border-color: #1B7A43;
      box-shadow: 0 2px 5px rgba(27, 122, 67, 0.25);
    }}
    .guide-hint {{
      font-size: 12px;
      color: #065F46;
      background: #D1FAE5;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 500;
    }}

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
      background: #1B7A43;
      color: #FFFFFF;
      font-weight: 600;
      font-size: 11.5px;
      padding: 10px 12px;
      border: 1px solid #145E33;
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
    tr:hover td {{ background-color: #F8FAFC; }}

    .col-stt {{ width: 50px; text-align: center; font-weight: 600; color: #6B7280; }}
    .col-date {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; }}
    .col-user {{ width: 95px; text-align: center; font-weight: 500; }}
    .col-due {{ width: 110px; text-align: center; font-family: monospace; font-size: 12.5px; color: #4B5563; }}
    .col-proj {{ width: 130px; font-weight: 600; color: #1E3A8A; text-align: center; }}
    .col-status {{ width: 115px; text-align: center; }}
    .col-src {{ width: 125px; color: #4B5563; }}
    .col-task {{ width: 380px; font-weight: 500; color: #111827; }}
    .col-prio {{ width: 115px; text-align: center; }}
    .col-note {{ width: 400px; color: #374151; }}
    .col-output {{ min-width: 420px; }}

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

    .gsheet-bottom-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 42px;
      background: #F1F3F4;
      border-top: 1px solid #DADCE0;
      display: flex;
      align-items: center;
      padding: 0 16px;
      gap: 4px;
      z-index: 200;
    }}
    .gsheet-tab {{
      height: 100%;
      padding: 0 16px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12.5px;
      font-weight: 600;
      color: #5F6368;
      background: transparent;
      border: none;
      border-right: 1px solid #DADCE0;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .gsheet-tab:hover {{ background: #E8EAED; color: #202124; }}
    .gsheet-tab.active {{
      background: #FFFFFF;
      color: #1B7A43;
      border-top: 3px solid #1B7A43;
      font-weight: 700;
    }}

    .toast {{
      position: fixed;
      bottom: 56px;
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
        <h1 id="header-title">[NEXS - GreenFi] Báo Cáo Theo Tuần — Tuần 1 - 2/11 - 6/11 (Ver 1 Green Village)</h1>
        <div id="header-subtitle">Thứ 2 (02/11) → Thứ 6 (06/11) · Hoàn thiện & Nghiệm thu Green Village Ver 1</div>
      </div>
    </div>
    <div class="sheets-actions">
      <button class="btn-action btn-purple" onclick="copyAppsScript()">
        ⚡ Copy Mã Apps Script (Tự Động Điền Cả 2 Tuần + Link Ảnh)
      </button>
      <button class="btn-action btn-green" onclick="copyWithHeader()">
        📋 Copy Kèm Tiêu Đề (Dán vào ô A1)
      </button>
      <button class="btn-action btn-outline" onclick="copyDataOnly()">
        📋 Copy Chỉ Dữ Liệu (Dán vào ô A2)
      </button>
      <a class="btn-action btn-blue" id="btn-download-csv" href="./{CSV_W1_PATH}" download>
        📥 Tải CSV Tuần Này
      </a>
      <a class="btn-action btn-amber" href="./{XLS_PATH}" download>
        📊 Tải Excel (.xls 2 Tuần)
      </a>
    </div>
  </div>

  <div class="week-switcher-banner">
    <div class="week-tabs-top">
      <button class="week-tab-btn active" id="top-btn-w1" onclick="selectWeek('w1')">
        📅 Tuần 1 - 2/11 - 6/11 · Green Village Ver 1 (15 việc)
      </button>
      <button class="week-tab-btn" id="top-btn-w2" onclick="selectWeek('w2')">
        🛒 Tuần 2 - 9/11 - 13/11 · App G-Xanh Ver 2 Sàn TMĐT (15 việc)
      </button>
      <button class="week-tab-btn" id="top-btn-all" onclick="selectWeek('all')">
        📚 Gộp Cả 2 Tuần (30 việc)
      </button>
    </div>
    <div class="guide-hint">
      📸 <strong>Đã gắn đầy đủ ảnh chụp từng tính năng:</strong> Bấm vào ảnh thu nhỏ hoặc nút <code>📸 Xem ảnh thực tế</code> ở cột cuối để xem ảnh full HD!
    </div>
  </div>

  <div class="sheets-toolbar">
    <div class="toolbar-metrics">
      <div class="metric-pill">👤 Người làm: <strong>Hoàng</strong></div>
      <div class="metric-pill">🎯 Dự án: <strong>Green Village (Ver 1 & Ver 2 G-Xanh)</strong></div>
      <div class="metric-pill">📅 Lịch làm việc: <strong id="metric-date-range">02/11/2026 - 06/11/2026 (5 buổi · 40 giờ)</strong></div>
      <div class="metric-pill success">⏱️ Định mức: <strong>8.0h/ngày · 100% Done</strong></div>
      <div class="metric-pill">📋 Số lượng: <strong id="metric-count">15 Đầu việc</strong></div>
      <div class="metric-pill">📌 Nguồn: <strong>Vinh và BLĐ</strong></div>
    </div>
    <div class="search-box">
      <span style="color:#6B7280; margin-right: 6px;">🔍</span>
      <input type="text" id="searchInput" placeholder="Tìm kiếm nhanh đầu việc, ngày, Ver 1, Ver 2..." onkeyup="filterTable()">
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
          <th class="col-output">Output / Tài liệu & Ảnh chụp tính năng</th>
        </tr>
      </thead>
      <tbody id="table-body">
      </tbody>
    </table>
  </div>

  <div class="gsheet-bottom-bar">
    <span style="font-size: 12px; color: #5F6368; margin-right: 8px;">📑 Các trang tính (Tabs trên Google Sheet):</span>
    <button class="gsheet-tab active" id="bot-btn-w1" onclick="selectWeek('w1')">Tuần 1 - 2/11 - 6/11 (Ver 1 Green Village)</button>
    <button class="gsheet-tab" id="bot-btn-w2" onclick="selectWeek('w2')">Tuần 2 - 9/11 - 13/11 (Ver 2 App G-Xanh)</button>
    <button class="gsheet-tab" id="bot-btn-all" onclick="selectWeek('all')">Tổng hợp 2 Tuần</button>
  </div>

  <textarea id="hiddenTsvHeader" style="position:fixed; left:-9999px; top:-9999px;"></textarea>
  <textarea id="hiddenTsvData" style="position:fixed; left:-9999px; top:-9999px;"></textarea>
  <textarea id="hiddenAppsScript" style="position:fixed; left:-9999px; top:-9999px;">{html.escape(apps_script_code)}</textarea>

  <div id="toast" class="toast">
    <span id="toastMsg">✅ Đã sao chép vào bộ nhớ tạm!</span>
  </div>

  <script>
    const WEEKS_DATA = {weeks_json};
    let currentWeekKey = 'w2';

    function selectWeek(weekKey) {{
      currentWeekKey = weekKey;
      const info = WEEKS_DATA[weekKey];
      if (!info) return;

      document.getElementById('header-title').innerText = '[NEXS - GreenFi] Báo Cáo Công Việc Theo Tuần — ' + info.tab_title;
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
      showToast('⚡ Đã copy toàn bộ mã Google Apps Script (kèm link ảnh)! Hãy dán vào Apps Script rồi bấm ▶️ Chạy (Run)!');
    }}

    function copyWithHeader() {{
      const info = WEEKS_DATA[currentWeekKey];
      const area = document.getElementById('hiddenTsvHeader');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã copy CẢ TIÊU ĐỀ + ' + info.count + ' dòng của [' + info.tab_title + ']! Hãy bấm vào ô A1 trên Google Sheet rồi dán (Ctrl+V).');
    }}

    function copyDataOnly() {{
      const info = WEEKS_DATA[currentWeekKey];
      const area = document.getElementById('hiddenTsvData');
      area.select();
      document.execCommand('copy');
      showToast('✅ Đã copy ' + info.count + ' dòng dữ liệu của [' + info.tab_title + ']! Hãy bấm vào ô A2 rồi dán (Ctrl+V).');
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      document.getElementById('toastMsg').innerText = msg;
      toast.style.display = 'block';
      setTimeout(() => {{ toast.style.display = 'none'; }}, 5000);
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

print("Updated all files with screenshot links and thumbnails successfully!")
