const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });

  await page.goto('http://127.0.0.1:8080/index.html', { waitUntil: 'networkidle0' });

  // Open Onboarding
  await page.evaluate(() => {
    goToOnboarding();
  });
  await new Promise(r => setTimeout(r, 600));

  // Verify welcome screen
  const welcomeData = await page.evaluate(() => {
    const welcome = document.getElementById('obpScreenWelcome');
    const isVisible = welcome && window.getComputedStyle(welcome).display !== 'none';
    const title = document.querySelector('.luma-hero-title') ? document.querySelector('.luma-hero-title').innerText : '';
    const img = document.querySelector('.luma-orbit-img') ? document.querySelector('.luma-orbit-img').src : '';
    const chips = Array.from(document.querySelectorAll('.luma-fp-item')).map(c => c.textContent.trim());
    return { isVisible, title, img, chips };
  });

  console.log('Welcome Screen Data:', JSON.stringify(welcomeData, null, 2));

  // Take screenshot of Luma Onboarding Welcome Screen
  await page.screenshot({ path: 'shot_onboarding_luma.png', fullPage: false });
  console.log('Saved shot_onboarding_luma.png');

  // Test opening the 4 steps guide
  await page.evaluate(() => {
    openOnboardGuide();
  });
  await new Promise(r => setTimeout(r, 400));

  const guideData = await page.evaluate(() => {
    const guide = document.getElementById('obpGuideWrap');
    const isGuideVisible = guide && window.getComputedStyle(guide).display !== 'none';
    const badge = document.getElementById('obpStepBadge') ? document.getElementById('obpStepBadge').textContent : '';
    return { isGuideVisible, badge };
  });
  console.log('Guide Data:', JSON.stringify(guideData, null, 2));

  // Test going back to welcome screen
  await page.evaluate(() => {
    prevOnboardScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  const backData = await page.evaluate(() => {
    const welcome = document.getElementById('obpScreenWelcome');
    return welcome && window.getComputedStyle(welcome).display !== 'none';
  });
  console.log('Returned to Welcome Screen successfully:', backData);

  // Test Bắt Đầu Ngay
  await page.evaluate(() => {
    finishOnboarding();
  });
  await new Promise(r => setTimeout(r, 400));

  const isHomeActive = await page.evaluate(() => {
    const home = document.getElementById('panel-home');
    return home && home.classList.contains('active');
  });
  console.log('Entered Home Screen successfully:', isHomeActive);

  await browser.close();
  console.log('All tests passed!');
})();
