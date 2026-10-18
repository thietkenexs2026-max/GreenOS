const puppeteer = require('puppeteer-core');

async function testWarehouseScreens() {
  console.log('🚀 Testing Full-Screen Transitions for Warehouse (Zero Popup)...');
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  page.on('console', msg => console.log('BROWSER:', msg.text()));
  page.on('pageerror', err => console.error('BROWSER ERROR:', err.message));

  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });

  // 1. Navigate to Warehouse
  await page.evaluate(() => {
    switchNavTab('orders');
    switchOrderSubTab('warehouse');
  });
  await new Promise(r => setTimeout(r, 400));

  // 2. Test Inbound Screen
  console.log('--- Test 1: Inbound Full Screen Transition ---');
  await page.evaluate(() => openWarehouseInboundScreen('wh_orange'));
  await new Promise(r => setTimeout(r, 400));

  const inboundState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-inbound');
    const ordersPanel = document.getElementById('panel-orders');
    const popupsVisible = Array.from(document.querySelectorAll('.dash-qr-modal-overlay')).filter(m => m.classList.contains('active') || m.classList.contains('show')).length;
    return {
      inboundActive: panel?.classList.contains('active'),
      ordersActive: ordersPanel?.classList.contains('active'),
      popupsVisible
    };
  });
  console.log('Inbound Screen State:', inboundState);
  if (!inboundState.inboundActive || inboundState.ordersActive || inboundState.popupsVisible > 0) {
    throw new Error('Inbound screen did not transition cleanly or popup appeared');
  }

  // Submit Inbound (+20 kg)
  await page.evaluate(() => {
    document.getElementById('whInboundQtyScreen').value = '20';
    submitWarehouseInboundScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  const afterInbound = await page.evaluate(() => {
    const ordersPanel = document.getElementById('panel-orders');
    const whOrange = BAC_BA_WAREHOUSE_PRODUCTS.find(p => p.id === 'wh_orange');
    return { ordersActive: ordersPanel?.classList.contains('active'), stock: whOrange?.stock };
  });
  console.log('Returned to Warehouse after Inbound:', afterInbound);
  if (!afterInbound.ordersActive || afterInbound.stock !== 370) {
    throw new Error(`Inbound submit failed or did not return to warehouse: stock=${afterInbound.stock}`);
  }

  // 3. Test Outbound Screen
  console.log('\n--- Test 2: Outbound Full Screen Transition ---');
  await page.evaluate(() => openWarehouseOutboundScreen('wh_banana'));
  await new Promise(r => setTimeout(r, 400));

  const outboundState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-outbound');
    const popupsVisible = Array.from(document.querySelectorAll('.dash-qr-modal-overlay')).filter(m => m.classList.contains('active') || m.classList.contains('show')).length;
    return { outboundActive: panel?.classList.contains('active'), popupsVisible };
  });
  console.log('Outbound Screen State:', outboundState);
  if (!outboundState.outboundActive || outboundState.popupsVisible > 0) {
    throw new Error('Outbound screen failed to open cleanly');
  }

  // Click Back
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // 4. Test Stock Card Screen
  console.log('\n--- Test 3: Stock Card Full Screen Transition ---');
  await page.evaluate(() => openWarehouseStockCardScreen('wh_banana'));
  await new Promise(r => setTimeout(r, 400));

  const stockCardState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-stockcard');
    const itemsCount = panel?.querySelectorAll('.wh-ledger-item').length;
    return { stockCardActive: panel?.classList.contains('active'), itemsCount };
  });
  console.log('Stock Card Screen State:', stockCardState);
  if (!stockCardState.stockCardActive || stockCardState.itemsCount === 0) {
    throw new Error('Stock card screen failed to display items');
  }

  // Click Back
  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // 5. Test QR Scanner Screen & Sub-Navigation
  console.log('\n--- Test 4: QR Scanner Full Screen & Sub-Navigation ---');
  await page.evaluate(() => openWarehouseScannerScreen());
  await new Promise(r => setTimeout(r, 400));

  const scannerState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-scanner');
    return { scannerActive: panel?.classList.contains('active') };
  });
  console.log('Scanner Screen State:', scannerState);
  if (!scannerState.scannerActive) {
    throw new Error('Scanner screen failed to activate');
  }

  // Simulate scan and click "Nhập thêm lô này"
  await page.evaluate(() => {
    simulateWarehouseQRScanScreen('LOT-2026-CS08');
    const btnIn = document.getElementById('btnWhQRInScreen');
    if (btnIn) btnIn.click();
  });
  await new Promise(r => setTimeout(r, 400));

  const fromScannerToInbound = await page.evaluate(() => {
    const inboundPanel = document.getElementById('panel-wh-inbound');
    const curVal = document.getElementById('whInboundProductSelectScreen')?.value;
    return { inboundActive: inboundPanel?.classList.contains('active'), curVal };
  });
  console.log('Navigation from Scanner to Inbound:', fromScannerToInbound);
  if (!fromScannerToInbound.inboundActive || fromScannerToInbound.curVal !== 'wh_banana') {
    throw new Error('Scanner sub-navigation to Inbound failed');
  }

  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // 6. Test Stock Audit Screen
  console.log('\n--- Test 5: Stock Audit Full Screen Transition ---');
  await page.evaluate(() => openWarehouseAuditScreen());
  await new Promise(r => setTimeout(r, 400));

  const auditState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-audit');
    const rowCount = panel?.querySelectorAll('.audit-screen-input').length;
    return { auditActive: panel?.classList.contains('active'), rowCount };
  });
  console.log('Audit Screen State:', auditState);
  if (!auditState.auditActive || auditState.rowCount !== 7) {
    throw new Error('Audit screen failed to display 7 items');
  }

  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // 7. Test Adjust Screen
  console.log('\n--- Test 6: Adjust Full Screen Transition ---');
  await page.evaluate(() => openWarehouseAdjustScreen('wh_tea'));
  await new Promise(r => setTimeout(r, 400));

  const adjustState = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-adjust');
    const nameVal = document.getElementById('whAdjustNameScreen')?.value;
    return { adjustActive: panel?.classList.contains('active'), nameVal };
  });
  console.log('Adjust Screen State:', adjustState);
  if (!adjustState.adjustActive || !adjustState.nameVal.includes('Trà Bát Tiên')) {
    throw new Error('Adjust screen failed to load product');
  }

  await page.evaluate(() => closeWarehouseScreens());
  await new Promise(r => setTimeout(r, 300));

  // 8. Test Viewport Overflow on all screens (375px, 390px, 412px)
  console.log('\n--- Test 7: Viewport Horizontal Overflow Check on All 6 Screens ---');
  const screens = [
    { name: 'Warehouse Main', open: () => closeWarehouseScreens() },
    { name: 'Inbound Screen', open: () => openWarehouseInboundScreen('wh_banana') },
    { name: 'Outbound Screen', open: () => openWarehouseOutboundScreen('wh_banana') },
    { name: 'Stock Card Screen', open: () => openWarehouseStockCardScreen('wh_banana') },
    { name: 'Scanner Screen', open: () => openWarehouseScannerScreen() },
    { name: 'Audit Screen', open: () => openWarehouseAuditScreen() },
    { name: 'Adjust Screen', open: () => openWarehouseAdjustScreen('wh_banana') }
  ];

  const viewports = [
    { width: 375, height: 812, name: '375px' },
    { width: 390, height: 844, name: '390px' },
    { width: 412, height: 915, name: '412px' }
  ];

  for (const s of screens) {
    for (const vp of viewports) {
      await page.setViewport(vp);
      await page.evaluate(s.open);
      await new Promise(r => setTimeout(r, 150));

      const overflow = await page.evaluate(() => {
        return {
          scrollW: document.documentElement.scrollWidth,
          clientW: document.documentElement.clientWidth,
          isOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth
        };
      });

      if (overflow.isOverflow) {
        throw new Error(`Screen [${s.name}] overflowed on viewport [${vp.name}]: scrollWidth=${overflow.scrollW}, clientWidth=${overflow.clientW}`);
      }
    }
    console.log(`✓ Screen [${s.name}]: 0 overflow across 375px, 390px, 412px`);
  }

  console.log('\n🎉 ALL WMS FULL-SCREEN TRANSITIONS PASSED 100% WITH ZERO POPUPS!');
  await browser.close();
}

testWarehouseScreens().catch(err => {
  console.error('❌ Test failed:', err);
  process.exit(1);
});
