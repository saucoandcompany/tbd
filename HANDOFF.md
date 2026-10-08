# Traspaso a sesión local — proyecto "venture solo" / Kit ISO 9001:2026

Fecha: 8 oct 2026. Origen: sesión en la nube (claude.ai/code). Todo lo de abajo está en esta rama:
`claude/solo-venture-independence-jo1gwz` del repo `saucoandcompany/tbd`. Clónala y trabaja desde ahí.

## 1. Qué hay en el repo

| Ruta | Qué es |
|---|---|
| `reports/Dolores en crecimiento con pruebas.md` | Informe completo: 17 candidatos puntuados, fichas, descartados, recomendación, límites, anexos de volumen de búsqueda y correcciones |
| `reports/Plan de preventa ISO 9001-2026.md` | Copia de registro del plan de preventa y negocio (la versión viva está en el documento de Claude, enlace abajo) |
| `research_notes/Dolores en crecimiento con pruebas/*.md` | Seis líneas de investigación (regulatorio, comunidades, marketplaces, anuncios, hardware, IA ops) + `search_volume_planner_trends.md` (datos reales del Planificador y Trends del 4 oct) |
| `research_notes/.../Validacion_ideas_negocio_4oct2026.docx` | Documento fuente de la sesión local con los datos del Planificador |

Documento vivo (informe + pestaña "Plan de preventa ISO 9001:2026"), editable y comentable:
https://claude.ai/code/artifact/4a8e16b4-30fa-447d-b71b-43e139d406f4

## 2. Decisiones tomadas (en orden)

1. Normach depende de Laura solo en la llamada de cierre; el resto ya lo opera Jorge. Se descartó rediseñar Normach porque Jorge sostiene que en B2B de servicios nadie compra sin hablar.
2. Se buscó desde cero un dolor con demanda demostrable, compatible con: sin cara pública, sin llamadas, compra online, B2B o prosumer, producible con IA + 1-2 h de revisión.
3. Ranking final (0-15, Riesgo invertido): **ISO 9001:2026 kit 12** · CE + CRA 11 · Manual Claude Code 11 (bajado por saturación) · ISO 27001 + RGPD 10 · GBP marca blanca 10 (subido con datos reales) · Verifactu 7 (bajado: −63 % tras aplazamiento).
4. Datos reales de búsqueda (Planificador, 4 oct): iso9001 320/mes ES (+242 %), claudecode 38.750 (+172 %, −33 % a 3 meses), cecra 560 (+49 %, puja 15,59 €), iso27001 30, gbp 14.120 (+105 %), verifactu 40.500 (−63 %).
5. **Candidato a validar: Kit de transición ISO 9001:2026.** Es "Normach con otra norma": producto cerrado en vez de servicio, sin firma ni reunión.
6. Marca de producto: **Normagrade** (norma + upgrade). Dominios normagrade.es/.com/.eu/.io sin DNS el 6 oct, NO comprados. Frase: "tu sistema de gestión, al día con la norma".
7. **Envío desde normach.es (dominio de fogueo), no desde dominio nuevo.** normach.eu queda solo para máquinas. Remitente: alias `equipo@normach.es` ("Equipo técnico de Normach") en la cuenta de Laura; mantiene la reputación del dominio. Laura no hace nada; quién factura (Sauco & Co SL si está constituida) y el reparto societario son asunto de Jorge y su gestor.
8. Es una **preventa**, no un Mom Test: se pide dinero. El Mom Test va como tercer correo solo a quien responde y no paga.

## 3. Oferta

- Esencial 149 € (correspondencia 2015→2026 cláusula a cláusula, checklist de brechas Excel, plan 90 días, registro de cambios para el auditor, guía 10 pág.).
- Completo 249 € / **preventa 149 €** (+ manual y 12 procedimientos revisados en Word, informe de revisión por la dirección, FAQ auditoría).
- Consultoras 590 € / preventa 390 € (licencia clientes ilimitados, sin marca).
- Entrega ≤ 15 días tras cierre; devolución íntegra si no se entrega. No reproduce texto ISO (derechos de autor); el comprador debe tener la norma.

## 4. Lead válido (los 5 criterios, todos)

Certificado ISO 9001 vigente (buscadores AENOR, Bureau Veritas, SGS, TÜV, DNV, Applus, IQNet) · caducidad del certificado en 2027 · pyme 20-150 empleados con un único responsable de calidad · sector industrial (metal, plástico, componentes, alimentación, instalaciones) · persona identificada con correo verificado y NO presente en cuentas.csv / cuentas_eu.csv de Normach. Consultoras aparte, no cuentan para el umbral.

Filtros Apollo/SN: títulos exactos "Responsable de Calidad", "Responsable de Sistemas de Gestión", "Responsable de Calidad y Medio Ambiente", "Jefe de Calidad", "Quality Manager"; persona y sede en España; 21-50 y 51-200; NAICS 31-33; email verificado/likely to engage. Apollo: 102 créditos de contacto disponibles hasta el 15 oct; la búsqueda por API no está en el plan (hay que buscar por interfaz).

## 5. Umbrales

Sobre 100 entregados: ≥5 pagos construir · 2-4 Mom Test con 10 y repetir · 0-1 cerrar.
Sobre 30-40 muy cualificados: ≥3 construir · 1-2 ampliar a 100 antes de decidir · 0 pagos y ≥5 respuestas con interés → Mom Test y repetir · 0 pagos y <3 respuestas → cerrar.

## 6. Mecánica para el Apps Script (normach.es)

Remitente equipo@normach.es · 25/día mar 13 a vie 16 (15/día si Postmaster "baja") · 08:30-11:00, 4-9 min aleatorios · asuntos A/B alternos · texto plano, un solo enlace (página en normach.es con dos muestras descargables sin email + botón Stripe), sin adjunto, sin píxel · parada por respuesta, rebote o "baja" · rebote se sustituye para llegar a 100 entregados · correo 2 a +24 h 16:00 a no respondidos · correo 3 (Mom Test: "¿cómo hicisteis la transición de 2015?", "¿cuánto costó y a quién?", "¿qué os falta para la 2026?") lun 19 solo a quien respondió y no pagó · cierre lun 19 oct 11:00 · misma cualificación legal y pie de baja que en máquinas.
Hoja: empresa, nombre, cargo, email, sector, certificador, caducidad_cert, fuente, cualificacion (0-5; entran 4-5), variante, fecha_envio_1/2/3, estado, respuesta_tipo, pago_fecha, importe, momtest_1/2/3, notas. "pagó" lo marca Jorge desde Stripe.

Textos de correo 1, correo 2, LinkedIn y esqueleto de página: en la pestaña del plan y en `reports/Plan de preventa ISO 9001-2026.md`.

## 7. Pendiente (bloqueantes primero)

- [ ] Verificar en iso.org fecha de publicación de ISO 9001:2026 (dato de fragmento: 16 sep 2026) y en IAF/ENAC el periodo de transición (si 3 años, el mensaje no puede vender urgencia). Comprar la norma (UNE si existe).
- [ ] Decidir quién factura (gestor) y el reparto societario (Sauco & Co SL: ¿constituida? ¿50/50?).
- [ ] Crear alias equipo@normach.es y "enviar como" en Gmail. Mirar Postmaster Tools del .es.
- [ ] Exportar 150 leads crudos (Apollo/SN) → cualificar → 100 (o 30-40) con cualificacion ≥4.
- [ ] Dos muestras (correspondencia de 2 cláusulas + capítulo de checklist). Página de muestras y preventa en normach.es. Enlace Stripe (EUR y USD).
- [ ] Apps Script y hoja. Cinco envíos de prueba a Gmail y Outlook propios.
- [ ] Mar 13: arrancar.

## 8. Prompt de arranque para la sesión local

```
Trabaja en el repo saucoandcompany/tbd, rama claude/solo-venture-independence-jo1gwz. Lee HANDOFF.md
y después reports/Plan de preventa ISO 9001-2026.md. El proyecto es la preventa escrita del Kit de
transición ISO 9001:2026 (marca de producto Normagrade, enviado desde normach.es como "Equipo técnico
de Normach"). Hoy toca: (1) con mi Chrome, exportar 150 leads de Apollo con los filtros de la sección 4
y cualificarlos contra los buscadores de certificados; (2) generar la hoja de seguimiento con las
columnas de la sección 6; (3) escribir el Apps Script de envío con los parámetros de la sección 6.
No compres créditos ni cambies planes; no envíes ningún correo real sin que yo lo apruebe.
```
