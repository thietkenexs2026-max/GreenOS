const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const outDir = path.join(__dirname, 'audit_screens');
if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 420, height: 900, deviceScaleFactor: 2 });
  
  await page.goto('http://localhost:8080/index.html', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 800));

  const panels = [
    { id: 'panel-home', name: '01_Trang_Chu', switchFn: () => switchNavTab('home') },
    { id: 'panel-step1', name: '02_Wizard_Step1_ChupAnh', switchFn: () => startWizardFlow() },
    { id: 'panel-step2', name: '03_Wizard_Step2_DinhGiaAI', switchFn: () => goToStep(2) },
    { id: 'panel-step3', name: '04_Wizard_Step3_XemTruoc', switchFn: () => goToStep(3) },
    { id: 'panel-market', name: '05_Cho_Xanh_Xa', switchFn: () => switchNavTab('market') },
    { id: 'panel-product-detail', name: '06_Chi_Tiet_San_Pham', switchFn: () => viewProductDetail('chuoi-say') },
    { id: 'panel-orders', name: '07_Don_Hang', switchFn: () => switchNavTab('orders') },
    { id: 'panel-order-detail', name: '08_Chi_Tiet_Don_Hang', switchFn: () => { if (typeof BAC_BA_ORDERS !== 'undefined' && BAC_BA_ORDERS.length) openOrderDetail(BAC_BA_ORDERS[0].id); } },
    { id: 'panel-picklist', name: '09_Soan_Hang_Picklist', switchFn: () => openPickListView() },
    { id: 'panel-dashboard', name: '10_Bao_Cao_Thong_Ke', switchFn: () => switchNavTab('dashboard') },
    { id: 'panel-account', name: '11_Tai_Khoan', switchFn: () => switchNavTab('account') },
    { id: 'panel-onboarding', name: '12_Onboarding_Step1', switchFn: () => goToOnboarding(1) },
    { id: 'panel-onboarding', name: '13_Onboarding_Login', switchFn: () => goToOnboarding('login') },
  ];

  const report = [];

  for (const item of panels) {
    console.log(`Checking ${item.name} (${item.id})...`);
    
    // Switch to panel
    await page.evaluate((panelId, name) => {
      try {
        if (name.includes('Trang_Chu')) switchNavTab('home');
        else if (name.includes('Step1')) startWizardFlow();
        else if (name.includes('Step2')) goToStep(2);
        else if (name.includes('Step3')) goToStep(3);
        else if (name.includes('Cho_Xanh')) switchNavTab('market');
        else if (name.includes('Chi_Tiet_San_Pham')) {
          if (typeof openProductDetailModal === 'function') openProductDetailModal(1);
        }
        else if (name.includes('Don_Hang') && !name.includes('Chi_Tiet')) switchNavTab('orders');
        else if (name.includes('Chi_Tiet_Don_Hang')) {
          if (typeof BAC_BA_ORDERS !== 'undefined' && BAC_BA_ORDERS.length) {
            openOrderDetail(BAC_BA_ORDERS[0].id);
          }
        }
        else if (name.includes('Picklist')) openPickListView();
        else if (name.includes('Bao_Cao')) switchNavTab('dashboard');
        else if (name.includes('Tai_Khoan')) switchNavTab('account');
        else if (name.includes('Onboarding_Step1')) goToOnboarding(1);
        else if (name.includes('Onboarding_Login')) goToOnboarding('login');
      } catch (e) {
        document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
        const p = document.getElementById(panelId);
        if (p) p.classList.add('active');
      }
    }, item.id, item.name);

    await new Promise(r => setTimeout(r, 600));

    // Audit text issues inside this active panel
    const issues = await page.evaluate((panelId) => {
      const panel = document.getElementById(panelId);
      if (!panel) return [];

      const detected = [];
      const walker = document.createTreeWalker(panel, NodeFilter.SHOW_ELEMENT);
      let node;

      while ((node = walker.nextNode())) {
        const style = window.getComputedStyle(node);
        if (style.display === 'none' || style.visibility === 'hidden') continue;

        // Skip naturally scrolling tracks or sliders
        if (node.classList.contains('promo-slides-track') || node.classList.contains('promo-carousel-container')) continue;
        if (node.classList.contains('swipeable-chips-wrap') || node.classList.contains('orders-sub-view')) continue;

        const isOverflowing = node.scrollWidth > node.clientWidth + 3 && style.overflowX !== 'auto' && style.overflowX !== 'scroll';
        
        let isTruncated = false;
        if (style.textOverflow === 'ellipsis') {
          if (node.scrollWidth > node.clientWidth + 1) {
            isTruncated = true;
          }
        }

        const text = (node.innerText || '').trim();
        
        if (isOverflowing && text.length > 0) {
          detected.push({
            type: 'HORIZONTAL_OVERFLOW',
            tag: node.tagName,
            className: node.className,
            text: text.slice(0, 60),
            scrollWidth: node.scrollWidth,
            clientWidth: node.clientWidth
          });
        }

        if (isTruncated && text.length > 0) {
          detected.push({
            type: 'TEXT_TRUNCATED_ELLIPSIS',
            tag: node.tagName,
            className: node.className,
            text: text.slice(0, 60),
            scrollWidth: node.scrollWidth,
            clientWidth: node.clientWidth
          });
        }
      }

      return detected;
    }, item.id);

    // Capture screenshots
    const shotPath = path.join(outDir, `${item.name}.png`);
    await page.screenshot({ path: shotPath });

    const isScrollable = await page.evaluate(() => {
      const sc = document.querySelector('.screen-container');
      return sc ? sc.scrollHeight > sc.clientHeight + 100 : false;
    });

    if (isScrollable) {
      await page.evaluate(() => {
        const sc = document.querySelector('.screen-container');
        if (sc) sc.scrollTo(0, sc.scrollHeight * 0.5);
      });
      await new Promise(r => setTimeout(r, 400));
      await page.screenshot({ path: path.join(outDir, `${item.name}_scrolled.png`) });
    }

    report.push({
      panel: item.name,
      issuesCount: issues.length,
      issues: issues
    });
  }

  // Also check modals: An Cư Job Modal
  console.log('Checking modal anCuJobModal...');
  await page.evaluate(() => {
    switchNavTab('home');
    if (typeof openAnCuJobModal === 'function') openAnCuJobModal();
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(outDir, '14_Modal_AnCuJob.png') });

  fs.writeFileSync('audit_report.json', JSON.stringify(report, null, 2), 'utf-8');
  console.log('Audit complete! Results saved to audit_report.json and screenshots in audit_screens/');

  await browser.close();
})();
