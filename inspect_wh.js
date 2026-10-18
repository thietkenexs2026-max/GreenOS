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

  // 1. Click switchNavTab('orders')
  await page.evaluate(() => switchNavTab('orders'));
  await new Promise(r => setTimeout(r, 200));

  // 2. Click subtab warehouse
  await page.evaluate(() => switchOrderSubTab('warehouse'));
  await new Promise(r => setTimeout(r, 200));

  // Take screenshot of warehouse main tab
  await page.screenshot({ path: 'shot_debug_warehouse_tab.png' });
  console.log('Saved shot_debug_warehouse_tab.png');

  // Let's check all visible elements and clicks
  const info = await page.evaluate(() => {
    const kpi = Array.from(document.querySelectorAll('.wh-kpi-card')).map(c => c.innerText.replace(/\n/g, ' '));
    const quick = Array.from(document.querySelectorAll('.wh-quick-action-btn')).map(c => c.innerText.replace(/\n/g, ' '));
    const cards = Array.from(document.querySelectorAll('.wh-product-card')).map(c => {
      const title = c.querySelector('.wh-card-title')?.innerText;
      const btns = Array.from(c.querySelectorAll('button')).map(b => b.innerText);
      return { title, btns };
    });
    return { kpi, quick, cardsCount: cards.length, sampleCard: cards[0] };
  });

  console.log('Warehouse page info:', JSON.stringify(info, null, 2));

  await browser.close();
})();
