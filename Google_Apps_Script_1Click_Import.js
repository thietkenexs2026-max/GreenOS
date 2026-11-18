// Bấm ▶️ Chạy (Run) ở bất kỳ hàm nào (capNhatBaoCaoTheoTuan / onOpen / capNhatBaoCaoThang10) đều tự động điền cả 2 Tuần!
function capNhatBaoCaoTheoTuan() { thucThiCapNhatCa2Tuan(); }
function onOpen() {
  try {
    SpreadsheetApp.getUi().createMenu('🌾 Đồng Bộ GreenOS')
      .addItem('⚡ 1-Click Cập Nhật Cả Tuần 1 (Ver 1) & Tuần 2 (Ver 2 G-Xanh)', 'capNhatBaoCaoTheoTuan')
      .addItem('📅 Chỉ Cập Nhật Tuần 1 (Ver 1 Green Village)', 'chiCapNhatTuan1_Ver1')
      .addItem('🛒 Chỉ Cập Nhật Tuần 2 (Ver 2 App G-Xanh)', 'chiCapNhatTuan2_Ver2_GXanh')
      .addToUi();
  } catch (e) {}
  thucThiCapNhatCa2Tuan();
}
function capNhatBaoCaoThang10() { thucThiCapNhatCa2Tuan(); }

const HEADER_11_COT = ['STT', 'Ngày (yyyy/mm/dd)', 'Người làm', 'Dự kiến hoàn thành', 'Nexs/ Greenfi', 'Tiến độ', 'Nguồn', 'Đầu việc', 'Thứ tự ưu tiên', 'Ghi chú', 'Output/Tài liệu'];

const DU_LIEU_TUAN_1_VER_1 = [
  ['1', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Dựng khung giao diện Bảng điều khiển Kinh tế & Lao động Cấp Xã (Actor 3 - UBND Xã Đồng Lam)', 'Gấp', 'Thiết kế bố cục 2 cột đồng bộ hệ sinh thái Green Village Ver 1: menu điều hướng cấp xã bên trái, đỉnh trang hiển thị thông tin lãnh đạo UBND xã và 4 thẻ KPI kinh tế nông thôn.', 'Khung giao diện Dashboard Cán bộ Xã Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png | 🔗 Link web: https://cho-xanh.vercel.app/commune-dashboard'],
  ['2', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Tích hợp Cổng trình diễn 3 nền tảng (Portal) và bàn làm việc đối sánh Dual Studio Workbench', 'Gấp', 'Đấu nối liên thông đủ 3 phân hệ của Green Village Ver 1 (Mobile Bác Ba, Dashboard HTX Yên Bình, Dashboard Cán bộ Xã) trên cùng một cổng trình diễn phục vụ báo cáo.', 'Cổng trình diễn 3 nền tảng Green Village Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png | 🔗 Link web: https://cho-xanh.vercel.app/portal'],
  ['3', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Đồng bộ phông chữ Lexend & Inter kèm bảng màu Emerald chuẩn nhận diện giữa Dashboard Xã và HTX', 'Trong tuần', 'Chuẩn hóa bộ biến màu Emerald (#064E3B, #10B981) kết hợp phông chữ Lexend đậm rõ cho các con số thống kê sản lượng và ngân sách, đảm bảo đồng nhất toàn bản Ver 1.', 'Hệ thống Typography & Bảng màu đồng bộ | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/01_dashboard_htx_tong_quan.webp | 🔗 Link web: https://cho-xanh.vercel.app/htx-dashboard'],
  ['4', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Xây dựng phân hệ theo dõi hồ sơ OCOP (OCOP Pipeline) và Ma trận xếp hạng các HTX trong xã', 'Gấp', 'Hiển thị tiến độ thẩm định từng sản phẩm OCOP 3 sao - 4 sao của các thôn và bảng chấm điểm xếp hạng năng lực vận hành của các HTX nông nghiệp trên địa bàn.', 'Bảng OCOP Pipeline & Ma trận xếp hạng HTX | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png | 🔗 Link web: https://cho-xanh.vercel.app/commune-dashboard'],
  ['5', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Lập trình tính năng Ký duyệt báo cáo điện tử và đóng dấu đỏ UBND Xã trực tiếp trên màn hình', 'Gấp', 'Làm cửa sổ xem trước công văn báo cáo tổng hợp kinh tế xã, tích hợp nút bấm ký số hiển thị con dấu đỏ chính thức của UBND xã và xuất biên bản nghiệm thu.', 'Luồng ký duyệt điện tử đóng dấu đỏ cấp xã | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/15_ver1_dashboard_xa_ky_so_dong_dau_do.png'],
  ['6', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Tích hợp thư viện Chart.js vẽ biểu đồ tăng trưởng sản lượng và cơ cấu lao động nông thôn', 'Trong tuần', 'Vẽ biểu đồ cột và biểu đồ đường thể hiện sản lượng tiêu thụ nông sản qua các tháng của Green Village Ver 1, tự động co giãn mượt mà trên cả PC và iPad.', 'Biểu đồ Chart.js mức số hoá & sản lượng mùa vụ | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'],
  ['7', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Thay thế toàn bộ ký tự Emoji rời rạc bằng hệ thống Icon SVG vector sắc nét trên toàn bộ Ver 1', 'Gấp', 'Thiết kế và gắn mới bộ icon SVG đồng nhất độ dày nét vẽ cho toàn bộ thanh menu, thẻ KPI, nút hành động và bảng xếp hạng trên Dashboard Xã và Cổng Portal.', '100% icon trên Dashboard Xã & Portal chuyển sang SVG | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png'],
  ['8', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Lập trình bộ lọc phạm vi Thôn/Bản và Tháng báo cáo tự động cập nhật lại biểu đồ thời gian thực', 'Trong tuần', 'Khi cán bộ xã chọn từng thôn hoặc đổi tháng báo cáo trên thanh công cụ, toàn bộ thẻ KPI và biểu đồ Chart.js tự động tính toán và vẽ lại số liệu ngay lập tức.', 'Bộ lọc Thôn/Tháng phản hồi tức thì (Reactive Charts) | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'],
  ['9', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Làm cửa sổ Modal nhập số liệu thực tế tại cuộc họp cập nhật thẳng vào biểu đồ cấp xã', 'Trong tuần', 'Cho phép cán bộ nhập nhanh sản lượng thu hoạch mới hoặc số hộ tham gia ngay trong lúc họp giao ban, bấm lưu là biểu đồ trên màn hình chiếu nhảy số theo.', 'Modal nhập số liệu trực tiếp trên Dashboard Xã | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'],
  ['10', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Rà soát và kiểm thử chéo toàn bộ luồng liên thông 4 Actor của phiên bản Green Village Ver 1', 'Gấp', 'Kiểm tra sự ăn khớp số liệu giữa Mobile Bác Ba đăng bán chuối sấy -> HTX Yên Bình duyệt đơn sỉ WinMart -> Cổng B2B -> Báo cáo tổng hợp tại UBND Xã.', 'Luồng dữ liệu 4 Actor của Ver 1 chạy thông suốt | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/05_cong_b2b_dat_don_si.webp'],
  ['11', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Tối ưu giao diện Dual Studio Workbench (studio-10.html) đặt song song Mobile và Desktop', 'Trong tuần', 'Tinh chỉnh khung trình diễn song song giúp Ban Lãnh Đạo vừa bấm thao tác trên máy Bác Ba bên trái vừa xem kết quả nhảy tức thì trên màn hình HTX/Xã bên phải.', 'Bàn làm việc đối sánh Dual Studio Ver 1 mượt mà | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png'],
  ['12', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Chụp và xử lý bộ 11 ảnh minh chứng giao diện thực tế (PNG & WebP) cho toàn bộ các màn hình Ver 1', 'Trong tuần', 'Chụp màn hình thực tế độ phân giải cao các phân hệ Dashboard HTX, duyệt sản phẩm, nghe audio nông dân, thẻ tài nguyên, cổng B2B, app Bác Ba và nén WebP dưới 100KB.', 'Bộ ảnh minh chứng Ver 1 chuẩn WebP | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp'],
  ['13', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Cấu hình định tuyến máy chủ Vercel (vercel.json) và đóng gói phát hành bản Green Village Ver 1', 'Gấp', 'Cập nhật đường dẫn tĩnh cho mobile.html, portal.html, htx-dashboard.html, commune-dashboard.html và thư mục ảnh minh chứng; kiểm tra mở link qua Zalo mượt 100%.', 'Bản Green Village Ver 1 vận hành trên Vercel | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/07_mobile_bac_ba_dark_mode.webp | 🔗 Link web: https://cho-xanh.vercel.app/portal'],
  ['14', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1] Tổng hợp hồ sơ nghiệm thu kết quả Green Village Ver 1 và chuẩn hóa công cụ báo cáo tự động', 'Gấp', 'Đóng gói toàn bộ link sản phẩm, hình ảnh kết quả thực tế của giai đoạn Ver 1 vào hệ thống báo cáo chuẩn 11 cột để bàn giao hoàn tất giai đoạn 1.', 'Hoàn tất bàn giao gói giao diện Green Village Ver 1 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/02_htx_duyet_san_pham.webp'],
  ['15', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 1 -> Ver 2] Họp tổng kết Ver 1 cùng Vinh & BLĐ, nhận đề bài phát triển Ver 2 (App G-Xanh Sàn TMĐT)', 'Trong tuần', 'Đánh giá kết quả Ver 1 và chốt định hướng chuyển sang làm Ver 2 từ tuần kế tiếp: xây dựng App G-Xanh (Từ Làng Ra Phố) hoạt động như sàn thương mại điện tử khép kín.', 'Chốt định hướng phát triển Ver 2 — App G-Xanh | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png']
];

const DU_LIEU_TUAN_2_VER_2_GXANH = [
  ['1', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Xây dựng Kế hoạch Phát triển Sản phẩm G-Xanh — Từ Làng Ra Phố (Mô hình Sàn TMĐT & Chuỗi bán lẻ)', 'Gấp', 'Lập tài liệu chiến lược Ver 2: chuyển từ mô hình đăng bán lẻ tẻ sang Sàn TMĐT & Chuỗi bán lẻ nông sản khép kín G-Xanh (Thu mua vùng trồng -> Tổng điều phối -> Cửa hàng & App Người mua).', 'Kế hoạch Sản phẩm G-Xanh Ver 2 (GXANH_PRODUCT_PLAN.md) | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'],
  ['2', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Thiết kế kiến trúc 3 tầng, tách biệt tuyệt đối 2 vòng tiền và lập ma trận 15 phân hệ (234 tính năng)', 'Gấp', 'Thiết kế luồng tách bạch Vòng tiền thẻ thành viên mua sắm TMĐT (nạp VietQR về Tổng, đối soát bù trừ T+1 trước 06:00 sáng) và Vòng vốn góp cổ đông; phân bổ 234 tính năng vào 3 giai đoạn P0/P1/P2.', 'Sơ đồ 2 vòng tiền & Ma trận 15 phân hệ Ver 2 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'],
  ['3', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Đặc tả chi tiết User Flow & Kịch bản xử lý lỗi (Error Cases) cho Sàn TMĐT App G-Xanh', 'Trong tuần', 'Viết đặc tả kỹ thuật UX phục hồi sự cố cho Ver 2 (320 dòng): khóa giữ tồn kho tạm thời 10 phút chống hết hàng đột xuất (OOS), kiểm tra bán kính giao hỏa tốc 5km giữ chuỗi lạnh 2-4 độ C và chống trừ điểm trùng.', 'Tài liệu Kiến trúc Chức năng & UX/UI G-Xanh Ver 2 | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['4', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Dựng khung Mobile Viewport 430px, thanh chuyển nhanh 5 màn hình và Bottom Tab Bar chuẩn Shopee UI', 'Gấp', 'Khởi tạo kiến trúc giao diện App G-Xanh Ver 2 (consumer-prototype.html): bộ màu xanh lá - cam Shopee (#15803d / #ee4d2d), thanh điều hướng đáy 5 tab (Chợ, GF-Track, Giỏ hàng, Thẻ Zalo, Tôi) có bong bóng đếm giỏ hàng.', 'Khung App Sàn TMĐT G-Xanh Ver 2 chuẩn Shopee UI | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | 🔗 Link web: https://cho-xanh.vercel.app/gxanh'],
  ['5', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Lập trình Header tìm kiếm nông sản thời gian thực, thanh cam kết chất lượng và dải lọc danh mục', 'Gấp', 'Làm ô tìm kiếm lọc tức thì theo tên nông sản hoặc tên thôn làng (handleSearch); dải cam kết 3 cột (100% Nguồn gốc, Đổi trả 24h, Chuỗi lạnh 2-4 độ C) và thanh tag lọc (Rau củ hữu cơ, Thịt cá bản địa, Đặc sản đóng gói).', 'Thanh tìm kiếm & Bộ lọc danh mục nông sản G-Xanh | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['6', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Làm Banner Phiên Chợ Sớm (Flash Sale) đếm ngược từng giây và lưới sản phẩm 2 cột chuẩn sàn TMĐT', 'Trong tuần', 'Lập trình đồng hồ đếm ngược phiên chợ chạy thực tế; thiết kế thẻ sản phẩm 2 cột (shopee-card) có nhãn GF-Track/OCOP góc trái, tem giảm giá (-15%, -21%) góc phải, nguồn gốc thôn, giá gạch ngang, đã bán và nút (+) thêm nhanh vào giỏ.', 'Màn 1: Sàn TMĐT Chợ G-Xanh Flash Sale & Lưới 2 cột | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['7', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Phát triển màn hình Chi tiết món hàng TMĐT với bộ chọn phân loại quy cách đóng gói tự động nhảy giá', 'Gấp', 'Hiển thị ảnh lớn sản phẩm, dải giá khuyến mãi nổi bật, điểm đánh giá sao, số lượng đã bán; làm bộ nút chọn quy cách (Hũ 500ml / Hũ 1 Lít, Khay 500g / Khay 1kg) bấm vào tự động cập nhật giá bán tương ứng.', 'Màn 2: Chi tiết sản phẩm TMĐT chọn quy cách động | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'],
  ['8', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Làm bảng thông số nguồn gốc hộ sản xuất và thanh công cụ mua hàng cố định đáy (Sticky Bottom CTA)', 'Trong tuần', 'Hiển thị rõ nguồn gốc thôn/nhà vườn, tiêu chuẩn tem GF-Track, hướng dẫn bảo quản; gắn thanh cố định đáy gồm cụm tăng giảm số lượng (stepper), nút Thêm vào giỏ (38px) và nút Mua Ngay cam Shopee (48px).', 'Thanh Sticky Bottom CTA Thêm vào giỏ & Mua Ngay | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'],
  ['9', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Lập trình màn hình Giỏ hàng TMĐT tự động gom nhóm theo từng Gian hàng/Thôn làng (CRUD đầy đủ)', 'Gấp', 'Tự động gom các món trong giỏ theo từng gian hàng/thôn (Đặc sản nhà chị Hoa, Mật ong nhà Khánh - Thôn Gò Mít); hỗ trợ tăng giảm số lượng từng món, xóa từng món, xóa toàn bộ giỏ và tự tính lại tổng tiền.', 'Màn 3: Giỏ hàng thông minh gom theo gian hàng/thôn | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/23_gxanh_gio_hang_gom_shop.png'],
  ['10', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Xây dựng cửa sổ chọn mã giảm giá G-Xanh Voucher tự động khấu trừ vào đơn hàng', 'Trong tuần', 'Làm Bottom Sheet chọn mã giảm giá (VOUCHER25K giảm 25.000đ cho đơn từ 200k, GXANHFREESHIP miễn phí vận chuyển hỏa tốc 50.000đ), bấm Áp dụng tự động trừ thẳng vào tổng thanh toán giỏ hàng.', 'Cửa sổ chọn và áp dụng mã giảm giá G-Xanh Voucher | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/24_gxanh_modal_voucher.png'],
  ['11', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Phát triển màn hình Thẻ thành viên Zalo Mini App và lưới 3 thẻ số dư điểm ngang song song', 'Gấp', 'Thiết kế thẻ thành viên điện tử (Digital Pass) hiển thị tổng điểm khả dụng (565.000 điểm) và lưới 3 cột ngang bằng nhau (Điểm nạp: 505.000, Điểm thưởng: 0, Hoa hồng: 60.000) kèm nút Nạp điểm & Lịch sử.', 'Màn 4: Ví & Thẻ thành viên Zalo Mini App 3 nguồn điểm | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'],
  ['12', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Lập trình khối Mã QR Thanh Toán Dùng 1 Lần tự động làm mới sau mỗi 60 giây chống gian lận', 'Gấp', 'Vẽ ma trận QR SVG sắc nét kèm đồng hồ đếm ngược 60s tự động tái tạo mã mới khi hết giờ hoặc khi khách bấm đổi mã trực tiếp, ngăn chặn hoàn toàn việc dùng ảnh chụp màn hình tĩnh tại quầy.', 'Bộ sinh mã QR thanh toán động 60s dùng 1 lần | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'],
  ['13', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Lập trình luồng Xác nhận đặt hàng (Checkout trừ điểm thẻ), Nạp điểm VietQR và Sổ lịch sử điểm', 'Gấp', 'Kiểm tra số dư điểm khi đặt đơn, tự động trừ điểm thẻ, sinh mã đơn DH-xxxx; làm modal nạp điểm 3 gói (200k/500k/1tr) tự sinh nội dung chuyển khoản NAP CX-302401 và tự động ghi vào lịch sử biến động điểm.', '3 Modal Đặt đơn, Nạp VietQR & Lịch sử điểm | 📸 Xem ảnh đặt đơn: https://cho-xanh.vercel.app/output_images/25_gxanh_modal_xac_nhan_dat_don.png | 📸 Ảnh nạp điểm: https://cho-xanh.vercel.app/output_images/27_gxanh_modal_nap_diem_vietqr.png | 📸 Ảnh lịch sử: https://cho-xanh.vercel.app/output_images/28_gxanh_modal_lich_su_diem.png'],
  ['14', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Xây dựng màn hình Tra cứu Tem GF-Track (3 tầng bằng chứng, 6 chặng) và Form đánh giá chất lượng', 'Gấp', 'Hiển thị huy hiệu Chính hãng GF-Track, 3 tầng bằng chứng (Nhật ký vùng trồng GPS, Chuỗi lạnh 3.2 độ C, Hồ sơ VietGAP), hành trình 6 chặng từ Xã Quy Đức đến kệ hàng và modal chấm sao + gắn tag nhận xét nhanh.', 'Màn 5: Tra cứu GF-Track & Đánh giá 5 sao | 📸 Xem ảnh GF-Track: https://cho-xanh.vercel.app/output_images/29_gxanh_tra_cuu_tem_gf_track.png | 📸 Ảnh đánh giá: https://cho-xanh.vercel.app/output_images/30_gxanh_modal_danh_gia_5sao.png'],
  ['15', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', '[Ver 2 - G-Xanh] Kiểm thử toàn diện 5 màn hình & 6 modal (2.374 dòng code) và đẩy toàn bộ bản Ver 2 lên nhánh hoang-dev', 'Gấp', 'Test kỹ toàn bộ thao tác CRUD giỏ hàng, áp voucher, nạp điểm, đặt đơn, chống tràn chữ trên màn hình 375px-430px và đẩy commit c875d503 (2.845 dòng) lên kho Git nhánh origin/hoang-dev.', 'Đồng bộ hoàn tất App Sàn TMĐT G-Xanh Ver 2 lên nhánh hoang-dev | 📸 Xem ảnh thực tế: https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png | 🔗 Link web: https://cho-xanh.vercel.app/gxanh']
];

function thucThiCapNhatCa2Tuan() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const s1 = ghiDuLieuVaoTabTuan(ss, 'Tuần 1 - 2/11 - 6/11', DU_LIEU_TUAN_1_VER_1, 137856941);
  const s2 = ghiDuLieuVaoTabTuan(ss, 'Tuần 2 - 9/11 - 13/11', DU_LIEU_TUAN_2_VER_2_GXANH, null);
  if (s1) ss.setActiveSheet(s1);
  SpreadsheetApp.flush();
  try {
    SpreadsheetApp.getUi().alert('🎉 ĐÃ CẬP NHẬT XONG CẢ 2 TUẦN (KÈM LINK ẢNH VERCEL GỌN ĐẸP)!\n- Tab Tuần 1 (2/11 - 6/11): 15 việc Ver 1 Green Village\n- Tab Tuần 2 (9/11 - 13/11): 15 việc Ver 2 App G-Xanh');
  } catch (e) {}
}

function chiCapNhatTuan1_Ver1() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const s1 = ghiDuLieuVaoTabTuan(ss, 'Tuần 1 - 2/11 - 6/11', DU_LIEU_TUAN_1_VER_1, 137856941);
  if (s1) ss.setActiveSheet(s1);
  SpreadsheetApp.flush();
}

function chiCapNhatTuan2_Ver2_GXanh() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const s2 = ghiDuLieuVaoTabTuan(ss, 'Tuần 2 - 9/11 - 13/11', DU_LIEU_TUAN_2_VER_2_GXANH, null);
  if (s2) ss.setActiveSheet(s2);
  SpreadsheetApp.flush();
}

function timHoacTaoTab(ss, sheetName, targetGid) {
  const allSheets = ss.getSheets();
  if (targetGid !== null && targetGid !== undefined) {
    for (let i = 0; i < allSheets.length; i++) {
      if (allSheets[i].getSheetId() === targetGid) return allSheets[i];
    }
  }
  const cleanTarget = sheetName.trim().toLowerCase();
  for (let i = 0; i < allSheets.length; i++) {
    if (allSheets[i].getName().trim().toLowerCase() === cleanTarget) return allSheets[i];
  }
  return ss.insertSheet(sheetName);
}

function ghiDuLieuVaoTabTuan(ss, sheetName, rowsData, targetGid) {
  if (sheetName.toLowerCase().indexOf('tháng 10') !== -1) return null;
  const sheet = timHoacTaoTab(ss, sheetName, targetGid);
  if (sheet.getSheetId() === 0 || sheet.getName().toLowerCase().indexOf('tháng 10') !== -1) return null;

  const allValues = [HEADER_11_COT].concat(rowsData);
  const totalRows = allValues.length;
  const totalCols = HEADER_11_COT.length;

  sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).clearDataValidations();
  sheet.clear();
  sheet.clearConditionalFormatRules();
  sheet.getRange(1, 1, totalRows, totalCols).setValues(allValues);
  apDungDinhDangVaDropdown(sheet, totalRows, totalCols, allValues);
  sheet.setActiveSelection('A1');
  return sheet;
}

function apDungDinhDangVaDropdown(sheet, totalRows, totalCols, csvData) {
  const maxRows = Math.max(sheet.getMaxRows(), totalRows + 20);
  const headerRange = sheet.getRange(1, 1, 1, totalCols);
  headerRange.setBackground('#1B7A43').setFontColor('#FFFFFF').setFontWeight('bold').setFontSize(10.5).setHorizontalAlignment('center').setVerticalAlignment('middle');
  sheet.setRowHeight(1, 42);

  if (totalRows > 1) {
    const dataRange = sheet.getRange(2, 1, totalRows - 1, totalCols);
    dataRange.setVerticalAlignment('middle').setFontSize(10).setWrap(true);
    for (let r = 2; r <= totalRows; r++) sheet.setRowHeight(r, 48);

    sheet.getRange(2, 1, totalRows - 1, 6).setHorizontalAlignment('center');
    sheet.getRange(2, 7, totalRows - 1, 2).setHorizontalAlignment('left');
    sheet.getRange(2, 9, totalRows - 1, 1).setHorizontalAlignment('center');
    sheet.getRange(2, 10, totalRows - 1, 2).setHorizontalAlignment('left');
  }

  sheet.getRange(1, 1, totalRows, totalCols).setBorder(true, true, true, true, true, true, '#E5E7EB', SpreadsheetApp.BorderStyle.SOLID);
  const widths = [55, 115, 105, 130, 140, 125, 135, 390, 130, 430, 520];
  for (let c = 0; c < widths.length; c++) sheet.setColumnWidth(c + 1, widths[c]);

  const applyRowCount = Math.min(maxRows - 1, 100);
  const statusRule = SpreadsheetApp.newDataValidation().requireValueInList(['Done', 'Đang làm', 'Chưa làm', 'Pending', 'Chờ duyệt', 'checking', 'Check pháp lý', 'Hủy'], true).setAllowInvalid(true).build();
  const priorityRule = SpreadsheetApp.newDataValidation().requireValueInList(['Gấp', 'Cao', 'Trong ngày', 'Trong tuần', 'Trong tháng', 'Thấp', 'Trong tuần này phải xong'], true).setAllowInvalid(true).build();
  const projectRule = SpreadsheetApp.newDataValidation().requireValueInList(['Green Village', 'Greenfi', 'WiseMeal', 'GFKey', 'G - NEXS', 'Nexs', 'OPS', 'ALL Companys'], true).setAllowInvalid(true).build();
  const assigneeRule = SpreadsheetApp.newDataValidation().requireValueInList(['Hoàng', 'Bảo', 'A VINH', 'ĐỨC', 'A BẢO', 'MAI PHƯƠNG', 'NGỌC', 'CƯỜNG'], true).setAllowInvalid(true).build();

  sheet.getRange(2, 6, applyRowCount, 1).setDataValidation(statusRule);
  sheet.getRange(2, 9, applyRowCount, 1).setDataValidation(priorityRule);
  sheet.getRange(2, 5, applyRowCount, 1).setDataValidation(projectRule);
  sheet.getRange(2, 3, applyRowCount, 1).setDataValidation(assigneeRule);

  const statusRange = sheet.getRange(2, 6, applyRowCount, 1);
  const priorityRange = sheet.getRange(2, 9, applyRowCount, 1);
  const projectRange = sheet.getRange(2, 5, applyRowCount, 1);

  sheet.setConditionalFormatRules([
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Done').setBackground('#DEF7EC').setFontColor('#03543F').setBold(true).setRanges([statusRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Đang làm').setBackground('#FEF3CD').setFontColor('#664D03').setBold(true).setRanges([statusRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Gấp').setBackground('#FDE8E8').setFontColor('#9B1C1C').setBold(true).setRanges([priorityRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Cao').setBackground('#FFEDD5').setFontColor('#9A3412').setBold(true).setRanges([priorityRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Trong tuần').setBackground('#E0E7FF').setFontColor('#3730A3').setRanges([priorityRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo('Green Village').setBackground('#E8F5E9').setFontColor('#1B5E20').setBold(true).setRanges([projectRange]).build()
  ]);

  if (csvData && csvData.length > 1) {
    const richTextValues = [];
    for (let i = 1; i < totalRows; i++) {
      const text = csvData[i][10] || '';
      const builder = SpreadsheetApp.newRichTextValue().setText(text);
      const urlRegex = /(https:\/\/[^\s|]+)/g;
      let match;
      while ((match = urlRegex.exec(text)) !== null) {
        builder.setLinkUrl(match.index, match.index + match[1].length, match[1]);
      }
      richTextValues.push([builder.build()]);
    }
    sheet.getRange(2, 11, totalRows - 1, 1).setRichTextValues(richTextValues);
  }
  sheet.setFrozenRows(1);
}
