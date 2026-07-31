# Error-Resilient Semantic Communication for Speech Transmission over Packet-Loss Networks

- **ID:** 25
- **Autores:** Zhuohang Han, Jincheng Dai, Shengshi Yao, Junyi Wang, Yanlong Li, Kai Niu, Wenjun Xu y Ping Zhang
- **Año:** 2025
- **Categoría:** Robustez de red y transmisión adaptativa
- **Prioridad:** Núcleo
- **PDF:** [`25_Glaris_Error_Resilient_Speech_SemCom.pdf`](../25_Glaris_Error_Resilient_Speech_SemCom.pdf)
- **Clave BibTeX:** `han2025glaris`

## Resumen en español

Glaris introduce un códec semántico resiliente que opera en el espacio latente generativo y sigue siendo compatible con redes digitales existentes. Priors generativos permiten ocultar paquetes perdidos equilibrando coherencia y fidelidad, y un mecanismo integrado limita la propagación de errores. En LibriSpeech supera códecs resilientes y reduce la redundancia frente a FEC tradicional, acercándose a la robustez de JSCC.

## Evidencia extraída

- **Representación:** Latentes generativos paquetizados con packet-loss concealment.
- **Bitrate:** Comparación eficiencia-redundancia; cifras por configuración en tablas.
- **Latencia:** Diseñado para tiempo real, pero cifra no incluida en el abstract.
- **Evaluación:** LibriSpeech; reconstrucción, robustez y eficiencia frente a FEC y códecs resilientes.
- **Canal/robustez:** Redes con packet loss dinámico.
- **Código o artefactos:** No indicado.
- **Resultado principal:** Logra robustez cercana a JSCC manteniendo compatibilidad digital y menor overhead que FEC.

## Limitaciones

La recuperación generativa puede inventar detalle y requiere evaluar deriva semántica.

## Uso en el TFM

Referencia principal para diseñar packetización, concealment y comparación con FEC.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
