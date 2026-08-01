# ContextCodec: Content-Focused Context Guidance for Ultra-Low Bitrate Speech Coding

- **ID:** 16
- **Autores:** Chengbin Liang, Wenqi Guo, Hao Cao y Zhijin Qin
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **PDF:** [`16_ContextCodec.pdf`](../16_ContextCodec.pdf)
- **Clave BibTeX:** `liang2026contextcodec`

## Resumen en español

ContextCodec prioriza el mensaje lingüístico cuando el bitrate cae por debajo de 1 kbps. Separa una rama acústica de otra de contexto alineada con fonemas mediante una pérdida contrastiva tipo CLIP y reduce la fuga de información paralingüística. El decoder recibe esta guía en todas sus etapas y un refinador latente autorregresivo permite alcanzar un compromiso sólido a 500 bps, con RTF 0,4886 en CPU móvil.

## Evidencia extraída

- **Representación:** Rama acústica y contexto fonético/content-focused desacoplado.
- **Bitrate:** Hasta 500 bps.
- **Latencia:** RTF 0,4886 en una CPU móvil típica; no equivale a latencia extremo a extremo.
- **Evaluación:** Calidad e inteligibilidad en régimen inferior a 1 kbps y ejecución móvil.
- **Canal/robustez:** No evalúa pérdidas de paquetes.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Compromiso calidad-inteligibilidad competitivo a 500 bps con ejecución sub-tiempo-real en móvil.

## Limitaciones

Al reducir fuga paralingüística puede perder identidad o emoción si no se transmite un canal auxiliar.

## Uso en el TFM

Candidato ultra-low-bitrate y evidencia para separar contenido de atributos paralingüísticos.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
