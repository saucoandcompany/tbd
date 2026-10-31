# GLP-1 ecosistema 2026 — Competencia, precios y casos con ingresos

Fecha de apertura de páginas: 31-10-2026. Investigador adversarial. Método: ~110 páginas abiertas con `pwfetch.js` (directo y `--browser`), `r.jina.ai`, `curl` y la API pública de búsqueda de iTunes (apps.apple.com). Marcas: **[ABIERTA]** = leído en la página; **[FRAGMENTO]** = sólo extracto de buscador o nota previa del repo; **NO ENCONTRADO / NO ACCESIBLE** = no se pudo obtener. Todas las cifras llevan moneda, fecha y URL (sección 8). "Sin dato" = no publicado en la página.

Contexto evaluado: Jorge (ingeniero, España, usuario de Mounjaro, deportista) estudia un producto de acompañamiento GLP-1: retención de masa muscular (fuerza + proteína), transición a mantenimiento al dejar el fármaco, nutrición frente a efectos secundarios. Un texto externo afirma que "las apps actuales solo cuentan calorías" y que hay un "ángulo muerto". Fragmentos previos del repo: app "Preserve: GLP-1 Muscle Tracker" a 9,99 $/mes o 49,99 $/año; planificador: top-3 apps del nicho con hasta 38.453 reseñas, competencia "High".

---

## 0) Veredictos H1–H6

| Hipótesis | Veredicto | Resumen en una línea |
|---|---|---|
| **H1** Los grandes ya cubren músculo y mantenimiento | **CORREGIDA** | Músculo: sí lo cubren (Noom "Muscle Defense" dentro de un GLP-1 Companion **gratis** desde 24-jun-2026; Omada con *Exercise Specialist* y "maintain muscle mass"; Found+Obé "MuscleGuard" 2024; Equinox protocolo para coaches). Proteína/coaching humano: WW, Ro, Calibrate, Hims. **Plan de salida del fármaco / mantenimiento post-fármaco: ningún grande lo publica** (sólo "maintenance dose" y avisos de rebote). Lilly Health y WeGoTogether (Novo) son apps gratuitas de registro de dosis sin fuerza ni músculo. |
| **H2** Apps independientes GLP-1 | **CORREGIDA** | "Las apps solo cuentan calorías" es falso: MyFitnessPal (GLP-1 Support gratis, 28-abr-2026), MyNetDiary (GLP-1 Companion en Premium, 5-may-2026), Shotsy (proteína), Noom, WW ya tienen funciones GLP-1. En el App Store EE. UU. hay **≥25 apps con "GLP-1 muscle/strength/protein" en el nombre, todas lanzadas feb–oct 2026 y todas con 0–9 valoraciones**; Preserve (id6766536655) tiene **0 valoraciones** en EE. UU. y España. Trackers líderes: MeAgain 39.671 val. (4,79), Shotsy 34.292 val. (4,83). Español: sólo trackers traducidos; ninguna app en español centrada en músculo. |
| **H3** Oferta en español/España | **CONFIRMADA** (con matiz) | En España el GLP-1 es sólo con receta (privada para obesidad), legal por telemedicina regulada (ZAVA: consulta 25 €, receta en 3 h). Productos específicos en español localizados: ~10 (ZAVA, Santé Clinics, 5 libros KDP con 0–24 reseñas, ~4 infoproductos Hotmart de 5,90–69 US$, 1 vídeo de entrenador con 1K vistas). **Ninguno centrado en músculo/fuerza con fármaco real.** Dorsia, Pharmacius, Mediktor, Hims España: sin oferta GLP-1 localizable. |
| **H4** Infoproductos y KDP en inglés | **CONFIRMADA** | Cookbooks saturados (líder "GLP-1 Air Fryer Cookbook" 339 reseñas, 19,97 $). Subnicho "GLP-1 muscle" en KDP: oleada feb–oct 2026, líder 115 reseñas ("Complete GLP-1 High Protein Cookbook", 13,99 $), la mayoría 0–5 reseñas. Skool: 170 comunidades "glp-1"; mayores de pago: GLP1 Enhanced HUB 4,1k miembros a 12 $/mes, Shape & Strength Club 827 a 47 $/mes, GLP1 Weight Loss that Lasts 553 a 9 $/mes. Substack: On The Pen "Bestseller", 175.000+ comunidad en redes; nº de suscriptores no publicado. BSR no visible en listados. |
| **H5** Casos con ingresos 5–50 k$ MRR | **CORREGIDA** | Sólo un caso grande: **Shotsy** (fundadora sola, ingeniera-usuaria): 1 M$ ARR a los 8 meses (feb-2025), 100.000+ descargas, premium 19,99 $/año, rentable, luego 2,25 M$ seed (ya no "indie"). Los casos verificados en TrustMRR (RevenueCat) están muy por debajo: GlowAgain 1.813 $ MRR / 340 subs (31-oct-2026), GLP-1 Tracker 631 $ MRR / 148 subs, PeptideTrack ~631 $/30 d. **No se encontró ningún caso verificable en 5–50 k$ MRR**; todos en inglés; Shotsy con cara (fundadora) y sin médico. |
| **H6** Creadores con cara | **CORREGIDA** (inglés) / **CONFIRMADA** (español) | Inglés: existen pero pequeños. Dr. Dan Obesity Expert 62,6K subs (farmacéutico; comunidad Mighty Networks, precio sin dato), On The Pen 37,9K (noticias), The Betty Method 21,4K (CPT; Skool 39 $/mes), Astrid Naranjo 5,35K (dietista; challenge 550 $). **No hay un "Greg Doucette del GLP-1"** (entrenador con cara >100K que venda programa de fuerza GLP-1). Español: ningún canal específico GLP-1+fitness >50K (Di Trainer 349 subs; los grandes —Dr. Sorio 700K, Jordi Benlliure 52,6K— son generalistas). |

---

## 1) Grandes: qué incluyen y precio

| Empresa / programa | Qué incluye (según página) | Precio (fecha) | Fuerza/músculo | Plan de salida del fármaco | Coaching humano | Estado |
|---|---|---|---|---|---|---|
| **Noom** GLP-1 Companion + Muscle Defense | Companion gratuito "para cualquiera que tome un GLP-1, con independencia del proveedor": efectos secundarios, hábitos, "preserving muscle mass"; Muscle Defense = biblioteca de vídeos de fuerza con FitOn (PR 9-may-2024). Noom Weight: 70 $/mes mensual o 209 $/año (17,50 $/mes). Noom Med (2024): programa GLP-1 149 $/mes (titular HLTH 13-sep-2024). App Store 873.814 val., 4,7; Google Play 4,1★, 314K reseñas, 10M+ descargas ("Noom: Weight Loss & GLP-1 Care") | Companion **0 $** desde 24-jun-2026; Noom Weight 70 $/mes o 209 $/año (31-oct-2026) | **Sí** (vídeos FitOn) | No encontrado | Sí (coaches en planes; PR habla de "content, coaching, community, clinicians") | [ABIERTA] PRs y /plans; noom.com/glp-1 bloqueado por captcha (NO ACCESIBLE) |
| **WeightWatchers Clinic / Med+** (Sequence redirige aquí) | Med+: acceso a GLP-1 con receta, "GLP-1 tracking tools and expert guidance", seguimiento de proteína y macros, dietistas registrados, Workshops con WW Coach, Connect, fitness content online. Medicación aparte. Core+ Signature 20 $/mes; Core Basic 10 $/mes. App Store 2.366.132 val., 4,84 | Med+ 25 $/mes 2 primeros meses, luego 74 $/mes (plan 12 meses; oferta hasta 3-nov-2026) | Proteína sí; fuerza no explícita | No ("weight regain will occur" al parar; "maintenance dose" con clínico) | Sí (WW Coach, dietistas) | [ABIERTA] |
| **Found** | Clínico + medicación; compuestos desde 99 $/mes con seguro o 169 $/mes cash (medicación incluida); marcas Zepbound/Wegovy desde 650 $/mes; Mounjaro ~1.100 $/mes; plan no-GLP-1 desde 49 $/mes; Medicare 50 $/mes; "Protein Calculator" gratuito | 99–169 $/mes (31-oct-2026) | MuscleGuard con Obé (programa de fuerza por fases, 2024) [ABIERTA athletech]; joinfound.com/muscleguard **404** hoy | No encontrado | "Ongoing clinician support" | [ABIERTA] |
| **Calibrate** | Metabolic Reset: visita clínica 20 min con labs, coaching 1:1 en vídeo, currículo (comida, ejercicio, sueño, emocional), gestión de seguro; medicación por seguro (copago ~25 $/mes) | 199 $/mes, compromiso 3 meses (597 $) (31-oct-2026) | No explícito | No | Sí (1:1 vídeo) | [ABIERTA] |
| **Ro Body** | Proveedores, mensajería ilimitada, gestión de efectos secundarios y titulación, registro de peso/dosis, "1:1 health coaching", calculadora de proteína gratis; medicación aparte | 39 $ primer mes; 74 $/mes anual prepagado; 149 $/mes mensual (31-oct-2026) | No explícito | No ("maintenance dose") | Sí | [ABIERTA] |
| **Hims / Hers Weight Loss** | Membresía + medicación: Wegovy pill desde 149 $/mes, Wegovy pen 199 $, Zepbound vial/KwikPen 299 $, Mounjaro/Zepbound marca 1.899 $/mes; "nutrition support", báscula, Zofran para náuseas, soporte IA + proveedor | Membresía 39 $ primer mes, luego 149 $/mes (31-oct-2026) | No | No ("stopping treatment may result in weight regain") | Care Team (mensajería) | [ABIERTA] vía r.jina.ai |
| **Lilly** LillyDirect + Lilly Health app | Zepbound vial self-pay: 2,5 mg 299 $/mes; 5 mg 399 $; 7,5–15 mg 449 $/mes con recarga en 45 días (regular 499–699 $). Lilly Health app gratis (App Store: 5.141 val., 4,75; lanz. 1-jun-2025): logbook de medicinas/actividad, educación, tarjeta de ahorro, "dose tracking and progress visualization" | 299–449 $/mes medicación; app 0 $ | **No** (sin fuerza/músculo en descripción) | No | No | [ABIERTA] |
| **Novo Nordisk** NovoCare + WeGoTogether | Wegovy self-pay: 199 $/mes 2 primeros meses (0,25/0,5 mg) luego 349 $/mes; 399 $ HD; Wegovy pill 149/199/299 $/mes según dosis; precio de lista 1.349,02 $/envase. App WeGoTogether (App Store: 62 val., 3,0; lanz. 24-sep-2025): registro de dosis, recordatorios, gráficas, contenidos de hábitos | 149–399 $/mes; app 0 $ | **No** | No | No | [ABIERTA] |
| **Omada** Enhanced GLP-1 Care Track | B2B (empleadores/aseguradoras): coach dedicado + CDCES, acceso a *Exercise Specialist*, navegación de medicación, nutrición (hidratación, proteína), "customized exercise plans… to help maintain muscle mass", herramientas conductuales, prescripción integrada; 150k+ miembros GLP-1; 67 % persistencia a 12 meses; 18,4 % pérdida media | Sin dato (venta a empresas) | **Sí** | Parcial: menciona miembros que discontinúan, sin plan publicado | Sí | [ABIERTA] (--browser) |
| **Form Health** | Clínica online: médico ABOM + dietistas registrados + APPs; cubierto por seguros incl. Medicare | Sin dato en home | No encontrado | No encontrado | Sí (dietistas) | [ABIERTA] |
| **Equinox** GLP-1 protocol | Formación de coaches (Equinox Fitness Training Institute) para mitigar pérdida muscular con fuerza/condicionamiento; no es programa fijo ni facilita fármacos (ene-2024) | PT ~160 $/sesión [FRAGMENTO búsqueda] | **Sí** | No | Sí (PT) | [ABIERTA] athletech (resto de artículo de pago); equinox.com redirige a tracker (NO ACCESIBLE) |
| **Zepbound "vial"** | Es el programa self-pay de LillyDirect (vial exclusivo, entrega gratis o Walmart) | Ver Lilly | No | No | No | [ABIERTA] |

Lectura: el **músculo** ya está en el marketing de Noom (gratis), Omada, Found (2024) y Equinox; **ningún grande ofrece un plan explícito de salida del fármaco ni de mantenimiento sin fármaco**.

---

## 2) Apps (App Store EE. UU. salvo indicación; API iTunes 31-10-2026)

| App (vendedor) | Precio | Valoraciones / nota | Lanzamiento | Español | Músculo/fuerza | Mantenimiento | Nota |
|---|---|---|---|---|---|---|---|
| **Preserve: GLP-1 Muscle Tracker** (forresTech, id6766536655) | Gratis + Pro 9,99 $/mes o 49,99 $/año | **0 valoraciones** (US y ES) | 15-jun-2026 (v1.03, act. 21-ago-2026) | No (EN) | **Sí** (fuerza, proteína, shot day) | No en descripción | Corrige el [FRAGMENTO] previo: precio confirmado, tracción nula [ABIERTA] |
| Preserve: GLP-1 Muscle Support (Fulltech, id6777307428) | Gratis | 4 val., 5,0 | 1-jul-2026 | No | Sí | No | Homónima [ABIERTA] |
| **Shotsy GLP-1 Tracker** (Shotsy Co.) | Gratis + premium 19,99 $/año | 34.292 val., 4,83 (US); 363 val., 4,67 (ES); Google Play 4,7★, 12,9K reseñas, 100K+ descargas | 29-may-2024 | **Sí** ("Shotsy - Rastreador GLP-1") | No (sí proteína) | No | [ABIERTA] |
| **MeAgain: GLP-1 Tracker** (DOTS Future Tech.) | Gratis + IAP | 39.671 val., 4,79 (US); 14 val. (ES) | 11-abr-2025 | No (EN) | No (sí proteína) | No | Probablemente el "38.453" del planificador [ABIERTA] |
| Glowise: GLP-1 Tracker & Diary | Gratis + IAP | 6.708 val., 4,77; ES 195 val. | 6-nov-2024 | Sí | No | No | [ABIERTA] |
| PeptidePal / Pep AI / Zepbound & Mounjaro Tracker / DreamMe / Zealthy / Peptide Tracker | Gratis + IAP | 4.912 / 3.992 / 3.354 / 3.271 / 2.848 / 2.840 val. | 2024–2026 | Parcial | No | No | Segunda capa de trackers [ABIERTA] |
| **MyFitnessPal** | Gratis; Premium (sin dato de precio en página) | 2.386.788 val., 4,71; ES 30.793 val., 4,63 | 2009 | Sí | No (proteína sí) | Sí (palabra en descripción) | "GLP-1 Support" gratis para todos (PR 28-abr-2026): seguimiento de medicación, efectos secundarios, recordatorios, comidas priorizando proteína [ABIERTA PR] |
| **MyNetDiary** | Premium (PR: GLP-1 Companion dentro de Premium) | 170.936 val., 4,81 | 2019 | No (EN) | Sí (cita 40 % masa magra, fuerza) | No | GLP-1 Companion 5-may-2026: recordatorios inyección, proteína, fibra, síntomas digestivos, menús RD 90 g+ proteína [ABIERTA PR]; precio 9,99 $/mes o 59,99 $/año [FRAGMENTO] |
| **Lose It!** | Gratis + Premium | 782.957 val., 4,77 | 2008 | Sí | No | Sí (descripción) | loseit.com/glp-1 404; GLP mencionado en descripción [ABIERTA] |
| **Noom** | 70 $/mes o 209 $/año | 873.814 val., 4,70 | 2013 | Sin dato | Sí (descripción) | No | Ver §1 |
| **WeightWatchers** | 10–74 $/mes | 2.366.132 val., 4,84 | 2009 | Sin dato | Sí (descripción) | No | Ver §1 |
| **MacroFactor** (Stronger By Science) | Suscripción (sin dato) | 23.693 val., 4,84; MacroFactor Workouts 4.856 val. (lanz. 12-ene-2026) | 2021 | Sin dato | Fuerza (Workouts) | No | **Sin función GLP-1**: macrofactor.com/glp-1 404; "GLP" ausente en descripción [ABIERTA] |
| **Carbon Diet Coach** (Layne Norton) | 11,99 $/mes; 59,99 $/6 m; 99,99 $/año | 14.000+ val., 4,8 (web) | — | Sin dato | "muscle gain, maintenance, reverse dieting" genérico | Sí (fase mantenimiento) | Sin contenido GLP-1 [ABIERTA] |
| **Fitbod** | Suscripción | 288.791 val., 4,81 | 2015 | Sin dato | Sí (genérico) | No | Sin GLP-1 en descripción [ABIERTA API] |
| Strong, Peloton, Equinox app, Hers app | — | — | — | — | — | — | Peloton/Equinox: URLs redirigen a trackers publicitarios (NO ACCESIBLE); Hers = Hims (§1) |
| **Cluster "GLP-1 muscle"** (25 apps): Strongly (4 val.), Pep Strength (9), WheyGPT (7), Bild Health (5), Protein First (5), Gyla (3), Protein Tracker for GLP-1 (3), Ballast (2), Gym Rookie (2), GLP Protein (2), Lifta (1), Petal (1), AFTR (1), meteoric (1), Olina (1), Lean (0), LeanMass ×2 (0), Retain (0), GLP-1 Muscle Coach (0), GLP-1 Muscle Guard (0), GLP Muscle Guard (0), MuscleAI (0), PepPal (0), Dosey (0) | Gratis + IAP | **0–9 valoraciones cada una** | feb–oct 2026 (mayoría jun–oct) | No (EN) | **Sí (todas)** | Welloop, Lifta, GLP-1 Muscle Guard, GLP Flow mencionan "maintenance" | Prueba de que el ángulo "músculo" está siendo atacado en masa sin tracción [ABIERTA API] |
| **App Store España** (búsquedas glp-1/ozempic/mounjaro) | — | Máx. 363 val. (Shotsy); Control de Peso & IMC 338; Glowise 195; OzemPro 105; Mounjaro Rastreador GLP AI 95 | — | Sí (traducciones) | OzemPro, Mounjaro Rastreador, Glia, Moun mencionan "músculo" | Glia y Moun mencionan "mantenimiento" | **Ninguna app en español centrada en músculo**; volumen ES ≈ 1 % del US (Shotsy 363 vs 34.292) [ABIERTA API] |

---

## 3) Oferta en español y en España

| Actor | Qué ofrece | Precio | Músculo/fuerza | Estado |
|---|---|---|---|---|
| **Marco legal (The Local, 4-jun-2026; AEMPS)** | Ozempic/Wegovy/Mounjaro sólo con receta (pública o privada); AEMPS alertó de dispensación sin receta; SNS financia sólo diabetes tipo 2 (Ozempic ~4 €); para obesidad el paciente paga íntegro. Prescripción online legal si hay médico colegiado | Ozempic 117,89 €/mes (pluma 4 agujas); 204,83 € dos meses | — | [ABIERTA] |
| **OCU (26-may-2025)** | Precios Mounjaro por mes: 2,5 mg 207,91 €; 5 mg 271,35 €; 7,5–10 mg 358,71 €; 12,5–15 mg 446,07 € | 207,91–446,07 €/mes | — | [ABIERTA] |
| **ZAVA (zavamed.com/es)** | Telemedicina: valoración online, receta en 3 h laborables, Mounjaro; recomienda "programa de ejercicio y dieta equilibrada" pero no lo ofrece | Consulta 25 € + fármaco en farmacia (rev. 22-abr-2026) | No | [ABIERTA] |
| **farma2go (farmacia online, blog farmacéutico)** | Guía 2026: recomienda endocrino o "plataforma online con consulta médica regulada"; vende alternativas OTC (Kobho GLP Pack) | Sin dato | No | [ABIERTA] |
| **Santé Clinics (Barcelona, 2-may-2026)** | Mounjaro con consulta nutricional obligatoria (proteína, hidratación), titulación progresiva; afirma "no construye músculo: se construye con proteína y fuerza" | Sin dato | Menciona, no programa | [ABIERTA] |
| **Clínicas Dorsia** | Home: cirugía estética, medicina y obesidad; páginas /tratamientos/obesidad y /blog/ozempic → 404 | Sin dato | No | [ABIERTA parcial] |
| **Hims España** | hims.com/es → "page not found": no opera en España | — | — | [ABIERTA] |
| **Pharmacius** | Parafarmacia online; no vende medicamentos con receta | — | — | [ABIERTA] |
| **Mediktor** | Plataforma B2B de triaje/gestión de pacientes; no vende GLP-1 | — | — | [ABIERTA] |
| **SaludOnNet** | "Programa de adelgazamiento" con control médico; precio no publicado | Sin dato | No | [FRAGMENTO] (página no cargó) |
| **Libros Amazon.es** (búsqueda "recetas wegovy mounjaro", curl 31-oct-2026) | En español: "El completo libro de cocina alto en proteínas GLP-1" (tapa blanda 16,99 €, sin reseñas); "Cocina GLP-1 en Español" (Kindle, 1 reseña, 1,0); "La cocina suave de la GLP-1" (Kindle 7,99 €, 1 reseña 4,5); "Recetario GLP-1: comidas pequeñas ricas en proteínas" (Kindle, 24 reseñas, 4,5); "El libro de cocina navideña GLP-1" (20,53 €, sin reseñas). En inglés en el mismo listado: "GLP-1 High-Protein Cookbook" 32 reseñas 4,6 | 7,99–20,53 € | Sólo proteína en recetas | [ABIERTA]; otras búsquedas Amazon.es ("dieta ozempic", "mounjaro", "ozempic") → **503 NO ACCESIBLE**; BSR no visible en listados |
| **Hotmart (es)** | "ozempic": ebook "Ozempic en tu cuerpo" 10 US$. "mounjaro": decenas de "Mounjaro casero/de chía/natural" (bebidas, no fármaco) 2–9,90 US$. "glp-1": "Protocolo GLP-1 a tu medida" 5,90 US$; "Activa tu GLP-1 natural 28 días"; "GLP-1 natural + perfil hormonal 1 a 1" 69 US$; "Cuerpo-Firme-GLP-1" (guía firmeza corporal); kit "¿esta pluma es original?" 15 US$ | 2–69 US$ | Ninguno de fuerza con fármaco | [ABIERTA] |
| **Udemy (es)** | Búsqueda bloqueada (403 security verification) | — | — | NO ACCESIBLE |
| **Instagram** | No abierto (requiere sesión) | — | — | NO ABIERTO |
| **YouTube en español** (búsqueda canales) | Específicos GLP-1: Ozempic Wegoby Mounjaro @OzWeMo 61 subs; Metodo Balance 56; Hormone Fitness Español 81; Di Trainer 349 subs (vídeo "Entrenar en Ozempic" 1K vistas, 7 meses); Dr. Miguel Ángel Tapia (vídeo 840 vistas); Adri Serrano fisio (vídeo 5,4K vistas); Clivi (clínica digital México) 4,02K. Generalistas que tocan el tema: Dr. Sorio Endocrinólogo 700K; DR LA ROSA 6,61M; xNutricion 494K/515K; Jordi Benlliure 52,6K (entrenador online, short "Ozempic, Mounjaro, Retatrutide? hábitos primero" 4,1K vistas); Fausto Alfaro 40,7K; Juan Bola 46,1K | Sin programa GLP-1 con precio | Di Trainer sí (vídeo) | [ABIERTA] |
| **Skool en español** | Ninguna comunidad en español en resultados "glp-1", "ozempic", "mounjaro" | — | — | [ABIERTA] |

Conteo de productos específicos en español: ZAVA, Santé Clinics, 5 libros, ~4 Hotmart, 1 vídeo-entrenador ≈ 10–11; **cero centrados en músculo con fármaco** (sólo "Cuerpo-Firme-GLP-1", guía de firmeza). H3 confirmada.

---

## 4) KDP e infoproductos en inglés (Amazon.com, pwfetch --browser, 31-10-2026; BSR no visible en listado → "sin dato")

| Título (autor, fecha) | Reseñas / nota | Precio | Músculo |
|---|---|---|---|
| The GLP-1 Air Fryer Cookbook (Luke Trenholm, 13-abr-2026) | 339 / 4,5 | 19,97 $ | No |
| The Ozempic Revolution (Alexandra Sowa, MD, 7-ene-2025) | 325 / 4,6 | 16,00 $ (lista 28,99) | Médico con cara |
| The Complete GLP-1 High Protein Cookbook… Preserve Lean Muscle (Brukonie Cahuloke, 3-jun-2026) — etiqueta "Best Seller" | 115 / 4,9 | 13,99 $ (Kindle 0,99) | **Sí** |
| The Complete GLP-1 Guide for Seniors… Protect Muscle (Charlie Sins, 24-jul-2026) | 111 / 4,2 | 17,99 $ (Kindle 2,99) | Sí |
| The GLP-1 Small Bites Easy Cookbook (Healthy Kitchen Press, 4-jun-2026) | 104 / 4,4 | 21,90 $ | No |
| The GLP-1 Diet Cookbook… Maintain Muscle (Feldman & Dalyai, 12-ago-2025) | 70 / 4,1 | 12,80 $ | Sí (título) |
| GLP-1 High Protein Cookbook for Seniors… Preserving Muscle Mass (S. Mitchell, 28-may-2026) | 37 / 4,3 | 17,97 $ (Kindle 2,99) | Sí |
| GLP-1 Muscle Preservation Cookbook (Scott L. Morgan, 16-jun-2026) | 33 / 4,7 | 19,99 $ (Kindle 8,99) | **Sí** |
| The Super Simple GLP-1 Diet Slow Cooker Cookbook… Protect Muscle (Jess Perkz, 5-oct-2026) | 24 / 4,9 | 14,99 $ | Sí |
| 101 Best Foods for the Ozempic Diet (11-ago-2025) | 18 / 4,2 | 9,99 $ | No |
| The Honest GLP-1 Guide… Muscle Loss, Plateaus (S. Alozie) | 5 / 5,0 | 17,99 $ | Sí |
| The GLP-1 Muscle Rule 12-Week Plan (Nadia Ellery, 7-sep-2026) | sin reseñas | Kindle 5,99 $ | **Sí** |
| The GLP-1 Muscle Manual (Jeffrey Goldman, 10-feb-2026) | sin reseñas | Kindle 4,99 $ | Sí |
| The GLP-1 Muscle Preservation Guide (Ariana Bellwyn, 16-ago-2026) | sin reseñas | Kindle 6,80 $ / 12,50 $ | Sí |
| THE GLP-1 Muscle Protection Guide (MK Kaonga, 29-mar-2026) | sin reseñas | Kindle 5,99 $ | Sí |
| GLP-1 Muscle Protection Cookbook for Seniors (A. Adesina, 16-jul-2026) | sin reseñas | 19,99 $ | Sí |
| The GLP-1 Muscle & Protein Tracker (diario, Bright Start Books, 14-oct-2026) | sin reseñas | 9,00 $ | Sí |
| Ultimate Ozempic Diet Cookbook (E. Julius, 21-mar-2025) y ~8 cookbooks "Ozempic" más | 1–8 reseñas | 13–18,99 $ | No |
| Búsqueda "off ozempic" | — | — | Resultado vacío (NO ACCESIBLE) |

**Newsletters (Substack/beehiiv)** [ABIERTA]: On The Pen (Dave Knapp): "Substack Bestseller", podcast top 1 % global, "comunidad de más de 175.000 personas en redes"; nº de suscriptores Substack **no publicado**. GLP-1 Snacks (gratis, martes y jueves, protein-first): sin cifra. Becky May | GLP-1 Dietitian, Fat Girl is The GLP-1 Artist, O Universo GLP-1 (pt): sin cifra. The Weekly Dose (beehiiv, pilares "Muscle Preservation", ≥51 números, ago-2026): sin cifra.

**Comunidades Skool** (170 resultados "glp-1", 31-10-2026) [ABIERTA]:

| Comunidad | Miembros | Precio | Enfoque |
|---|---|---|---|
| Project Biohacked – Peptides | 15,1k | Gratis | Péptidos, sourcing |
| GLP1 Enhanced HUB (farmacéutica) | 4,1k | 12 $/mes | Nutrición, fitness, "weaning down or off GLP1 meds" |
| Coach Cam's Peptide Academy | 1,5k | 10 $/mes | Péptidos, GLP-1 |
| GLP-1 Real Talk Community | 1,2k | Gratis | Incluye "maintenance" |
| Shape & Strength Club (mujeres 35–50) | 827 | 47 $/mes | **Fuerza en casa** |
| GLP-1 Mounjarian Tribe (UK) | 693 | Gratis | Apoyo |
| GLP1 Weight Loss that Lasts (PT + nutrición) | 553 | 9 $/mes | Proteína diaria, "workouts that protect your muscle" |
| Bliv GLP-1 Community | 408 | Gratis | Apoyo |
| The Daily Pep-Talk (Peptides) | 219 | 25 $/mes | Precios de kits |
| Peptide Rebels | 183 | 15 $/mes | Mercado gris |
| My GLP1 Journal Community | 163 | 25 $ | Apoyo |
| Hormone Health & GLP1 Coaching | 60 | 97 $/mes | Mujeres 40+ |
| STACKED: GLP-1 + Peptides | 60 | 29 $/mes | Músculo, mujeres 40+ |
| Radiant Fat Loss Skool | 14 | 49 $/mes | Entrenamiento por fases 365 días |
| Betty Collective GLP1 Coaching | 29 | 39 $/mes | Entrenadora que perdió 100 lb |
| MyEHQ GLP-1 Coaching & Aftercare | 17 | 16 $/mes | **"Vida después de Mounjaro/Wegovy", evitar rebote** |
| The Healthy GLP-1 Method | 10 | 797 $/año | Mujeres 35+, "protect muscle, build strength" |
| BodyRecompRX (farmacéutico) | 2 | 5.830 $/año | "Lose fat, protect muscle, maintain long-term" |
| Beyond the GLP-1 | 2 | 2 $/mes | "Rebuild muscle… after medication" |

Lectura: el ticket típico es 9–47 $/mes; sólo tres comunidades de pago superan 500 miembros y la mayor (4,1k × 12 $) implica ≤ ~49 k$/mes brutos si todos pagaran (cálculo propio, no verificado). "Salida/aftercare" existe sólo en micro-comunidades (17 y 2 miembros).

---

## 5) Casos con ingresos (2024–2026)

| Caso | Producto | Ingresos | Equipo | Captación | Fuente / estado |
|---|---|---|---|---|---|
| **Shotsy** (Aja Beckett, Portland) | Tracker GLP-1 iOS/Android, freemium, premium 19,99 $/año | **1 M$ ARR run-rate a los 8 meses (20-feb-2025)**; 100.000+ descargas; "rentable"; seed 2,25 M$ (Adverb Ventures). Estimación AppGoblin Android: <10 k$/mes [FRAGMENTO] | Fundadora sola (ingeniera iOS autodidacta, usuaria) → equipo tras la ronda | Subreddit r/Zepbound como beta y lanzadera, boca a boca, sin ads; "todo lo importante es gratis" | [ABIERTA] Silicon Florist, RevenueCat (3-dic-2025), thecreatorsai |
| **GlowAgain** (Promi LLC) | Tracker GLP-1 | MRR 1.813 $, 340 subs activas, 1.295 $ últimos 30 días (+36 %), verificado RevenueCat, tracked desde 3-ago-2026, actualizado 31-oct-2026; App Store 297 val., 4,60; en venta en Flippa (anuncio: ~2.100 $ MRR, 25.043 $ acumulados) [FRAGMENTO] | Indie | Sin dato | [ABIERTA] TrustMRR; Flippa (sólo navegación) |
| **GLP-1 Tracker** (Arif E. Kiraz) | Tracker dosis/hambre/agua + widget | MRR 631 $, 148 subs, acumulado 5.950 $, 410 $ últimos 30 d (31-oct-2026) | Solo | Sin dato | [ABIERTA] TrustMRR |
| **PeptideTrack** | Tracker péptidos/GLP-1/TRT, Pro 9,99 $/mes o 39,99 $/año | ~631 $ últimos 30 d; 142 subs [FRAGMENTO MRR 620 $] | Solo | Sin dato | [ABIERTA] TrustMRR |
| Zemly (Brasil) | Tracker | 5 $ últimos 30 d | Solo | — | [ABIERTA] TrustMRR |
| GlpFlow (Indie Hackers, 26-mar-2026) | Tracker iOS privacy-first | Sin ingresos publicados; fundador "no soy usuario" | Solo | Post IH | [ABIERTA] |
| Noom, WW, Hims (753 M$/trim.), Found (VC) | Corporativos | Ya en repo [FRAGMENTO] | — | — | — |
| Indie Hackers búsqueda | — | Error 410 | — | — | NO ACCESIBLE |
| Starter Story búsqueda | — | Muro de registro | — | — | NO ACCESIBLE |

Veredicto H5: **no hay caso verificable en la banda 5–50 k$ MRR**: o es Shotsy (≈83 k$/mes implícito en feb-2025 y hoy VC-backed) o son <2 k$ MRR. Ninguno con médico; Shotsy con cara de fundadora-usuaria.

---

## 6) Creadores con cara (YouTube, búsqueda por canales, 31-10-2026)

| Canal | Idioma | Suscriptores | Qué vende | Precio | Estado |
|---|---|---|---|---|---|
| Dr. Dan \| Obesity Expert (@theofficialdrdan, farmacéutico) | EN | 62,6K (932 vídeos) | "Dr. Dan's Empowerment Hub" (Mighty Networks): coaching, Q&A, cursos, herramientas GLP-1; 14 días gratis | Sin dato en página /plans | [ABIERTA] |
| On The Pen Podcast (Dave Knapp) | EN | 37,9K | Noticias GLP-1; Substack "Bestseller"; comunidad 175.000+ en redes; canal hermano GLP-1 Medicare 323 | Sin dato | [ABIERTA] |
| The Betty Method (CPT, perdió 115 lb) | EN | 21,4K (94 vídeos) | Coaching mujeres 35+ "strength training, body recomposition"; Skool "Betty Collective" (29 miembros); afiliación AG1 | 39 $/mes (Skool) | [ABIERTA] |
| JOFITNESS (Coach Jo) | EN | 20,1K | Academia/challenge genérico | Sin dato | [ABIERTA] |
| Nyk Bokuniewicz (journey) | EN | 13,7K | Contenido | — | [ABIERTA] |
| Jet Lag & Gym Life (perdió 130 lb) | EN | 11,9K | Contenido | — | [ABIERTA] |
| Astrid Naranjo \| Dietitian \| GLP-1 & Fitness coach | EN | 5,35K (764 vídeos) | Guías 3,99–21,99 $; "InsideOut Fit 16 Weeks Challenge" 550 $; "Free guide: The Last Dose Plan" | 3,99–550 $ | [ABIERTA] |
| My GLP-1 Journey (Rebecca) | EN | 4,8K | Contenido | — | [ABIERTA] |
| Holistic GLP-1 Podcast (E. McGann) | EN | 4,71K | Microdosing holístico | Sin dato | [ABIERTA] |
| The GLP-1 Athlete | EN | 1,31K | Contenido | — | [ABIERTA] |
| GLP-1 Muscle Coach (@kevincox9279) / Dante Budhan GLP-1 Strength Coach / GLP1CoachMike (farmacéutico) | EN | 258 / 132 / 203 | Coaching | Sin dato | [ABIERTA] |
| Shape & Strength Club (@skinnyfatfixcoach) | EN | 5 (YouTube) | Skool 827 miembros | 47 $/mes | [ABIERTA] |
| Vídeos de fuerza GLP-1 con más vistas: "How To START EXERCISE On GLP1" (Dr. G) 14K; "GLP-1 Strength Protocol" (TRX) 5K; "Exercise on GLP-1" (Fit with Frank) 10K; short "How To Improve Your Shape On A GLP-1" 65K; "On GLP-1? Don't Lose Muscle" 32K | EN | — | — | — | [ABIERTA] |
| Generalistas que aparecen en la búsqueda GLP-1: Jeff Nippard 8,76M; Renaissance Periodization 3,9M; Health Coach Kait 651K; James Smith 469K | EN | — | No específicos GLP-1 | — | [ABIERTA] |
| **Español**: Dr. Sorio Endocrinólogo 700K; DR LA ROSA 6,61M; xNutricion 494K/515K; Jordi Benlliure 52,6K (entrenador online, formulario); Juan Bola 46,1K; Fausto Alfaro 40,7K; Dra. Ana María Kausel 161K; Di Trainer 349; @OzWeMo 61; Metodo Balance 56; Clivi 4,02K | ES | ver cifras | Ninguno vende programa GLP-1 específico | — | [ABIERTA] |

¿Existe un "Greg Doucette del GLP-1"? **No en inglés** (el mayor específico es un farmacéutico con 62,6K; la entrenadora con cara más visible, Betty, tiene 21,4K y 29 miembros de pago). **No en español** (ningún canal específico >50K; CONFIRMADA).

---

## 7) Veredicto sobre el "ángulo muerto"

1. **"Las apps actuales solo cuentan calorías" → FALSO.** MyFitnessPal (gratis, 28-abr-2026), MyNetDiary (Premium, 5-may-2026), Noom (Companion gratis con Muscle Defense, 24-jun-2026), WW (GLP-1 tracking + proteína), Shotsy (proteína) y ≥25 micro-apps "GLP-1 muscle" ya atacan proteína/músculo. El problema no es ausencia de oferta sino **ausencia de tracción**: la mejor app "muscle" tiene 9 valoraciones; Preserve, 0.
2. **Músculo/fuerza como ángulo → cubierto en marketing, no en resultados.** Noom lo regala; Omada lo vende a empresas; Equinox lo vende como PT (~160 $/sesión). Un indie en inglés compite contra "gratis" (Noom, MFP) y contra 25 clones lanzados en 5 meses.
3. **Transición a mantenimiento / salida del fármaco → hueco real y verificado.** Ningún grande publica plan de salida (sólo avisos de rebote y "maintenance dose"). Lo único hallado: MyEHQ Aftercare (17 miembros, 16 $/mes), GLP1 Enhanced HUB ("weaning off", 4,1k, 12 $/mes), Astrid "The Last Dose Plan" (guía gratis), Beyond the GLP-1 (2 miembros). Precaución: el hueco puede existir porque el usuario deja de pagar cuando deja el fármaco.
4. **Español/España → vacío real pero mercado diminuto hoy.** ~10 productos, ninguno de músculo; receta privada obligatoria; fármaco 208–446 €/mes (Mounjaro) que absorbe el presupuesto del usuario; App Store España ≈ 1 % del volumen de EE. UU. (Shotsy 363 vs 34.292 valoraciones).
5. **Ticket observado**: apps 9,99 $/mes o 20–60 $/año; comunidades 9–47 $/mes; coaching con cara 39–97 $/mes o 550–797 $/programa; grandes 74–199 $/mes (sin fármaco).
6. **Ingresos realistas**: sólo Shotsy pasó de 1 M$ ARR (2024–25, primer movil, Reddit); los verificados 2026 están en 0,6–1,8 k$ MRR. Hipótesis "5–50 k$ MRR para solos" **no sostenida** por ningún dato abierto.

Conclusión adversarial: el ángulo muerto **no es "músculo"** (ya lo cubren gratis y en masa); el hueco defendible es **"salida del fármaco y mantenimiento sin fármaco" + idioma español**, con la advertencia de que es pequeño y de retención dudosa.

---

## 8) URLs abiertas y estado

| URL | Estado |
|---|---|
| https://www.weightwatchers.com/us/clinic | [ABIERTA] |
| https://www.weightwatchers.com/us/plans | [ABIERTA] (jina) |
| https://www.joinsequence.com/ | [ABIERTA] → redirige a WW clinic |
| https://www.joinfound.com/ | [ABIERTA] |
| https://www.joinfound.com/muscleguard | [ABIERTA] 404 |
| https://www.joincalibrate.com/ y /pricing | [ABIERTA] |
| https://ro.co/weight-loss/ | [ABIERTA] |
| https://www.hims.com/weight-loss | [ABIERTA] (jina; directo = captcha) |
| https://www.forhers.com/weight-loss | [ABIERTA] (jina) |
| https://www.hims.com/es | [ABIERTA] 404 |
| https://lillydirect.lilly.com/pharmacy/zepbound | [ABIERTA] (jina) |
| https://zepbound.lilly.com/support | [ABIERTA] (jina) |
| https://zepbound.lilly.com/coverage-savings | NO ACCESIBLE (captcha) |
| https://www.novocare.com/obesity/products/wegovy.html | [ABIERTA] |
| https://www.wegovy.com/taking-wegovy/wegovy-app.html | 404 |
| https://itunes.apple.com/search?term=wegovy / zepbound (WeGoTogether, Lilly Health) | [ABIERTA API] |
| https://www.noom.com/glp-1/ | NO ACCESIBLE (bot gate, también --browser) |
| https://www.noom.com/plans | [ABIERTA] (jina → blog de precios) |
| https://www.noom.com/pricing/ , /blog/noom-muscle-defense/ | 404 |
| https://insider.fitt.co/press-release/noom-adds-muscle-defense-to-its-glp-1-companion-program-… | [ABIERTA] |
| https://norfolkdailynews.com/online_features/press_releases/noom-launches-free-version-of-its-powerful-glp-1-companion-… | [ABIERTA] |
| https://hlth.com/insights/news/noom-launches-149-glp-1-weight-loss-program-with-sustainable-approach-2024-09-13 | [ABIERTA] (sólo titular/fecha útil) |
| https://play.google.com/store/apps/details?id=com.wsl.noom | [ABIERTA] (jina) |
| https://www.omadahealth.com/glp-1-care-track | [ABIERTA] (--browser; jina sólo navegación) |
| https://www.omadahealth.com/glp-1 | 404 |
| https://www.formhealth.co/ | [ABIERTA] |
| https://athletechnews.com/ozempic-muscle-mass-retention-programs/ | [ABIERTA] |
| https://athletechnews.com/equinox-training-program-weight-loss-drugs/ | [ABIERTA] (parcial, resto de pago) |
| https://www.equinox.com/glp-1 , /articles/2024/06/glp-1 ; https://www.onepeloton.com/glp-1 | NO ACCESIBLE (redirigen a tracker publicitario) |
| https://obefitness.com/muscleguard | redirige a login |
| https://apps.apple.com/us/app/preserve-glp-1-muscle-tracker/id6766536655 | [ABIERTA] |
| https://itunes.apple.com/lookup?id=6766536655,… (US y ES) | [ABIERTA API] |
| https://itunes.apple.com/search?term=glp1 / ozempic / mounjaro / shotsy / glp-1+muscle / glp-1+tracker (US); glp-1 / ozempic / mounjaro (ES); noom / macrofactor / fitbod / weightwatchers / carbon | [ABIERTA API] (carbon: respuesta inválida) |
| https://play.google.com/store/apps/details?id=com.shotsy.app | [ABIERTA] (jina) |
| https://play.google.com/store/search?q=glp-1%20tracker&c=apps | [ABIERTA] (sin parsear) |
| https://www.shotsy.app/ | NO ACCESIBLE (timeout) |
| https://siliconflorist.com/2025/02/20/shotsy-lands-2-million-for-weight-loss-shot-tracking-app/ | [ABIERTA] |
| https://www.revenuecat.com/blog/growth/aja-beckett-shotsy-launched-podcast-2025 | [ABIERTA] |
| https://thecreatorsai.com/p/copy-apps-with-ai-medical-tracker | [ABIERTA] |
| https://appgoblin.info/apps/6499510249 | [ABIERTA] |
| https://www.globenewswire.com/news-release/2026/04/28/3282728/0/en/MyFitnessPal-Launches-Comprehensive-GLP-1-Support-… | [ABIERTA] |
| https://www.myfitnesspal.com/glp-1 | NO ACCESIBLE (captcha) |
| https://digital-release.kxan.com/…/mynetdiary-launches-glp-1-companion-for-ozempic-wegovy-and-mounjaro-users | [ABIERTA] |
| https://macrofactorapp.com/glp-1/ ; https://www.loseit.com/glp-1/ | 404 |
| https://joincarbon.com/ | [ABIERTA] |
| https://www.thelocal.es/20260604/whats-the-law-on-ozempic-for-weight-loss-in-spain | [ABIERTA] |
| https://www.ocu.org/salud/medicamentos/noticias/mounjaro-adelgazar | [ABIERTA] |
| https://www.zavamed.com/es/mounjaro.html | [ABIERTA] |
| https://farma2go.com/en/blogs/cuidate/glp-1-weight-loss-injections | [ABIERTA] |
| https://santeclinics.com/blog/mounjaro-in-barcelona-indications-benefits-and-medical-follow-up | [ABIERTA] |
| https://www.saludonnet.com/blog/opiniones-de-mounjaro-otro-medicamento-para-adelgazar/ | NO ACCESIBLE (vacío) |
| https://www.dorsia.es/ ; /tratamientos/obesidad/ ; /blog/ozempic/ | home [ABIERTA]; subpáginas 404; clinicasdorsia.com no resuelve |
| https://www.pharmacius.com/ ; https://www.mediktor.com/es | [ABIERTA] (sin GLP-1) |
| https://www.latercera.com/paula/evitar-la-perdida-de-musculo-el-nuevo-negocio-… | [ABIERTA] (Chile, contexto) |
| https://www.amazon.es/s?k=recetas+wegovy+mounjaro&i=stripbooks | [ABIERTA] (curl) |
| https://www.amazon.es/s?k=dieta+ozempic ; k=mounjaro ; k=ozempic | NO ACCESIBLE (503 / "Lo sentimos") |
| https://www.amazon.com/s?k=ozempic+cookbook&i=stripbooks | [ABIERTA] (--browser) |
| https://www.amazon.com/s?k=glp-1+muscle&i=stripbooks | [ABIERTA] (--browser) |
| https://www.amazon.com/s?k=off+ozempic&i=stripbooks | NO ACCESIBLE (vacío) |
| https://hotmart.com/es/marketplace/busca?q=ozempic / mounjaro / glp-1 | [ABIERTA] |
| https://www.udemy.com/courses/search/?q=ozempic&lang=es ; q=glp-1 | NO ACCESIBLE (403) |
| https://substack.com/search/glp-1?searching=all_posts ; all_publications | [ABIERTA] |
| https://onthepen.substack.com/about | [ABIERTA] |
| https://glp1snacks.substack.com/about | [ABIERTA] |
| https://the-weekly-dose.beehiiv.com/ | [ABIERTA] |
| https://www.skool.com/discovery?q=glp-1 / ozempic / mounjaro | [ABIERTA] |
| https://trustmrr.com/search?q=glp ; /?q=glp-1 ; /startups?search=glp | [ABIERTA] (sin filtro útil) |
| https://trustmrr.com/startup/glowagain ; /startup/glp ; /startup/peptidetrack ; /startup/zemly | [ABIERTA] |
| https://flippa.com/13885757-glowagain-glp-1-shot-tracker | [ABIERTA] (sólo navegación; cifras [FRAGMENTO]) |
| https://www.indiehackers.com/search?q=glp-1 | 410 |
| https://www.indiehackers.com/post/i-built-a-glp-1-tracker-app-… | [ABIERTA] |
| https://www.starterstory.com/search?q=glp-1 | NO ACCESIBLE (muro de registro) |
| https://outputperformance.com/services/glp-1-strength-training | [ABIERTA] (gimnasio St. Louis, sin precio) |
| https://www.youtube.com/results?search_query=glp-1+strength+training+coach ; ozempic+entrenamiento+fuerza+músculo | [ABIERTA] (--browser) |
| https://www.youtube.com/results?search_query=…&sp=EgIQAg%253D%253D (canales: ozempic, ozempic español, mounjaro entrenamiento, glp-1 fitness, glp-1 coach, on the pen glp-1, semaglutida entrenamiento fuerza, glp-1 español nutricionista, Di Trainer ozempic) | [ABIERTA] (--browser); "glp-1" solo → vacío |
| https://www.youtube.com/@theofficialdrdan ; @jordibenlliure ; @Astrid.thefitdietitian ; @TheBettyMethod ; @GLP1Hub | [ABIERTA] (--browser); @onthepen → vacío |
| https://drdans-empowermenthub.mn.co/ ; /plans | [ABIERTA] (sin precio) |
| https://bettymethod.com/ ; https://astrid-dietitian.com/shop | [ABIERTA] |
| Instagram (creadores en español) | NO ABIERTO (sesión requerida) |

Búsquedas web (WebSearch) usadas como [FRAGMENTO]: Noom precios/Companion gratis; MFP GLP-1 Nutrition Plan 2024; Shotsy ingresos; telemedicina España; YouTube GLP-1 strength; creadores en español; apps indie MRR (TrustMRR/Flippa); programas España; Equinox precio PT.
