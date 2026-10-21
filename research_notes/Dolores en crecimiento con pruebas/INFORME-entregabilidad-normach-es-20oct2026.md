# Entregabilidad de normach.es: preventa ISO 9001 (13 al 16 de octubre de 2026)

Revisión de solo lectura hecha el 20/10/2026. No se ha enviado nada y no se ha tocado el DNS, Workspace ni Postmaster.

## Tabla por día

| Día | Enviados (Gmail) | Vistos DMARC Google | Vistos DMARC Microsoft | DKIM pass | SPF pass (alineado) | Disposición | Tasa de spam (Postmaster) | Reputación (Postmaster) |
|---|---|---|---|---|---|---|---|---|
| Mar 13 | 27 | 1 | 19 | 19 de 20 (95 %) | 0 % (SPF pasa para normach.eu) | 19 none, **1 quarantine** | sin datos | sin datos |
| Mié 14 | 26 | 5 | sin informe | 5 de 5 (100 %) | 0 % (SPF pasa para normach.eu) | none | sin datos | sin datos |
| Jue 15 | 26 | 3 | sin informe | 3 de 3 (100 %) | 0 % (SPF pasa para normach.eu) | none | sin datos | sin datos |
| Vie 16 | 20 | 1 | 16 | 17 de 17 (100 %) | 0 % (SPF pasa para normach.eu) | none | sin datos | sin datos |

Notas:
- **Qué cubren los informes.** Solo ven los correos que llegan a buzones de Google o de Microsoft. Entre los dos cubren 45 de los 99 envíos. El resto fue a otros servidores, que no mandan informes.
- **Faltan dos días de Microsoft.** No envió informe del 14 ni del 15.
- **Días fuera de la campaña.** Google tiene informes del 12 (3 mensajes, las pruebas) y del 18 (1 mensaje). No hay informe de Google del 17.
- **SPF.** Pasa en todas las filas, pero para normach.eu: el remitente técnico es la cuenta principal de Workspace, normach.eu. Por eso no se alinea con el From normach.es. DMARC pasa gracias a DKIM (d=normach.es), y en esta configuración es lo esperado.
- **La única fila con fallo.** Es la del 13 en Microsoft, desde 35.174.145.124 (us.cloud-sec-av.com, la pasarela de seguridad de correo de un destinatario). Esa pasarela vuelve a enviar el mensaje y rompe la firma DKIM. El resultado es DKIM fail y SPF softfail, y la política p=quarantine lo mandó a cuarentena. No es nadie enviando con nuestro dominio.
- **Fallos en IPs de Google:** ninguno. Todas las IPs de origen son de Google (209.85.220.41 y el rango 2607:f8b0:4864:20::/64), salvo la pasarela de seguridad.

## Veredicto por bloque

- **Autenticación: limpia.** DKIM pasa en 44 de 45 mensajes y DMARC alinea por DKIM. El único fallo es la pasarela de un destinatario, no un problema nuestro.
- **Colocación (bandeja o spam): no se puede saber.** normach.es no está añadido en Postmaster, y tampoco normach.eu ni normach.net, así que no hay datos. No lo he añadido.
- **Listas negras: no.** Están limpios normach.es (68 listas), 209.85.220.41, 35.174.145.124 y 74.125.224.52 (60 listas cada una). 74.125.224.52 ya no está en SpamCop ni en MailSpike.
- **DNS: correcto.**
  - SPF: incluye _spf.google.com y hace 1 búsqueda de 10.
  - DKIM: hay clave en google._domainkey.
  - DMARC: p=quarantine con pct=100 y los informes van a laura@normach.eu.
  - MX: apunta a smtp.google.com.
  - BIMI: no hay. default._bimi responde solo porque hay un comodín que apunta al aparcamiento de DonDominio.

## Lectura honesta

1. Los datos dicen que los correos se aceptaron, se autenticaron y no fueron rechazados. En Google y Microsoft, la política DMARC no mandó ninguno a cuarentena salvo 1 de 45.
2. Lo que no dicen es si cayeron en la bandeja de entrada o en spam: esa decisión la toma el filtro de cada proveedor y no aparece en DMARC. Sin Postmaster ni una prueba con buzones propios, no se puede saber si "llegó y no respondieron" o "no lo vieron".
3. Aunque se añadiera ahora, Postmaster casi no mostraría nada para esta campaña: Google solo vio entre 1 y 5 mensajes al día, muy por debajo del volumen que necesita para dar datos. La única manera de saberlo es una prueba de colocación con buzones propios en Gmail y Outlook.
