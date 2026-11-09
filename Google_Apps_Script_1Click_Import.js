/**
 * ==============================================================================
 * GOOGLE APPS SCRIPT: ĐỒNG BỘ BÁO CÁO THÁNG 10 (HOÀNG - GREENOS)
 * CHUẨN 11 CỘT - KHẮC PHỤC TRIỆT ĐỂ LỖI XÁC THỰC Ô F2 (DATA VALIDATION)
 * ==============================================================================
 * 
 * NGUYÊN NHÂN LỖI Ô F2:
 * Ở bản cũ (12 cột), Cột F là cột Dự án (chỉ nhận Green Village, Greenfi...).
 * Lệnh sheet.clear() của Google Sheet không tự xóa quy tắc xác thực (Data Validation) cũ.
 * Do đó khi chuyển về chuẩn 11 cột, Cột F là cột Tiến độ (Done, Đang làm...), Google Sheet
 * chặn lại vì vướng quy tắc cũ của cột F.
 * 
 * GIẢI PHÁP:
 * Thêm lệnh: sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).clearDataValidations();
 * để gỡ sạch toàn bộ quy tắc cũ TRƯỚC KHI nạp dữ liệu, sau đó thiết lập lại Dropdown mới chuẩn 100%.
 */

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🌾 Đồng Bộ GreenOS')
    .addItem('⚡ 1-Click Nạp 70 Đầu Việc & Giãn Bảng Thoáng Đẹp', 'capNhatBaoCaoThang10')
    .addItem('🎨 Chỉ Cập Nhật Dropdown & Giãn Cột (Không Xóa Dữ Liệu)', 'caiDatDropdownVaDinhDang')
    .addToUi();
}

/**
 * 1. Hàm nạp đầy đủ dữ liệu từ hệ thống và tự động làm đẹp toàn diện
 */
function capNhatBaoCaoThang10() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // URL CSV chuẩn 11 cột với tham số chống cache (Cache-Busting)
  const cacheBuster = new Date().getTime();
  const url = "https://cho-xanh.vercel.app/Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv?t=" + cacheBuster;
  
  const response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
  if (response.getResponseCode() !== 200) {
    SpreadsheetApp.getUi().alert("❌ Không thể tải file CSV từ server (Mã lỗi " + response.getResponseCode() + ").");
    return;
  }
  
  const csvData = Utilities.parseCsv(response.getContentText("UTF-8"));
  if (!csvData || csvData.length === 0) {
    SpreadsheetApp.getUi().alert("❌ Dữ liệu CSV rỗng!");
    return;
  }

  const totalRows = csvData.length;
  const totalCols = csvData[0].length; // Chuẩn 11 cột

  // 1. GỠ BỎ TOÀN BỘ QUY TẮC XÁC THỰC CŨ TRƯỚC TIÊN (Fix triệt để lỗi ô F2)
  sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).clearDataValidations();
  
  // 2. Xóa nội dung và định dạng cũ
  sheet.clear();
  sheet.clearConditionalFormatRules();

  // 3. Ghi toàn bộ dữ liệu 70 dòng vào trang tính an toàn 100%
  sheet.getRange(1, 1, totalRows, totalCols).setValues(csvData);

  // 4. Áp dụng định dạng, dropdown và giãn khoảng cách
  apDungDinhDangVaDropdown(sheet, totalRows, totalCols, csvData);

  SpreadsheetApp.getUi().alert("🎉 Hoàn tất! Đã đồng bộ 70 đầu việc cả tháng 10 chuẩn 11 cột, giãn dòng thoáng đẹp và tạo Dropdown đầy đủ!");
}

/**
 * 2. Hàm chỉ cập nhật Dropdown và giãn khoảng cách (Dành cho trường hợp bạn đã có dữ liệu sẵn trên Sheet)
 */
function caiDatDropdownVaDinhDang() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const totalRows = Math.max(sheet.getLastRow(), 71);
  const totalCols = 11;

  // Gỡ bỏ validation cũ tránh xung đột
  sheet.getRange(1, 1, sheet.getMaxRows(), sheet.getMaxColumns()).clearDataValidations();

  apDungDinhDangVaDropdown(sheet, totalRows, totalCols, null);
  SpreadsheetApp.getUi().alert("🎉 Đã cập nhật xong Dropdown lựa chọn và giãn dòng thoáng đẹp cho bảng của bạn!");
}

/**
 * Hàm chung: Định dạng bảng, giãn dòng thoáng, tạo Dropdown và đổi màu
 */
function apDungDinhDangVaDropdown(sheet, totalRows, totalCols, csvData) {
  const maxRows = Math.max(sheet.getMaxRows(), totalRows + 20);

  // 1. ĐỊNH DẠNG HÀNG TIÊU ĐỀ CHUẨN GREENFI (Màu xanh lá đậm, chữ trắng, cao 42px)
  const headerRange = sheet.getRange(1, 1, 1, totalCols);
  headerRange.setBackground("#1B7A43");
  headerRange.setFontColor("#FFFFFF");
  headerRange.setFontWeight("bold");
  headerRange.setFontSize(10.5);
  headerRange.setHorizontalAlignment("center");
  headerRange.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 42);

  // 2. CHỮ KHÔNG BỊ SÁT: Căn giữa theo chiều dọc (Vertical Middle) + Giãn chiều cao hàng (48px)
  const dataRange = sheet.getRange(2, 1, totalRows - 1, totalCols);
  dataRange.setVerticalAlignment("middle");
  dataRange.setFontSize(10);
  dataRange.setWrap(true);

  // Đặt chiều cao từng hàng rộng rãi (48px cho dễ đọc, chữ không chạm mép)
  for (let r = 2; r <= totalRows; r++) {
    sheet.setRowHeight(r, 48);
  }

  // Căn lề ngang cho từng loại dữ liệu
  sheet.getRange(2, 1, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 1: STT
  sheet.getRange(2, 2, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 2: Ngày (yyyy/mm/dd)
  sheet.getRange(2, 3, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 3: Người làm
  sheet.getRange(2, 4, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 4: Dự kiến hoàn thành
  sheet.getRange(2, 5, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 5: Nexs/ Greenfi
  sheet.getRange(2, 6, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 6: Tiến độ
  sheet.getRange(2, 7, totalRows - 1, 1).setHorizontalAlignment("left");   // Cột 7: Nguồn
  sheet.getRange(2, 8, totalRows - 1, 1).setHorizontalAlignment("left");   // Cột 8: Đầu việc
  sheet.getRange(2, 9, totalRows - 1, 1).setHorizontalAlignment("center"); // Cột 9: Thứ tự ưu tiên
  sheet.getRange(2, 10, totalRows - 1, 1).setHorizontalAlignment("left");  // Cột 10: Ghi chú
  sheet.getRange(2, 11, totalRows - 1, 1).setHorizontalAlignment("left");  // Cột 11: Output/Tài liệu

  // Viền ô màu xám nhạt thanh lịch (#E5E7EB)
  sheet.getRange(1, 1, totalRows, totalCols).setBorder(
    true, true, true, true, true, true,
    "#E5E7EB", SpreadsheetApp.BorderStyle.SOLID
  );

  // 3. ĐỘ RỘNG CỘT RỘNG RÃI, THOÁNG ĐÃNG (KHÔNG BỊ SÁT CHỮ)
  sheet.setColumnWidth(1, 55);   // STT
  sheet.setColumnWidth(2, 115);  // Ngày (yyyy/mm/dd)
  sheet.setColumnWidth(3, 105);  // Người làm
  sheet.setColumnWidth(4, 130);  // Dự kiến hoàn thành
  sheet.setColumnWidth(5, 140);  // Nexs/ Greenfi (Dự án)
  sheet.setColumnWidth(6, 125);  // Tiến độ
  sheet.setColumnWidth(7, 135);  // Nguồn
  sheet.setColumnWidth(8, 380);  // Đầu việc (Mở rộng thoải mái)
  sheet.setColumnWidth(9, 130);  // Thứ tự ưu tiên
  sheet.setColumnWidth(10, 420); // Ghi chú (Rộng rãi, đọc thoáng)
  sheet.setColumnWidth(11, 500); // Output/Tài liệu (Rộng rãi, link rõ ràng)

  // 4. TẠO CÁC DROPDOWN CHIPS LỰA CHỌN KHỚP 100% LINK MẪU GỐC CỦA CÔNG TY
  const applyRowCount = Math.min(maxRows - 1, 300);

  // A. Dropdown Cột 6 (Cột F): Tiến độ (Trạng thái)
  const statusList = ['Done', 'Đang làm', 'Chưa làm', 'Pending', 'Chờ duyệt', 'checking', 'Check pháp lý', 'Hủy'];
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(statusList, true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 6, applyRowCount, 1).setDataValidation(statusRule);

  // B. Dropdown Cột 9 (Cột I): Thứ tự ưu tiên
  const priorityList = ['Gấp', 'Cao', 'Trong ngày', 'Trong tuần', 'Trong tháng', 'Thấp', 'Trong tuần này phải xong'];
  const priorityRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(priorityList, true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 9, applyRowCount, 1).setDataValidation(priorityRule);

  // C. Dropdown Cột 5 (Cột E): Nexs/ Greenfi (Dự án)
  const projectList = ['Green Village', 'Greenfi', 'WiseMeal', 'GFKey', 'G - NEXS', 'Nexs', 'OPS', 'ALL Companys'];
  const projectRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(projectList, true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 5, applyRowCount, 1).setDataValidation(projectRule);

  // D. Dropdown Cột 3 (Cột C): Người làm
  const assigneeList = ['Hoàng', 'A VINH', 'ĐỨC', 'A BẢO', 'MAI PHƯƠNG', 'NGỌC', 'CƯỜNG'];
  const assigneeRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(assigneeList, true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 3, applyRowCount, 1).setDataValidation(assigneeRule);

  // 5. TỰ ĐỘNG ĐỔ MÀU SẮC CHO DROPDOWN (CONDITIONAL FORMATTING)
  const statusRange = sheet.getRange(2, 6, applyRowCount, 1);
  const priorityRange = sheet.getRange(2, 9, applyRowCount, 1);
  const projectRange = sheet.getRange(2, 5, applyRowCount, 1);

  const rules = [];

  // Màu sắc Tiến độ (Status)
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Done").setBackground("#DEF7EC").setFontColor("#03543F").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Đang làm").setBackground("#FEF3CD").setFontColor("#664D03").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Chưa làm").setBackground("#F3F4F6").setFontColor("#4B5563")
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Pending").setBackground("#FFEDD5").setFontColor("#9A3412").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Chờ duyệt").setBackground("#E0F2FE").setFontColor("#0369A1").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("checking").setBackground("#F3E8FF").setFontColor("#6B21A8").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Check pháp lý").setBackground("#FCE7F3").setFontColor("#9D174D").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Hủy").setBackground("#FDE8E8").setFontColor("#9B1C1C").setBold(true)
    .setRanges([statusRange]).build());

  // Màu sắc Thứ tự ưu tiên
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Gấp").setBackground("#FDE8E8").setFontColor("#9B1C1C").setBold(true)
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Cao").setBackground("#FFEDD5").setFontColor("#9A3412").setBold(true)
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Trong ngày").setBackground("#FEF08A").setFontColor("#713F12").setBold(true)
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Trong tuần").setBackground("#E0E7FF").setFontColor("#3730A3")
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Trong tháng").setBackground("#F1F5F9").setFontColor("#475569")
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Thấp").setBackground("#ECFDF5").setFontColor("#065F46")
    .setRanges([priorityRange]).build());

  // Màu sắc Dự án
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Green Village").setBackground("#E8F5E9").setFontColor("#1B5E20").setBold(true)
    .setRanges([projectRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Greenfi").setBackground("#F0FDF4").setFontColor("#15803D").setBold(true)
    .setRanges([projectRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("WiseMeal").setBackground("#FFFBEB").setFontColor("#B45309").setBold(true)
    .setRanges([projectRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("GFKey").setBackground("#EFF6FF").setFontColor("#1D4ED8").setBold(true)
    .setRanges([projectRange]).build());

  sheet.setConditionalFormatRules(rules);

  // 6. GẮN SIÊU LIÊN KẾT (CLICKABLE HYPERLINKS) VÀO CỘT OUTPUT/TÀI LIỆU (CỘT 11)
  if (csvData && csvData.length > 1) {
    const outputRange = sheet.getRange(2, 11, totalRows - 1, 1);
    const richTextValues = [];
    for (let i = 1; i < totalRows; i++) {
      const text = csvData[i][10] || "";
      const builder = SpreadsheetApp.newRichTextValue().setText(text);
      
      const urlRegex = /(https:\/\/[^\s|]+)/g;
      let match;
      while ((match = urlRegex.exec(text)) !== null) {
        const foundUrl = match[1];
        builder.setLinkUrl(match.index, match.index + foundUrl.length, foundUrl);
      }
      richTextValues.push([builder.build()]);
    }
    outputRange.setRichTextValues(richTextValues);
  }

  // 7. Cố định hàng tiêu đề
  sheet.setFrozenRows(1);
}
