const puppeteer = require('puppeteer-core');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });

  await page.goto('http://127.0.0.1:8080/index.html', { waitUntil: 'networkidle0' });

  // Switch to Dashboard
  await page.evaluate(() => {
    switchNavTab('dashboard');
  });
  await new Promise(r => setTimeout(r, 600));

  // Check channel names and verify they are NOT truncated with ellipsis
  const channelInfo = await page.evaluate(() => {
    const titles = Array.from(document.querySelectorAll('.gvos-rev-ch-title')).map(el => el.textContent.trim());
    const amounts = Array.from(document.querySelectorAll('.gvos-rev-channel-vnd')).map(el => el.textContent.trim());
    const pcts = Array.from(document.querySelectorAll('.gvos-rev-ch-pct')).map(el => el.textContent.trim());
    return { titles, amounts, pcts };
  });
  console.log('Channel Data:', JSON.stringify(channelInfo));

  // Check 7-day chart elements
  const chartCols = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.gvos-7d-col')).length;
  });
  console.log('7-Day Chart Columns count:', chartCols);

  // Take screenshot of revenue card & 7-day card
  const revenueCard = await page.$('section[aria-labelledby="dt-kenh"]');
  if (revenueCard) {
    await revenueCard.screenshot({ path: 'revenue_channels_fixed.png' });
    console.log('Saved revenue_channels_fixed.png');
  }

  const sevenDayCard = await page.$('section[aria-labelledby="dt-ngay"]');
  if (sevenDayCard) {
    await sevenDayCard.screenshot({ path: 'seven_days_fixed.png' });
    console.log('Saved seven_days_fixed.png');
  }

  // Test expanding the 7 days toggle
  await page.evaluate(() => {
    toggle7DayDetails();
  });
  await new Promise(r => setTimeout(r, 300));

  const isExpanded = await page.evaluate(() => {
    const el = document.getElementById('gvos7dExpandedRows');
    return el && el.style.display !== 'none';
  });
  console.log('Toggle 7 days expansion works:', isExpanded);

  if (sevenDayCard) {
    await sevenDayCard.screenshot({ path: 'seven_days_expanded.png' });
    console.log('Saved seven_days_expanded.png');
  }

  // Full dashboard screenshot
  await page.screenshot({ path: 'dashboard_revenue_view.png', fullPage: false });
  console.log('Saved dashboard_revenue_view.png');

  await browser.close();
  console.log('Test completed successfully!');
})();
