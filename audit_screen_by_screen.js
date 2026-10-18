const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

const panels = [
  'panel-onboarding',
  'panel-home',
  'panel-step1',
  'panel-step2',
  'panel-step3',
  'panel-zalo',
  'panel-inventory',
  'panel-market',
  'panel-product-detail',
  'panel-support',
  'panel-orders',
  'panel-order-detail',
  'panel-picklist',
  'panel-dashboard',
  'panel-account',
  'panel-ancujob',
  'panel-ancujob-post',
  'panel-ancujob-dispatch',
  'panel-ancujob-detail'
];

const jsSection = html.slice(html.indexOf('<script>'));

const results = [];

panels.forEach((pId, pIdx) => {
  const nextPId = panels[pIdx + 1];
  const startIdx = html.indexOf(`id="${pId}"`);
  if (startIdx === -1) {
    results.push({ panel: pId, error: 'NOT_FOUND' });
    return;
  }
  let endIdx;
  if (nextPId) {
    endIdx = html.indexOf(`id="${nextPId}"`);
  } else {
    // Last panel ends at </main>
    endIdx = html.indexOf('</main>', startIdx);
  }
  const panelHtml = html.slice(startIdx, endIdx);

  // Find all buttons inside this panel
  const btnMatches = [...panelHtml.matchAll(/<button\b([^>]*)>([\s\S]*?)<\/button>/gi)];
  // Find all divs with onclick or cursor:pointer
  const divClicks = [...panelHtml.matchAll(/<div\b([^>]*(?:onclick|cursor:\s*pointer)[^>]*)>([\s\S]*?)<\/div>/gi)];
  // Find all <a> tags
  const aMatches = [...panelHtml.matchAll(/<a\b([^>]*)>([\s\S]*?)<\/a>/gi)];

  const buttons = btnMatches.map(m => {
    const attrs = m[1];
    const text = m[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ').slice(0, 35);
    const onclickMatch = /onclick\s*=\s*["']([^"']*)["']/i.exec(attrs);
    const idMatch = /id\s*=\s*["']([^"']*)["']/i.exec(attrs);
    const classMatch = /class\s*=\s*["']([^"']*)["']/i.exec(attrs);
    return {
      type: 'button',
      text,
      id: idMatch ? idMatch[1] : null,
      class: classMatch ? classMatch[1] : null,
      onclick: onclickMatch ? onclickMatch[1] : null
    };
  });

  const cardsAndDivs = divClicks.map(m => {
    const attrs = m[1];
    const text = m[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ').slice(0, 35);
    const onclickMatch = /onclick\s*=\s*["']([^"']*)["']/i.exec(attrs);
    const idMatch = /id\s*=\s*["']([^"']*)["']/i.exec(attrs);
    const classMatch = /class\s*=\s*["']([^"']*)["']/i.exec(attrs);
    return {
      type: 'clickable_div_or_card',
      text,
      id: idMatch ? idMatch[1] : null,
      class: classMatch ? classMatch[1] : null,
      onclick: onclickMatch ? onclickMatch[1] : null
    };
  });

  // Verify missing items
  const missing = [];
  buttons.forEach(b => {
    if (!b.onclick) {
      // Check if ID handled in JS
      if (!b.id || !jsSection.includes(b.id)) {
        missing.push(b);
      }
    }
  });

  cardsAndDivs.forEach(c => {
    if (!c.onclick) {
      if (!c.id || !jsSection.includes(c.id)) {
        missing.push(c);
      }
    }
  });

  results.push({
    panel: pId,
    totalButtons: buttons.length,
    totalCards: cardsAndDivs.length,
    missing: missing
  });
});

console.log('=== KẾT QUẢ KIỂM TRA TỪNG MÀN HÌNH ===');
results.forEach(r => {
  console.log(`\n📺 [${r.panel}]: ${r.totalButtons} buttons | ${r.totalCards} cards/divs có tương tác`);
  if (r.missing.length === 0) {
    console.log('   ✅ 100% tất cả nút và thẻ đều có điều hướng/sự kiện xử lý!');
  } else {
    console.log(`   ⚠️ CÓ ${r.missing.length} NÚT/THẺ CHƯA CÓ ĐIỀU HƯỚNG:`);
    r.missing.forEach(m => {
      console.log(`      - [${m.type}] "${m.text}" | id: ${m.id} | class: ${m.class}`);
    });
  }
});
