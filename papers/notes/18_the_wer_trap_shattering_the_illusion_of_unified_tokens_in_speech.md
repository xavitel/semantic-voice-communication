# The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models

- **ID:** 18
- **Autores:** Xiangyu Zhang, Yuxin Li, Haoyang Zhang, Shiqi Han, Hexin Liu, Qiquan Zhang, Beena Ahmed y Julien Epps
- **Año:** 2026
- **Categoría:** Evaluación y límites de representación
- **Prioridad:** Núcleo
- **PDF:** [`18_The_WER_Trap.pdf`](../18_The_WER_Trap.pdf)
- **Clave BibTeX:** `zhang2026wertrap`

## Resumen en español

The WER Trap demuestra que un tokenizer puede alcanzar WER bajo y, aun así, producir voz acústicamente ininteligible. Mediante compresión dinámica alineada con fronteras semánticas aísla tokens casi puramente lingüísticos; incluso con duraciones oráculo, los generadores pierden articulación y microdinámica. El resultado cuestiona la idea de un token único para comprensión y generación y defiende representaciones explícitamente desacopladas.

## Evidencia extraída

- **Representación:** Tokens semánticos ultracomprimidos y alineados dinámicamente.
- **Bitrate:** Frame rate extremo; las cifras exactas deben tomarse de las tablas.
- **Latencia:** No es el foco.
- **Evaluación:** WER frente a inteligibilidad acústica y síntesis con alineaciones oráculo.
- **Canal/robustez:** Sin canal.
- **Código o artefactos:** No indicado.
- **Resultado principal:** WER bajo no implica que la representación contenga trayectorias fonéticas suficientes para sintetizar voz inteligible.

## Limitaciones

El resultado depende del tokenizer y generador estudiados, pero expone una limitación metodológica general.

## Uso en el TFM

Obliga a evaluar WER junto con calidad, speaker similarity, prosodia y escucha humana.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
