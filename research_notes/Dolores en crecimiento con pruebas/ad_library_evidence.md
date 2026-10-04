# Ad-library evidence of long-running paid ads for replicable B2B / prosumer digital offers (Spain, EU, global)

Observation date for everything below: 2026-10-04.

**Critical access note (read first).** In this environment the network egress proxy returned `403` on CONNECT for every ad-library host and for every landing page I tried. Specifically blocked (both via curl and via the WebFetch tool, which reported `EGRESS_BLOCKED`): `facebook.com/ads/library`, `graph.facebook.com` (Ads Archive API), `transparency.meta.com`, `adstransparency.google.com`, `linkedin.com/ad-library`, `ads.tiktok.com` / `library.tiktok.com`, and third-party ad-spy mirrors (`bigspy.com`, `app.foreplay.co`, `adspyder.io`, `adheart.me`, `poweradspy.com`, `minea.com`, `atria.co`, `adbeat.com`), plus every advertiser landing page tested (`advisera.com`, `hightable.io`, `revoluziona.gumroad.com`, `billin.net`, `upliora.es`). The only working tool was web search (server-side), which returns titles, URLs and short snippets.

**Consequence for the assignment's hard constraint ("only include ads whose start date and active status you actually observed"):** I was unable to observe *any* ad start date or active status first-hand in any of the four libraries. Therefore this file contains **zero first-hand ad-library observations**. Everything in it is either (a) a documented account of what each library exposes and how to collect it, (b) clearly-labelled **secondary** ad-library summaries surfaced via search snippets, or (c) landing-page pricing surfaced via search snippets (not fetched pages). The report writer should treat the advertiser list as a *candidate shortlist to verify*, not as verified evidence of 6+ months of continuous ads.

---

## Key Question 1 — Meta Ad Library (Spain / EU, active ads): which advertisers in compliance, invoicing, Verifactu, cybersecurity policies, ISO templates, technical documentation, CE marking, AI automation, Notion/Excel systems have 2025/early-2026 start dates and are still active?

### Takeaway
Not observable from this environment: the Meta Ad Library (and its Graph API) was egress-blocked, and search engines do not index individual ad-library result pages, so no advertiser, start date or active-variant count could be confirmed. The only Meta-library-derived datapoints I could obtain are secondary (opus.pro mirror: Vanta 10 active creatives averaging 171 days run time; Drata also indexed) and are global/English, not Spain-specific.

### Cited Findings
- The Meta Ad Library shows "the ad creative, start dates, platforms, and active status of any advertiser, plus impression ranges for all ads", and allows filtering by status (active/inactive), platform, language and creation date — [Trendtrack guide](https://www.trendtrack.io/es/blog-post/facebook-ad-library-definicion-y-guia-2026); [Metricool](https://metricool.com/es/biblioteca-facebook-ads/)
- For EU-delivered ads (Spain included) Meta surfaces beneficiary/payer disclosures and shows "location, age, and gender used in ad targeting"; ads are stored for seven years regardless of status, and inactive EU/UK ads are archived "for one year after their last impression" — [Influencer Marketing Hub, ad transparency centers](https://influencermarketinghub.com/ad-transparency-centers-libraries)
- The Ad Library itself "doesn't let you track ad longevity — you can't see how many days an ad has been running"; practitioners work around this by reading each ad's "Started running on" date and filtering for ads active 14–30+ days as the proxy for proven messaging — [Adkit, SaaS ad examples](https://adkit.so/resources/ads-examples/saas-ad-examples); [Marpipe](https://www.marpipe.com/blog/mastering-the-facebook-ad-library)
- Secondary source, global/English: opus.pro's mirror of the Facebook Ad Library for **Vanta** (SOC 2 / ISO 27001 compliance automation) states "Across the 10 ads indexed, the average run time is 171 days" with "10 active creatives currently tracked", ranked by run duration — [opus.pro Vanta ad library](https://www.opus.pro/agent/ads-library/vanta-ads) (secondary; observation of the snippet 2026-10-04; underlying page not fetched)
- Secondary source, global/English: opus.pro also indexes **Drata** ads "ranked by run duration" — [opus.pro Drata ad library](https://www.opus.pro/agent/ads-library/drata-ads) (snippet did not show the number of ads or average run time)
- Secondary source showing the methodology is feasible: Adligator pulled monday.com's full Meta Ad Library history (1,880 ads) "on 19 August 2026 by searching monday.com's Facebook page ID (314197722000030); the live Meta Ad Library was cross-checked the same day" — [Adligator monday.com case study](https://adligator.com/blog/monday-com-facebook-ads-b2b-saas-case-study)
- A `site:facebook.com/ads/library verifactu` search returned no indexed ad-library pages at all (only Verifactu explainers from Zoho, Xolo, Holded) — [search result set, e.g. Holded Verifactu ebook LP](https://www.holded.com/lp/ebook-verifactu-smes)
- The compliance-automation category (Vanta, Secureframe, Drata, Thoropass/Laika) is explicitly described as "fueling a race to acquire customers via paid advertising" after raising "a total of $441M" — [Sacra](https://sacra.com/p/vanta-secureframe-laika-arming-the-rebels/) (context for why these are the long-running Meta advertisers in the compliance space)

### Inferences
- The Vanta figure (10 active creatives, mean 171 days) is the closest thing to a "6+ month continuous ads" signal I could obtain, and it is for a demo-led enterprise SaaS, not a self-serve product — so it is evidence that the *pain* (audit-ready compliance documentation) sustains paid acquisition, not that a faceless self-serve kit is being advertised that long.
- Because no Spain-filtered Meta results could be observed, no claim can be made about Verifactu/ISO/CE/Notion advertisers in Spain having 2025 start dates. Candidate Spanish advertisers to verify (based on their visibility in Verifactu/compliance search results, not on ad data): Holded, Quipu, Billin, Anfix, ContaSimple, FacturaDirecta, Declarando, Billeo, Lido, Advisera (ES localised site).

### Gaps
- No Meta Ad Library start dates, active status or variant counts for any Spain/EU advertiser (egress blocked; API blocked).
- Whether Advisera, High Table, or any Gumroad/Notion-template seller runs Meta ads at all — not observable.
- Exact observation date behind the opus.pro Vanta/Drata figures (the mirror describes itself as "live", but I could not open it to confirm the snapshot date).

---

## Key Question 2 — Google Ads Transparency Center (Spain / EU, last 12 months): which advertisers run search/display ads in these categories?

### Takeaway
Not observable: `adstransparency.google.com` was blocked and its advertiser pages are not indexed by search engines. The library does expose first-shown dates, times-shown ranges and audience summaries for EEA regions (Spain qualifies), so the data exists but could not be read here.

### Cited Findings
- The Ads Transparency Center lets users see "the ads an advertiser has run, which ads were shown in a certain region, and the last date an ad ran and the format of the ad", searchable by advertiser or website with topic, time and country filters; Google expanded it in 2025 with improved advertiser identity visibility — [Influencer Marketing Hub](https://influencermarketinghub.com/ad-transparency-centers-libraries); [Google Ads policy help](https://support.google.com/adspolicy/answer/13733850)
- When the region is switched to Germany "or any other EEA country", each ad additionally shows "a first-shown date, a times-shown range, a topic label, and a summary of the audience selection" — [Moda, Google Ads Transparency Center guide](https://moda.app/blog/google-ads-transparency-center)
- A `site:adstransparency.google.com` query for Holded / Quipu / Billin / Advisera returned only scraper tooling, confirming the advertiser pages are not search-indexed — e.g. [Apify Google Ads Transparency scraper](https://apify.com/scraperoka/google-ads-transparency-scraper); [Apify scraper by advertiser name](https://apify.com/sourcedirect/google-ads-transparency-scraper.md)
- Verifactu market context driving search demand: Verifactu becomes mandatory 1 Jan 2027 for companies (turnover under €6M) and 1 Jul 2027 for self-employed, after a one-year postponement announced Dec 2025 — [Última Hora](https://www.ultimahora.es/noticias/nacional/2025/12/02/2523773/verifactu-sistema-facturacion-digital-pymes-autonomos-aplaza-ano.html); [Billdu FAQ](https://faq.billdu.com/en/articles/15230054-what-is-verifactu-spain)
- Advertisers with Verifactu-focused landing pages / content surfaced in search (candidates to check in the Transparency Center): Holded ([Verifactu SME ebook LP](https://www.holded.com/lp/ebook-verifactu-smes)), Billin ([Verifactu software comparison](https://www.billin.net/blog/mejores-programas-verifactu/)), Billeo ([Verifactu landing](https://www.billeo.es/software-facturacion-verifactu)), Lido ([e-invoicing for autónomos](https://www.lido.app/es/factura-electronica-autonomos)), Declarando ([site](https://declarando.es/?p=39334)), Zoho Books ([Verifactu KB](https://www.zoho.com/en-fr/books/kb/e-invoicing/spain/what-is-verifactu.html)), Xolo ([Verifactu FAQ](https://www.xolo.io/zz-es/faq/xolo-spain/category/platform/article/what-is-verifactu))

### Inferences
- The Verifactu deadline slip to 2027 means Spanish invoicing SaaS have a known, extended window to keep running "avoid sanctions" search ads; a faceless brand could compete on the documentation/explainer side (checklists, comparison reports) rather than on the regulated software itself, which requires AEAT-compliant systems.

### Gaps
- No Google Ads Transparency data (advertiser list, first-shown dates, formats) for Spain or any EU country — blocked.
- No evidence on whether template/kit sellers (Advisera, High Table, Gumroad sellers) run Google search ads in Spain.

---

## Key Question 3 — LinkedIn Ad Library: which B2B advertisers target compliance / documentation pains with long-running campaigns?

### Takeaway
Not observable: `linkedin.com/ad-library` was blocked and `site:linkedin.com/ad-library` returned nothing indexed. The library does expose run dates and impression bands for EU-targeted ads (since June 2023), which is exactly the data the assignment needs, and third-party tools exist that sort LinkedIn ads by days running.

### Cited Findings
- LinkedIn's Ad Library is "a free, public database of every ad that has run on LinkedIn since June 2023", built for the EU Digital Services Act; "run dates, impressions bands, impression splits by country, and targeting choices are shown only for ads targeting the European Union" — [Lunio, LinkedIn Ads Library](https://www.lunio.ai/blog/linkedin-ads-library?hsLang=en); [Moda, LinkedIn Ad Library](https://moda.app/blog/linkedin-ad-library)
- "The dates the ad ran and estimated total impressions as a band (such as 1k to 5k) are shown only when targeting includes the EU"; impressions by country are rounded to the nearest percent — [Apify, Long-Running LinkedIn Ads Finder](https://apify.com/davidbenittah/long-running-linkedin-ads-finder.md)
- Tooling exists to list LinkedIn ads "running 30+ days for any keyword or advertiser", sorted by days running with headline, body, CTA and campaign period — [Apify Long-Running LinkedIn Ads Finder](https://apify.com/davidbenittah/long-running-linkedin-ads-finder); worked example [auditing HubSpot's longest-running ads](https://apify.com/davidbenittah/long-running-linkedin-ads-finder/examples/competitor-advertiser-audit)
- Searches `site:linkedin.com/ad-library ISO 27001 templates` and `site:linkedin.com/ad-library Verifactu` returned no ad-library pages; instead they surfaced the organic template sellers High Table ([ISO 27001 templates](https://hightable.io/product-category/iso-27001-templates)) and UpGuard ([free ISO 27001 templates](https://upguard.com/templates/iso-27001)) and Verifactu explainers from Sovos and VAT IT ([VAT IT Spain Verifactu guide](https://vatit.com/nl/e-invoicing-guide/spain-verifactu/))

### Inferences
- The LinkedIn library is the most promising of the three for the assignment because EU-targeted ads carry explicit run dates; a follow-up from an unblocked network should query keywords "ISO 27001", "SOC 2", "RGPD", "Verifactu", "NIS2", "CE marking", "documentación técnica" with country = Spain and sort by campaign period.

### Gaps
- No LinkedIn advertiser, run date or impression band observed for any compliance/documentation ad.

---

## Key Question 4 — What do landing pages reveal about pricing, guarantees and self-serve vs. demo? (Prioritise self-serve.)

### Takeaway
Landing pages could not be fetched (blocked), but search snippets give enough to classify a handful of offers: ISO 27001 document toolkits (Advisera ~US$797–997; High Table £597 with certification-or-money-back guarantee) and Spanish invoicing SaaS (€7–35/month) are self-serve; Gumroad Notion "sistema de empresa" templates sell at $8–50; RGPD kits for SMEs sell at ~€25; AI-automation for Spanish SMEs is priced as services (€2.5k–25k setup), i.e. not self-serve.

### Cited Findings
**ISO / information-security document packs (self-serve checkout, instant download)**
- Advisera (ES-localised site) sells ISO 27001 document toolkits with 37–100 editable Word/Excel documents; price shown in USD ("USD $797" in the pricing snippet); after payment "envían un correo electrónico con un enlace para descargar los documentos"; accepts credit card or bank transfer — [Advisera ES pricing](https://advisera.com/27001academy/es/precios/)
- Advisera's consultant package is "$997 USD and includes 64 documents covering all requirements for both ISO 27001 and ISO 22301" — [Advisera ES product tour](https://advisera.com/27001academy/es/tour-del-producto)
- Advisera: "Immediately after the transaction is processed, you will receive an email with a download link for instant access" — [Advisera help FAQ](https://help.advisera.com/?p=2084); GDPR toolkit individual docs priced e.g. €49.90 — [Advisera RGPD documents](https://advisera.com/es/documentos-del-paquete/rgpd-ue/descripcion-del-puesto-de-delegado-de-proteccion-de-datos/)
- Advisera's content hook is a free preview download of every toolkit ("Descargue una vista previa gratuita"), i.e. lead-magnet funnel — [Advisera ISO 27001 free preview ES](https://advisera.com/es/iso-27001-vistaprevia-gratuita/); [Advisera RGPD free preview ES](https://advisera.com/es/rgpd-ue-vistaprevia-gratuita/)
- High Table (UK, English, global): ISO 27001 Toolkit Business Edition priced "£597.00", with "a guarantee of your certification – or you can have your money back" and a "100% No-Risk Money Back Guarantee"; includes a free consultation meeting and weekly clinics — [High Table toolkit pricing](https://hightable.io/iso-27001-toolkit-pricing/); [High Table Business Edition product](https://hightable.io/product/iso-27001-templates-toolkit/)
- Other ISO 27001 toolkit sellers visible organically: IT Governance (UK, "leading provider of IT GRC documentation toolkits") — [Cambridge Network](https://www.cambridgenetwork.co.uk/news/tried-and-tested-tools-streamline-iso-27001-isms-implementation-says-it-governance); GRC Solutions EU store — [grcsolutions.io ISO 27001 toolkit](https://eu.grcsolutions.io/product/iso-27001-toolkit); The Art of Service — [store](https://store.theartofservice.com/ISO-27001-Toolkit)

**RGPD / data-protection kits for Spanish SMEs (self-serve, low ticket)**
- "KIT RGPD Y FIRMA DIGITAL" on Gumroad by Revoluziona: €25; for "emprendedores, autónomos y pymes"; promise is complying with GDPR "sin contactar a profesionales externos"; includes aviso legal, política de privacidad, capas informativas, política de cookies, condiciones de contratación, formularios de derechos, consentimiento WhatsApp — [Revoluziona Gumroad](https://revoluziona.gumroad.com/l/rgdp)
- Reference budget for SME data-protection compliance: €100–500/yr basic, €500–2,000/yr medium — [Usercentrics ES checklist PDF](https://usercentrics.com/es/wp-content/uploads/sites/6/2026/05/Checklist_-Costes-de-proteccion-de-datos-para-tu-empresa.pdf)

**Verifactu / invoicing SaaS for autónomos (self-serve monthly plans)**
- Basic-plan prices: Holded €14/mo, Quipu €9.50/mo, Anfix €19.90/mo, ContaSimple €9.99/mo, FacturaDirecta €7/mo, Sage 50 €35/mo — [WWWhatsnew apps para autónomos 2026](https://wwwhatsnew.com/?p=492420)
- Billin Pro plan €9/mo with Verifactu included from March 2026 — [Billin, mejores programas Verifactu](https://www.billin.net/blog/mejores-programas-verifactu/)
- Pain named in category content: "evitan sanciones" (avoid penalties) — [Ecosistema Startup, Verifactu 2026 apps](https://ecosistemastartup.com/?p=81586); "autónomos en alerta" — [Vozpópuli](https://www.vozpopuli.com/economia/autonomos-en-alerta-quienes-quedaran-fuera-del-sistema-verifactu-y-que-debes-saber-sobre-la-nueva-factura.html)

**Notion business systems for Spanish-speaking SMEs (self-serve, Gumroad)**
- "Administra Toda tu Empresa en Notion" $8 — [Gumroad](https://saracatcas.gumroad.com/l/tuempresaentera); "Sistema de Empresa" $19 and "Sistema de Empresa Óptimo" $29 — [Gumroad Valkyrie28](https://valkyrie28.gumroad.com/l/etttr), [Gumroad Valkyrie28](https://valkyrie28.gumroad.com/l/vgqfo); "Administrador de Empresas Avanzadas" $29 — [Gumroad](https://picassoespanol.gumroad.com/l/hrdgau); "Plantilla Notion PYMEs" $50 including 30 min consulting — [Gumroad](https://szapatae7.gumroad.com/l/cxebp)

**AI automation for Spanish SMEs (service-led, not self-serve)**
- Spanish SME AI projects quoted at €2,500 (autónomo) to €25,000 setup, plus €200–800/mo operation; AI agents per flow €5,000–15,000 setup + €300–600/mo; back-office automation (n8n + AI) €5,000–12,000 setup; in-company workshop €3,500–5,500 — [Upliora, coste agentes IA pymes 2026](https://www.upliora.es/blog/coste-agentes-ia-pymes-espana-2026); [Upliora, cuánto cuesta implementar IA](https://www.upliora.es/blog/cuanto-cuesta-implementar-ia-pyme-espana-por-tipo-proyecto-2026)

**CE marking / technical file**
- No self-serve Spanish CE-marking template kit surfaced; the market is service-priced (e.g. EU MDR technical documentation compilation "$12,000 (documentation only) or $25,000") — [Pure Global, technical file cost 2026](https://www.pureglobal.com/es/blog-posts/medical-device-technical-file-compilation-cost-2026); only a generic English "CE Marking and Machinery Directive Kit" from The Art of Service appeared — [store](https://store.theartofservice.com/ce-marking-and-machinery-directive-kit-publication-date-2024-03/)

### Inferences
- The clearest self-serve, faceless-replicable models with visible pricing are the ISO/RGPD document toolkits (€25 to ~£600/US$1,000) sold with free previews and money-back/certification guarantees; the strong guarantee (High Table) is itself a replicable offer lever.
- AI-automation-for-SMEs in Spain is currently monetised almost entirely as services/demos; a faceless digital product here would be a gap, not a proven pattern.
- Spanish Notion "business system" templates are a crowded, low-price ($8–50) Gumroad niche with no observed paid-ad activity.

### Gaps
- No landing page was fetched, so guarantees, checkout flows and exact EUR prices are from snippets only (Advisera's ES page showed USD, not EUR). Whether any of these sellers runs *ads* (vs. SEO only) remains unverified.
- No CE-marking or technical-documentation self-serve kit for Spain/EU was found.

---

## Key Question 5 — Which pains recur across many advertisers (crowded) vs. few long-running advertisers (profitable but less contested)?

### Takeaway
With no first-hand ad counts, crowding can only be inferred from the number of distinct sellers visible in search: Verifactu/invoicing SaaS (≥8 brands) and Notion business templates (≥6 Gumroad sellers) look crowded; ISO 27001 toolkits have a small set of established sellers (Advisera, High Table, IT Governance, GRC Solutions) with high tickets and guarantees; RGPD kits for Spanish SMEs and CE-marking/technical-documentation kits have the fewest visible sellers.

### Cited Findings
- Crowded (invoicing/Verifactu): at least Holded, Quipu, Anfix, ContaSimple, FacturaDirecta, Sage 50, Billin, Billeo, Lido, Declarando, Zoho Books and Xolo all publish Verifactu offers — [WWWhatsnew](https://wwwhatsnew.com/?p=492420); [Billin](https://www.billin.net/blog/mejores-programas-verifactu/); [Billeo](https://www.billeo.es/software-facturacion-verifactu); [Lido](https://www.lido.app/es/factura-electronica-autonomos); [Zoho](https://www.zoho.com/en-fr/books/kb/e-invoicing/spain/what-is-verifactu.html); [Xolo](https://www.xolo.io/zz-es/faq/xolo-spain/category/platform/article/what-is-verifactu)
- Crowded (Notion business systems ES): ≥6 distinct Gumroad sellers at $8–50 — [Gumroad listing examples](https://valkyrie28.gumroad.com/l/vgqfo), [Gumroad](https://picassoespanol.gumroad.com/l/hrdgau), [Gumroad](https://saracatcas.gumroad.com/l/tuempresaentera)
- Compliance automation (SOC 2 / ISO 27001 SaaS, global): well-funded cohort ($441M raised) in a "race to acquire customers via paid advertising"; Vanta's mirror shows 10 active creatives with a 171-day mean run — [Sacra](https://sacra.com/p/vanta-secureframe-laika-arming-the-rebels/); [opus.pro Vanta](https://www.opus.pro/agent/ads-library/vanta-ads) (secondary)
- Less contested (ISO 27001 *document toolkits*): a handful of sellers with premium tickets and guarantees — Advisera US$797–997 ([pricing](https://advisera.com/27001academy/es/precios/)), High Table £597 with money-back ([pricing](https://hightable.io/iso-27001-toolkit-pricing/)), IT Governance ([news](https://www.cambridgenetwork.co.uk/news/tried-and-tested-tools-streamline-iso-27001-isms-implementation-says-it-governance)), GRC Solutions ([store](https://eu.grcsolutions.io/product/iso-27001-toolkit))
- Least visible sellers (RGPD kit ES; CE marking kit ES): one €25 Gumroad RGPD kit ([Revoluziona](https://revoluziona.gumroad.com/l/rgdp)) and no Spanish CE-marking kit; Advisera covers RGPD only via per-document sales ([Advisera RGPD](https://advisera.com/es/documentos-del-paquete/rgpd-ue/politica-de-proteccion-de-datos-personales/))

### Inferences
- Recurring pain language across categories: "evitar sanciones" (Verifactu), "cumplir sin profesionales externos" (RGPD kit), "guaranteed certification / money back" (ISO toolkits), "audit-ready" (compliance SaaS). Sanction-avoidance plus "do it without a consultant" is the common thread a faceless brand can reuse.
- Advisera's localised Spanish ISO/RGPD toolkits priced in USD suggest an opening for a EUR-priced, Spain-specific document pack (ENS, RGPD+LSSI, Verifactu readiness checklist), but this is an inference from pricing/localisation, not from ad data.

### Gaps
- Crowding could not be measured by active-ad counts or advertiser counts in any library; the above ranking is by organic search visibility and should be re-run against the Meta/LinkedIn libraries from an unblocked network.
- TikTok Creative Center top ads for Spain were not accessible at all (blocked), so no TikTok evidence exists in this file.

---

## Recommended verification protocol (for whoever can reach the libraries)
- Meta: `facebook.com/ads/library/?active_status=active&ad_type=all&country=ES&q=<term>&search_type=keyword_unordered`; record "Started running on" per ad, count active variants per Page, check "EU transparency" panel for reach by country. Terms: verifactu, ISO 27001, ENS, RGPD, NIS2, marcado CE, documentación técnica, automatización IA pymes, plantilla Notion empresa. Repeat for DE/FR/IT/PT.
- Google: `adstransparency.google.com/?region=ES&query=<advertiser or domain>`; in EEA regions each ad carries a first-shown date and times-shown range ([Moda](https://moda.app/blog/google-ads-transparency-center)).
- LinkedIn: `linkedin.com/ad-library/search?keyword=<term>&countries=ES`; EU-targeted ads show run dates and impression bands ([Lunio](https://www.lunio.ai/blog/linkedin-ads-library?hsLang=en)); sort by campaign period or use a 30+-day finder ([Apify](https://apify.com/davidbenittah/long-running-linkedin-ads-finder)).
- Start with these candidate advertisers (candidates only; none confirmed): Holded, Quipu, Billin, Anfix, ContaSimple, FacturaDirecta, Declarando, Billeo, Lido, Advisera, High Table, IT Governance, Vanta, Drata, Secureframe, Sprinto, Upliora.
