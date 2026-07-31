# SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound

- **ID:** 10
- **Autores:** Haohe Liu, Xuenan Xu, Yi Yuan, Mengyue Wu, Wenwu Wang y Mark D. Plumbley
- **Año:** 2024
- **Categoría:** Códecs semánticos y ultra-bajo bitrate
- **Prioridad:** Núcleo
- **PDF:** [`10_SemantiCodec.pdf`](../10_SemantiCodec.pdf)
- **Clave BibTeX:** `liu2024semanticodec`

## Resumen en español

SemantiCodec combina un encoder semántico AudioMAE discretizado mediante k-means con un encoder acústico residual y un decoder de difusión. Funciona con voz, música y sonido general a 25, 50 o 100 tokens por segundo, equivalentes a 0,31-1,40 kbps. Reporta mejor reconstrucción que Descript y representaciones más informativas semánticamente que otros códecs, incluso con menor tasa.

## Evidencia extraída

- **Representación:** Dos flujos: tokens semánticos AudioMAE y tokens acústicos residuales.
- **Bitrate:** 0,31-1,40 kbps; 25-100 tokens/s.
- **Latencia:** Decoder de difusión; no orientado a streaming de baja latencia.
- **Evaluación:** Reconstrucción y contenido semántico en voz, música y audio general.
- **Canal/robustez:** No incluye packet loss.
- **Código o artefactos:** Sí; código y demos públicos.
- **Resultado principal:** Mejora Descript a tasas ultra-bajas y conserva más información semántica.

## Limitaciones

La difusión compromete latencia y el audio general puede diluir objetivos específicos de voz.

## Uso en el TFM

Referencia ultra-low-bitrate y ejemplo claro de separación semántico-acústica.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
