# Large Speech Model Enabled Semantic Communication

- **ID:** 24
- **Autores:** Yun Tian, Zhijin Qin, Guocheng Lv, Ye Jin, Kaibin Huang y Zhu Han
- **Año:** 2025
- **Categoría:** Robustez de red y transmisión adaptativa
- **Prioridad:** Núcleo
- **PDF:** [`24_LargeSC.pdf`](../24_LargeSC.pdf)
- **Clave BibTeX:** `tian2025largesc`

## Resumen en español

LargeSC integra Mimi como tokenizer, un controlador que adapta la tasa y aplica protección desigual dentro del flujo y Moshi ajustado con LoRA para recuperar tokens perdidos. El sistema responde al contenido, la probabilidad de pérdida y el presupuesto de ancho de banda. Opera entre 550 bps y 2,06 kbps, mejora la calidad frente a baselines con pérdidas altas y alcanza aproximadamente 460 ms extremo a extremo.

## Evidencia extraída

- **Representación:** Tokens Mimi con control adaptativo, UEP y recuperación generativa Moshi.
- **Bitrate:** 550 bps-2,06 kbps.
- **Latencia:** Aproximadamente 460 ms extremo a extremo.
- **Evaluación:** Calidad bajo diferentes probabilidades de pérdida y restricciones de ancho de banda.
- **Canal/robustez:** Packet loss dinámico y UEP dentro del bitstream.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Mantiene mejor calidad bajo pérdidas altas con bitrate adaptativo y recuperación generativa.

## Limitaciones

460 ms supera el objetivo conversacional de 300 ms y depende de modelos fundacionales pesados.

## Uso en el TFM

Arquitectura objetivo para el experimento de packet loss, adaptación y recuperación.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
