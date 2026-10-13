import{
j as e
}
from"./vendor-react-DWSMirXw.js";
import{
l as C,a as k,d as S
}
from"./day-YzirYrUp.js";
import{
u as E
}
from"./use-back-CkadEuin.js";
import{
d as N,b1 as w,aN as x,K as L,Q as D,b2 as _,aT as O,aP as T,l as M,ao as $,W as A,J as H,F as K
}
from"./index-DNEPjpjh.js";
import{
e as v,j as B
}
from"./orders-k-b7CgfK.js";
import{
C as y
}
from"./art-model-BBSBb1v1.js";
import{
M as P
}
from"./MoneyPath-BirKp-nq.js";
import{
C as R
}
from"./ChannelMark-BFRcmIIK.js";
import{
C as F
}
from"./orders-model-C1MjWSyY.js";
import{
f as b
}
from"./format-BVpxaOlS.js";
import{
I as q
}
from"./CxBadges-CdWpbXcU.js";
import{
C as I
}
from"./ContourBand-DpuUYZAJ.js";
import{
u as Q
}
from"./useQueries-B2sqn_tr.js";
import{
l as V,o as J,u as U
}
from"./use-orders-BihT4WjI.js";
import"./calm-CKlBhP23.js";
import"./check-tr-ScFLk.js";
import"./undo-2-C1ywHouo.js";
import"./house-Bii5UhvD.js";
import"./shopping-bag-g6S_W2_2.js";
import"./message-circle-Cy_Rzm8X.js";
import"./order-action-words-CoU6-3BJ.js";
import"./cho-xanh-D6Ml3r5J.js";
import"./handshake-Tba4cA5K.js";
import"./bell-ring-BIpDWIZb.js";
import"./user-check-a55CUGWN.js";
import"./eye-EogC0IcI.js";
import"./circle-dot-Dxh-ug9W.js";
import"./ban-BQaFkSQi.js";
import"./csv-CbzwKy2z.js";
import"./use-market-DzAwoMtE.js";
const W=1e6,X=t=>Math.round(t/1e5)/10;
function z({
channel:t
}
){
const o=F.map(a=>{
var r;
return{
c:a,label:v[a],vnd:((r=t(a))==null?void 0:r.totals.amount_vnd)??null
}

}
),l=Math.max(1,...o.map(a=>a.vnd??0));
return e.jsxs("section",{
"aria-labelledby":"dt-kenh",className:"space-y-3 rounded-card border border-line bg-md-container p-3",children:[e.jsxs("div",{
children:[e.jsx("h2",{
id:"dt-kenh",className:"text-base font-bold text-md-on-surface",children:"Doanh thu theo kênh"
}
),e.jsx("p",{
className:"text-sm text-fg-muted",children:"Triệu đồng, đơn đã bán trong tháng. Kênh dưới 1 triệu ghi đủ số."
}
)]
}
),e.jsx("ul",{
"aria-hidden":!0,className:"space-y-2",children:o.map(({
c:a,label:r,vnd:s
}
)=>e.jsxs("li",{
className:"grid grid-cols-[minmax(6rem,8rem)_1fr] items-center gap-3",children:[e.jsxs("span",{
className:"flex items-center gap-1.5 text-sm text-fg",children:[e.jsx(R,{
channel:a,iconOnly:!0,className:N(y[a].text,"shrink-0")
}
),e.jsx("span",{
className:"truncate",children:r
}
)]
}
),e.jsxs("span",{
className:"flex items-center gap-2",children:[s!==null&&s>0&&e.jsx("span",{
className:N("h-3 rounded-full",y[a].bg),style:{
width:`${
Math.max(s/l*70,3)
}
%`
}

}
),e.jsx("span",{
className:"text-sm font-semibold tabular-nums text-fg",children:s===null?"Chưa có giá":s<W?b(s):X(s).toLocaleString("vi-VN")
}
)]
}
)]
}
,a))
}
),e.jsxs("table",{
className:"sr-only",children:[e.jsx("caption",{
children:"Doanh thu theo kênh"
}
),e.jsx("thead",{
children:e.jsxs("tr",{
children:[e.jsx("th",{
scope:"col",children:"Kênh"
}
),e.jsx("th",{
scope:"col",children:"Doanh thu"
}
)]
}
)
}
),e.jsx("tbody",{
children:o.map(a=>e.jsxs("tr",{
children:[e.jsx("th",{
scope:"row",children:a.label
}
),e.jsx("td",{
children:a.vnd===null?"Chưa có giá":b(a.vnd)
}
)]
}
,a.label))
}
)]
}
)]
}
)
}
function G({
days:t,day:o
}
){
return e.jsxs("section",{
"aria-labelledby":"dt-ngay",className:"space-y-2 rounded-card border border-line bg-md-container p-3",children:[e.jsx("h2",{
id:"dt-ngay",className:"text-base font-bold text-md-on-surface",children:"7 ngày gần nhất"
}
),e.jsxs("table",{
className:"w-full border-collapse text-left text-base",children:[e.jsx("thead",{
children:e.jsxs("tr",{
className:"text-sm text-fg-muted",children:[e.jsx("th",{
scope:"col",className:"py-1 font-semibold",children:"Ngày"
}
),e.jsx("th",{
scope:"col",className:"py-1 text-right font-semibold",children:"Đơn đã bán"
}
),e.jsx("th",{
scope:"col",className:"py-1 text-right font-semibold",children:"Tiền"
}
)]
}
)
}
),e.jsx("tbody",{
children:t.map(l=>{
const a=o(l);
return e.jsxs("tr",{
className:"border-t border-line",children:[e.jsx("th",{
scope:"row",className:"min-h-12 py-3 font-medium tabular-nums text-fg",children:w(`${
l
}
T12:00:00+07:00`).slice(0,5)
}
),e.jsx("td",{
className:"py-3 text-right tabular-nums text-fg",children:a?x(a.pagination.total):"—"
}
),e.jsx("td",{
className:"py-3 text-right tabular-nums text-fg",children:a?a.totals.amount_vnd===null?"Chưa có giá":b(a.totals.amount_vnd):"—"
}
)]
}
,l)
}
)
}
)]
}
)]
}
)
}
function Y({
held:t
}
){
return e.jsxs("section",{
"aria-labelledby":"dt-doi-tac",className:"space-y-2 rounded-card border border-line bg-md-container p-3",children:[e.jsx("h2",{
id:"dt-doi-tac",className:"text-base font-bold text-md-on-surface",children:"Chợ Xanh · tiền Đối tác đã nhận"
}
),e.jsx(P,{
payment:{
method:"ck_doi_tac",status:"da_nhan",claimed_at:null
}
,status:"da_giao"
}
),e.jsx("dl",{
className:"border-t border-line pt-2 text-base",children:e.jsxs("div",{
className:"flex items-baseline justify-between gap-3",children:[e.jsx("dt",{
className:"text-fg-muted",children:"Đơn hoàn thành trong tháng"
}
),e.jsx("dd",{
className:"text-right font-semibold tabular-nums text-fg",children:t?t.totals.amount_vnd===null?"Chưa có giá":`${
b(t.totals.amount_vnd)
}
 · ${
x(t.pagination.total)
}
 đơn`:"—"
}
)]
}
)
}
),e.jsx("p",{
className:"text-sm text-fg-muted",children:"Người mua đã chuyển cho Đối tác, chưa trừ phí. Đối tác đối soát rồi trả cho bạn."
}
)]
}
)
}
function Z({
value:t,months:o,running:l,onChange:a
}
){
return e.jsxs("div",{
className:"flex flex-wrap items-end gap-3",children:[e.jsx("div",{
className:"min-w-[12rem] flex-1",children:e.jsx(L,{
label:"Tháng",children:r=>e.jsx(D,{
...r,className:"min-h-12 text-base",value:t,onChange:s=>a(s.target.value),children:o.map(s=>e.jsx("option",{
value:s,children:_(s)
}
,s))
}
)
}
)
}
),t===l&&e.jsx(O,{
tone:"info",icon:T,children:"Chưa đủ tháng"
}
)]
}
)
}
function ee({
amount:t,orders:o,month:l
}
){
return e.jsxs("section",{
"aria-labelledby":"dt-chinh",className:"overflow-hidden rounded-card border border-line bg-md-container",children:[e.jsx("img",{
src:"/anh-mau/cho/banner/banner-mat-ong-vu-xuan-800.webp",alt:"",width:800,height:267,decoding:"async",className:"ambient-photo h-20 w-full object-cover"
}
),e.jsxs(I,{
className:"space-y-1 p-3",children:[e.jsxs("div",{
className:"flex items-center gap-2",children:[e.jsx("h2",{
id:"dt-chinh",className:"flex-1 text-base font-bold text-fg",children:`Doanh thu ${
_(l).toLowerCase()
}
`
}
),e.jsx(q,{

}
)]
}
),e.jsx("p",{
className:"type-stat tabular-nums text-fg",children:t===null?"Chưa có giá":b(t)
}
),e.jsx("p",{
className:"text-base text-fg-muted",children:`${
x(o)
}
 đơn đã bán. Không tính phí giao, đơn huỷ và trả hàng.`
}
)]
}
)]
}
)
}
function f({
label:t,value:o
}
){
return e.jsxs("li",{
className:"rounded-card bg-md-surface p-2.5",children:[e.jsx("span",{
className:"block text-xl font-bold tabular-nums text-md-on-surface",children:o
}
),e.jsx("span",{
className:"block text-sm text-md-on-variant",children:t
}
)]
}
)
}
function te({
counts:t
}
){
const o=t.moi+t.da_xac_nhan+t.cho_lay_hang+t.dang_giao+t.da_giao;
return e.jsxs("ul",{
"aria-label":"Đơn trong tháng",className:"grid grid-cols-3 gap-2",children:[e.jsx(f,{
label:"Hoàn thành",value:x(t.hoan_thanh)
}
),e.jsx(f,{
label:"Đang xử lý",value:x(o)
}
),e.jsx(f,{
label:"Huỷ, trả hàng",value:x(t.da_huy+t.tra_hang)
}
)]
}
)
}
const j=B.join(","),ae=Object.keys(v);
function se(t,o,l){
var g;
const a=o||"1970-01",r=`${
a
}
-01`,s=C(a),h=l&&l>=r&&l<=s?l:s,p=Array.from({
length:7
}
,(n,d)=>k(h,-d)),c=[{
key:"month",params:{
from:r,to:s,status:j
}

}
,...ae.map(n=>({
key:n,params:{
from:r,to:s,status:j,channel:n
}

}
)),...p.map(n=>({
key:n,params:{
from:n,to:n,status:j
}

}
)),{
key:"payout",params:{
from:r,to:s,status:"hoan_thanh",channel:"cho_xanh",payment_status:"da_nhan"
}

}
],i=Q({
queries:c.map(({
params:n
}
)=>{
const d={
...n,limit:1
}
;
return{
queryKey:J.appList(t??"",d),queryFn:()=>V(t,d),enabled:!!t&&!!l,staleTime:0
}

}
)
}
),m=Object.fromEntries(c.map((n,d)=>[n.key,i[d]])),u=n=>{
var d;
return(d=m[n])==null?void 0:d.data
}
;
return{
month:m.month,channel:n=>u(n),days:p,day:n=>u(n),payout:m.payout,pending:i.some(n=>n.isPending),error:((g=i.find(n=>n.isError))==null?void 0:g.error)??null,refetch:()=>i.forEach(n=>void n.refetch())
}

}
const ne=/^\d{
4
}
-(0[1-9]|1[0-2])$/;
function re(t){
const[o,l]=t.split("-").map(Number);
return[0,1,2].map(a=>{
const r=o*12+(l-1)-a;
return`${
Math.floor(r/12)
}
-${
String(r%12+1).padStart(2,"0")
}
`
}
)
}
function He(){
const{
householdId:t
}
=M(),{
back:o
}
=E("/"),[l,a]=$(),r=U(t),s=r.data?S(Date.parse(r.data.updated_at)):null,h=(s==null?void 0:s.slice(0,7))??"",p=l.get("thang")??"",c=ne.test(p)?p:h,i=se(t,c,s),m=h?re(h):[];
c&&!m.includes(c)&&m.push(c);
const u=i.month.data;
return e.jsxs(e.Fragment,{
children:[e.jsx(A,{
title:"Doanh thu",subtitle:"Tháng này bán được bao nhiêu",back:o
}
),m.length>0&&e.jsx(Z,{
value:c,months:m.sort().reverse(),running:h,onChange:g=>a(g===h?{

}
:{
thang:g
}
,{
replace:!0
}
)
}
),r.isError||i.error?e.jsx(H,{
error:r.error??i.error,subject:"household",onRetry:()=>r.isError?void r.refetch():i.refetch()
}
):!s||i.pending||!u?e.jsx(K,{
label:"Đang tính doanh thu"
}
):e.jsxs(e.Fragment,{
children:[e.jsx(ee,{
amount:u.totals.amount_vnd,orders:u.pagination.total,month:c
}
),e.jsx(te,{
counts:u.counts
}
),e.jsx(z,{
channel:i.channel
}
),e.jsx(G,{
days:i.days,day:i.day
}
),e.jsx(Y,{
held:i.payout.data
}
)]
}
)]
}
)
}
export{
He as RevenuePage
}
;



