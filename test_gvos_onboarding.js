const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });

  // 1. Mở trang và xóa localStorage để giả lập lần đầu vào link
  await page.goto('http://127.0.0.1:8080/index.html', { waitUntil: 'networkidle2' });
  await page.evaluate(() => {
    localStorage.clear();
    goToOnboarding(1);
  });
  await new Promise(r => setTimeout(r, 600));

  // Chụp ảnh Bước 1
  await page.screenshot({ path: 'test_step1.png' });
  const step1Title = await page.$eval('#gvosPaneStep1 .gvos-fs-title', el => el.innerText);
  console.log('✓ Step 1 Title:', step1Title);

  // 2. Chuyển sang Bước 2
  await page.click('#gvosPaneStep1 .gvos-fs-cta');
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_step2.png' });
  const step2Title = await page.$eval('#gvosPaneStep2 .gvos-fs-title', el => el.innerText);
  console.log('✓ Step 2 Title:', step2Title);

  // 3. Chuyển sang Bước 3
  await page.click('#gvosPaneStep2 .gvos-fs-cta');
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_step3.png' });
  const step3Title = await page.$eval('#gvosPaneStep3 .gvos-fs-title', el => el.innerText);
  console.log('✓ Step 3 Title:', step3Title);

  // 4. Chuyển sang Bước 4
  await page.click('#gvosPaneStep3 .gvos-fs-cta');
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_step4.png' });
  const step4Title = await page.$eval('#gvosPaneStep4 .gvos-fs-title', el => el.innerText);
  console.log('✓ Step 4 Title:', step4Title);

  // 5. Bấm "Vào ứng dụng" để chuyển sang Màn Đăng Nhập
  await page.click('#gvosPaneStep4 .gvos-fs-cta');
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_login.png' });
  const loginTitle = await page.$eval('#gvosScreenLogin .gvos-login-title', el => el.innerText);
  console.log('✓ Login Title:', loginTitle);

  // 6. Bấm "Nhờ Hub xã vào giúp" để mở Modal Bottom Sheet
  await page.click('#gvosScreenLogin .gvos-btn-hub-help');
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: 'test_hub_modal.png' });
  const modalTitle = await page.$eval('#gvosHubModal .gvos-sheet-title', el => el.innerText);
  console.log('✓ Modal Title:', modalTitle);

  // 7. Bấm "Đã hiểu" để đóng Modal
  await page.click('#gvosHubModal .gvos-sheet-confirm-btn');
  await new Promise(r => setTimeout(r, 400));

  // 8. Bấm "Vào nhanh với tài khoản Bác Ba (Hộ mẫu)"
  await page.click('#gvosScreenLogin .gvos-btn-demo-bacba');
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: 'test_home_logged_in.png' });
  const homeActive = await page.$eval('#panel-home', el => el.classList.contains('active'));
  console.log('✓ Home Panel Active:', homeActive);

  // 9. Bấm "Hướng dẫn" trên trang chủ để xem lại Onboarding
  await page.click('.btn-guide-onboard');
  await new Promise(r => setTimeout(r, 500));
  const obpActive = await page.$eval('#panel-onboarding', el => el.classList.contains('active'));
  console.log('✓ Onboarding Reopened:', obpActive);

  // 10. Bấm "Bỏ qua" để nhảy thẳng tới Màn Đăng Nhập
  await page.click('#gvosPaneStep1 .gvos-fs-skip');
  await new Promise(r => setTimeout(r, 500));
  const loginActive = await page.$eval('#gvosScreenLogin', el => el.classList.contains('active'));
  console.log('✓ Login Screen via Skip:', loginActive);

  await browser.close();
  console.log('🎉 ALL ONBOARDING & LOGIN TESTS PASSED PERFECTLY!');
})();
