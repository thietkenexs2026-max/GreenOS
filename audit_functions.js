const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Find all onclick handlers
const onclickRegex = /onclick\s*=\s*["']([^"']+)["']/gi;
let m;
const calledFuncs = new Set();
const callMap = {};

while ((m = onclickRegex.exec(html)) !== null) {
  const code = m[1].trim();
  // extract function calls e.g. foo(bar) -> foo
  const fMatches = [...code.matchAll(/([a-zA-Z0-9_$]+)\s*\(/g)];
  fMatches.forEach(fm => {
    const fn = fm[1];
    if (!['if', 'alert', 'confirm', 'console', 'setTimeout', 'stopPropagation', 'preventDefault'].includes(fn)) {
      calledFuncs.add(fn);
      if (!callMap[fn]) callMap[fn] = [];
      callMap[fn].push(code);
    }
  });
}

console.log('Tổng số hàm được gọi trong onclick:', calledFuncs.size);

const js = html.slice(html.indexOf('<script>'));
const missingFuncs = [];

calledFuncs.forEach(fn => {
  // Check if defined as function fn, var fn =, window.fn =, const fn =, let fn =
  const isDefined = new RegExp('(?:function\\s+' + fn + '\\b|window\\.' + fn + '\\s*=|\\b' + fn + '\\s*=\\s*(?:function|\\())').test(js);
  if (!isDefined) {
    missingFuncs.push({ name: fn, callers: callMap[fn] });
  }
});

console.log('Số hàm KHÔNG TÌM THẤY ĐỊNH NGHĨA trong <script>:', missingFuncs.length);
missingFuncs.forEach(mf => {
  console.log(`❌ Hàm: [${mf.name}] | Gọi từ:`, mf.callers.slice(0, 3));
});
