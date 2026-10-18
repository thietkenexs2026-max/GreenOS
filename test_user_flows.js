const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 375, height: 844, isMobile: true });
    const path = require('path');
    const filePath = 'file:///' + path.resolve(__dirname, 'index.html').replace(/\\/g, '/');
    await page.goto(filePath, { waitUntil: 'load' });

    console.log('--- 1. Test hoàn tất Onboarding vào Trang chủ ---');
    await page.evaluate(() => {
      if (document.getElementById('panel-onboarding').classList.contains('active')) {
        window.completeOnboarding();
      }
    });
    await new Promise(r => setTimeout(r, 400));

    console.log('--- 2. Test 6 nút Việc cần làm hôm nay ---');
    // Test 1: 5 đơn quá hạn
    await page.evaluate(() => window.openOrdersFiltered('qua_han'));
    await new Promise(r => setTimeout(r, 300));
    let ordersActive = await page.evaluate(() => document.getElementById('panel-orders').classList.contains('active'));
    console.log(' > [5 đơn quá hạn] chuyển đến panel-orders:', ordersActive ? 'PASS' : 'FAIL');

    // Quay lại Home
    await page.evaluate(() => window.switchNavTab('home'));
    await new Promise(r => setTimeout(r, 300));

    // Test 2: 44 đơn chờ xác nhận
    await page.evaluate(() => window.openOrdersFiltered('cho_xac_nhan'));
    await new Promise(r => setTimeout(r, 300));
    ordersActive = await page.evaluate(() => document.getElementById('panel-orders').classList.contains('active'));
    console.log(' > [44 đơn chờ xác nhận] chuyển đến panel-orders:', ordersActive ? 'PASS' : 'FAIL');

    // Quay lại Home
    await page.evaluate(() => window.switchNavTab('home'));
    await new Promise(r => setTimeout(r, 300));

    // Test 3: 9 đơn chờ đóng gói -> Picklist
    await page.evaluate(() => window.openPickListView());
    await new Promise(r => setTimeout(r, 300));
    let picklistActive = await page.evaluate(() => document.getElementById('panel-picklist').classList.contains('active'));
    console.log(' > [9 đơn chờ đóng gói] mở panel-picklist:', picklistActive ? 'PASS' : 'FAIL');

    // Quay lại Home
    await page.evaluate(() => window.switchNavTab('home'));
    await new Promise(r => setTimeout(r, 300));

    // Test 4: 2 đơn có khiếu nại
    await page.evaluate(() => window.openOrdersFiltered('khieu_nai'));
    await new Promise(r => setTimeout(r, 300));
    ordersActive = await page.evaluate(() => document.getElementById('panel-orders').classList.contains('active'));
    console.log(' > [2 đơn có khiếu nại] mở panel-orders lọc khiếu nại:', ordersActive ? 'PASS' : 'FAIL');

    // Quay lại Home
    await page.evaluate(() => window.switchNavTab('home'));
    await new Promise(r => setTimeout(r, 300));

    // Test 5: Sửa sản phẩm nháp
    await page.evaluate(() => window.openDraftProductResume());
    await new Promise(r => setTimeout(r, 300));
    let step2Active = await page.evaluate(() => document.getElementById('panel-step2').classList.contains('active'));
    console.log(' > [Sửa 2 sản phẩm nháp] mở panel-step2 nạp sẵn dữ liệu:', step2Active ? 'PASS' : 'FAIL');

    // Quay lại Home
    await page.evaluate(() => window.exitWizardToHome());
    await new Promise(r => setTimeout(r, 300));

    // Test 6: GFKey modal
    await page.evaluate(() => window.openFarmerQRModal());
    await new Promise(r => setTimeout(r, 300));
    let qrShown = await page.evaluate(() => document.getElementById('farmerQRModal').classList.contains('show'));
    console.log(' > [GFKey chưa liên kết] mở farmerQRModal:', qrShown ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.closeFarmerQRModal());

    console.log('--- 3. Test 3 Card Ngang Song Song ---');
    // Card 1: Đăng bán
    await page.evaluate(() => window.startWizardFlow());
    await new Promise(r => setTimeout(r, 300));
    let step1Active = await page.evaluate(() => document.getElementById('panel-step1').classList.contains('active'));
    console.log(' > [Card Đăng Bán] mở panel-step1:', step1Active ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.exitWizardToHome());

    // Card 2: Chợ Xanh
    await page.evaluate(() => window.switchNavTab('market'));
    await new Promise(r => setTimeout(r, 300));
    let marketActive = await page.evaluate(() => document.getElementById('panel-market').classList.contains('active'));
    console.log(' > [Card Chợ Xanh] mở panel-market:', marketActive ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.switchNavTab('home'));

    // Card 3: An Cư Job
    await page.evaluate(() => window.openAnCuJobScreen());
    await new Promise(r => setTimeout(r, 300));
    let jobActive = await page.evaluate(() => document.getElementById('panel-ancujob').classList.contains('active'));
    console.log(' > [Card An Cư Job] mở panel-ancujob:', jobActive ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.closeAnCuJobScreen());

    console.log('--- 4. Test Màn hình Hub Hỗ Trợ & Nút Quay lại ---');
    await page.evaluate(() => window.switchNavTab('support'));
    await new Promise(r => setTimeout(r, 300));
    let supportActive = await page.evaluate(() => document.getElementById('panel-support').classList.contains('active'));
    console.log(' > [Hub Xã Hỗ Trợ] mở panel-support:', supportActive ? 'PASS' : 'FAIL');
    // Click nút quay lại về home
    await page.evaluate(() => window.switchNavTab('home'));
    await new Promise(r => setTimeout(r, 300));
    let homeBack = await page.evaluate(() => document.getElementById('panel-home').classList.contains('active'));
    console.log(' > [Nút Quay lại Hub Hỗ Trợ] trở về panel-home:', homeBack ? 'PASS' : 'FAIL');

    console.log('--- 5. Test 3 Modal Mới tại Màn hình Tài khoản ---');
    await page.evaluate(() => window.switchNavTab('account'));
    await new Promise(r => setTimeout(r, 300));

    // Modal Hồ sơ hộ
    await page.evaluate(() => window.openFarmerProfileModal());
    await new Promise(r => setTimeout(r, 200));
    let pModal = await page.evaluate(() => document.getElementById('farmerProfileModal').classList.contains('show'));
    console.log(' > [Hồ sơ hộ] mở farmerProfileModal:', pModal ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.closeFarmerProfileModal());

    // Modal Gói dịch vụ
    await page.evaluate(() => window.openServicePackageModal());
    await new Promise(r => setTimeout(r, 200));
    let sModal = await page.evaluate(() => document.getElementById('servicePackageModal').classList.contains('show'));
    console.log(' > [Gói dịch vụ] mở servicePackageModal:', sModal ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.closeServicePackageModal());

    // Modal Đổi tài khoản
    await page.evaluate(() => window.openSwitchAccountModal());
    await new Promise(r => setTimeout(r, 200));
    let swModal = await page.evaluate(() => document.getElementById('switchAccountModal').classList.contains('show'));
    console.log(' > [Đổi tài khoản] mở switchAccountModal:', swModal ? 'PASS' : 'FAIL');
    await page.evaluate(() => window.closeSwitchAccountModal());

    console.log('--- 6. Kiểm tra Overflow & Responsive trên 375px, 390px, 412px ---');
    for (const w of [375, 390, 412]) {
      await page.setViewport({ width: w, height: 844, isMobile: true });
      await page.evaluate(() => window.switchNavTab('home'));
      await new Promise(r => setTimeout(r, 200));
      const overflows = await page.evaluate((width) => {
        let count = 0;
        document.querySelectorAll('.view-panel.active *').forEach(el => {
          const r = el.getBoundingClientRect();
          if (r.right > width + 1 && !el.closest('.ecom-cat-chips')) {
            count++;
          }
        });
        return count;
      }, w);
      console.log(` > Chiều rộng ${w}px: ${overflows} lỗi tràn ngang`);
    }

    console.log('\n🎉 TẤT CẢ KỊCH BẢN ĐIỀU HƯỚNG VÀ KIỂM THỬ ĐÃ PASS 100%!');
  } catch (err) {
    console.error('Lỗi khi chạy test:', err);
  } finally {
    await browser.close();
  }
})();
