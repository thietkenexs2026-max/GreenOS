const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true });
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle0' });

  // 1. Screenshot Home Banner & 3-card section
  await page.screenshot({ path: 'test_home_banner.png' });

  // 2. Click An Cu Job
  const clicked = await page.evaluate(() => {
    const el = document.querySelector('[onclick*="openAnCuJob"]');
    if (el) {
      el.click();
      return true;
    }
    return false;
  });

  await new Promise(r => setTimeout(r, 600));

  // 3. Screenshot An Cu Job full screen
  await page.screenshot({ path: 'test_ancujob_screen.png' });

  // 4. Test Category Filter
  await page.evaluate(() => {
    const chips = document.querySelectorAll('#panel-ancujob .ecom-chip-item');
    if (chips.length > 1) chips[1].click(); // click second chip
  });
  await new Promise(r => setTimeout(r, 300));
  await page.screenshot({ path: 'test_ancujob_filtered.png' });

  // 5. Test Return to Home
  await page.evaluate(() => {
    const backBtn = document.querySelector('#panel-ancujob button[onclick*="closeAnCuJobScreen"]');
    if (backBtn) backBtn.click();
  });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'test_after_back.png' });

  const state = await page.evaluate((clickedVal) => {
    const modal = document.getElementById('anCuJobModal');
    const panelAnCu = document.getElementById('panel-ancujob');
    const panelHome = document.getElementById('panel-home');
    return {
      clicked: clickedVal,
      modalExists: !!modal,
      panelAnCuActive: panelAnCu ? panelAnCu.classList.contains('active') : false,
      panelHomeActive: panelHome ? panelHome.classList.contains('active') : false,
    };
  }, clicked);

  console.log('Verification state:', JSON.stringify(state, null, 2));
  await browser.close();
})();
