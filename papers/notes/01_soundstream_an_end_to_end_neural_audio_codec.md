# SoundStream: An End-to-End Neural Audio Codec

- **ID:** 01
- **Autores:** Neil Zeghidour, Alejandro Luebs, Ahmed Omran, Jan Skoglund y Marco Tagliasacchi
- **Año:** 2021
- **Categoría:** Códecs neuronales fundamentales
- **Prioridad:** Núcleo
- **PDF:** [`SoundStream_An_End-to-End_Neural_Audio_Codec.pdf`](../SoundStream_An_End-to-End_Neural_Audio_Codec.pdf)
- **Clave BibTeX:** `zeghidour2021soundstream`

## Resumen en español

SoundStream presenta un códec neuronal de audio entrenado de extremo a extremo que combina un encoder y decoder convolucionales con cuantización vectorial residual. El dropout estructurado de los cuantizadores permite operar con un único modelo entre 3 y 18 kbps. A 3 kbps supera subjetivamente a Opus a 12 kbps, se aproxima a EVS a 9,6 kbps y admite ejecución en streaming y en tiempo real sobre CPU móvil.

## Evidencia extraída

- **Representación:** Tokens acústicos discretos obtenidos mediante RVQ.
- **Bitrate:** 3-18 kbps; resultado destacado a 3 kbps.
- **Latencia:** Baja latencia y streaming; cifra exacta no indicada en el abstract.
- **Evaluación:** Evaluación subjetiva a 24 kHz frente a Opus y EVS; audio general, voz y música.
- **Canal/robustez:** No modela pérdidas de paquetes ni canal inalámbrico.
- **Código o artefactos:** No indicado en el artículo del corpus.
- **Resultado principal:** SoundStream a 3 kbps supera a Opus a 12 kbps y se aproxima a EVS a 9,6 kbps.

## Limitaciones

Optimiza fidelidad acústica, no separa explícitamente contenido, identidad y prosodia, y no evalúa robustez de red.

## Uso en el TFM

Baseline histórico para medir cuánto aporta una representación semántica respecto a un RVQ puramente acústico.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
