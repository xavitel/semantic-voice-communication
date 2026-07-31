# LDCodec: A High Quality Neural Audio Codec with Low-Complexity Decoder

- **ID:** 12
- **Autores:** Jiawei Jiang, Linping Xu, Dejun Zhang, Qingbo Huang, Xianjun Xia y Yijian Xiao
- **Año:** 2025
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Apoyo
- **PDF:** [`12_LDCodec.pdf`](../12_LDCodec.pdf)
- **Clave BibTeX:** `jiang2025ldcodec`

## Resumen en español

LDCodec se orienta a receptores con recursos limitados, especialmente smartphones. Combina una unidad residual ligera, cuantización LSRVQ, discriminadores subband-fullband y pérdidas perceptuales. A 6 kbps supera subjetiva y objetivamente a Opus a 12 kbps reduciendo la complejidad del decoder.

## Evidencia extraída

- **Representación:** Latentes acústicos con cuantización residual de corto y largo plazo.
- **Bitrate:** 6 kbps en el resultado principal.
- **Latencia:** Orientado a clientes móviles; cifra no indicada en el abstract.
- **Evaluación:** Pruebas subjetivas y objetivas frente a Opus.
- **Canal/robustez:** Sin packet loss.
- **Código o artefactos:** No indicado.
- **Resultado principal:** LDCodec a 6 kbps supera a Opus a 12 kbps con decoder de menor complejidad.

## Limitaciones

Bitrate superior al objetivo semántico y sin separación explícita de atributos.

## Uso en el TFM

Referencia de coste del receptor y despliegue en hardware limitado.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
