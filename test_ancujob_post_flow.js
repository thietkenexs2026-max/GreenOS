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
    if (window.openAnCuJobScreen) window.openAnCuJobScreen();
  });
  await new Promise(r => setTimeout(r, 400));

  // 2. Click "➕ Đăng tin tuyển"
  await page.evaluate(() => {
    if (window.openAnCuJobPostScreen) window.openAnCuJobPostScreen();
  });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: 'test_post_screen_initial.png' });

  // 3. Test Custom Benefit input: "Biếu thêm 5kg cam mang về"
  await page.evaluate(() => {
    const input = document.getElementById('ancuCustomBenefitInput');
    if (input) {
      input.value = 'Biếu thêm 5kg cam mang về';
      window.addCustomBenefit();
    }
    // Increment worker count to 4
    window.adjustWorkerCount(1);
  });
  await new Promise(r => setTimeout(r, 300));
  await page.screenshot({ path: 'test_post_screen_custom_benefit.png' });

  // 4. Test Submit Job Post
  await page.evaluate(() => {
    window.submitAnCuJobPost();
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_after_post_submitted.png' });

  // 5. Check LocalStorage and DOM
  const result = await page.evaluate(() => {
    const saved = localStorage.getItem('gvos_ancujob_posts');
    const panelAnCu = document.getElementById('panel-ancujob');
    const firstJob = document.querySelector('#ancuJobListContainer .ancu-job-item');
    return {
      panelAnCuActive: panelAnCu ? panelAnCu.classList.contains('active') : false,
      hasSavedStorage: !!saved,
      savedCount: saved ? JSON.parse(saved).length : 0,
      firstJobText: firstJob ? firstJob.innerText.slice(0, 100) : ''
    };
  });

  console.log('Test Result:', JSON.stringify(result, null, 2));
  await browser.close();
})();
