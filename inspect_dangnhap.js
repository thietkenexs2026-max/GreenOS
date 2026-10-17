const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });

  await page.goto('https://gvos.greenfi.vn/chao-mung?tu=%2F&buoc=4', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));

  // Click button "Vào ứng dụng"
  console.log('Clicking Vào ứng dụng...');
  await page.evaluate(() => {
    const btns = Array.from(document.querySelectorAll('button'));
    const btn = btns.find(b => b.textContent.includes('Vào ứng dụng'));
    if (btn) btn.click();
  });

  await new Promise(r => setTimeout(r, 3000));
  console.log('Current URL after click:', page.url());

  // Screenshot
  await page.screenshot({ path: 'gvos_after_step4.png', fullPage: false });

  const pageText = await page.evaluate(() => document.body.innerText);
  console.log('Page text length:', pageText.length);
  require('fs').writeFileSync('gvos_dangnhap_text.txt', pageText, 'utf-8');

  // Let's also check if there is a button "Nhờ Hub xã vào hồ sơ hộ" or similar
  const buttons = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('button, a')).map(el => el.textContent.trim());
  });
  console.log('Buttons/Links found:', buttons);

  // If there is "Nhờ Hub xã", click it
  await page.evaluate(() => {
    const el = Array.from(document.querySelectorAll('button, a')).find(b => b.textContent.includes('Hub xã'));
    if (el) el.click();
  });
  await new Promise(r => setTimeout(r, 1500));
  await page.screenshot({ path: 'gvos_hub_modal.png', fullPage: false });

  await browser.close();
})();
