# SPG-Codec: Exploring the Role and Boundaries of Semantic Priors in Ultra-Low-Bitrate Neural Speech Coding

- **ID:** 17
- **Autores:** Mingyu Zhao, Zijian Lin, Kun Wei y Zhiyong Wu
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **PDF:** [`17_SPG_Codec.pdf`](../17_SPG_Codec.pdf)
- **Clave BibTeX:** `zhao2026spgcodec`

## Resumen en español

SPG-Codec analiza de forma sistemática cuándo ayudan los priors congelados HuBERT y Whisper. A 1,5 kbps pueden reducir relativamente el WER alrededor de un 10 %, pero el beneficio desaparece al superar aproximadamente 6 kbps, fenómeno denominado Semantic Retirement. HuBERT conserva mejor prosodia y timbre, mientras Whisper reduce alucinaciones fonéticas en ruido; una regulación dependiente del bitrate equilibra naturalidad y consistencia.

## Evidencia extraída

- **Representación:** Latentes de códec condicionados por priors semánticos HuBERT o Whisper.
- **Bitrate:** Análisis desde 1,5 kbps; frontera práctica alrededor de 6 kbps.
- **Latencia:** No destacada; priors congelados añaden cómputo.
- **Evaluación:** WER, alucinaciones, prosodia, timbre, ruido y generalización a hablantes no vistos.
- **Canal/robustez:** Robustez a ruido acústico, no packet loss.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Los priors ayudan en ultra-bajo bitrate pero dejan de aportar al crecer la capacidad.

## Limitaciones

No existe un prior universal: Whisper y HuBERT favorecen atributos diferentes.

## Uso en el TFM

Justifica una selección de prior dependiente del bitrate y ablaciones semántico-acústicas.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
