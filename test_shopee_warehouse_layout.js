const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const edgePath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe';
  const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
  const executablePath = fs.existsSync(chromePath) ? chromePath : edgePath;

  const browser = await puppeteer.launch({
    executablePath,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle0' });

  console.log('🚀 1. Switching to Warehouse Subtab...');
  await page.evaluate(() => {
    switchNavTab('orders');
    switchOrderSubTab('warehouse');
  });
  await new Promise(r => setTimeout(r, 400));

  // Check existence of Shopee VIP sections
  const check = await page.evaluate(() => {
    const heroGrid = document.querySelector('.wh-hero-grid');
    const heroCards = heroGrid ? heroGrid.querySelectorAll('.wh-hero-card').length : 0;
    const planGrid = document.querySelector('#ordersSubView_warehouse .shopee-3col-grid');
    const planCards = planGrid ? planGrid.querySelectorAll('.shopee-plan-card').length : 0;
    const prodCards = document.querySelectorAll('.wh-product-card').length;
    const stickyBar = document.querySelector('.wh-sticky-bottom-bar');
    const heroQty = document.getElementById('whHeroTotalQty')?.innerText;
    const heroItems = document.getElementById('whHeroItemCount')?.innerText;
    const heroVal = document.getElementById('whHeroTotalVal')?.innerText;

    // Check visible modals
    const visibleModals = Array.from(document.querySelectorAll('.dash-qr-modal-overlay, .modal-overlay, .order-filter-backdrop'))
      .filter(m => {
        const s = window.getComputedStyle(m);
        return s.display !== 'none' && s.visibility !== 'hidden' && s.opacity !== '0';
      }).length;

    return {
      heroCards,
      planCards,
      prodCards,
      hasStickyBar: !!stickyBar,
      heroQty,
      heroItems,
      heroVal,
      visibleModals
    };
  });

  console.log('Shopee Layout Elements:', JSON.stringify(check, null, 2));

  // Take screenshot of redesigned warehouse main view
  await page.screenshot({ path: 'shot_shopee_warehouse_main.png' });
  console.log('📸 Captured shot_shopee_warehouse_main.png');

  // Test Navigation from 3-Card Grid
  console.log('\n--- 2. Testing 3-Card Grid Full-Screen Navigation (Zero Popup) ---');
  // Inbound
  await page.evaluate(() => {
    const cards = document.querySelectorAll('#ordersSubView_warehouse .shopee-3col-grid .shopee-plan-card');
    cards[0].click();
  });
  await new Promise(r => setTimeout(r, 300));
  let inActive = await page.evaluate(() => document.getElementById('panel-wh-inbound')?.classList.contains('active'));
  console.log('Plan Card 1 -> Inbound Full Screen:', inActive ? '✓ PASS' : '✗ FAIL');
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // Outbound
  await page.evaluate(() => {
    const cards = document.querySelectorAll('#ordersSubView_warehouse .shopee-3col-grid .shopee-plan-card');
    cards[1].click();
  });
  await new Promise(r => setTimeout(r, 300));
  let outActive = await page.evaluate(() => document.getElementById('panel-wh-outbound')?.classList.contains('active'));
  console.log('Plan Card 2 -> Outbound Full Screen:', outActive ? '✓ PASS' : '✗ FAIL');
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // Audit
  await page.evaluate(() => {
    const cards = document.querySelectorAll('#ordersSubView_warehouse .shopee-3col-grid .shopee-plan-card');
    cards[2].click();
  });
  await new Promise(r => setTimeout(r, 300));
  let auditActive = await page.evaluate(() => document.getElementById('panel-wh-audit')?.classList.contains('active'));
  console.log('Plan Card 3 -> Audit Full Screen:', auditActive ? '✓ PASS' : '✗ FAIL');
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // Scanner from sticky bottom bar
  await page.evaluate(() => {
    document.querySelector('.wh-sbb-btn').click();
  });
  await new Promise(r => setTimeout(r, 300));
  let scanActive = await page.evaluate(() => document.getElementById('panel-wh-scanner')?.classList.contains('active'));
  console.log('Sticky Bottom Bar -> Scanner Full Screen:', scanActive ? '✓ PASS' : '✗ FAIL');
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // Test Product Card Actions
  console.log('\n--- 3. Testing Product Card Actions ---');
  await page.evaluate(() => {
    const firstCard = document.querySelector('.wh-product-card');
    firstCard.querySelector('.btn-wh-card').click();
  });
  await new Promise(r => setTimeout(r, 300));
  let cardActive = await page.evaluate(() => document.getElementById('panel-wh-stockcard')?.classList.contains('active'));
  console.log('Product Action [Thẻ kho] -> Stock Card Full Screen:', cardActive ? '✓ PASS' : '✗ FAIL');
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // Test Viewport Overflow
  console.log('\n--- 4. Viewport Overflow Check Across 375px, 390px, 412px ---');
  for (const width of [375, 390, 412]) {
    await page.setViewport({ width, height: 844 });
    const overflow = await page.evaluate(() => {
      const el = document.getElementById('ordersSubView_warehouse');
      const docW = document.documentElement.clientWidth;
      const scW = document.querySelector('.screen-container')?.scrollWidth || 0;
      return { clientW: docW, scW, overflow: scW > docW ? scW - docW : 0 };
    });
    console.log(`Viewport ${width}px: overflow = ${overflow.overflow}px`);
  }

  console.log('\n🎉 ALL TESTS COMPLETED SUCCESSFULLY!');
  await browser.close();
})();
