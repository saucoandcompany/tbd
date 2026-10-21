// Uso: node pwfetch.js <url> [--browser]  -> imprime texto de la página (máx 20k chars)
// Sin --browser usa el cliente HTTP de Playwright (respeta NODE_EXTRA_CA_CERTS). Con --browser usa Chromium (para páginas con JS).
const { chromium, request } = require('playwright');
const url = process.argv[2]; const useBrowser = process.argv.includes('--browser');
const strip = h => h.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/gi,'').replace(/<[^>]+>/g,' ').replace(/\s+/g,' ').trim();
(async () => {
  try {
    if (!useBrowser) {
      const ctx = await request.newContext({ proxy: { server: process.env.HTTPS_PROXY }, timeout: 25000, extraHTTPHeaders: { 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/130 Safari/537.36' } });
      const r = await ctx.get(url); const body = await r.text();
      console.log(`STATUS ${r.status()} ${url}\n`); console.log(strip(body).slice(0, 20000)); await ctx.dispose(); return;
    }
    const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', headless: true, proxy: { server: process.env.HTTPS_PROXY } });
    const page = await (await browser.newContext()).newPage();
    const r = await page.goto(url, { timeout: 30000, waitUntil: 'networkidle' });
    console.log(`STATUS ${r && r.status()} ${url}\n`); console.log((await page.innerText('body')).replace(/\s+/g,' ').slice(0, 20000));
    await browser.close();
  } catch (e) { console.log('FAIL', url, e.message.split('\n')[0]); process.exit(2); }
})();
