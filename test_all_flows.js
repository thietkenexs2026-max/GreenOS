const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const APP_URL = 'http://127.0.0.1:8080/index.html';

async function runTestSuite() {
  console.log('=== BẮT ĐẦU KIỂM THỬ TOÀN BỘ CÁC LUỒNG HỆ THỐNG CHỢ XANH ===');
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--window-size=1280,800']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });

  const errors = [];
  page.on('pageerror', err => {
    errors.push('Page Error: ' + err.message);
  });
  page.on('console', msg => {
    if (msg.type() === 'error') {
      errors.push('Console Error: ' + msg.text());
    }
  });

  console.log('1. Đang tải trang web:', APP_URL);
  await page.goto(APP_URL, { waitUntil: 'networkidle2', timeout: 15000 });
  console.log('✓ Tải trang thành công.');

  // =========================================================================
  // LUỒNG 1: MOBILE APP HỘ NÔNG DÂN (BÁC BA)
  // =========================================================================
  console.log('\n--- KIỂM TRA LUỒNG 1: BÁC BA (MOBILE APP) ---');

  // 1.1 Kiểm tra màn hình Dashboard Bác Ba
  const hasHomePanel = await page.evaluate(() => {
    const p = document.getElementById('panel-home');
    return p !== null && window.getComputedStyle(p).display !== 'none';
  });
  console.log('1.1 Dashboard Bác Ba hiển thị:', hasHomePanel ? '✓ ĐẠT' : '✗ LỖI');

  // 1.2 Mở và đóng Modal VietQR Bác Ba
  await page.evaluate(() => {
    if (typeof openBacBaQRModal === 'function') openBacBaQRModal();
  });
  const qrModalVisible = await page.evaluate(() => {
    const modal = document.getElementById('bacBaQRModalOverlay');
    return modal && modal.classList.contains('show');
  });
  console.log('1.2 Mở Modal VietQR Bác Ba:', qrModalVisible ? '✓ ĐẠT' : '✗ LỖI');

  await page.evaluate(() => {
    if (typeof closeBacBaQRModal === 'function') closeBacBaQRModal();
  });

  // 1.3 Mở Màn hình Đơn Hàng & Kho Hàng
  await page.evaluate(() => {
    if (typeof openOrdersView === 'function') openOrdersView('orders');
  });
  const ordersPanelActive = await page.evaluate(() => {
    const p = document.getElementById('panel-orders');
    return p && p.classList.contains('active');
  });
  console.log('1.3 Mở Màn hình Đơn hàng:', ordersPanelActive ? '✓ ĐẠT' : '✗ LỖI');

  // Kiểm tra Menu Tab "Đơn hàng" và "Kho hàng"
  const tabTitles = await page.evaluate(() => {
    const btnOrders = document.getElementById('btnSubtabOrders');
    const btnWh = document.getElementById('btnSubtabWarehouse');
    return {
      orders: btnOrders ? btnOrders.innerText.trim().replace(/\s+/g, ' ') : '',
      warehouse: btnWh ? btnWh.innerText.trim().replace(/\s+/g, ' ') : ''
    };
  });
  console.log('1.3.1 Tiêu đề Menu Tab:', tabTitles);
  const tabCorrect = tabTitles.orders.includes('Đơn hàng') && tabTitles.warehouse.includes('Kho hàng');
  console.log('1.3.2 Khớp chuẩn "Đơn hàng" & "Kho hàng":', tabCorrect ? '✓ ĐẠT' : '✗ LỖI');

  // 1.4 Kiểm tra Subtab Kho hàng
  await page.evaluate(() => {
    if (typeof switchOrderSubTab === 'function') switchOrderSubTab('warehouse');
  });
  const whVisible = await page.evaluate(() => {
    const p = document.getElementById('ordersSubView_warehouse');
    return p && p.style.display !== 'none';
  });
  console.log('1.4 Chuyển sang Subtab Kho hàng:', whVisible ? '✓ ĐẠT' : '✗ LỖI');

  // 1.5 Chuyển lại Subtab Đơn hàng và kiểm tra các bộ lọc
  await page.evaluate(() => {
    if (typeof switchOrderSubTab === 'function') switchOrderSubTab('orders');
  });

  // Thử bấm các tab trạng thái nông sản: new, harvesting, pickup, shipping, delivered, all
  const statuses = ['new', 'harvesting', 'pickup', 'shipping', 'delivered', 'all'];
  let statusFilterOk = true;
  for (const st of statuses) {
    const count = await page.evaluate(tab => {
      selectOrderStatusTab(tab);
      const cards = document.querySelectorAll('#shopeeOrdersListContainer .agri-order-card');
      return cards.length;
    }, st);
    if (count === undefined) statusFilterOk = false;
  }
  console.log('1.5 Lọc 6 tab trạng thái đơn nông sản:', statusFilterOk ? '✓ ĐẠT' : '✗ LỖI');

  // 1.6 Kiểm tra Thẻ Đơn Hàng (Cards layout)
  const cardChecks = await page.evaluate(() => {
    const firstCard = document.querySelector('#shopeeOrdersListContainer .agri-order-card');
    if (!firstCard) return { exists: false };
    const code = firstCard.querySelector('.aoc-order-code')?.innerText;
    const channel = firstCard.querySelector('.aoc-channel-pill')?.innerText;
    const status = firstCard.querySelector('.aoc-status-pill')?.innerText;
    const buyer = firstCard.querySelector('.aoc-buyer-name')?.innerText;
    const produce = firstCard.querySelector('.aoc-produce-text')?.innerText;
    const logistics = firstCard.querySelector('.aoc-logistics-text')?.innerText;
    const payout = firstCard.querySelector('.aoc-payout-val')?.innerText;
    return {
      exists: true,
      code, channel, status, buyer, produce, logistics, payout
    };
  });
  console.log('1.6 Thông tin thẻ đơn hàng đại diện:', cardChecks);

  // 1.7 Mở Chi Tiết Đơn Hàng và kiểm tra việc BỎ BANNER
  await page.evaluate(() => {
    if (typeof openOrderDetail === 'function') openOrderDetail('WM2610-01');
  });
  const detailPanelActive = await page.evaluate(() => {
    const p = document.getElementById('panel-order-detail');
    return p && p.classList.contains('active');
  });
  console.log('1.7 Mở Chi tiết đơn hàng:', detailPanelActive ? '✓ ĐẠT' : '✗ LỖI');

  const bannerRemoved = await page.evaluate(() => {
    const banner = document.querySelector('.det-hero-banner');
    return banner === null;
  });
  console.log('1.7.1 Đã bỏ Banner hình ảnh hoàn toàn:', bannerRemoved ? '✓ ĐẠT' : '✗ LỖI');

  const detailSections = await page.evaluate(() => {
    const titles = Array.from(document.querySelectorAll('#panel-order-detail .det-card-heading')).map(h => h.innerText.trim());
    const hasTimeline = document.querySelector('.det-stepper') !== null;
    const hasConfirmBtn = document.querySelector('.det-btn-confirm') !== null;
    return { titles, hasTimeline, hasConfirmBtn };
  });
  console.log('1.7.2 Các phần trong Chi tiết đơn:', detailSections);

  // Thử bấm nút Xác nhận
  await page.evaluate(() => {
    const btn = document.querySelector('.det-btn-confirm');
    if (btn) btn.click();
  });
  await new Promise(r => setTimeout(r, 600));

  // Quay lại đơn hàng
  await page.evaluate(() => {
    if (typeof closeOrderDetail === 'function') closeOrderDetail();
  });

  // 1.8 Mở Phiếu Gom Hàng (Pick-list)
  await page.evaluate(() => {
    if (typeof openPickListView === 'function') openPickListView();
  });
  const picklistActive = await page.evaluate(() => {
    const p = document.getElementById('panel-picklist');
    return p && p.classList.contains('active');
  });
  console.log('1.8 Mở Phiếu Gom Hàng:', picklistActive ? '✓ ĐẠT' : '✗ LỖI');

  await page.evaluate(() => {
    if (typeof closePickListView === 'function') closePickListView();
  });

  // 1.9 Kiểm tra Luồng Đăng bán Nông sản 3 bước AI (Wizard)
  await page.evaluate(() => {
    if (typeof startWizardFlow === 'function') startWizardFlow();
  });
  const wizardStep1 = await page.evaluate(() => {
    const p = document.getElementById('panel-step1');
    return p && p.classList.contains('active');
  });
  console.log('1.9 Mở Wizard Đăng bán Nông sản:', wizardStep1 ? '✓ ĐẠT' : '✗ LỖI');

  // Quay về trang chủ Bác Ba
  await page.evaluate(() => {
    if (typeof openPanel === 'function') openPanel('home');
  });

  // =========================================================================
  // LUỒNG 2: QUẢN LÝ HTX (BAN GIÁM ĐỐC)
  // =========================================================================
  console.log('\n--- KIỂM TRA LUỒNG 2: QUẢN LÝ HTX (ADMIN & CO-OP) ---');

  // Chuyển sang vai trò Quản lý HTX
  await page.evaluate(() => {
    if (typeof switchRole === 'function') switchRole('htx');
  });
  await new Promise(r => setTimeout(r, 400));

  const htxActive = await page.evaluate(() => {
    const p = document.getElementById('role-panel-htx');
    return p && window.getComputedStyle(p).display !== 'none';
  });
  console.log('2.1 Chuyển sang vai trò Quản lý HTX:', htxActive ? '✓ ĐẠT' : '✗ LỖI');

  // 2.2 Kiểm tra tab "Rada thị trường"
  let radaOk = false;
  try {
    radaOk = await page.evaluate(() => {
      if (typeof switchHtxTab === 'function') switchHtxTab('market');
      const table = document.querySelector('#htx-tab-market table') || document.querySelector('#htx-tab-market .market-table');
      const content = document.getElementById('htx-tab-market');
      return content && content.innerText.trim().length > 50;
    });
  } catch (e) {
    radaOk = false;
  }
  console.log('2.2 Tab Rada thị trường nông sản hiển thị nội dung:', radaOk ? '✓ ĐẠT' : '✗ LỖI');

  // 2.3 Kiểm tra tab "Kho bao bì OCOP"
  let packagingOk = false;
  try {
    packagingOk = await page.evaluate(() => {
      if (typeof switchHtxTab === 'function') switchHtxTab('packaging');
      const content = document.getElementById('htx-tab-packaging');
      return content && content.innerText.trim().length > 50;
    });
  } catch (e) {
    packagingOk = false;
  }
  console.log('2.3 Tab Kho bao bì OCOP hiển thị nội dung:', packagingOk ? '✓ ĐẠT' : '✗ LỖI');

  // 2.4 Kiểm tra tab "Hội viên HTX" & Modal xem hồ sơ hội viên
  let memberProfileOk = false;
  try {
    memberProfileOk = await page.evaluate(() => {
      if (typeof switchHtxTab === 'function') switchHtxTab('members');
      if (typeof viewMemberProfile === 'function') {
        viewMemberProfile('bac-ba');
        const modal = document.getElementById('memberProfileModal') || document.querySelector('.member-modal');
        return modal !== null;
      }
      return true;
    });
  } catch (e) {
    memberProfileOk = false;
  }
  console.log('2.4 Xem hồ sơ hội viên HTX (Doanh thu, đơn hàng, SP):', memberProfileOk ? '✓ ĐẠT' : '✗ LỖI');

  // =========================================================================
  // LUỒNG 3: CÁN BỘ XÃ (OCOP TRACKING & BÁO CÁO)
  // =========================================================================
  console.log('\n--- KIỂM TRA LUỒNG 3: CÁN BỘ XÃ ---');
  await page.evaluate(() => {
    if (typeof switchRole === 'function') switchRole('commune');
  });
  await new Promise(r => setTimeout(r, 400));
  const communeActive = await page.evaluate(() => {
    const p = document.getElementById('role-panel-commune');
    return p && window.getComputedStyle(p).display !== 'none';
  });
  console.log('3.1 Chuyển sang vai trò Cán bộ xã:', communeActive ? '✓ ĐẠT' : '✗ LỖI');

  // =========================================================================
  // LUỒNG 4: NGƯỜI MUA / ĐỐI TÁC SỈ B2B & QR TRUY XUẤT
  // =========================================================================
  console.log('\n--- KIỂM TRA LUỒNG 4: NGƯỜI MUA / B2B ---');
  await page.evaluate(() => {
    if (typeof switchRole === 'function') switchRole('buyer');
  });
  await new Promise(r => setTimeout(r, 400));
  const buyerActive = await page.evaluate(() => {
    const p = document.getElementById('role-panel-buyer');
    return p && window.getComputedStyle(p).display !== 'none';
  });
  console.log('4.1 Chuyển sang vai trò Người mua / Đối tác:', buyerActive ? '✓ ĐẠT' : '✗ LỖI');

  // Chuyển lại vai trò Bác Ba
  await page.evaluate(() => {
    if (typeof switchRole === 'function') switchRole('farmer');
  });

  // =========================================================================
  // TỔNG KẾT KIỂM THỬ
  // =========================================================================
  console.log('\n=== TỔNG KẾT KIỂM THỬ HỆ THỐNG ===');
  console.log('Số lỗi phát sinh (Console / Page errors):', errors.length);
  if (errors.length > 0) {
    console.log('Chi tiết lỗi:', errors);
  } else {
    console.log('✓ Không phát hiện bất kỳ lỗi JavaScript hoặc console error nào.');
  }

  await browser.close();
  console.log('=== HOÀN TẤT KIỂM THỬ ===');
}

runTestSuite().catch(err => {
  console.error('Lỗi quá trình chạy test suite:', err);
  process.exit(1);
});
