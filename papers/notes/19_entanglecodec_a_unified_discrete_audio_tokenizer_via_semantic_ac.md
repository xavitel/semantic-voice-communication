# EntangleCodec: A Unified Discrete Audio Tokenizer via Semantic-Acoustic Entanglement

- **ID:** 19
- **Autores:** Hui Li, Yangfan Gao, Junlin Shang, Changhao Jiang, Tao Gui, Qi Zhang y Xuanjing Huang
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **PDF:** [`19_EntangleCodec.pdf`](../19_EntangleCodec.pdf)
- **Clave BibTeX:** `li2026entanglecodec`

## Resumen en español

EntangleCodec busca un único flujo discreto útil tanto para comprensión como para generación. Antes de cuantizar, alinea audio con captions ricas que incluyen contenido, identidad, emoción, prosodia y escena; un decoder de difusión con flow matching recupera voz, música y sonido general. Iguala la reconstrucción de códecs especializados, mejora hasta 7,4 puntos MMAR y permite que modelos de audio pequeños superen sistemas mucho mayores.

## Evidencia extraída

- **Representación:** Flujo único de tokens semántico-acústicos alineado con captions.
- **Bitrate:** Compacto; la cifra operativa debe extraerse de la configuración experimental.
- **Latencia:** Decoder de difusión y modelos de lenguaje; no orientado explícitamente a streaming.
- **Evaluación:** Reconstrucción, MMAR, TTS, text-to-audio y escalado de audio language models.
- **Canal/robustez:** Sin red.
- **Código o artefactos:** Sí; código y pesos públicos.
- **Resultado principal:** Hasta +7,4 en MMAR y buena reconstrucción con un flujo unificado.

## Limitaciones

Entrelazar atributos reduce control explícito y el decoder generativo complica latencia.

## Uso en el TFM

Contrapunto directo al desacoplamiento defendido por The WER Trap y candidato para comprensión+generación.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
