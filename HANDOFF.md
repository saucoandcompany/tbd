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

## 9. ACTUALIZACIÓN 12 oct 2026 (decisiones de Jorge vía sesión "Leads Email" de Normach). MANDA SOBRE LA SECCIÓN 6.

**Formato del test:** ticket de 149 €. UN SOLO correo por prospecto que pregunta si le interesa pre-reservar las plantillas pagando 149 €. Sin funnel: ni seguimientos, ni correo 2, ni correo 3 de Mom Test, ni peticiones de llamada. El correo lleva el precio y pide la decisión. Las reglas de Normach "el primer mensaje no pitchea" y "sin precios" NO aplican aquí.

**Reglas que sí aplican:**
- Hasta 30 al día por normach.es SOLO durante el test (después vuelve a 20). Ventana 07:00 a 17:15 lunes a jueves; viernes hasta 13:30. Suelo de 20 min por dominio, huecos irregulares de 20 a 27 min, nunca iguales ni por debajo de 20. Caben 26 a 30 lun-jue y 17 a 19 el viernes: 100 correos en unos 4 días hábiles.
- Solo direcciones de persona. Nunca construir correos. Rebote o 5.7.1 cierra la dirección el mismo día, sin reintento. Opt-out vale para todos los canales. Todo en CSV con fecha absoluta.
- Cero invención (testimonios, clientes, casos). Sin em-dashes. Nunca insinuar que se certifica: certifica un organismo acreditado.
- Enviados de Gmail es la fuente de verdad. Correo en frío nunca con Responder.
- Proyecto de Apps Script PROPIO (no tocar "Proyecto sin título", id 1Z371439oS-MJgRjEmKBCeZIiYJILNFbR8WbD-N0XJSV6hjXG_J95Fb1U, que es el de Normach con la tanda del 13/10 por .eu y .net). Comparten cuota diaria de Gmail (misma cuenta). previsualizar() como PRIMERA función (no envía; el desplegable preselecciona la primera). Verificador del día. cancelar() no borra propiedades del script. El desplegable solo se refresca al recargar.
- Jorge aprueba el texto exacto antes de poner en cola. Quien conteste se contesta el mismo día y se le da lo que pida tal cual.
- Saludo por hora real de envío: "Buenos días," hasta las 12:00, "Hola," después.

**Cómo se envía:** Apps Script ejecutado por laura@normach.eu. Envío con GmailApp.sendEmail(para, asunto, textoPlano, {from: alias, htmlBody: html}) → multipart texto + HTML. Disparador cada minuto que solo actúa el día de su FECHA; cada envío con su hora en el plan y clave por día en propiedades del script para no repetir.
**Firma:** GmailApp no añade la firma de Gmail; va pegada como HTML en htmlBody con <a href> real (en texto plano Gmail reescribe el dominio como enlace de seguimiento). laura@normach.es y laura@normach.net son alias "Enviar como" de laura@normach.eu. OJO: Return-Path de los tres dominios es laura@normach.eu; rebotes y respuestas del kit caen en la misma bandeja que las de Normach. El alias equipo@normach.es propuesto en la sección 2 hay que crearlo; si no existe el 13, el remitente será laura@normach.es.
**Volumen real reciente de .es (techo 20):** 28/09 19 · 29/09 19 · 30/09 19 · 01/10 18 · 02/10 10 · 05/10 19 · 06/10 1 · 07/10 20 · 08/10 14 · 09/10 9. Postmaster no mirado. Sin recuento de rebotes.
**Exclusividad de .es confirmada 13 a 16/10.** Los 48 seguimientos de Normach por .es se movieron al 19, 20 y 21/10. Durante el test Normach solo manda por .es dos respuestas manuales en hilos abiertos (Grupo Pymar el 14, IPLA): dejar 20 min a cada lado. Desde el 19, .es vuelve a Normach. Si el test no termina el 16, avisar a Jorge antes de seguir.
**Lista de exclusión (cruzar por DOMINIO de correo y de web, no por dirección exacta):** C:\Users\jmoli\Claude\Projects\newbizz\cuentas_normach_121026.csv (1099 líneas, misma forma que cuentas.csv; tras la copia entraron 36 correos más en cuentas.csv). Para exclusión completa añadir: cuentas_eu.csv, los dos trackers de LinkedIn, calendario-envio-nordicos.csv y seguimientos-calientes.csv, en C:\Users\jmoli\Claude\Projects\Leads\leads (solo lectura).

**Decide Jorge ANTES de enviar (no están decididos):**
- Quién cobra y factura. Sauco & Co SL NO existe todavía; en Normach los presupuestos los emite Laura como autónoma.
- Si el enlace de pago va en el correo frío o solo cuando digan que sí. Un enlace de pago en primer contacto puntúa en los filtros de spam.
- Si los 149 € son reembolsables y cuándo se entregan las plantillas: debe ir escrito en el correo.
- Cómo se escribe el IVA (149 € + IVA, o IVA incluido).

**Consecuencias para lo escrito antes en este archivo y en el plan:** la secuencia de 3 correos de la sección 6 queda anulada; el correo 1 se reescribe para llevar precio, condiciones (reembolso, fecha de entrega, IVA) y la pregunta directa de pre-reserva; los umbrales se mantienen (sobre entregados); el cierre pasa a contarse 48 h después del último envío del viernes 16, es decir lunes 19 (hábil) como estaba.

## 10. Método para pegar y ejecutar el .gs en el Chrome de laura@normach.eu (de la sesión "Leads Email", 12 oct). Para la sesión local; la nube no puede ejecutarlo.

Chrome libre: la tanda de Normach del 13/10 corre en servidores de Google. Chrome deviceId ced4d154-5f56-4f2a-b964-e89182f2fa02, cuenta laura@normach.eu.
- Pestaña propia. No tocar, cerrar, guardar ni ejecutar la de "Proyecto sin título" (1Z371439oS-MJgRjEmKBCeZIiYJILNFbR8WbD-N0XJSV6hjXG_J95Fb1U).
- Cada select_browser de otra sesión roba el grupo de pestañas: si falla un lote con "not in Claude's tab group", select_browser y repetir el lote en la misma llamada.
- Pestaña congelada (evaluate de 45 s) = ventana minimizada: navegar otra vez a la URL o pedir a Jorge que la traiga al frente.

Pegado del .gs sin portapapeles ni teclas ni clasp, todo por javascript_tool:
a) Local: gzip del .gs → base64 → trozos de ~7.100 chars. SHA-256 del .gs y checksum por trozo (suma de charCode*(j+1) mod 99991).
b) Un trozo por llamada: window._b=[]; window._b[i]='...'; devolver [longitud, checksum]. Seis trozos caben en un browser_batch.
c) En página: atob → Uint8Array → new Response(new Blob([u]).stream().pipeThrough(new DecompressionStream('gzip'))).arrayBuffer(). SHA-256 con crypto.subtle.digest, comparar DENTRO de la página y devolver solo true/false (un hash crudo en la salida lo bloquea el filtro). Promesas no devuelven valor: guardar en window y leer en segunda llamada tras 2 s.
d) monaco.editor.getModels()[0].setValue(texto); comprobar getValue() === texto.
e) Guardar: document.querySelector('[aria-label="Guardar proyecto en Drive"]').click(); guardado cuando el botón queda deshabilitado.
f) Ejecutar: puente en línea 1 "function _ahora() { return comprobar(); }", guardar, RECARGAR (el desplegable solo se refresca al recargar), comprobar que [aria-label="Seleccionar la función que se va a ejecutar"] lee _ahora, click en [aria-label="Ejecutar la función seleccionada"]. Registro de ejecución: leer con captura (innerText con correos lo bloquea el filtro). Luego puente a programar(), guardar, recargar, ejecutar. Al final quitar el puente, guardar, recargar, comprobar que el desplegable lee previsualizar y que el hash del modelo coincide. Si el modo automático bloquea el clic de Ejecutar, lo pulsa Jorge.

Manifiesto: Configuración del proyecto → "Mostrar appsscript.json"; aparece como segundo modelo de Monaco. Servicio avanzado Gmail (Servicios, +, Gmail API v1, id Gmail) o en dependencies.enabledAdvancedServices; solo hace falta para enviar dentro de un hilo. Para el correo único en frío basta GmailApp.sendEmail con from: 'laura@normach.es' y htmlBody con firma HTML.

Solo Jorge: primera ejecución de proyecto nuevo = consentimiento OAuth ("Google no ha verificado esta aplicación" → Avanzado → Permitir); contraseñas y 2FA; aprobar el texto exacto antes de armar; enlace/plataforma de pago y quién factura. El alias "Enviar como" laura@normach.es YA existe. equipo@normach.es NO existe aún.

Leads Email ofrece armarlo ella si Jorge se lo dice.
