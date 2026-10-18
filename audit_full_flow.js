const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

console.log('=====================================================');
console.log('   TOÀN DIỆN KIỂM TRA ĐIỀU HƯỚNG GREENOS (CHỢ XANH)  ');
console.log('=====================================================\n');

// 1. Phân tích các Màn hình (Panels)
const panels = [...html.matchAll(/\bid="(panel-[^"]+)"/gi)].map(m => m[1]);
console.log(`[1] TỔNG QUAN CÁC MÀN HÌNH (${panels.length} MÀN):`);

panels.forEach(pId => {
  // Tìm khối panel
  const startIdx = html.indexOf(`id="${pId}"`);
  // Lấy 2000 ký tự đầu tiên của panel để check header/back button
  const snippet = html.slice(startIdx, startIdx + 2000);
  
  // Kiểm tra nút back hoặc cách thoát khỏi màn hình
  const backMatches = [...snippet.matchAll(/onclick="([^"]*(?:open|switch|close|show|tab|history|navigate)[^"]*)"/gi)].map(m => m[1]);
  
  console.log(` • Màn: ${pId.padEnd(24)} | Nút điều hướng/Back: ${backMatches.length > 0 ? '✓ (' + backMatches[0].slice(0, 35) + ')' : '⚠️ Cần kiểm tra'}`);
});

// 2. Kiểm tra chi tiết 10 nút chưa có onclick trực tiếp
console.log('\n[2] KIỂM TRA CHI TIẾT CÁC NÚT ĐANG THIẾU ONCLICK HOẶC NẰM TRONG CARD:');
const inspectElements = [
  'vcl-circle-btn',
  'action-pill',
  'btn-apsc-view'
];

inspectElements.forEach(cls => {
  const regex = new RegExp(`(<[^>]*class="[^"]*${cls}[^"]*"[^>]*>[\\s\\S]*?<\\/[a-z0-9]+>)`, 'gi');
  let match;
  let count = 0;
  while ((match = regex.exec(html)) !== null) {
    count++;
    const idx = match.index;
    // Lấy ngữ cảnh cha xung quanh 400 ký tự trước
    const parentContext = html.slice(Math.max(0, idx - 400), idx + 200);
    const parentHasOnclick = /onclick="([^"]+)"/i.exec(parentContext);
    const sub = html.slice(0, idx);
    const panelMatch = [...sub.matchAll(/id="(panel-[^"]+)"/g)].pop();
    const panel = panelMatch ? panelMatch[1] : 'Ngoài panel (header/modal/etc)';

    console.log(`\n -> [Class: ${cls} #${count}] tại màn [${panel}]:`);
    console.log(`    Tag: ${match[0].slice(0, 80).replace(/\n/g, ' ')}...`);
    if (parentHasOnclick) {
      console.log(`    ✓ Thẻ cha đã có onclick: ${parentHasOnclick[1]}`);
    } else {
      console.log(`    ❌ KHÔNG CÓ onclick trên chính nó và không thấy onclick ở thẻ cha gần kề!`);
    }
  }
});

// 3. Kiểm tra các thẻ <a> (Hyperlinks)
console.log('\n[3] KIỂM TRA TẤT CẢ CÁC THẺ LIÊN KẾT <a>:');
const linkRegex = /<a\b([^>]*)>([\s\S]*?)<\/a>/gi;
let lMatch;
let totalLinks = 0;
let deadLinks = [];

while ((lMatch = linkRegex.exec(html)) !== null) {
  totalLinks++;
  const attrs = lMatch[1];
  const body = lMatch[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
  const hrefMatch = /href\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const onclickMatch = /onclick\s*=\s*["']([^"']*)["']/i.exec(attrs);
  const href = hrefMatch ? hrefMatch[1].trim() : '';

  if (!onclickMatch && (!href || href === '#' || href.startsWith('javascript:void'))) {
    const idx = lMatch.index;
    const sub = html.slice(0, idx);
    const panelMatch = [...sub.matchAll(/id="(panel-[^"]+)"/g)].pop();
    deadLinks.push({
      text: body.slice(0, 30),
      href,
      panel: panelMatch ? panelMatch[1] : 'unknown',
      full: lMatch[0].slice(0, 80)
    });
  }
}
console.log(`Tổng số thẻ <a>: ${totalLinks}`);
console.log(`Số link dead / rỗng (# hoặc không có điều hướng): ${deadLinks.length}`);
deadLinks.forEach(dl => {
  console.log(` - [Link chết] "${dl.text}" | href: "${dl.href}" tại màn: ${dl.panel}`);
});

// 4. Kiểm tra các Tab Bottom Navigation
console.log('\n[4] KIỂM TRA THANH ĐIỀU HƯỚNG DƯỚI (BOTTOM DOCK / TAB BAR):');
const bottomNavRegex = /<(?:button|div)\b[^>]*class="[^"]*nav-tab-item[^"]*"[^>]*>([\s\S]*?)<\/(?:button|div)>/gi;
let bnMatch;
let countTab = 0;
while ((bnMatch = bottomNavRegex.exec(html)) !== null) {
  countTab++;
  const tagStr = bnMatch[0];
  const hasOnclick = /onclick="([^"]+)"/i.exec(tagStr);
  const text = bnMatch[1].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
  console.log(` Tab ${countTab}: "${text}" -> Onclick: ${hasOnclick ? hasOnclick[1] : '❌ THIẾU ONCLICK'}`);
}

// 5. Kiểm tra các Quick Action Cards tại Trang chủ
console.log('\n[5] KIỂM TRA CÁC THẺ CARD TẠI TRANG CHỦ (PANEL-HOME):');
const homeStart = html.indexOf('id="panel-home"');
const homeEnd = html.indexOf('id="panel-step1"');
const homeHtml = html.slice(homeStart, homeEnd);

const homeCards = [...homeHtml.matchAll(/<div\b([^>]*class="[^"]*(?:card|banner|hub|action|item)[^"]*"[^>]*)>([\s\S]*?)<\/div>/gi)];
console.log(`Số lượng thẻ tiềm năng tại trang chủ: ${homeCards.length}`);
homeCards.forEach(c => {
  const attrs = c[1];
  const body = c[2].replace(/<[^>]+>/g, '').trim().replace(/\s+/g, ' ');
  const hasOnclick = /onclick="([^"]+)"/i.exec(attrs);
  if (/cursor:\s*pointer/i.test(attrs) || /banner/i.test(attrs) || /hub/i.test(attrs)) {
    console.log(` - Card: "${body.slice(0, 35)}" | Onclick: ${hasOnclick ? hasOnclick[1] : '⚠️ KHÔNG CÓ TRỰC TIẾP'}`);
  }
});
