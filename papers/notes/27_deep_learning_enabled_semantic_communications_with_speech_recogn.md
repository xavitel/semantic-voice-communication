# Deep Learning Enabled Semantic Communications with Speech Recognition and Synthesis

- **ID:** 27
- **Autores:** Zhenzi Weng, Zhijin Qin, Xiaoming Tao, Chengkang Pan, Guangyi Liu y Geoffrey Ye Li
- **Año:** 2022
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **PDF:** [`27_DeepSC_ST_Speech_Recognition_and_Synthesis.pdf`](../27_DeepSC_ST_Speech_Recognition_and_Synthesis.pdf)
- **Clave BibTeX:** `weng2022deepscst`

## Resumen en español

DeepSC-ST trata reconocimiento y síntesis como las tareas de una comunicación semántica de voz. Un encoder conjunto semántico-canal transmite características orientadas a recuperar texto; el receptor sintetiza voz con ese texto y la información del hablante. Un único modelo robusto opera en diversas condiciones de canal y supera sistemas convencionales y otros enfoques deep-learning, especialmente a SNR bajo; el trabajo incluye una demo de prueba de concepto.

## Evidencia extraída

- **Representación:** Características semánticas para ASR más información del hablante para TTS.
- **Bitrate:** Reducción significativa de datos; cifras deben tomarse del experimento original.
- **Latencia:** No reportada en el abstract.
- **Evaluación:** Reconocimiento, síntesis y robustez a varios SNR; demostración software.
- **Canal/robustez:** Modelo robusto frente a condiciones dinámicas y bajo SNR.
- **Código o artefactos:** Demo software descrita; disponibilidad actual debe verificarse.
- **Resultado principal:** Ventaja especialmente clara en bajo SNR al transmitir características orientadas a tarea.

## Limitaciones

La reconstrucción mediada por texto puede perder prosodia, emoción y matices no lingüísticos.

## Uso en el TFM

Antecedente más directo de la cascada ASR + identidad + TTS propuesta como baseline.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
