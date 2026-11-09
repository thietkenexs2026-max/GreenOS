/**
 * ==============================================================================
 * GOOGLE APPS SCRIPT: 1-CLICK ĐỒNG BỘ BÁO CÁO THÁNG 10 (HOÀNG - GREENOS)
 * CHUẨN 11 CỘT KHỚP 100% GOOGLE SHEET MẪU (NEXS - GREENFI)
 * ==============================================================================
 * 
 * HƯỚNG DẪN SỬ DỤNG:
 * 1. Mở file Google Sheet của bạn.
 * 2. Trên thanh menu, chọn: Tiện ích mở rộng (Extensions) -> Apps Script.
 * 3. Dán toàn bộ nội dung file này vào và bấm biểu tượng "Lưu" (Ctrl + S).
 * 4. Tải lại trang Google Sheet (F5).
 * 5. Trên menu xuất hiện tab: "🌾 Đồng Bộ GreenOS" -> Click "⚡ 1-Click Nạp 70 Đầu Việc & Tạo Dropdown".
 */

function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🌾 Đồng Bộ GreenOS')
    .addItem('⚡ 1-Click Nạp 70 Đầu Việc & Tạo Dropdown + Link Click', 'capNhatBaoCaoThang10')
    .addToUi();
}

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

  // 1. Xóa nội dung và định dạng cũ
  sheet.clear();
  sheet.clearConditionalFormatRules();

  // 2. Ghi toàn bộ dữ liệu 70 dòng vào trang tính (1 hàng tiêu đề + 70 dòng dữ liệu)
  sheet.getRange(1, 1, totalRows, totalCols).setValues(csvData);

  // 3. Định dạng hàng tiêu đề chuẩn GreenFi (Màu xanh lá đậm đặc trưng)
  const headerRange = sheet.getRange(1, 1, 1, totalCols);
  headerRange.setBackground("#1B7A43");
  headerRange.setFontColor("#FFFFFF");
  headerRange.setFontWeight("bold");
  headerRange.setHorizontalAlignment("center");
  headerRange.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 38);

  // 4. Căn chỉnh lề các cột
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

  // 5. THIẾT LẬP CÁC DROPDOWN CHIPS KHỚP 100% GOOGLE SHEET MẪU CỦA CÔNG TY
  // Dropdown Cột 3: Người làm
  const assigneeRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Hoàng', 'A VINH', 'ĐỨC', 'A BẢO', 'MAI PHƯƠNG', 'NGỌC', 'CƯỜNG'], true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 3, totalRows - 1, 1).setDataValidation(assigneeRule);

  // Dropdown Cột 5: Nexs/ Greenfi
  const projectRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Green Village', 'Greenfi', 'WiseMeal', 'GFKey', 'G - NEXS', 'Nexs', 'OPS', 'ALL Companys'], true)
    .setAllowInvalid(true)
    .build();
  sheet.getRange(2, 5, totalRows - 1, 1).setDataValidation(projectRule);

  // Dropdown Cột 6: Tiến độ (Status chuẩn công ty)
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Done', 'Đang làm', 'Chưa làm', 'Pending', 'Chờ duyệt', 'Hủy', 'checking', 'Check pháp lý'], true)
    .setAllowInvalid(true)
    .build();
  const statusRange = sheet.getRange(2, 6, totalRows - 1, 1);
  statusRange.setDataValidation(statusRule);

  // Dropdown Cột 9: Thứ tự ưu tiên
  const priorityRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Gấp', 'Cao', 'Trong ngày', 'Trong tuần', 'Trong tháng', 'Thấp'], true)
    .setAllowInvalid(true)
    .build();
  const priorityRange = sheet.getRange(2, 9, totalRows - 1, 1);
  priorityRange.setDataValidation(priorityRule);

  // 6. CONDITIONAL FORMATTING - ĐỔ MÀU CHIPS TRẠNG THÁI & ƯU TIÊN
  const rules = [];
  // Màu Tiến độ
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Done").setBackground("#DEF7EC").setFontColor("#03543F").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Đang làm").setBackground("#FEF3C7").setFontColor("#92400E").setBold(true)
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
    .whenTextEqualTo("Hủy").setBackground("#FDE8E8").setFontColor("#9B1C1C").setBold(true)
    .setRanges([statusRange]).build());

  // Màu Thứ tự ưu tiên
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

  sheet.setConditionalFormatRules(rules);

  // 7. GẮN SIÊU LIÊN KẾT (CLICKABLE HYPERLINKS) VÀO CỘT OUTPUT/TÀI LIỆU (CỘT 11)
  const outputRange = sheet.getRange(2, 11, totalRows - 1, 1);
  const richTextValues = [];
  for (let i = 1; i < totalRows; i++) {
    const text = csvData[i][10] || "";
    const builder = SpreadsheetApp.newRichTextValue().setText(text);
    
    // Tìm các link URL https://... để gắn link click trực tiếp
    const urlRegex = /(https:\/\/[^\s|]+)/g;
    let match;
    while ((match = urlRegex.exec(text)) !== null) {
      const foundUrl = match[1];
      builder.setLinkUrl(match.index, match.index + foundUrl.length, foundUrl);
    }
    richTextValues.push([builder.build()]);
  }
  outputRange.setRichTextValues(richTextValues);

  // 8. TỰ ĐỘNG XUỐNG DÒNG (WRAP TEXT) & CĂN CHỈNH ĐỘ RỘNG CỘT CHUẨN GOOGLE SHEET MẪU
  sheet.getRange(1, 1, totalRows, totalCols).setWrap(true);
  sheet.setColumnWidth(1, 50);   // STT
  sheet.setColumnWidth(2, 105);  // Ngày (yyyy/mm/dd)
  sheet.setColumnWidth(3, 90);   // Người làm
  sheet.setColumnWidth(4, 110);  // Dự kiến hoàn thành
  sheet.setColumnWidth(5, 120);  // Nexs/ Greenfi
  sheet.setColumnWidth(6, 105);  // Tiến độ
  sheet.setColumnWidth(7, 110);  // Nguồn
  sheet.setColumnWidth(8, 300);  // Đầu việc
  sheet.setColumnWidth(9, 110);  // Thứ tự ưu tiên
  sheet.setColumnWidth(10, 340); // Ghi chú
  sheet.setColumnWidth(11, 420); // Output/Tài liệu

  // 9. Cố định hàng tiêu đề (Freeze Header)
  sheet.setFrozenRows(1);

  SpreadsheetApp.getUi().alert("🎉 Hoàn tất! Đã đồng bộ đầy đủ " + (totalRows - 1) + " đầu việc cả tháng 10 chuẩn 11 cột, tạo Dropdown Chips và gắn Link click trực tiếp!");
}
