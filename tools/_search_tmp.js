// node search.js "query" [engine=yahoo|ddg]
const { request } = require('playwright');
const q = process.argv[2]; const eng = process.argv[3] || 'yahoo';
const dec = s => s.replace(/<[^>]+>/g,'').replace(/&amp;/g,'&').replace(/&quot;/g,'"').replace(/&#39;/g,"'").replace(/&#(\d+);/g,(m,n)=>String.fromCharCode(n)).replace(/&[a-z]+;/g,' ').replace(/\s+/g,' ').trim();
(async () => {
  const ctx = await request.newContext({ proxy: { server: process.env.HTTPS_PROXY }, timeout: 40000, extraHTTPHeaders: { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36', 'Accept-Language': 'es-ES,es;q=0.9' } });
  let url = eng==='ddg' ? 'https://lite.duckduckgo.com/lite/?kl=es-es&q='+encodeURIComponent(q) : 'https://search.yahoo.com/search?n=15&p='+encodeURIComponent(q);
  const r = await ctx.get(url); const h = await r.text();
  console.log('########## '+q+' ['+eng+' '+r.status()+']');
  if (eng==='ddg') {
    const ls=[...h.matchAll(/<a rel="nofollow" href="([^"]+)" class='result-link'>([\s\S]*?)<\/a>/g)];
    const sn=[...h.matchAll(/<td class='result-snippet'>([\s\S]*?)<\/td>/g)];
    if(!ls.length) console.log('NO RESULTS: '+dec(h).slice(0,200));
    ls.slice(0,12).forEach((m,i)=>{let u=m[1].replace(/&amp;/g,'&');const mm=u.match(/uddg=([^&]+)/);if(mm)u=decodeURIComponent(mm[1]);console.log('- '+dec(m[2])+'\n  '+u+'\n  '+(sn[i]?dec(sn[i][1]).slice(0,220):''));});
  } else {
    const items=[...h.matchAll(/<div class="compTitle[^"]*">[\s\S]*?<a[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>[\s\S]*?(?:<p class="[^"]*fc-falcon[^"]*">([\s\S]*?)<\/p>|<\/div>)/g)];
    if(!items.length) console.log('NO RESULTS: '+dec(h).slice(0,200));
    items.slice(0,12).forEach(m=>{let u=m[1];const mm=u.match(/RU=([^/]+)\//);if(mm)u=decodeURIComponent(mm[1]);console.log('- '+dec(m[2])+'\n  '+u+'\n  '+(m[3]?dec(m[3]).slice(0,220):''));});
  }
  await ctx.dispose();
})().catch(e=>console.log('FAIL',e.message.split('\n')[0]));
