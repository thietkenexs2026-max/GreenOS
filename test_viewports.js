const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  // Test across multiple mobile viewports: 375 (iPhone SE/mini), 390 (iPhone 13/14), 412 (Android/Pixel)
  const viewports = [
    { width: 375, height: 812, name: 'iPhone_375' },
    { width: 390, height: 844, name: 'iPhone_390' },
    { width: 412, height: 915, name: 'Android_412' }
  ];

  const screens = [
    { name: '01_Trang_Chu', action: () => window.switchNavTab && window.switchNavTab('home') },
    { name: '02_Wizard_Step1', action: () => window.startWizardFlow && window.startWizardFlow() },
    { name: '03_Wizard_Step2', action: () => window.goToStep && window.goToStep(2) },
    { name: '04_Wizard_Step3', action: () => window.goToStep && window.goToStep(3) },
    { name: '05_Cho_Xanh_MyStore', action: () => { window.switchNavTab && window.switchNavTab('market'); window.switchMarketSubTab && window.switchMarketSubTab('myStore'); } },
    { name: '05_Cho_Xanh_Explore', action: () => { window.switchNavTab && window.switchNavTab('market'); window.switchMarketSubTab && window.switchMarketSubTab('explore'); } },
    { name: '06_Chi_Tiet_San_Pham', action: () => { if (typeof openProductDetailModal === 'function') openProductDetailModal(1); } },
    { name: '07_Don_Hang', action: () => window.switchNavTab && window.switchNavTab('orders') },
    { name: '08_Chi_Tiet_Don_Hang', action: () => { if (typeof BAC_BA_ORDERS !== 'undefined' && BAC_BA_ORDERS.length) openOrderDetail(BAC_BA_ORDERS[0].id); } },
    { name: '09_Soan_Hang_Picklist', action: () => window.openPickListView && window.openPickListView() },
    { name: '10_Bao_Cao_Thong_Ke', action: () => window.switchNavTab && window.switchNavTab('dashboard') },
    { name: '11_Tai_Khoan', action: () => window.switchNavTab && window.switchNavTab('account') },
    { name: '14_Modal_AnCuJob', action: () => window.openAnCuJobModal && window.openAnCuJobModal() }
  ];

  const allProblems = [];

  for (const vp of viewports) {
    await page.setViewport({ width: vp.width, height: vp.height, deviceScaleFactor: 2 });
    await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });
    await new Promise(r => setTimeout(r, 400));

    for (const sc of screens) {
      await page.evaluate(sc.action);
      await new Promise(r => setTimeout(r, 300));

      const screenBugs = await page.evaluate((vpName, scName, screenW) => {
        const bugs = [];
        const bodyW = document.body.clientWidth;

        // Helper: get visible elements
        function isVisible(el) {
          const s = window.getComputedStyle(el);
          if (s.display === 'none' || s.visibility === 'hidden' || s.opacity === '0') return false;
          const r = el.getBoundingClientRect();
          return r.width > 0 && r.height > 0;
        }

        // 1. Check ALL buttons
        const buttons = Array.from(document.querySelectorAll('button, .btn, [role="button"], input[type="button"], input[type="submit"]')).filter(isVisible);
        buttons.forEach(btn => {
          const r = btn.getBoundingClientRect();
          const s = window.getComputedStyle(btn);
          const text = btn.innerText.trim().replace(/\s+/g, ' ');

          // Check if button text wraps awkwardly when it shouldn't
          // If button is a single-action button (not a multi-row card) and has height > 48px or has multiple lines of text
          const isCardLike = btn.className.includes('card') || btn.className.includes('item') || btn.className.includes('tile');
          if (!isCardLike && text.length > 0 && text.length < 35) {
            // Check if text has wrapped into multiple lines
            const range = document.createRange();
            if (btn.childNodes.length === 1 && btn.childNodes[0].nodeType === Node.TEXT_NODE) {
              range.selectNodeContents(btn.childNodes[0]);
              const tRect = range.getBoundingClientRect();
              if (tRect.height > 24) {
                bugs.push({
                  viewport: vpName,
                  screen: scName,
                  type: 'BUTTON_TEXT_WRAPPED',
                  text,
                  btnHeight: r.height,
                  textHeight: tRect.height,
                  className: btn.className
                });
              }
            }
          }

          // Check if button overflows its container or viewport (excluding intentional horizontal scrollers)
          const inHorizontalScroller = btn.closest('.horizontal-scroll') || btn.closest('.ecom-cat-chips') || btn.closest('.osb-demo-suggestions') || btn.closest('.osb-sug-tags') || btn.closest('.agri-status-tabs-container') || btn.closest('.agri-status-tabs');
          if (r.right > screenW + 2 && !inHorizontalScroller) {
            bugs.push({
              viewport: vpName,
              screen: scName,
              type: 'BUTTON_OVERFLOW_RIGHT',
              text,
              right: r.right,
              screenW,
              className: btn.className
            });
          }

          // Check if button text is clipped
          if (btn.scrollWidth > btn.clientWidth + 2 && s.overflow === 'hidden' && s.textOverflow !== 'ellipsis') {
            bugs.push({
              viewport: vpName,
              screen: scName,
              type: 'BUTTON_TEXT_CLIPPED',
              text,
              scrollW: btn.scrollWidth,
              clientW: btn.clientWidth,
              className: btn.className
            });
          }
        });

        // 2. Check ALL Cards & containers
        const cards = Array.from(document.querySelectorAll('.card, [class*="card"], [class*="-box"], [class*="item"], .hump-card-nav-row, .ecom-product-card, .ancu-job-item, .order-item')).filter(isVisible);
        cards.forEach(card => {
          const r = card.getBoundingClientRect();
          const s = window.getComputedStyle(card);
          const cName = typeof card.className === 'string' ? card.className : '';

          const inHorizontalScroller = card.closest('.horizontal-scroll') || card.closest('.ecom-cat-chips') || card.closest('.osb-tags-row') || card.closest('.agri-status-tabs-container') || card.closest('.agri-status-tabs');
          if (r.right > screenW + 2 && !card.closest('.horizontal-scroll') && !card.closest('.tabs-scroll') && !inHorizontalScroller) {
            bugs.push({
              viewport: vpName,
              screen: scName,
              type: 'CARD_OVERFLOW_VIEWPORT',
              text: card.innerText.trim().slice(0, 30),
              right: r.right,
              screenW,
              className: cName
            });
          }

          // Check children with nowrap that overflow card width
          const textChildren = card.querySelectorAll('h1, h2, h3, h4, h5, h6, p, span, div');
          textChildren.forEach(tc => {
            if (tc.children.length === 0 && tc.innerText.trim()) {
              const tcS = window.getComputedStyle(tc);
              if (tc.scrollWidth > tc.clientWidth + 2 && tcS.whiteSpace === 'nowrap' && tcS.textOverflow !== 'ellipsis' && tcS.overflow !== 'hidden') {
                bugs.push({
                  viewport: vpName,
                  screen: scName,
                  type: 'CARD_TEXT_SPILL',
                  text: tc.innerText.trim().slice(0, 35),
                  scrollW: tc.scrollWidth,
                  clientW: tc.clientWidth,
                  className: typeof tc.className === 'string' ? tc.className : ''
                });
              }
            }
          });
        });

        return bugs;
      }, vp.name, sc.name, vp.width);

      if (screenBugs.length > 0) {
        allProblems.push(...screenBugs);
      }
    }
  }

  console.log('Total viewport problems found:', allProblems.length);
  fs.writeFileSync('viewport_problems.json', JSON.stringify(allProblems, null, 2));
  console.log(JSON.stringify(allProblems.slice(0, 30), null, 2));

  await browser.close();
})();
