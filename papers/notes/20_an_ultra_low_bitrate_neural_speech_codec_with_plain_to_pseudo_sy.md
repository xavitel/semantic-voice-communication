# An Ultra-Low-Bitrate Neural Speech Codec with Plain-to-Pseudo Synergistic Vector Quantization

- **ID:** 20
- **Autores:** Xiao-Hang Jiang, Yang Ai, Fei Liu, Rui-Chen Zheng, Jian-Qing Gao, Zhen-Hua Ling y Ji Wu
- **Año:** 2026
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **PDF:** [`20_P2PSynCodec.pdf`](../20_P2PSynCodec.pdf)
- **Clave BibTeX:** `jiang2026p2psyncodec`

## Resumen en español

P2PSynCodec observa que las últimas capas de un RVQ consumen el mismo bitrate aunque aporten cada vez menos. Sustituye esos códigos transmitidos por pseudo-tokens predichos en el receptor: solo un cuantizador básico genera bits y varios pseudo-cuantizadores reconstruyen detalle sin coste de transmisión. A 0,5 kbps alcanza una calidad comparable a códecs rivales de 2 kbps.

## Evidencia extraída

- **Representación:** Un flujo VQ transmitido y pseudo-tokens VQ predichos en el receptor.
- **Bitrate:** 0,5 kbps; comparación con referencias a 2,0 kbps.
- **Latencia:** No indicada; la predicción de pseudo-tokens añade cómputo.
- **Evaluación:** Calidad de reconstrucción frente a códecs competitivos.
- **Canal/robustez:** Sin pérdidas de paquetes.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Calidad comparable a 2 kbps transmitiendo solo 0,5 kbps.

## Limitaciones

El receptor debe inferir detalle y puede degradarse fuera de distribución o con errores del flujo base.

## Uso en el TFM

Ejemplo directo de recuperación generativa para reducir payload y candidato ultra-low-bitrate.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
