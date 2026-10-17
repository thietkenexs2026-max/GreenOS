const puppeteer = require('puppeteer-core');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  for (const w of [375, 390, 412]) {
    await page.setViewport({ width: w, height: 844, isMobile: true });
    await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle0' });
    await page.evaluate(() => {
      window.openAnCuJobDispatchScreen();
    });
    await new Promise(r => setTimeout(r, 400));
    
    // Also trigger handleUnreachableWorker to test the error state layout
    const bugs = await page.evaluate((width) => {
      const issues = [];
      const panel = document.getElementById('panel-ancujob-dispatch');
      if (!panel) return ['Panel not found'];
      
      const elements = Array.from(panel.querySelectorAll('*'));
      elements.forEach(el => {
        const r = el.getBoundingClientRect();
        const s = window.getComputedStyle(el);
        
        // 1. Check overflow right
        if (r.right > width + 1 && s.overflow !== 'hidden' && s.overflowX !== 'auto' && !el.closest('.ecom-cat-chips')) {
          issues.push({
            tag: el.tagName,
            class: el.className,
            text: el.innerText ? el.innerText.trim().slice(0, 30) : '',
            right: r.right,
            width,
            issue: 'OVERFLOW_RIGHT'
          });
        }
        
        // 2. Check buttons wrapping & styling
        if (el.tagName === 'BUTTON') {
          if (s.whiteSpace !== 'nowrap') {
            issues.push({
              tag: 'BUTTON',
              text: el.innerText ? el.innerText.trim().slice(0, 30) : '',
              issue: 'BUTTON_NO_NOWRAP',
              whiteSpace: s.whiteSpace
            });
          }
          if (r.width > width) {
            issues.push({
              tag: 'BUTTON',
              text: el.innerText ? el.innerText.trim().slice(0, 30) : '',
              issue: 'BUTTON_WIDER_THAN_VIEWPORT',
              btnWidth: r.width,
              width
            });
          }
        }
      });
      return issues;
    }, w);
    
    console.log(`=== Viewport ${w}px ===`);
    console.log(JSON.stringify(bugs, null, 2));
    await page.screenshot({ path: `audit_dispatch_${w}.png` });

    // Test after clicking handleUnreachableWorker
    await page.evaluate(() => {
      window.handleUnreachableWorker('Chú Bảy Cường');
    });
    await new Promise(r => setTimeout(r, 300));
    await page.screenshot({ path: `audit_dispatch_${w}_unreachable.png` });

    const bugsAfter = await page.evaluate((width) => {
      const issues = [];
      const panel = document.getElementById('panel-ancujob-dispatch');
      const elements = Array.from(panel.querySelectorAll('*'));
      elements.forEach(el => {
        const r = el.getBoundingClientRect();
        const s = window.getComputedStyle(el);
        if (r.right > width + 1 && s.overflow !== 'hidden' && s.overflowX !== 'auto' && !el.closest('.ecom-cat-chips')) {
          issues.push({
            tag: el.tagName,
            class: el.className,
            text: el.innerText ? el.innerText.trim().slice(0, 30) : '',
            right: r.right,
            width,
            issue: 'OVERFLOW_RIGHT'
          });
        }
        if (el.tagName === 'BUTTON') {
          if (s.whiteSpace !== 'nowrap') {
            issues.push({
              tag: 'BUTTON',
              text: el.innerText ? el.innerText.trim().slice(0, 30) : '',
              issue: 'BUTTON_NO_NOWRAP',
              whiteSpace: s.whiteSpace
            });
          }
        }
      });
      return issues;
    }, w);
    console.log(`=== Viewport ${w}px After Unreachable ===`);
    console.log(JSON.stringify(bugsAfter, null, 2));
  }
  await browser.close();
})();
