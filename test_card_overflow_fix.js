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
  // Test at iPhone SE (375px) - the narrowest modern screen where overflow occurred!
  await page.setViewport({ width: 375, height: 812, deviceScaleFactor: 2 });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle0' });

  await page.evaluate(() => {
    switchNavTab('orders');
    switchOrderSubTab('warehouse');
  });
  await new Promise(r => setTimeout(r, 400));

  // Check card elements and bounds
  const cardData = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.wh-product-card')).slice(0, 2);
    return cards.map(c => {
      const cRect = c.getBoundingClientRect();
      const btns = Array.from(c.querySelectorAll('button')).map(b => {
        const bRect = b.getBoundingClientRect();
        return {
          text: b.innerText.trim(),
          left: bRect.left,
          right: bRect.right,
          isInside: bRect.right <= cRect.right + 1 && bRect.left >= cRect.left - 1
        };
      });
      return {
        cardRight: cRect.right,
        cardWidth: cRect.width,
        btns
      };
    });
  });

  console.log('--- Card Elements Geometry Check on 375px screen ---');
  console.log(JSON.stringify(cardData, null, 2));

  // Scroll to the product cards and take screenshot
  await page.evaluate(() => {
    const firstCard = document.querySelector('.wh-product-card');
    if (firstCard) firstCard.scrollIntoView({ behavior: 'instant', block: 'center' });
  });

  await page.screenshot({ path: 'shot_card_fixed_375px.png' });
  console.log('📸 Captured shot_card_fixed_375px.png');

  // Test click on Sổ xuất nhập link
  await page.evaluate(() => {
    const link = document.querySelector('.wh-product-card .btn-wh-card');
    link.click();
  });
  await new Promise(r => setTimeout(r, 300));
  const isStockCardActive = await page.evaluate(() => {
    return document.getElementById('panel-wh-stockcard')?.classList.contains('active');
  });
  console.log('Click [Sổ xuất nhập] -> Full screen active:', isStockCardActive ? '✓ PASS' : '✗ FAIL');

  await browser.close();
})();
