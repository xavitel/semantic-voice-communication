# HASCom: A Heterogeneous Affective-Semantic Communication Framework for Speech Transmission

- **ID:** 22
- **Autores:** Zhenjia Yu, Taojie Zhu, Md Arman Hossain, Zineb Zbarna y Lei Wang
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Núcleo
- **PDF:** [`22_HASCom_Affective_Semantic_Communication.pdf`](../22_HASCom_Affective_Semantic_Communication.pdf)
- **Clave BibTeX:** `yu2026hascom`

## Resumen en español

HASCom separa la información lingüística y afectiva en dos canales heterogéneos. Los fonemas discretos se protegen digitalmente con LDPC para garantizar recuperación, mientras embeddings emocionales continuos viajan mediante JSCC analógico para evitar cuantización irreversible y cliff effect. Un decoder de difusión guiado por semántica y emoción supera baselines en AWGN y Rayleigh a SNR bajo, con menos de 0,1 ms en los módulos JSCC.

## Evidencia extraída

- **Representación:** Fonemas discretos protegidos y embeddings emocionales continuos.
- **Bitrate:** Debe extraerse por configuración; dos flujos con protección diferente.
- **Latencia:** Menos de 0,1 ms para módulos JSCC; no es latencia completa del sistema de difusión.
- **Evaluación:** Similitud semántica y MOS bajo AWGN y Rayleigh.
- **Canal/robustez:** AWGN y Rayleigh; diseño híbrido LDPC/JSCC.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Mejora similitud y MOS a SNR bajo preservando contenido y afecto por vías distintas.

## Limitaciones

La cifra de JSCC no incluye todo el decoder; complejidad y sincronización de dos flujos.

## Uso en el TFM

Arquitectura de referencia para transmitir emoción como side-channel protegido de manera diferenciada.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
