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

  // 1. Go to Warehouse tab
  await page.evaluate(() => {
    switchNavTab('orders');
    switchOrderSubTab('warehouse');
  });
  await new Promise(r => setTimeout(r, 400));

  // Check buttons on warehouse product cards
  const cardsCheck = await page.evaluate(() => {
    const cards = document.querySelectorAll('.wh-product-card');
    let totalCardBtns = 0;
    cards.forEach(c => {
      totalCardBtns += c.querySelectorAll('button').length;
    });
    return {
      cardCount: cards.length,
      totalCardBtns
    };
  });

  console.log('--- 1. Warehouse List Cards Check ---');
  console.log('Cards count:', cardsCheck.cardCount);
  console.log('Buttons on outside cards (should be 0):', cardsCheck.totalCardBtns);

  await page.screenshot({ path: 'shot_clean_warehouse_list.png' });
  console.log('📸 Captured shot_clean_warehouse_list.png');

  // 2. Click first product card
  console.log('\n--- 2. Tapping on first product card ---');
  await page.evaluate(() => {
    const firstCard = document.querySelector('.wh-product-card');
    firstCard.click();
  });
  await new Promise(r => setTimeout(r, 400));

  const adjustCheck = await page.evaluate(() => {
    const panel = document.getElementById('panel-wh-adjust');
    const isActive = panel?.classList.contains('active');
    const heroTitle = panel?.querySelector('#whAdjustProductHero h2')?.innerText;
    const nameVal = document.getElementById('whAdjustNameScreen')?.value;
    const stockVal = document.getElementById('whAdjustStockScreen')?.value;
    const priceVal = document.getElementById('whAdjustPriceScreen')?.value;
    const locVal = document.getElementById('whAdjustLocationScreen')?.value;
    const expiryVal = document.getElementById('whAdjustExpiryScreen')?.value;
    const historyCount = panel?.querySelectorAll('#whAdjustHistoryList > div > div')?.length || 0;

    return {
      isActive,
      heroTitle,
      nameVal,
      stockVal,
      priceVal,
      locVal,
      expiryVal,
      historyCount
    };
  });

  console.log('All-in-One Product Screen State:');
  console.log(JSON.stringify(adjustCheck, null, 2));

  await page.screenshot({ path: 'shot_all_in_one_product_screen.png' });
  console.log('📸 Captured shot_all_in_one_product_screen.png');

  // 3. Test Save action
  console.log('\n--- 3. Testing Save Action ---');
  await page.evaluate(() => {
    document.getElementById('whAdjustStockScreen').value = '380';
    submitWarehouseAdjustScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  const afterSave = await page.evaluate(() => {
    const isOrdersActive = document.getElementById('panel-orders')?.classList.contains('active');
    const firstCardText = document.querySelector('.wh-product-card')?.innerText;
    return {
      isOrdersActive,
      hasUpdatedStock: firstCardText.includes('380')
    };
  });

  console.log('After Save State:', JSON.stringify(afterSave, null, 2));

  await browser.close();
})();
