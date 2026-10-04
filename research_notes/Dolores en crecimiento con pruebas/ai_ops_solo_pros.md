# Demand for packaged "AI operating systems" for one-person businesses built on Claude Code / MCP (2026)

Observation date for everything below: 2026-10-04. Method note: the session's web-search budget was exhausted mid-task and the egress proxy blocked direct page fetches to Reddit, Hacker News, Gumroad, Maven, Udemy, Skool, Indie Hackers, Substack, Product Hunt, Wikipedia and most blogs. Only github.com, anthropic.com and claude.com pages could be fetched directly. Every other figure below comes from search-engine snippets of the cited page and should be treated as "reported by the page as indexed on 2026-10-04", not as a verified read of the full page. Items that could not be verified at all are in Gaps.

## KQ1. How fast is interest in Claude Code and MCP growing (Trends, GitHub stars, npm, Anthropic announcements)?

### Takeaway
Hard numbers point to very fast growth through 2026: Claude Code's repo went from ~138k stars (Feb 2026) to 149.4k (verified 2026-10-04), Anthropic's own skills repo sits at 179.6k stars, the MCP TypeScript SDK hit 35–45M weekly npm downloads in mid-2026, OpenClaw (the open-source "always-on digital employee" launched Jan 2026) reached 391k stars, and Anthropic reported Claude Code revenue growing >10x YoY with weekly active users doubling Jan→Feb 2026. Google Trends itself could not be queried; the directional proxies (HN mentions peaking Feb 2026 at 5,408/month) all point up.

### Cited Findings
**GitHub stars (verified directly on github.com, 2026-10-04)**
- anthropics/claude-code: 149.4k stars, 25.5k forks, 5k+ open issues; README now marks npm install as "Deprecated" in favour of native installers — [GitHub anthropics/claude-code](https://github.com/anthropics/claude-code)
- Earlier snapshots for comparison: 138,310 stars in Feb 2026 and 140.4k stars / 22.6k forks on 2026-08-06, i.e. roughly +11k stars Feb→Oct 2026 — [gradually.ai Claude Code statistics](https://www.gradually.ai/en/claude-code-statistics/); [gittrend.io anthropics/claude-code](https://gittrend.io/repo/anthropics/claude-code)
- anthropics/skills (official Agent Skills repo, launched Oct 2025): 179.6k stars, 21.2k forks; available in Claude Code, Claude.ai paid plans and the API; installable as a plugin marketplace (`/plugin marketplace add anthropics/skills`); Notion listed as partner skill — [GitHub anthropics/skills](https://github.com/anthropics/skills)
- modelcontextprotocol/servers: 91k stars, 11.8k forks (reference implementations only; directs users to the MCP Registry for community servers) — [GitHub modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- modelcontextprotocol/registry: 7.3k stars; launched in preview 2025-09-08, API freeze v0.1 on 2025-10-24, still "preview", no public server count on the page — [GitHub modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry)
- openclaw/openclaw: 391k stars, 82.3k forks; "open-source AI assistant that runs on your own computer and meets you in the channels you already use: Discord, iMessage, Slack, Teams, Telegram, WhatsApp, and 20+ more"; stewarded by a 501(c)(3) foundation, no paid tier; links to ClawHub skills marketplace — [GitHub openclaw/openclaw](https://github.com/openclaw/openclaw)
- OpenClaw was launched late January 2026 by Peter Steinberger and had "190k+ GitHub stars" when the Wikipedia snippet was indexed, so it roughly doubled to 391k by Oct 2026 — [Wikipedia: Peter Steinberger](https://en.wikipedia.org/wiki/Peter_Steinberger_(programmer)) (snippet only)
- Community aggregators: davila7/claude-code-templates 32.4k stars (free, MIT; agents, commands, hooks, MCPs, 100+ components) — [GitHub davila7/claude-code-templates](https://github.com/davila7/claude-code-templates); hesreallyhim/awesome-claude-code 55.1k stars, developer-oriented with no business-ops section — [GitHub awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

**npm downloads (snippets; api.npmjs.org was blocked)**
- @modelcontextprotocol/sdk weekly downloads in 2026: 35.5M (early June), 39.3M (late June), 35.6M (mid-July), 39.6M and 45.5M (late July 2026) — [Builder Radar newsletter archive](https://buttondown.com/Builder-Radar/archive/)
- On 2026-07-27 the SDK was split into nine packages (@modelcontextprotocol/server, /client, ...), and six weeks later the legacy @modelcontextprotocol/sdk still accounted for 86% of weekly installs across the three — [thepromptshelf.dev MCP SDK v2 migration](https://thepromptshelf.dev/blog/mcp-typescript-sdk-v2-migration-claude-md-2026)
- Snyk Advisor page shows 10,476,355 weekly downloads for @modelcontextprotocol/sdk (date of the snapshot not visible; conflicts with the 35–45M figures above, probably because of the package split) — [Snyk Advisor @modelcontextprotocol/sdk](https://dev.snyk.io/advisor/npm-package/@modelcontextprotocol/sdk)
- Claude Code npm: 47.6M downloads in the 30 days before Feb 2026 — [gradually.ai](https://www.gradually.ai/en/claude-code-statistics/) (npm distribution has since been deprecated per the repo README, so npm is no longer a usable 2026 proxy)

**Anthropic announcements (money, not hype)**
- 2026-02-12: Anthropic raised $30B Series G; Claude Code revenue "growing more than 10x year over year"; 4% of GitHub public commits attributed to Claude Code — [Gigazine 2026-02-13](https://www.gigazine.net/gsc_news/en/20260213-anthropic-30-billion-series-g-funding); [Simon Willison 2026-02-12](https://feeds.simonwillison.net/2026/Feb/12/anthropic/)
- Claude Code weekly active users doubled Jan→Feb 2026; 2026 Claude Code revenue expected to exceed $2.5B; >50% of Claude Code revenue from businesses; corporate subscription plans up 4x since start of 2026 — [36kr](https://eu.36kr.com/en/p/3681105640910722); [Sacra Anthropic](https://sacra.com/c/anthropic)
- Anthropic revenue: >$100M (2024), >$1B (2025), projected $14B (2026) — [Sacra](https://sacra.com/c/anthropic); [getpanto Anthropic statistics](https://www.getpanto.ai/blog/anthropic-ai-statistics)
- Claude Code "overtook GitHub Copilot and Cursor within 8 months" to become the most-used AI coding agent (third-party claim) — [gradually.ai](https://www.gradually.ai/en/claude-code-statistics/)
- Agent Skills launched 2025-10-16 for Claude apps (Pro/Max/Team/Enterprise), API, Claude Code and Agent SDK; partners Box, Canva, Notion, Rakuten ("What once took a day, we can now accomplish in an hour") — [claude.com/blog/skills](https://claude.com/blog/skills) (fetched directly)
- Agent Skills spec published as an open standard at agentskills.io on 2025-12-18 — [Verdent Claude Skills timeline](https://www.verdent.ai/guides/claude-skills-announcement-news)
- Claude Cowork (GUI, non-technical "Claude Code") launched in research preview 2026-01-30; "Record a Skill" (screen recording + voice → reusable skill) shipped 2026-07-21 — [unite.ai](https://www.unite.ai/anthropic-brings-claude-code-power-to-everyone-with-cowork); [The AI Colony](https://theaicolony.beehiiv.com/p/anthropic-launches-claude-cowork-for-non-coders); [aiweekly.co Record a Skill](https://aiweekly.co/alerts/anthropic-ships-record-a-skill-in-claude-cowork-desktop-app)
- Cowork page (fetched directly, latest update 2026-08-26): targets "marketing, sales, legal, finance, and business operations"; included in Pro $17–20/mo, Max $100/$200, Team $20/seat; "Skills" sold as domain bundles (Brand Voice, Legal, Finance); scheduled unattended runs — [claude.com/blog/cowork-research-preview](https://claude.com/blog/cowork-research-preview)
- Claude Code "Projects" relaunched 2026-09-17 as coordinator + parallel cloud agent threads — [theaicareerlab](https://theaicareerlab.com/blog/claude-code-projects-parallel-agents-beta-2026)
- X (Twitter) shipped a hosted remote MCP server with 200+ endpoints on 2026-06-30 (sign that mainstream platforms are exposing MCP) — [usecarly.com](https://www.usecarly.com/blog/claude-twitter-integration/)

**Attention proxies**
- "Claude Code" mentioned 50,420 times on Hacker News 2009–2026, peaking Feb 2026 at 5,408 mentions in one month — [Hacker Trends](https://hackernewstrends.com/trends/claude-code)
- Google's own Trends API alpha (July 2025) exists and several Google-Trends MCP servers are available, but no published 24-month chart for "Claude Code"/"MCP" was found — [Houtini Google Trends in Claude Code](https://houtini.com/articles/how-to-connect-google-trends-to-claude-code/)

### Inferences
- The growth is real and recent (most inflection in Jan–Feb 2026: Cowork launch, OpenClaw, Series G, HN peak), which is exactly the window in which non-developers started being addressed by Anthropic itself.
- Anthropic is moving down-market toward the target buyer (Cowork for "business operations", Record-a-Skill, Pro plan at $17–20). This both validates the pain and threatens third-party "setup" products: the vendor is packaging workflows itself.
- npm download numbers for MCP are inflated by CI installs; use them as direction (up 2025→mid-2026), not as user counts.

### Gaps
- Google Trends 24-month index values for "Claude Code", "MCP", "AI agents for business": not obtainable (no fetchable source; search budget exhausted). Needs a manual Trends pull.
- Exact MCP Registry server count and @modelcontextprotocol/* monthly download series: api.npmjs.org and registry pages blocked.
- Star-history curves (star-history.com) not fetchable; only point snapshots above.

## KQ2. What do solo consultants and freelancers say they struggle with when setting this up? (verbatim, 2026)

### Takeaway
The dominant complaint is not "the AI is weak" but "setup is the wall": MCP/terminal configuration, cryptic errors, and lack of a pre-wired business context make most non-technical operators give up or copy-paste manually. The credible 2026 practitioner accounts that work (consultants running inbox/CRM/proposals on Claude Code) all describe a self-built folder-of-CLAUDE.md-files system plus one CRM as source of truth, i.e. exactly what a packaged product would ship. Verbatim Reddit/X quotes could not be retrieved (blocked), so the quotes below are from indexed newsletters and blogs.

### Cited Findings
- Setup pain, stated plainly: "Understanding MCP and implementing it are two completely different challenges, and most people give up after the first cryptic error message or don't even try given the complexity of the implementation process." — [aimaker.substack.com, MCP video walkthrough](https://aimaker.substack.com/p/how-to-implement-mcp-claude-desktop-video-walkthrough-notion-firecrawl-zapier-perplexity-brave-search)
- Same source frames the pre-MCP state as the pain: "Without MCP, you're copying and pasting between Claude and everything else. With MCP, Claude reads your real data, takes actions, and remembers across sessions." Notion MCP described as "the easiest starting point" for non-technical work — [Build to Launch: Best MCP servers for Claude Code](https://buildtolaunch.substack.com/p/best-mcp-servers-claude-code)
- Non-technical framing of what Claude Code is: "Claude Code without MCP is like a phone that only makes calls — MCP servers are the apps"; "over 1,000 already exist" — [Build to Launch](https://buildtolaunch.substack.com/p/best-mcp-servers-claude-code)
- Guide aimed at non-technical users exists because the terminal is the barrier: Cowork "removes the terminal barrier that has kept one of the most powerful AI tools inaccessible to the majority of professionals" — [unite.ai on Cowork](https://www.unite.ai/anthropic-brings-claude-code-power-to-everyone-with-cowork)
- Solo consultant practice description (2026): the practice "lives in a version-controlled folder that Claude reads at the start of every session, with Close CRM as the source of truth"; "Each client is a folder with inside it: a CLAUDE.md that tells any session the rules for that account, meeting notes by date, a research folder, a delivery folder with one subfolder per project, and a reference folder for the durable facts." — [Amit Kothari, How I run my whole consulting practice with Claude](https://amitkoth.com/how-i-run-consulting-claude/)
- Second solo-consultant account titled "AI for Consultants: How a Solo Practice Runs on Claude (2026)" — [justinmckelvey.com](https://justinmckelvey.com/blog/ai-for-consultants) (content not fetchable)
- Freelancer newsletter "I Built 11 Claude Workflows That Run My Freelance Business on Autopilot" lists a morning brief that "reads Gmail, Calendar, and Notion", and a lead workflow that "enriches companies, scores leads, and drafts personalized replies or referrals while logging everything in a Notion CRM"; author also sells a Gumroad pack "+200 Claude Prompts & Skills" — [Growth with Alex #14](https://growthwithalex.substack.com/p/14-i-built-11-claude-workflows-that); [growthwithalex.gumroad.com](https://growthwithalex.gumroad.com/l/aayyyy)
- Consultant-specific skills list "the Claude Code skills a solo consultant should actually run": proposal-writer ("interview you about a prospect, then produce a 3–5 page proposal"), meeting-notes summariser ("transcript in (Otter, Granola, Read.ai), structured notes out: decisions, action items with owners, open questions"), follow-up-sequencer ("four-touch cadence after a discovery call, a proposal send...") — [Knack: Claude Code skills for consultants](https://knack.run/blog/claude-code-skills-for-consultants/)
- Inbox use case is already a flagship demo: "One user manages their entire inbox through Claude Code, with it filtering out noise and only showing emails that actually need a reply" — [Michael Crist, Non-Technical Person's Complete Guide to Claude Code](https://michaelcrist.substack.com/p/claude-code)
- CRM vendor pitching the exact workflow: "find every deal with a positive LinkedIn or WhatsApp reply in the last 7 days, move them to qualified, and create follow-up tasks"; Breakcold exposes "54 tools" via its Claude integration — [Breakcold: 6 CRMs wired to Claude](https://www.breakcold.com/blog/best-crms-with-claude-integration)
- OpenClaw solo-founder setups: "Founders who push through the first two weeks of setup end up running operations that would have required a $3,000–$5,000/month virtual assistant budget" and "Early adopters report 20–50 hours per week saved" (vendor-blog claims, not independent) — [solvea.cx OpenClaw solo founder setup](https://solvea.cx/blog/openclaw-solo-founder-setup); [solobusinesshub](https://www.solobusinesshub.com/act-now/openclaw-2026-ai-revolution/)
- "Community-validated starting point for solopreneur automation is the four-agent stack: an orchestrator (Claude), a dev agent (Codex), a marketing agent (Gemini), and a business agent" — [superframeworks OpenClaw business ideas](https://superframeworks.com/articles/openclaw-business-ideas-indie-hackers)
- Guides explicitly for business owners exist as multi-part series ("Claude Code for business owners: 5 core concepts", parts 1–3) — [MindStudio](https://www.mindstudio.ai/blog/claude-code-business-owners-5-core-concepts)
- HN thread "Claude for Small Business" exists (item 48130950) and "Tell HN: I'm 60 years old. Claude Code has re-ignited a passion" (item 47282777), both 2026 — [HN 48130950](https://news.ycombinator.com/item?id=48130950); [HN 47282777](https://news.ycombinator.com/item?id=47282777) (content not fetchable)
- Established-vendor shortfall for solo operators (where the DIY pain comes from): Zapier Professional "$19.99/month for just 750 tasks" vs Make "10,000 operations for $9/month"; "strict no-refund policy"; "the more successful your automations become, the more you pay"; users "recommend introducing a subscription tier tailored for freelancers" — [tryorbye Zapier review 2026](https://www.tryorbye.com/products/zapier); [syncgtm Zapier review](https://syncgtm.com/blog/zapier-review); [checkthat.ai Zapier reviews](https://checkthat.ai/brands/zapier/reviews)
- HubSpot Breeze: "one HubSpot Solutions Partner reported that after demoing Breeze to four clients, all four declined to upgrade"; "buying a CRM to save fifty cents a resolution never pays back"; onboarding fees "$1,500 up to $7,000+" — [default.com Breeze review](https://www.default.com/post/hubspot-breeze-ai-review-and-pricing); [a8gent Breeze](https://a8gent.com/platforms/hubspot-breeze); [resolve247 Breeze pricing](https://resolve247.ai/blog/hubspot-ai-agent-pricing/)
- Notion AI: "The extra is actually way more expensive than the Pro plan I subscribed to" (user complaint quoted) — [eesel.ai Notion AI review 2026](https://www.eesel.ai/blog/notion-ai-review)

### Inferences
- The pain is concentrated at step zero (install, connect Gmail/Calendar/Notion/CRM via MCP, write the first CLAUDE.md) rather than at prompt quality; a product that ships a working folder structure + connector setup + approval gate addresses the stated failure point.
- The practitioners who succeeded converged on the same architecture (per-client folders, CLAUDE.md rules, one CRM as truth, morning brief, meeting-notes → actions, proposal generator). That convergence is evidence the "operating system" framing matches how buyers already think.
- Incumbent tools (Zapier, HubSpot, Notion AI) are priced for teams; solo operators explicitly ask for a cheaper tier. A sub-200 EUR one-off sits far below their annual cost.

### Gaps
- No verbatim Reddit (r/ClaudeAI, r/ClaudeCode, r/consulting, r/freelance) or X posts with dates/links could be retrieved: Reddit, HN and X fetches were blocked and search budget ran out before targeted quote mining. This is the biggest hole; a manual pass on those subreddits is needed.
- No evidence yet on "approval queue" as a stated need in buyers' own words.

## KQ3. Which paid products in this space show real traction (sales, reviews, revenue posts)? Include Spanish-language offers.

### Takeaway
Many products exist, few publish numbers. The strongest money evidence: a marketing consultant made $3,000 in 45 days selling 25 Claude skills at $99; one creator reports >$10k since March 2026 from a one-time-purchase "skill stack"; Skool communities for Claude Code show 8k members at $9/mo and several at $29–97/mo; Maven cohorts on "AI agents that run your business (Claude)" at $695–$1,300; a Notion "Second Brain" template with 23,000+ downloads and 334 five-star ratings. Spanish-language supply is courses (125–590 EUR), not packaged operating systems.

### Cited Findings
**Skill packs / templates (digital products, no call)**
- "The Solopreneur Skills Pack — 5 Claude Code Skills for Solo Builders", $24, skills /anti-slop, /repurpose, /weekly-review, /launch-prep, /profit-snapshot, "all future additions at no extra cost" — [soloskills.gumroad.com](https://soloskills.gumroad.com/l/sdosug) (ratings/sales not visible in snippet)
- "Claude Skills for Founders" — "40 CLAUDE.md skill files that turn Claude Code into a co-founder who knows landing pages, pricing, sales, launches, and ops" — [aidesignlab.gumroad.com](https://aidesignlab.gumroad.com/l/claude-skills-for-founders) (price not in snippet)
- ToolGenX / agentskillpacks.com: "19 products carrying 100+ skills, priced $9–$119", run by İsmail Günaydın (Istanbul) since 2022, rebuilt as own shop June 2026 on Next.js + Supabase; no sales numbers published — [agentskillpacks.com](https://www.agentskillpacks.com/)
- Claudecademy Essential $49 (environment setup, skills, agents) — listed "not currently for sale" per snippet; Claudecademy Builder $149 "system for building and selling with Claude Code" — [claudecademy.gumroad.com/l/essential](https://claudecademy.gumroad.com/l/essential); [claudecademy.gumroad.com/l/builder](https://claudecademy.gumroad.com/l/builder)
- "Master Marketing Claude Skills Bundle" — [inflectual.gumroad.com](https://inflectual.gumroad.com/l/master-marketing-claude-skills-bundle); "Claude Skills Pack - Prompt Guy" — [thinkaiprompt.gumroad.com](https://thinkaiprompt.gumroad.com/l/claude-skills); "Claude Code Prompt Pack - 50+ Battle-Tested Developer Prompts" — [maxtendies.gumroad.com](https://maxtendies.gumroad.com/l/claude-code-prompt-pack); "Claude AI Prompt Library (2026 Edition)" — [digitalwealthwithsa.gumroad.com](https://digitalwealthwithsa.gumroad.com/l/claudeprompts) (prices/ratings not in snippets)
- "Freelance OS" products on Gumroad (Notion-based freelance operating systems, pre-AI framing) — [productiveselfco.gumroad.com/l/freelanceos](https://productiveselfco.gumroad.com/l/freelanceos); [heycalvins.gumroad.com/l/freelanceos](https://heycalvins.gumroad.com/l/freelanceos)
- Notion Second Brain template: "#1 Second Brain Template on Gumroad has over 23,000 downloads and 334+ five-star ratings"; another at $47 — [heyismail.gumroad.com/l/PARA](https://heyismail.gumroad.com/l/PARA); [rixleezy.gumroad.com](https://rixleezy.gumroad.com/l/secondbrainsystem)

**Revenue posts (money, self-reported)**
- Indie Hackers: solo founder from India "made $57 in 48 hours" selling 120 Claude "cheat codes" at $5–$10 tiers — [Indie Hackers post](https://www.indiehackers.com/post/i-made-57-in-48-hours-selling-claude-cheat-codes-here-s-what-worked-and-what-didn-t-01d7f1f61c)
- "a marketing consultant made $3,000 selling 25 Claude skills he'd built for his own client work, priced at $99, with nearly all profit in 45 days" — [ryandoser.com Sell Claude Skills](https://ryandoser.com/sell-claude-skills/)
- "a skill stack product made over $10,000 passively since March as a one-time purchase" — [ryandoser.com Make money with Claude](https://ryandoser.com/make-money-with-claude/); related: "This Claude AI Side Hustle Made Me Over $5K" — [ryandoser.com](https://ryandoser.com/claude-ai-side-hustle/) (same creator; promotional, unverified)
- "CLAUDE.md configuration files, structured prompt libraries, and pre-built workflow exports are sold on platforms like Gumroad and Lemon Squeezy, with well-documented setups for specific use cases priced at $27 to $97"; "Templates work best when bundled with Claude Code skills inside a product a buyer already needed" — [bigideasdb.com](https://bigideasdb.com/how-to-make-money-with-claude-code)
- Reality check from same ecosystem: "surveys of indie-hacker products consistently find that more than half make no revenue at all, and roughly 70% earn under $1,000 in monthly recurring revenue" — [gladlabs.io](https://www.gladlabs.io/posts/decoding-the-indie-hacker-blueprint-what-revenue-r-ba48746c)
- "How to Build a Claude Code Skill That Actually Sells on Gumroad" (DEV, 2026) — [dev.to/manja316](https://dev.to/manja316/how-to-build-a-claude-code-skill-that-actually-sells-on-gumroad-4kdm) (content not fetchable)

**Higher-ticket "operating system" / done-with-you**
- "Second Brain AI" (Iwo Szapar): "designed for non-technical users with pre-built CLAUDE.md business context templates and ready-to-use subagent workflows ... pricing starting at $237 (DIY) to $1,797 (Done-With-You)"; has a /customers page — [iwoszapar.com best Claude Code productivity systems 2026](https://www.iwoszapar.com/p/best-claude-code-productivity-systems-2026); [iwoszapar.com/customers](https://www.iwoszapar.com/customers)
- Maven cohort "Your AI C-Suite: Build a team of AI Agents that run your Business (Claude)" $695; Cowork edition runs Nov 8–Dec 20 (6 weeks) — [maven.com/hinamian](https://maven.com/hinamian/build-ai-agent-team-with-claude); [maven.com/futurefactors](https://maven.com/futurefactors/build-ai-agent-team-with-claude)
- Maven "Launch Marketing Agents in Claude Code" $1,300 — [maven.com/laura-beaulieu](https://maven.com/laura-beaulieu/launch-marketing-agents-in-claude-code)
- "OpenClaw for Small Business" — "AI agent that handles customer messages, bookings, follow-ups, and daily ops", 50+ tools (WhatsApp, Google Calendar, Shopify, QuickBooks, HubSpot) — [openclawforsmallbusiness.com](https://www.openclawforsmallbusiness.com/) (pricing not in snippet)

**Paid communities (recurring)**
- Claude Code Club (Skool): $9/month, ~8k members, led by Duncan Rogoff; price "set to rise to $58/month once the community hits 8,100 members" — [skool.com/claudecodeclub](https://www.skool.com/claudecodeclub/about); [AcademyGems review](https://academygems.com/reviews/claude-code-club)
- Claude Club $97/mo (Sept 2026, up from $87 summer rate); AI Innovators $67/mo (Aug 2026, down from $97); Agentic Labs $29/mo ~655 members; AI Captains Academy $83/mo or $497/yr ~95 members; Claude Code Academy $69/mo "will rise to $150/month at 1,300 members" — [AcademyGems best Claude Code Skool communities](https://academygems.com/best/claude-code-skool-communities); [aifunnelinsider Claude Club](https://aifunnelinsider.com/claude-club-skool-review-2026/); [skoolmakers Claude Code Academy](https://skoolmakers.com/communities/claude-code-academy/)

**Courses (Udemy, student counts as traction)**
- "The Complete AI Coding Course (2026) — Cursor, Claude Code": 5,343 students; "MCP: Build Agents with Claude, Cursor, Flowise, Python & n8n": Bestseller, 741 students; Frank Kane's Claude Code course: 608 students; "Claude Code - Practical Guide": 6 students — [reactjava.substack: I tried 20+ Claude Code courses on Udemy](https://reactjava.substack.com/p/i-tried-20-claude-code-courses-on)
- Udemy course titled "Claude Code Full Course: How to Build & Sell (2026)" exists — [udemy.com](https://www.udemy.com/course/claude-code-full-course-how-to-build-sell-2026) (students not in snippet)

**Spanish-language offers**
- ESIC "Curso Intensivo en Claude AI" (Chat, Cowork, Code; "automatización y análisis"): 590 EUR — [esic.edu](https://www.esic.edu/master-y-postgrado/curso-claude-code-online)
- ADR Formación "Curso de Claude Code: Automatización con IA sin código", 25 h, 125 EUR (175 EUR with tutor) — [adrformacion.com](https://www.adrformacion.com/curso-online/prx0000062)
- cursoclaudecode.com "De Cero a Experto", 93 lessons incl. Hooks, Skills, Agent Teams, MCP: 297 EUR (list 497 EUR) — [cursoclaudecode.com](https://www.cursoclaudecode.com/)
- DevTalles Claude Code guide (MCP, hooks): $60 — [cursos.devtalles.com](https://cursos.devtalles.com/courses/claude-code-guia-completa)
- Fixtergeek "Claude Code Power User": MXN 1,490 — [fixtergeek.com](https://www.fixtergeek.com/claude)
- Webcurso 70 h "Vibe Coding" course: 577 EUR (bonificable) — [webcurso.es](https://www.webcurso.es/cursos-trabajadores/claude-code)
- MasterEnClaude: 10 modules/87 lessons, "MCP, Claude Code, agentes y API a un negocio real", with module on selling as "freelance, consultoría o SaaS"; English/Spanish/Russian — [masterenclaude.com](https://masterenclaude.com/en) (price not in snippet)
- Consultores IA "Curso de Claude en español" — [consultoresia.com](https://consultoresia.com/curso-claude-espanol/); Codigofacilito and EDteam Claude Code courses (free start) — [codigofacilito.com](https://codigofacilito.com/cursos/claude-code); [ed.team](https://ed.team/cursos/claude-code)
- Hotmart: a Portuguese "Pack de templates Claude Code" (copy-paste templates) exists; no Spanish Claude Code skills pack for autónomos was found on Hotmart — [hotmart.com pack de templates Claude Code](https://hotmart.com/pt-br/marketplace/produtos/pack-de-templates-claude-code/Y105296286A)
- Spanish-language Cowork news site exists (claudecoworkexpert.com/es) — [claudecoworkexpert.com/es](https://www.claudecoworkexpert.com/es/noticias/cowork-launch/)

### Inferences
- Proven willingness to pay clusters at three bands: $9–$49 impulse packs (many sellers, little proof), $99–$297 "built from my own client work" packs and Spanish courses (the few published wins: $3k/45 days at $99; >$10k one-time stack), and $695–$1,797 cohorts/done-with-you.
- The 100–200 EUR gap between "prompt pack" and "cohort" is where the evidence of real sales sits ($99 pack, 125–175 EUR ADR course, $149 Claudecademy Builder), and the Spanish market has courses there but no packaged ops system.
- Skool community pricing ladders (price rises with member count) show operators expect sustained demand; 8k members at $9 implies at least ~$70k/mo gross for one community (inference from reported figures).

### Gaps
- Gumroad rating counts, sales counts and review text for every pack above: Gumroad pages blocked. The report writer should state "sales numbers not published" unless manually checked.
- Maven enrolment numbers and reviews: page blocked.
- Second Brain AI customer count: /customers page blocked.
- MasterEnClaude and openclawforsmallbusiness.com prices: not in snippets.

## KQ4. What price points are buyers paying, and is there evidence of refunds or disappointment?

### Takeaway
Observed price points: $5–$24 (prompt/cheat-code packs), $27–$97 (documented workflow setups), $99–$149 (skill packs built from client work; Claudecademy Builder), 125–297 EUR (Spanish courses), $237 (DIY second brain), $695–$1,797 (cohorts/done-with-you), $9–$97/month (Skool). Direct evidence of refunds/disappointment on Claude-skill products was not found; the only disappointment evidence located is structural (indie-product survey: >50% make nothing) and incumbent-tool complaints (Zapier "no-refund policy").

### Cited Findings
- $5–$10 tiers → $57 in 48 h (Indie Hackers) — [Indie Hackers](https://www.indiehackers.com/post/i-made-57-in-48-hours-selling-claude-cheat-codes-here-s-what-worked-and-what-didn-t-01d7f1f61c)
- $24 Solopreneur Skills Pack — [soloskills.gumroad.com](https://soloskills.gumroad.com/l/sdosug)
- $27–$97 "well-documented setups for specific use cases" — [bigideasdb](https://bigideasdb.com/how-to-make-money-with-claude-code)
- $99 × 25 skills → $3,000 in 45 days — [ryandoser.com](https://ryandoser.com/sell-claude-skills/)
- $9–$119 ToolGenX packs — [agentskillpacks.com](https://www.agentskillpacks.com/)
- $49 / $149 Claudecademy — [claudecademy.gumroad.com/l/builder](https://claudecademy.gumroad.com/l/builder)
- $237 DIY → $1,797 DWY (Second Brain AI) — [iwoszapar.com](https://www.iwoszapar.com/p/best-claude-code-productivity-systems-2026)
- $695 / $1,300 Maven cohorts; "Maven cohorts typically range from $1,500-2,500" generally — [maven.com/hinamian](https://maven.com/hinamian/build-ai-agent-team-with-claude); [igotanoffer Maven alternatives](https://igotanoffer.com/en/advice/maven-alternatives)
- Skool: $9 → $58 (Claude Code Club), $29, $67–$97, $69 → $150 — [AcademyGems](https://academygems.com/best/claude-code-skool-communities)
- OpenClaw/ClawHub: "Premium skills sell for $10 to $200 each, enterprise custom builds go for $500 to $2,000"; "3 skills priced at $15-25 each generates $300-900 per month"; "90/10 revenue split" (promotional blog claims, unverified) — [pcbuildadvisor Can OpenClaw make money](https://www.pcbuildadvisor.com/can-openclaw-really-make-money-the-top-10-ways-to-do-it-in-2026/); [superframeworks OpenClaw make money guide](https://superframeworks.com/articles/openclaw-make-money-guide)
- Spanish courses 125–590 EUR (see KQ3) — [adrformacion.com](https://www.adrformacion.com/curso-online/prx0000062); [esic.edu](https://www.esic.edu/master-y-postgrado/curso-claude-code-online)
- Disappointment, structural: ">50% of indie-hacker products make no revenue; ~70% under $1,000 MRR" — [gladlabs.io](https://www.gladlabs.io/posts/decoding-the-indie-hacker-blueprint-what-revenue-r-ba48746c)
- Disappointment, demos vs reality: "Claude Code money claims: the 8-minute demo, examined — Income Reality Check" (critical piece on "I asked Claude Code to make me as much money as possible" videos) — [income-reality-check.pages.dev](https://income-reality-check.pages.dev/a/i-asked-claude-code-to-make-me-as-much-money-as-possible/)
- Saturation signals: "The Skills ecosystem exploded in early 2026, with thousands of skills across GitHub, making it hard to separate genuinely useful ones from the noise" — [thepromptshelf best Claude Code skills 2026](https://thepromptshelf.dev/blog/best-claude-code-skills-2026/); a marketplace advertising "7,500+ skills" — [agensi.io Claude marketplace](https://www.agensi.io/claude-marketplace); ClawHub "5,700+ skills" by March 2026 — [claudemarket.ai](https://claudemarket.ai/blog/best-places-to-find-openclaw-skills)
- Free substitutes are abundant and large: 122 free sales skills (MIT) — [GitHub louisblythe/Sales-Skills](https://github.com/louisblythe/Sales-Skills); PM Skills Marketplace "65 PM skills and 36 chained workflows across 8 Claude plugins" open source — [productcompass.pm](https://www.productcompass.pm/p/pm-skills-marketplace-claude); claude-code-templates 32.4k stars free — [GitHub davila7](https://github.com/davila7/claude-code-templates)
- Incumbent refund friction: Zapier "strict no-refund policy" cited as a reason not to recommend — [tryorbye Zapier](https://www.tryorbye.com/products/zapier)
- Claudecademy Essential ($49) "not currently for sale" per snippet — possible withdrawal/repricing signal — [claudecademy.gumroad.com/l/essential](https://claudecademy.gumroad.com/l/essential)

### Inferences
- Raw skill files are commoditised (free repos with 100+ skills, marketplaces with thousands); price holds only when the product bundles setup, business context and a workflow the buyer "already needed" (bigideasdb's phrasing), which supports pricing a packaged ops system above the $24 pack tier and below cohort tier.
- Absence of visible refund complaints is weak evidence (Gumroad reviews unreadable here), not evidence of satisfaction.

### Gaps
- No Gumroad/Udemy/Skool review text with refund or "not worth it" sentiment for Claude-skill products was retrievable; the targeted search returned only unrelated Gumroad items. Needs manual review scrape.
- Udemy ratings distribution for Claude Code courses not captured.

## KQ5. Are there distribution channels for faceless sellers (skills marketplaces, GitHub, Gumroad, newsletters) with evidence that faceless products sell?

### Takeaway
Channels exist and are growing: Gumroad (dominant for packs), the official Claude Code plugin marketplace mechanism (any GitHub repo can be a marketplace), third-party directories (claudemarketplaces.com, skillsdirectory.com, claudeskills.info, mcpmarket.com, agensi.io 7,500+ skills), ClawHub (5,700+ skills, 90/10 split), Product Hunt (Claude Skills Hub #11 of day; Claude Marketplace #15 monthly, Mar 2026) and Skool. Evidence that *faceless* products sell is thin: the published wins ($3k, $10k) come from personal-brand creators; the only brand-less shop found (ToolGenX, pseudonymous storefront) publishes no numbers, and a ~$57 result came from an anonymous-ish first-time seller.

### Cited Findings
- Gumroad is the default venue in every how-to found: [dev.to how to build a skill that sells on Gumroad](https://dev.to/manja316/how-to-build-a-claude-code-skill-that-actually-sells-on-gumroad-4kdm); [ryandoser.com](https://ryandoser.com/sell-claude-skills/); [agent37 How to monetize Claude Code skills](https://www.agent37.com/blog/monetize-claude-code-skills); Medium "10 Claude prompts to build and sell a digital product on Gumroad" — [medium.com/activated-thinker](https://medium.com/activated-thinker/these-10-claude-prompts-can-build-and-sell-a-digital-product-on-gumroad-for-free-7d3b2bb9d9de)
- Gumroad even has Claude Code skills to run a Gumroad store (listed on several directories, free) — [mcpmarket.com Gumroad Pro](https://mcpmarket.com/tools/skills/gumroad-pro-merchant-management); [skillsdirectory.com Gumroad Automation](https://www.skillsdirectory.com/skills/onfire7777-gumroad-automation); [claudeskills.info](https://claudeskills.info/skill/gumroad-automation/)
- Official distribution primitive: any GitHub repo can be added as a plugin marketplace (`/plugin marketplace add <owner>/<repo>`), documented in Anthropic's own skills repo — [GitHub anthropics/skills](https://github.com/anthropics/skills)
- Third-party directories indexing skills/plugins: claudemarketplaces.com (skills + plugins, e.g. ComposioHQ/awesome-claude-skills) — [claudemarketplaces.com](https://claudemarketplaces.com/plugins/composiohq-awesome-claude-skills/Gumroad%20Automation); vibehackers.io — [vibehackers.io](https://vibehackers.io/claude-code/skills/producthunt-launches); claudedirectory.org — [claudedirectory.org](https://www.claudedirectory.org/for/ai-agent-development); agensi.io "Browse 7,500+ Skills" — [agensi.io](https://www.agensi.io/claude-marketplace); context-link.ai Cowork skills — [context-link.ai](https://www.context-link.ai/claude-cowork-skills/google-trends)
- ClawHub (OpenClaw) official marketplace launched March 2026, 5,700+ skills, "90/10 revenue split" (creator keeps 90%) per promotional sources — [claudemarket.ai](https://claudemarket.ai/blog/best-places-to-find-openclaw-skills); [superframeworks](https://superframeworks.com/articles/openclaw-make-money-guide)
- Product Hunt: "Claude Skills Hub" directory launched 2025, day rank #11 — [producthunt.com/products/claude-skills-hub](https://www.producthunt.com/products/claude-skills-hub); "Claude Marketplace" ranked #15 on the March 2026 monthly leaderboard — [producthunt.com leaderboard 2026/3](https://www.producthunt.com/leaderboard/monthly/2026/3)
- Newsletters as channel: Growth with Alex (Substack issue → Gumroad pack) — [growthwithalex.substack.com](https://growthwithalex.substack.com/p/14-i-built-11-claude-workflows-that); Build to Launch (Substack, AI agents section) — [buildtolaunch.substack.com](https://buildtolaunch.substack.com/t/ai-agents); AI Blew My Mind "How to sell Claude skills" — [aiblewmymind.substack.com](https://aiblewmymind.substack.com/p/sell-claude-skills); Medium "Claude Code Business Stack: 7 income streams" — [medium.com/@0xmega](https://medium.com/@0xmega/the-claude-code-business-stack-7-income-streams-content-creators-are-using-right-now-c870a4d98133)
- Faceless/brand-less seller example: ToolGenX (agentskillpacks.com), 19 products $9–$119, operated under a shop name from Istanbul, no public sales figures — [agentskillpacks.com](https://www.agentskillpacks.com/)
- Low-identity first-timer result: $57 in 48 h from a solo founder in India (Indie Hackers post, pseudonymous handle) — [Indie Hackers](https://www.indiehackers.com/post/i-made-57-in-48-hours-selling-claude-cheat-codes-here-s-what-worked-and-what-didn-t-01d7f1f61c)
- Personal-brand results are the ones with numbers: Ryan Doser (YouTube/blog) $5k and $10k claims; marketing consultant $3k — [ryandoser.com](https://ryandoser.com/make-money-with-claude/)
- Upwork lists "Claude specialists" for hire (Sep 2026), i.e. the service route competes with the product route — [Upwork Claude specialists](https://www.upwork.com/hire/claude-specialists/)
- Localized directory/news sites already exist in DE/EN/ES/IT for Cowork, implying SEO traffic exists in Spanish — [claudecoworkexpert.com/es](https://www.claudecoworkexpert.com/es/noticias/cowork-launch/)

### Inferences
- Distribution for a faceless digital product is feasible via Gumroad + GitHub-as-marketplace + directory listings + SEO pages; the missing proof is a faceless seller publishing revenue. The evidence skews toward "audience sells packs", not "packs sell themselves".
- ClawHub's 90/10 split and 5,700+ skills in two months suggest marketplaces will be flooded with free/cheap skills; differentiation must come from the assembled workflow + setup, not from individual skills.

### Gaps
- No faceless seller with disclosed revenue for Claude/MCP products was found.
- Product Hunt upvote counts for Claude skill marketplaces not retrieved (page blocked).
- Gumroad Discover listing counts (how many "Claude Code" products exist) not retrievable.
