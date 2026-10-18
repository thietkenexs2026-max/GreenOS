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

  // 1. Screen panel-ancujob
  await page.evaluate(() => openAnCuJobScreen());
  await new Promise(r => setTimeout(r, 300));
  const m1 = await page.evaluate(() => {
    const row = document.querySelector('#panel-ancujob .shopee-btn-row');
    const btns = row.querySelectorAll('button');
    const r1 = btns[0].getBoundingClientRect();
    const r2 = btns[1].getBoundingClientRect();
    return { name: 'Main AnCuJob', hDiff: Math.abs(r1.height - r2.height), topDiff: Math.abs(r1.top - r2.top), h1: r1.height, h2: r2.height };
  });

  // 2. Screen panel-ancujob-post
  await page.evaluate(() => openAnCuJobPostScreen());
  await new Promise(r => setTimeout(r, 300));
  const m2 = await page.evaluate(() => {
    const row = document.querySelector('#panel-ancujob-post .shopee-btn-row');
    const btns = row.querySelectorAll('button');
    const r1 = btns[0].getBoundingClientRect();
    const r2 = btns[1].getBoundingClientRect();
    return { name: 'Post Job', hDiff: Math.abs(r1.height - r2.height), topDiff: Math.abs(r1.top - r2.top), h1: r1.height, h2: r2.height };
  });

  // 3. Screen panel-ancujob-detail
  await page.evaluate(() => openAnCuJobDetailScreen('job-1'));
  await new Promise(r => setTimeout(r, 300));
  const m3 = await page.evaluate(() => {
    const row = document.querySelector('#panel-ancujob-detail .shopee-btn-row');
    const btns = row.querySelectorAll('button');
    const r1 = btns[0].getBoundingClientRect();
    const r2 = btns[1].getBoundingClientRect();
    return { name: 'Detail Job', hDiff: Math.abs(r1.height - r2.height), topDiff: Math.abs(r1.top - r2.top), h1: r1.height, h2: r2.height };
  });

  console.log('Results:', JSON.stringify([m1, m2, m3], null, 2));

  await browser.close();
})();
