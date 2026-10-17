const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const urls = [
    { name: 'step1', url: 'https://gvos.greenfi.vn/chao-mung?tu=%2F' },
    { name: 'step2', url: 'https://gvos.greenfi.vn/chao-mung?tu=%2F&buoc=2' },
    { name: 'step3', url: 'https://gvos.greenfi.vn/chao-mung?tu=%2F&buoc=3' },
    { name: 'step4', url: 'https://gvos.greenfi.vn/chao-mung?tu=%2F&buoc=4' },
    { name: 'dangnhap', url: 'https://gvos.greenfi.vn/dang-nhap?tu=%2F' }
  ];

  const results = {};

  for (const item of urls) {
    const page = await browser.newPage();
    await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
    console.log(`Navigating to ${item.name}: ${item.url}`);
    try {
      await page.goto(item.url, { waitUntil: 'networkidle2', timeout: 30000 });
      await new Promise(r => setTimeout(r, 2000));
      
      const screenshotPath = `gvos_${item.name}.png`;
      await page.screenshot({ path: screenshotPath, fullPage: false });
      
      const pageData = await page.evaluate(() => {
        return {
          title: document.title,
          innerText: document.body.innerText,
          html: document.getElementById('root') ? document.getElementById('root').innerHTML : document.body.innerHTML
        };
      });

      results[item.name] = pageData;
      console.log(`Captured ${item.name} (${pageData.innerText.length} chars)`);
    } catch (e) {
      console.error(`Error on ${item.name}:`, e.message);
    }
    await page.close();
  }

  fs.writeFileSync('gvos_pages_data.json', JSON.stringify(results, null, 2), 'utf-8');
  console.log('Saved all data to gvos_pages_data.json');

  await browser.close();
})();
