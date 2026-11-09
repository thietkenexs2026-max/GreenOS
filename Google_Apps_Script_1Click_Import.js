/**
 * Tự động tạo menu trên thanh công cụ Google Sheet khi mở file
 */
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('🌾 Đồng Bộ GreenOS')
    .addItem('⚡ 1-Click Nạp Báo Cáo & Tạo Dropdown + Link Click', 'capNhatBaoCaoThang10')
    .addToUi();
}

/**
 * Hàm kéo dữ liệu, tạo Dropdown Select Chips và gán Link ảnh click trực tiếp
 */
function capNhatBaoCaoThang10() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const url = "https://cho-xanh.vercel.app/Bao_Cao_Cong_Viec_Thang_10_Hoang_GreenOS.csv";
  
  const response = UrlFetchApp.fetch(url);
  const csvData = Utilities.parseCsv(response.getContentText("UTF-8"));
  
  // 1. Xóa nội dung và định dạng cũ
  sheet.clear();
  sheet.clearConditionalFormatRules();
  
  // 2. Ghi toàn bộ dữ liệu 62 dòng vào trang tính
  const totalRows = csvData.length;
  const totalCols = csvData[0].length;
  sheet.getRange(1, 1, totalRows, totalCols).setValues(csvData);
  
  // 3. Định dạng hàng tiêu đề chuẩn GreenFi
  const headerRange = sheet.getRange(1, 1, 1, totalCols);
  headerRange.setBackground("#1B7A43"); // Xanh lá thương hiệu GreenFi
  headerRange.setFontColor("#FFFFFF");
  headerRange.setFontWeight("bold");
  headerRange.setHorizontalAlignment("center");
  headerRange.setVerticalAlignment("middle");
  sheet.setRowHeight(1, 38);
  
  // 4. Căn chỉnh lề các cột
  sheet.getRange(2, 1, totalRows - 1, 1).setHorizontalAlignment("center"); // STT
  sheet.getRange(2, 2, totalRows - 1, 1).setHorizontalAlignment("center"); // Ngày
  sheet.getRange(2, 3, totalRows - 1, 1).setHorizontalAlignment("center"); // Người làm
  sheet.getRange(2, 4, totalRows - 1, 1).setHorizontalAlignment("center"); // Dự kiến
  sheet.getRange(2, 5, totalRows - 1, 1).setHorizontalAlignment("center"); // Thời lượng
  sheet.getRange(2, 6, totalRows - 1, 1).setHorizontalAlignment("center"); // Dự án
  sheet.getRange(2, 7, totalRows - 1, 1).setHorizontalAlignment("center"); // Tiến độ
  sheet.getRange(2, 8, totalRows - 1, 1).setHorizontalAlignment("center"); // Nguồn
  sheet.getRange(2, 10, totalRows - 1, 1).setHorizontalAlignment("center"); // Ưu tiên
  
  // 5. TẠO CÁC DROPDOWN CHIPS (Trình đơn chọn thả xuống)
  // Dropdown Cột Tiến độ (Cột 7)
  const statusRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Done', 'Đang làm', 'Chưa làm', 'Pending', 'Chờ duyệt', 'Hủy'], true)
    .setAllowInvalid(false)
    .build();
  const statusRange = sheet.getRange(2, 7, totalRows - 1, 1);
  statusRange.setDataValidation(statusRule);

  // Dropdown Cột Thứ tự ưu tiên (Cột 10)
  const priorityRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Gấp', 'Cao', 'Trong tuần', 'Trong tháng'], true)
    .setAllowInvalid(false)
    .build();
  const priorityRange = sheet.getRange(2, 10, totalRows - 1, 1);
  priorityRange.setDataValidation(priorityRule);

  // Dropdown Cột Nexs/ Greenfi (Cột 6)
  const projectRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Green Village', 'Greenfi', 'GFKey', 'WiseMeal', 'G - NEXS', 'OPS'], true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange(2, 6, totalRows - 1, 1).setDataValidation(projectRule);

  // Dropdown Cột Người làm (Cột 3)
  const assigneeRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['Hoàng', 'A VINH', 'ĐỨC', 'A BẢO', 'NGỌC', 'MAI PHƯƠNG', 'CƯỜNG'], true)
    .setAllowInvalid(false)
    .build();
  sheet.getRange(2, 3, totalRows - 1, 1).setDataValidation(assigneeRule);

  // 6. THIẾT LẬP MÀU SẮC TỰ ĐỘNG CHO DROPDOWN
  const rules = [];
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Done").setBackground("#D1E7DD").setFontColor("#0F5132").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Đang làm").setBackground("#FFF3CD").setFontColor("#664D03").setBold(true)
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Chưa làm").setBackground("#F8F9FA").setFontColor("#5F6368")
    .setRanges([statusRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Pending").setBackground("#FFE5D0").setFontColor("#984C0C").setBold(true)
    .setRanges([statusRange]).build());

  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Gấp").setBackground("#F8D7DA").setFontColor("#842029").setBold(true)
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Cao").setBackground("#FFE0B2").setFontColor("#E65100").setBold(true)
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Trong tuần").setBackground("#E0E7FF").setFontColor("#3730A3")
    .setRanges([priorityRange]).build());
  rules.push(SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo("Trong tháng").setBackground("#F1F5F9").setFontColor("#475569")
    .setRanges([priorityRange]).build());

  sheet.setConditionalFormatRules(rules);

  // 7. BIẾN CÁC ĐƯỜNG LINK ẢNH THÀNH LINK BẤM ĐƯỢC TRỰC TIẾP (CLICKABLE HYPERLINKS)
  const outputRange = sheet.getRange(2, 12, totalRows - 1, 1);
  const richTextValues = [];
  for (let i = 1; i < totalRows; i++) {
    const text = csvData[i][11] || "";
    const builder = SpreadsheetApp.newRichTextValue().setText(text);
    
    // Tự động tìm tất cả link https://... trong ô để gắn siêu liên kết bấm được
    const urlRegex = /(https:\/\/[^\s|]+)/g;
    let match;
    while ((match = urlRegex.exec(text)) !== null) {
      const foundUrl = match[1];
      builder.setLinkUrl(match.index, match.index + foundUrl.length, foundUrl);
    }
    richTextValues.push([builder.build()]);
  }
  outputRange.setRichTextValues(richTextValues);

  // 8. Tự động xuống dòng (Wrap Text) & Chỉnh độ rộng cột chuẩn bảng mẫu
  sheet.getRange(1, 1, totalRows, totalCols).setWrap(true);
  sheet.setColumnWidth(1, 55);   // STT
  sheet.setColumnWidth(2, 105);  // Ngày
  sheet.setColumnWidth(3, 100);  // Người làm
  sheet.setColumnWidth(4, 110);  // Dự kiến
  sheet.setColumnWidth(5, 80);   // Thời lượng
  sheet.setColumnWidth(6, 120);  // Nexs/Greenfi
  sheet.setColumnWidth(7, 105);  // Tiến độ
  sheet.setColumnWidth(8, 120);  // Nguồn
  sheet.setColumnWidth(9, 280);  // Đầu việc
  sheet.setColumnWidth(10, 105); // Ưu tiên
  sheet.setColumnWidth(11, 320); // Ghi chú
  sheet.setColumnWidth(12, 420); // Output
  
  // 9. Cố định hàng tiêu đề
  sheet.setFrozenRows(1);
  
  SpreadsheetApp.getUi().alert("🎉 Hoàn tất! Đã tạo Dropdown Chips và gắn Link ảnh Click được trực tiếp!");
}
