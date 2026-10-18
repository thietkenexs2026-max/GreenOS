const puppeteer = require('puppeteer-core');

async function runWarehouseTests() {
  console.log('🚀 Starting Agricultural WMS Automated Verification...');
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  // Capture page console logs and errors
  page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
  page.on('pageerror', err => console.error('BROWSER ERROR:', err.message));

  const viewports = [
    { width: 375, height: 812, name: 'iPhone X / SE (375px)' },
    { width: 390, height: 844, name: 'iPhone 14 / 15 (390px)' },
    { width: 412, height: 915, name: 'Samsung Galaxy / Pixel (412px)' }
  ];

  await page.setViewport(viewports[1]);
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });

  // 1. Switch to orders tab then warehouse subtab
  console.log('\n--- Step 1: Navigating to Warehouse View ---');
  await page.evaluate(() => {
    switchNavTab('orders');
    switchOrderSubTab('warehouse');
  });

  await new Promise(r => setTimeout(r, 600));

  // 2. Check KPI values
  const kpiData = await page.evaluate(() => {
    return {
      items: document.getElementById('whKpiTotalItems')?.textContent,
      qty: document.getElementById('whKpiTotalQty')?.textContent,
      low: document.getElementById('whKpiLowCount')?.textContent,
      val: document.getElementById('whKpiTotalValue')?.textContent,
      displayedCards: document.querySelectorAll('.wh-product-card').length
    };
  });
  console.log('📊 KPI Check:', kpiData);
  if (kpiData.items !== '7' || kpiData.displayedCards !== 7) {
    throw new Error(`Unexpected KPI count: items=${kpiData.items}, cards=${kpiData.displayedCards}`);
  }

  // 3. Test Inbound Modal
  console.log('\n--- Step 2: Testing Inbound Modal (+25 kg) ---');
  await page.evaluate(() => {
    openWarehouseInboundModal('wh_orange');
    document.getElementById('whInboundQty').value = '25';
    document.getElementById('whInboundNote').value = 'Hái đợt chiều tại Nương Đồi Cam';
    submitWarehouseInbound();
  });
  await new Promise(r => setTimeout(r, 400));

  const orangeStock = await page.evaluate(() => {
    const p = BAC_BA_WAREHOUSE_PRODUCTS.find(x => x.id === 'wh_orange');
    const toast = document.querySelector('.toast-container')?.textContent;
    return { stock: p.stock, historyLength: p.history.length, lastNote: p.history[0].note, toast };
  });
  console.log('🍊 Cam Sành after inbound (+25):', orangeStock);
  if (orangeStock.stock !== 375) {
    throw new Error(`Expected orange stock 375, got ${orangeStock.stock}`);
  }

  // 4. Test Outbound Modal
  console.log('\n--- Step 3: Testing Outbound Modal (-15 gói) ---');
  await page.evaluate(() => {
    openWarehouseOutboundModal('wh_banana');
    document.getElementById('whOutboundQty').value = '15';
    document.getElementById('whOutboundNote').value = 'Giao xe tải HTX chuyến chiều';
    submitWarehouseOutbound();
  });
  await new Promise(r => setTimeout(r, 400));

  const bananaStock = await page.evaluate(() => {
    const p = BAC_BA_WAREHOUSE_PRODUCTS.find(x => x.id === 'wh_banana');
    return { stock: p.stock, historyLength: p.history.length, lastNote: p.history[0].note };
  });
  console.log('🍌 Chuối sấy after outbound (-15):', bananaStock);
  if (bananaStock.stock !== 70) {
    throw new Error(`Expected banana stock 70, got ${bananaStock.stock}`);
  }

  // 5. Test Stock Card Modal
  console.log('\n--- Step 4: Testing Stock Card Modal ---');
  await page.evaluate(() => {
    openWarehouseStockCardModal('wh_banana');
  });
  await new Promise(r => setTimeout(r, 400));

  const stockCardInfo = await page.evaluate(() => {
    const modal = document.getElementById('warehouseStockCardModal');
    const isActive = modal?.classList.contains('active');
    const itemsCount = modal?.querySelectorAll('.wh-ledger-item').length;
    return { isActive, itemsCount };
  });
  console.log('📋 Stock Card Ledger:', stockCardInfo);
  if (!stockCardInfo.isActive || stockCardInfo.itemsCount === 0) {
    throw new Error('Stock Card Modal failed to render items');
  }

  await page.evaluate(() => closeWarehouseStockCardModal());
  await new Promise(r => setTimeout(r, 300));

  // 6. Test QR Scanner Simulation
  console.log('\n--- Step 5: Testing QR Code Scanner Simulation ---');
  await page.evaluate(() => {
    openWarehouseQRScanModal();
    simulateWarehouseQRScan('LOT-2026-CS08');
  });
  await new Promise(r => setTimeout(r, 400));

  const qrScanRes = await page.evaluate(() => {
    const resBox = document.getElementById('whQRScanResultBox');
    const isVisible = resBox && resBox.style.display !== 'none';
    const batch = document.getElementById('whQRResultBatch')?.textContent;
    return { isVisible, batch };
  });
  console.log('📷 QR Scan Result:', qrScanRes);
  if (!qrScanRes.isVisible || qrScanRes.batch !== 'LOT-2026-CS08') {
    throw new Error('QR Scanner simulation failed');
  }

  await page.evaluate(() => closeWarehouseQRScanModal());
  await new Promise(r => setTimeout(r, 300));

  // 7. Test Stock Audit Modal
  console.log('\n--- Step 6: Testing Stock Audit Modal ---');
  await page.evaluate(() => {
    openWarehouseStockAuditModal();
    // modify honey actual count from 24 to 26 (+2)
    const honeyInput = document.querySelector('.audit-count-input[data-id="wh_honey"]');
    if (honeyInput) {
      honeyInput.value = '26';
    }
    submitWarehouseStockAudit();
  });
  await new Promise(r => setTimeout(r, 400));

  const honeyAudited = await page.evaluate(() => {
    const p = BAC_BA_WAREHOUSE_PRODUCTS.find(x => x.id === 'wh_honey');
    return { stock: p.stock, lastType: p.history[0].type, lastNote: p.history[0].note };
  });
  console.log('🍯 Mật ong after audit:', honeyAudited);
  if (honeyAudited.stock !== 26 || honeyAudited.lastType !== 'audit') {
    throw new Error('Stock audit reconciliation failed');
  }

  // 8. Test Zero Horizontal Overflow across 3 viewports
  console.log('\n--- Step 7: Testing Viewport Overflow & Shopee Standards ---');
  for (const vp of viewports) {
    await page.setViewport(vp);
    await new Promise(r => setTimeout(r, 200));

    const overflowCheck = await page.evaluate(() => {
      const container = document.querySelector('.screen-container') || document.body;
      const whView = document.getElementById('ordersSubView_warehouse');
      const docW = document.documentElement.clientWidth;
      const scrollW = document.documentElement.scrollWidth;
      const whScrollW = whView ? whView.scrollWidth : 0;
      const whClientW = whView ? whView.clientWidth : 0;
      return {
        docOverflow: scrollW > docW,
        scrollW,
        docW,
        whOverflow: whScrollW > (whClientW + 2) // allowance for subpixel
      };
    });

    console.log(`📱 Viewport ${vp.name}: Doc overflow=${overflowCheck.docOverflow}, Page scrollWidth=${overflowCheck.scrollW}, clientWidth=${overflowCheck.docW}`);
    if (overflowCheck.docOverflow) {
      throw new Error(`Viewport horizontal overflow detected on ${vp.name}!`);
    }
  }

  console.log('\n🎉 ALL WMS AGRICULTURAL TESTS PASSED 100%!');
  await browser.close();
}

runWarehouseTests().catch(err => {
  console.error('❌ Test failed:', err);
  process.exit(1);
});
