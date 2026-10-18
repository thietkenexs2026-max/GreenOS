const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

// 1. Identify all screens / view-panels
const panelMatches = [...html.matchAll(/id="(panel-[^"]+)"/g)].map(m => m[1]);
console.log('=== DANH SÁCH TẤT CẢ MÀN HÌNH (VIEW PANELS) ===');
console.log('Tổng số màn:', panelMatches.length);
panelMatches.forEach((p, idx) => console.log(`${idx + 1}. ${p}`));

// 2. Identify all modals / overlays / popups
const modalMatches = [...html.matchAll(/id="([^"]*(?:modal|overlay|popup|sheet|drawer|dialog)[^"]*)"/gi)].map(m => m[1]);
console.log('\n=== DANH SÁCH MODAL / POPUP / SHEET ===');
console.log('Tổng số modal:', modalMatches.length);
modalMatches.forEach((m, idx) => console.log(`${idx + 1}. ${m}`));

// 3. Identify all buttons and their onclick or missing onclick
console.log('\n=== KIỂM TRA TẤT CẢ BUTTONS ===');
const buttonRegex = /<button\b([^>]*)>([\s\S]*?)<\/button>/gi;
let bMatch;
let totalButtons = 0;
let buttonsWithoutOnclick = [];
let buttonsWithEmptyOrHash = [];

while ((bMatch = buttonRegex.exec(html)) !== null) {
  totalButtons++;
  const attrs = bMatch[1];
  const body = bMatch[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
  const hasOnclick = /onclick\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const idMatch = /id\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const classMatch = /class\s*=\s*["']([^"']*)["']/i.exec(attrs);

  const btnInfo = {
    index: totalButtons,
    id: idMatch ? idMatch[1] : null,
    className: classMatch ? classMatch[1] : null,
    text: body.slice(0, 40),
    onclick: hasOnclick ? hasOnclick[1] : null
  };

  if (!hasOnclick) {
    buttonsWithoutOnclick.push(btnInfo);
  } else if (!hasOnclick[1].trim() || hasOnclick[1].trim() === '#' || hasOnclick[1].trim().startsWith('javascript:void')) {
    buttonsWithEmptyOrHash.push(btnInfo);
  }
}

console.log(`Tổng số nút <button>: ${totalButtons}`);
console.log(`Số nút KHÔNG CÓ onclick trong HTML: ${buttonsWithoutOnclick.length}`);
console.log(`Số nút có onclick rỗng hoặc void: ${buttonsWithEmptyOrHash.length}`);

// 4. Check if buttons without onclick have addEventListener or submit type
const jsSection = html.slice(html.indexOf('<script>'));
let buttonsReallyMissing = [];

buttonsWithoutOnclick.forEach(btn => {
  let isHandled = false;
  if (btn.id && jsSection.includes(btn.id)) {
    isHandled = true;
  }
  // Check if it's type="submit" in a form
  // Or check if class is targeted in addEventListener
  if (btn.className) {
    const classes = btn.className.split(' ');
    for (const c of classes) {
      if (c && jsSection.includes(`.${c}`) || jsSection.includes(`'${c}'`) || jsSection.includes(`"${c}"`)) {
        isHandled = true;
        break;
      }
    }
  }
  if (!isHandled) {
    buttonsReallyMissing.push(btn);
  }
});

console.log(`Số nút THỰC SỰ THIẾU SỰ KIỆN / ĐIỀU HƯỚNG: ${buttonsReallyMissing.length}`);
buttonsReallyMissing.forEach(btn => {
  // Find which panel contains this button
  const btnTag = html.indexOf(btn.id ? `id="${btn.id}"` : btn.text);
  let panel = 'Chưa xác định';
  if (btnTag !== -1) {
    const sub = html.slice(0, btnTag);
    const pMatch = [...sub.matchAll(/id="(panel-[^"]+)"/g)].pop();
    if (pMatch) panel = pMatch[1];
  }
  console.log(`- [NÚT] "${btn.text}" | id: ${btn.id || 'none'} | class: ${btn.className || 'none'} | Nằm tại màn: ${panel}`);
});

// 5. Check cards and clickable elements
console.log('\n=== KIỂM TRA CÁC CARD VÀ PHẦN TỬ DẠNG THẺ ===');
const cardRegex = /<div\b([^>]*class="[^"]*(?:card|item|banner|tile|chip|option)[^"]*"[^>]*)>([\s\S]*?)<\/div>/gi;
let cMatch;
let totalCards = 0;
let cardsWithCursorPointerNoClick = [];

while ((cMatch = cardRegex.exec(html)) !== null) {
  totalCards++;
  const attrs = cMatch[1];
  const body = cMatch[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
  const hasOnclick = /onclick\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const idMatch = /id\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const classMatch = /class\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const hasCursorPointer = /cursor:\s*pointer/i.test(attrs);

  if (hasCursorPointer && !hasOnclick) {
    let isHandled = false;
    if (idMatch && jsSection.includes(idMatch[1])) isHandled = true;
    if (!isHandled) {
      cardsWithCursorPointerNoClick.push({
        id: idMatch ? idMatch[1] : null,
        className: classMatch ? classMatch[1] : null,
        text: body.slice(0, 50),
        attrs: attrs.slice(0, 100)
      });
    }
  }
}

console.log(`Tổng thẻ quét: ${totalCards}`);
console.log(`Thẻ có style cursor:pointer nhưng KHÔNG CÓ onclick / điều hướng: ${cardsWithCursorPointerNoClick.length}`);
