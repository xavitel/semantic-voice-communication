# Wireless Deep Speech Semantic Transmission

- **ID:** 14
- **Autores:** Zixuan Xiao, Shengshi Yao, Jincheng Dai, Sixian Wang, Kai Niu y Ping Zhang
- **Año:** 2022
- **Categoría:** Comunicación semántica de voz
- **Prioridad:** Núcleo
- **PDF:** [`14_Wireless_Deep_Speech_Semantic_Transmission.pdf`](../14_Wireless_Deep_Speech_Semantic_Transmission.pdf)
- **Clave BibTeX:** `xiao2022dsst`

## Resumen en español

DSST aprende una transformación no lineal de la voz a un espacio semántico y un encoder conjunto fuente-canal. Un modelo entrópico estima la importancia desigual de las características para asignar tasas distintas, mientras un mecanismo adaptativo permite usar un único modelo a diversos SNR. Frente a sistemas convencionales y semánticos previos mejora métricas objetivas y subjetivas y ahorra hasta un 75 % de ancho de banda a igual calidad.

## Evidencia extraída

- **Representación:** Latentes semánticos continuos con codificación fuente-canal y asignación de tasa por importancia.
- **Bitrate:** Flexible; hasta 75 % menos ancho de banda a calidad equivalente.
- **Latencia:** No indicada en el abstract.
- **Evaluación:** Métricas objetivas y subjetivas sobre varios estados de canal.
- **Canal/robustez:** Adaptación explícita a SNR en canal inalámbrico.
- **Código o artefactos:** Demo de audio pública.
- **Resultado principal:** Ahorro de hasta 75 % de ancho de banda frente a sistemas semánticos comparados.

## Limitaciones

Arquitectura JSCC difícil de integrar con redes digitales existentes y comparación condicionada al modelo de canal.

## Uso en el TFM

Fundamenta el eje comunicación, adaptación a SNR y rate-distortion del TFM.

## Estado de revisión

Ficha inicial basada en abstract, conclusiones y datos explícitos del artículo. Las cifras que se usen en la memoria final deberán contrastarse de nuevo con la tabla o sección experimental original.
