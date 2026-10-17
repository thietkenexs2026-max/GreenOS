const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 420, height: 920, deviceScaleFactor: 2 });
  
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 800));

  // Scroll directly into the 3 cards view inside screen-container
  await page.evaluate(() => {
    const el = document.querySelector('.home-unified-market-publish-section');
    if (el) {
      el.scrollIntoView({ behavior: 'instant', block: 'center' });
    }
  });
  await new Promise(r => setTimeout(r, 400));

  // Screenshot showing the 3 navigation cards
  await page.screenshot({ path: path.join(__dirname, 'shot_3cards_nav.png'), fullPage: false });
  console.log('Saved shot_3cards_nav.png');

  // Open the An Cư Job modal and screenshot
  await page.evaluate(() => {
    if (typeof openAnCuJobModal === 'function') openAnCuJobModal();
  });
  await new Promise(r => setTimeout(r, 500));

  await page.screenshot({ path: path.join(__dirname, 'shot_ancujob_modal.png'), fullPage: false });
  console.log('Saved shot_ancujob_modal.png');

  await browser.close();
  console.log('Finished capturing!');
})();
