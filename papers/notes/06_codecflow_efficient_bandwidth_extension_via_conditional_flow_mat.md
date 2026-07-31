# CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space

- **ID:** 06
- **Autores:** Bowen Zhang, Junchuan Zhao, Ian McLoughlin, Ye Wang y A. S. Madhukumar
- **Año:** 2026
- **Categoría:** Reconstrucción y mejora generativa
- **Prioridad:** Apoyo
- **PDF:** [`06_CodecFlow.pdf`](../06_CodecFlow.pdf)
- **Clave BibTeX:** `zhang2026codecflow`

## Resumen en español

CodecFlow realiza extensión de ancho de banda directamente en el espacio latente compacto de un códec neuronal. Combina flow matching condicionado por sonoridad con un RVQ restringido estructuralmente para alinear representaciones de baja y alta resolución. En tareas de 8 a 16 kHz y de 8 a 44,1 kHz mejora fidelidad espectral y calidad perceptual evitando parte del coste de modelar espectrogramas o waveform completos.

## Evidencia extraída

- **Representación:** Embeddings continuos de códec y RVQ estructurado.
- **Bitrate:** No reportado como sistema de transmisión; parte de audio limitado en banda.
- **Latencia:** Enfatiza eficiencia, pero no ofrece latencia conversacional en el abstract.
- **Evaluación:** Extensión 8→16 kHz y 8→44,1 kHz; fidelidad espectral y calidad perceptual.
- **Canal/robustez:** Sin canal ni pérdidas de paquetes.
- **Código o artefactos:** No indicado.
- **Resultado principal:** La reconstrucción en latentes iguala o supera métodos de BWE y reduce artefactos de alta frecuencia.

## Limitaciones

Resuelve restauración de banda, no compresión semántica extremo a extremo.

## Uso en el TFM

Referencia para un decoder generativo que recupere detalle acústico no transmitido.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
