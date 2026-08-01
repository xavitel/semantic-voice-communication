# A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation

- **ID:** 08
- **Autores:** Hanchen Pei, Shujie Liu, Yanqing Liu, Jianwei Yu, Yuanhang Qian, Gongping Huang, Sheng Zhao y Yan Lu
- **Año:** 2026
- **Categoría:** Identidad, prosodia y emoción
- **Prioridad:** Apoyo
- **PDF:** [`08_SpeechEdit_Unified_Neural_Codec_LM.pdf`](../08_SpeechEdit_Unified_Neural_Codec_LM.pdf)
- **Clave BibTeX:** `pei2026speechedit`

## Resumen en español

SpeechEdit amplía el TTS zero-shot con control selectivo de atributos. El modelo reproduce por defecto el perfil acústico completo de un prompt, pero permite sustituir únicamente rasgos indicados explícitamente, como timbre o prosodia. Se entrena con LibriEdit, construido a partir de pares diferenciales de LibriHeavy, y mantiene naturalidad y robustez mientras ofrece control localizado.

## Evidencia extraída

- **Representación:** Tokens de códec condicionados por prompt y órdenes de edición de atributos.
- **Bitrate:** No se evalúa como códec de transmisión.
- **Latencia:** No indicada; generación de TTS.
- **Evaluación:** Naturalidad, robustez y control de atributos sobre LibriEdit/LibriHeavy.
- **Canal/robustez:** Sin canal.
- **Código o artefactos:** Demo y muestras públicas.
- **Resultado principal:** Permite editar atributos concretos sin reemplazar todo el perfil acústico del hablante.

## Limitaciones

No está optimizado para streaming ni cuantifica el coste de transmitir señales de control.

## Uso en el TFM

Apoya una interfaz explícita para separar identidad, contenido y prosodia en la cascada modular.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
