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

  // 1. Open An Cu Job
  await page.evaluate(() => {
    window.openAnCuJobScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  // 2. Open Dispatch Screen
  await page.evaluate(() => {
    window.openAnCuJobDispatchScreen();
  });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'test_dispatch_screen.png' });

  // 3. Click "⚠️ Báo không liên lạc được" for Chú Bảy Cường
  await page.evaluate(() => {
    window.handleUnreachableWorker('Chú Bảy Cường');
  });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'test_dispatch_after_unreachable.png' });

  // 4. Test Weather Delay action
  await page.evaluate(() => {
    window.handleWeatherDelay();
  });
  await new Promise(r => setTimeout(r, 300));
  await page.screenshot({ path: 'test_dispatch_weather_toast.png' });

  // 5. Test Close Dispatch Screen
  await page.evaluate(() => {
    window.closeAnCuJobDispatchScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  const state = await page.evaluate(() => {
    const pDispatch = document.getElementById('panel-ancujob-dispatch');
    const pAnCu = document.getElementById('panel-ancujob');
    return {
      dispatchActive: pDispatch ? pDispatch.classList.contains('active') : false,
      ancuActive: pAnCu ? pAnCu.classList.contains('active') : false,
    };
  });

  console.log('Dispatch Test State:', JSON.stringify(state, null, 2));
  await browser.close();
})();
