# HoliTok: A Continuous Holistic Tokenization with Robust Dual Capabilities of Speech Generation and Understanding

- **ID:** 21
- **Autores:** Bohan Li, Shi Lian, Hankun Wang, Yiwei Guo, Yu Xi, Zhihan Li, Da Zheng, Colin Zhang y Kai Yu
- **Año:** 2026
- **Categoría:** Tokenización y modelos generativos
- **Prioridad:** Núcleo
- **PDF:** [`21_HoliTok.pdf`](../21_HoliTok.pdf)
- **Clave BibTeX:** `li2026holitok`

## Resumen en español

HoliTok propone una representación continua común para generación y comprensión. Codifica voz de 48 kHz en secuencias de 25 Hz y 128 dimensiones mediante entrenamiento progresivo que preserva señal, incorpora semántica y mantiene facilidad de modelado. Sobre ella construye un sistema AR+DiT que realiza síntesis y reconocimiento; entre las representaciones comparadas es la única que funciona de forma robusta en la arquitectura unificada sin trucos adicionales.

## Evidencia extraída

- **Representación:** Latentes continuos holísticos de 25 Hz y 128 dimensiones.
- **Bitrate:** No cuantizado como bitstream; 25 vectores/s antes de cuantización.
- **Latencia:** No definida como sistema streaming.
- **Evaluación:** Reconstrucción, síntesis controlable, ASR y modelado unificado.
- **Canal/robustez:** Sin canal.
- **Código o artefactos:** Sí; código público.
- **Resultado principal:** Única representación evaluada robusta en generación y comprensión unificadas sin ajustes extra.

## Limitaciones

Al ser continua no constituye todavía un payload digital de bitrate medible.

## Uso en el TFM

Referencia de representación unificada y advertencia sobre convertir frame rate en bitrate real.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
