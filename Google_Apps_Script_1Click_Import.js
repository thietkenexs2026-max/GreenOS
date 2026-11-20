// Bấm ▶️ Chạy (Run) ở bất kỳ hàm nào cũng tự động điền cả 2 Tuần!
function capNhatBaoCaoTheoTuan() { thucThiCapNhatCa2Tuan(); }
function onOpen() {
  try {
    SpreadsheetApp.getUi().createMenu('🌾 Đồng Bộ GreenOS')
      .addItem('⚡ 1-Click Cập Nhật Cả Tuần 1 & Tuần 2', 'capNhatBaoCaoTheoTuan')
      .addItem('📅 Chỉ Cập Nhật Tuần 1 (Green Village Ver 1)', 'chiCapNhatTuan1_Ver1')
      .addItem('🛒 Chỉ Cập Nhật Tuần 2 (App G-Xanh Ver 2)', 'chiCapNhatTuan2_Ver2_GXanh')
      .addToUi();
  } catch (e) {}
  thucThiCapNhatCa2Tuan();
}
function capNhatBaoCaoThang10() { thucThiCapNhatCa2Tuan(); }

const HEADER_11_COT = ['STT', 'Ngày (yyyy/mm/dd)', 'Người làm', 'Dự kiến hoàn thành', 'Nexs/ Greenfi', 'Tiến độ', 'Nguồn', 'Đầu việc', 'Thứ tự ưu tiên', 'Ghi chú', 'Output/Tài liệu'];

const DU_LIEU_TUAN_1_VER_1 = [
  ['1', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Dựng khung trang quản lý cho cán bộ xã Đồng Lam', 'Gấp', 'Chia bố cục 2 cột giống bên HTX, cột trái là menu, bên trên để4 thẻ thống kê số hộ với sản lượng trong xã.', 'https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png\nhttps://cho-xanh.vercel.app/commune-dashboard'],
  ['2', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Gộp 3 màn hình Bác Ba, HTX với Xã vào chung trang Portal', 'Gấp', 'Làm thanh chuyển qua lại giữa 3 màn hình để lúc mở demo cho sếp bấm chuyển tab luôn không phải mở nhiều link.', 'https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png\nhttps://cho-xanh.vercel.app/portal'],
  ['3', '2026/11/02', 'Hoàng', '02/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Chỉnh lại font chữ với màu xanh cho đồng bộ với trang HTX', 'Trong tuần', 'Đổi sang font Lexend cho mấy con số nhìn rõ hơn, chỉnh lại tông màu xanh lá đậm.', 'https://cho-xanh.vercel.app/output_images/01_dashboard_htx_tong_quan.webp'],
  ['4', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm bảng xếp hạng 3 HTX và theo dõi hồ sơ OCOP', 'Gấp', 'Liệt kê tiến độ làm hồ sơ OCOP 3-4 sao của từng thôn với bảng chấm điểm các HTX trong xã.', 'https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'],
  ['5', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm phần ký duyệt báo cáo tháng có đóng dấu đỏ của xã', 'Gấp', 'Bấm nút phê duyệt là hiện con dấu đỏ của UBND xã đóng lên góc văn bản để xuất file báo cáo.', 'https://cho-xanh.vercel.app/output_images/15_ver1_dashboard_xa_ky_so_dong_dau_do.png'],
  ['6', '2026/11/03', 'Hoàng', '03/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Vẽ biểu đồ mức số hoá với sản lượng mùa vụ bằng Chart.js', 'Trong tuần', 'Vẽ 3 biểu đồ theo dõi số hộ lên sàn, lượt mượn máy nông nghiệp với sản lượng thu hoạch.', 'https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'],
  ['7', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Thay hết mấy cái icon emoji cũ sang icon SVG', 'Gấp', 'Mấy chỗ menu với thẻ số liệu trước để emoji nhìn hơi rối nên thay hết sang icon nét vẽ SVG cho gọn.', 'https://cho-xanh.vercel.app/output_images/12_ver1_dashboard_xa_tong_quan.png'],
  ['8', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm bộ lọc theo thôn và tháng để biểu đồ tự nhảy số', 'Trong tuần', 'Chọn thôn hoặc đổi tháng báo cáo ở góc trên là số liệu với biểu đồ bên dưới tự đổi theo.', 'https://cho-xanh.vercel.app/output_images/13_ver1_dashboard_xa_bieu_do_chartjs.png'],
  ['9', '2026/11/04', 'Hoàng', '04/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Thêm form nhập nhanh số liệu trực tiếp trên trang xã', 'Trong tuần', 'Làm popup để nhập thêm sản lượng mới ngay trên web, bấm lưu là biểu đồ cập nhật luôn.', 'https://cho-xanh.vercel.app/output_images/14_ver1_dashboard_xa_xep_hang_htx_ocop.png'],
  ['10', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Test lại luồng dữ liệu từ app Bác Ba sang HTX và Xã', 'Gấp', 'Kiểm tra từ lúc nông dân đăng bán chuối sấy đến lúc HTX duyệt đơn sỉ WinMart xem số liệu có khớp nhau không.', 'https://cho-xanh.vercel.app/output_images/05_cong_b2b_dat_don_si.webp'],
  ['11', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Chỉnh lại màn hình Dual Studio để vừa xem điện thoại vừa xem web', 'Trong tuần', 'Đặt khung điện thoại Bác Ba cạnh màn hình HTX để lúc demo bấm bên này thì bên kia nhảy thông báo luôn.', 'https://cho-xanh.vercel.app/output_images/16_ver1_portal_3_nen_tang.png'],
  ['12', '2026/11/05', 'Hoàng', '05/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Chụp lại toàn bộ màn hình Ver 1 và nén sang đuôi WebP', 'Trong tuần', 'Chụp lại 11 màn hình của bản Ver 1 rồi nén nhẹ xuống để mở trên mạng 4G không bị chậm.', 'https://cho-xanh.vercel.app/output_images/06_mobile_bac_ba_trang_chu.webp'],
  ['13', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Cấu hình lại file vercel.json và đẩy bản Ver 1 lên host', 'Gấp', 'Sửa lại đường dẫn ngắn cho các trang mobile, portal, htx-dashboard rồi đẩy code lên Vercel.', 'https://cho-xanh.vercel.app/output_images/07_mobile_bac_ba_dark_mode.webp\nhttps://cho-xanh.vercel.app/portal'],
  ['14', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Rà soát nghiệm thu xong bản Green Village Ver 1', 'Gấp', 'Kiểm tra lại toàn bộ link web và ảnh chụp màn hình bản Ver 1 để chốt giai đoạn 1.', 'https://cho-xanh.vercel.app/output_images/02_htx_duyet_san_pham.webp'],
  ['15', '2026/11/06', 'Hoàng', '06/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Họp với Vinh chốt hướng làm bản Ver 2 sang app G-Xanh', 'Trong tuần', 'Thống nhất dừng kiểu nông dân tự đăng lẻ tẻ, chuyển sang làm app G-Xanh bán hàng như sàn thương mại điện tử.', 'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png']
];

const DU_LIEU_TUAN_2_VER_2_GXANH = [
  ['1', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Viết tài liệu kế hoạch sản phẩm cho bản Ver 2 (App G-Xanh)', 'Gấp', 'Lên khung mô hình chuỗi bán lẻ và sàn G-Xanh Từ Làng Ra Phố: gom hàng từ xã về tổng rồi bán qua cửa hàng và app.', 'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'],
  ['2', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Vẽ sơ đồ tách 2 dòng tiền và chia 15 phân hệ chức năng', 'Gấp', 'Tách riêng tiền khách nạp thẻ mua hàng với tiền cổ đông góp vốn mở điểm, chia 234 tính năng ra 3 giai đoạn làm dần.', 'https://cho-xanh.vercel.app/output_images/20_gxanh_mockup_quan_tri_chuoi_2_vong_tien.png'],
  ['3', '2026/11/09', 'Hoàng', '09/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Viết kịch bản xử lý các lỗi hay gặp khi khách mua hàng trên app', 'Trong tuần', 'Tính trước mấy trường hợp hết hàng đột xuất tại quầy, khách ngoài bán kính giao lạnh 5km hoặc bấm thanh toán 2 lần.', 'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['4', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Dựng khung giao diện điện thoại cho app mua hàng G-Xanh', 'Gấp', 'Làm khung màn hình 430px kiểu Shopee, gắn thanh menu 5 tab dưới đáy (Chợ, GF-Track, Giỏ hàng, Thẻ Zalo, Tôi).', 'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png\nhttps://cho-xanh.vercel.app/gxanh'],
  ['5', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm thanh tìm kiếm nông sản và các nút lọc theo nhóm hàng', 'Gấp', 'Gõ tên món hoặc tên thôn là lọc ra sản phẩm luôn; thêm các nút lọc Rau củ hữu cơ, Thịt cá bản địa, Đặc sản đóng gói.', 'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['6', '2026/11/10', 'Hoàng', '10/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm khung Phiên Chợ Sớm đếm ngược giờ và danh sách sản phẩm 2 cột', 'Trong tuần', 'Thêm đồng hồ đếm ngược phiên chợ sáng, làm thẻ sản phẩm 2 cột có giá giảm, số lượng đã bán và nút dấu cộng thêm nhanh vào giỏ.', 'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png'],
  ['7', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm màn hình xem chi tiết món hàng và chọn quy cách đóng gói', 'Gấp', 'Bấm vào sản phẩm hiện ảnh to, đánh giá sao, chọn loại Hũ 500ml hay 1 Lít (hoặc Khay 500g / 1kg) thì giá tiền tự đổi theo.', 'https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'],
  ['8', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm phần thông tin nguồn gốc nhà vườn và cụm nút Mua Ngay dưới đáy', 'Trong tuần', 'Ghi rõ hàng của hộ nào, thôn nào, bảo quản ra sao; dưới đáy gắn nút tăng giảm số lượng, Thêm vào giỏ và Mua Ngay.', 'https://cho-xanh.vercel.app/output_images/22_gxanh_chi_tiet_san_pham.png'],
  ['9', '2026/11/11', 'Hoàng', '11/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm màn hình Giỏ hàng gom các món theo từng nhà vườn', 'Gấp', 'Món nào cùng một nhà vườn thì gom chung vào 1 khung giống Shopee, chỉnh thêm bớt số lượng hoặc xóa món là tự tính lại tổng tiền.', 'https://cho-xanh.vercel.app/output_images/23_gxanh_gio_hang_gom_shop.png'],
  ['10', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm popup chọn mã giảm giá trừ tiền trực tiếp trong giỏ hàng', 'Trong tuần', 'Thêm 2 mã giảm 25k với mã miễn phí ship hỏa tốc 50k, bấm áp dụng là trừ thẳng vào số tiền cần thanh toán.', 'https://cho-xanh.vercel.app/output_images/24_gxanh_modal_voucher.png'],
  ['11', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Dựng màn hình Thẻ thành viên Zalo hiển thị 3 loại điểm', 'Gấp', 'Làm thẻ thành viên màu xanh hiện tổng điểm đang có, chia 3 ô: Điểm nạp, Điểm thưởng, Hoa hồng giới thiệu.', 'https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'],
  ['12', '2026/11/12', 'Hoàng', '12/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm mã QR thanh toán tự đổi mới sau mỗi 60 giây', 'Gấp', 'Khách đưa mã QR này cho thu ngân quét trừ điểm, cứ hết 60s hoặc bấm vào là tự đổi mã mới để tránh chụp ảnh màn hình dùng lại.', 'https://cho-xanh.vercel.app/output_images/26_gxanh_the_thanh_vien_zalo_qr60s.png'],
  ['13', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm phần xác nhận đặt đơn, nạp thêm điểm VietQR và lịch sử điểm', 'Gấp', 'Bấm đặt hàng thì trừ điểm trong thẻ và lưu mã đơn; nếu thiếu điểm thì mở form nạp 200k/500k/1tr qua VietQR và ghi lại lịch sử cộng trừ điểm.', 'https://cho-xanh.vercel.app/output_images/25_gxanh_modal_xac_nhan_dat_don.png\nhttps://cho-xanh.vercel.app/output_images/27_gxanh_modal_nap_diem_vietqr.png\nhttps://cho-xanh.vercel.app/output_images/28_gxanh_modal_lich_su_diem.png'],
  ['14', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Làm màn hình tra cứu tem GF-Track 6 chặng và gửi đánh giá sao', 'Gấp', 'Hiện thông tin nhật ký vùng trồng, nhiệt độ xe lạnh 3.2 độ C, giấy kiểm nghiệm VietGAP, hành trình 6 chặng từ ruộng lên kệ và form chấm 5 sao.', 'https://cho-xanh.vercel.app/output_images/29_gxanh_tra_cuu_tem_gf_track.png\nhttps://cho-xanh.vercel.app/output_images/30_gxanh_modal_danh_gia_5sao.png'],
  ['15', '2026/11/13', 'Hoàng', '13/11/2026', 'Green Village', 'Done', 'Vinh và BLĐ', 'Test lại toàn bộ các màn hình app G-Xanh và đẩy code lên nhánh hoang-dev', 'Gấp', 'Kiểm tra lại hết các nút thêm giỏ, áp mã, nạp điểm, đặt hàng trên khung điện thoại rồi commit đẩy lên nhánh hoang-dev.', 'https://cho-xanh.vercel.app/output_images/21_gxanh_trang_chu_cho_phien.png\nhttps://cho-xanh.vercel.app/gxanh']
];

function thucThiCapNhatCa2Tuan() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const s1 = ghiDuLieuVaoTabTuan(ss, 'Tuần 1 - 2/11 - 6/11', DU_LIEU_TUAN_1_VER_1, 137856941);
  const s2 = ghiDuLieuVaoTabTuan(ss, 'Tuần 2 - 9/11 - 13/11', DU_LIEU_TUAN_2_VER_2_GXANH, null);
  if (s1) ss.setActiveSheet(s1);
  SpreadsheetApp.flush();
  try {
    SpreadsheetApp.getUi().alert('🎉 Đã cập nhật xong cả 2 tuần (Văn phong ngắn gọn tự nhiên + Link ảnh gọn)!');
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
  const widths = [55, 115, 105, 130, 140, 125, 135, 360, 130, 410, 460];
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
      const urlRegex = /(https:\/\/[^\s\n]+)/g;
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
