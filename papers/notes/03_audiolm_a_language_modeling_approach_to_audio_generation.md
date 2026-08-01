# AudioLM: a Language Modeling Approach to Audio Generation

- **ID:** 03
- **Autores:** Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier Pietquin, Matt Sharifi, Dominik Roblek, Olivier Teboul, David Grangier, Marco Tagliasacchi y Neil Zeghidour
- **Año:** 2022
- **Categoría:** Tokenización y modelos generativos
- **Prioridad:** Núcleo
- **PDF:** [`AudioLM_a_Language_Modeling_Approach_to_Audio_Generation.pdf`](../AudioLM_a_Language_Modeling_Approach_to_Audio_Generation.pdf)
- **Clave BibTeX:** `borsos2022audiolm`

## Resumen en español

AudioLM formula la generación de audio como modelado de lenguaje sobre tokens discretos. Combina tokens semánticos derivados de un modelo auto-supervisado, que capturan estructura de largo plazo, con tokens acústicos de SoundStream para recuperar alta fidelidad. Sin transcripciones, genera continuaciones de voz plausibles y conserva identidad y prosodia, estableciendo el paradigma jerárquico semántico-acústico que siguen muchos sistemas posteriores.

## Evidencia extraída

- **Representación:** Jerarquía de tokens semánticos w2v-BERT y tokens acústicos SoundStream.
- **Bitrate:** No se plantea como códec de comunicaciones ni reporta un bitrate operativo principal.
- **Latencia:** Generación autorregresiva offline; no orientada a conversación en tiempo real.
- **Evaluación:** Continuación de voz y piano; calidad, coherencia y conservación de hablante/prosodia.
- **Canal/robustez:** Sin canal de comunicaciones.
- **Código o artefactos:** No indicado como implementación completa en el PDF.
- **Resultado principal:** La combinación jerárquica resuelve el compromiso entre coherencia semántica y calidad acústica.

## Limitaciones

No es un sistema de transmisión, no optimiza latencia ni robustez y depende de generación autorregresiva costosa.

## Uso en el TFM

Fundamenta la separación de flujos semánticos y acústicos del diseño objetivo.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
