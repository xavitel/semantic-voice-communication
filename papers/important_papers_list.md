# Important Papers to Review

## Semantic Communications
1. **"Deep Learning Enabled Semantic Communication Systems"**
2. **"Semantic Communications: A Survey"**
3. **"Task-Oriented Semantic Communications"**

## End-to-End Neural Audio Codecs & Generative Audio (State of the Art: 2025-2026)

4. **"StreamVoiceAnon+: Emotion-Preserving Streaming Speaker Anonymization via Frame-Level Acoustic Distillation"** (March 2026)
   * **Authors:** Nikita Kuzmin, Kong Aik Lee, Eng Siong Chng
   * **Link:** [arXiv:2603.06079](https://arxiv.org/abs/2603.06079) | [PDF](https://arxiv.org/pdf/2603.06079)
   * **Note:** Addresses the problem of preserving emotion when using neural audio codec language models in streaming scenarios (latency ~180ms). Highly relevant for maintaining emotion without explicitly extracting it via side-channels.

5. **"Reconstruct! Don't Encode: Self-Supervised Representation Reconstruction Loss for High-Intelligibility and Low-Latency Streaming Neural Audio Codec"** (March 2026)
   * **Authors:** Junhyeok Lee, Xiluo He, et al.
   * **Link:** [arXiv:2603.05887](https://arxiv.org/abs/2603.05887) | [PDF](https://arxiv.org/pdf/2603.05887)
   * **Note:** Introduces a zero-lookahead streaming Transformer codec ("JHCodec") aimed at maintaining high intelligibility at minimal latency for real-time deployment.

6. **"CodecFlow: Efficient Bandwidth Extension via Conditional Flow Matching in Neural Codec Latent Space"** (March 2026)
   * **Authors:** Bowen Zhang, et al.
   * **Link:** [arXiv:2603.02022](https://arxiv.org/abs/2603.02022) | [PDF](https://arxiv.org/pdf/2603.02022)
   * **Note:** Focuses on reconstructing low-bandwidth speech directly in the compact latent space of a neural codec, avoiding costly spectrogram or waveform modeling.

7. **"Hierarchical Decoding for Discrete Speech Synthesis with Multi-Resolution Spoof Detection"** (March 2026)
   * **Authors:** Junchuan Zhao, Minh Duc Vu, Ye Wang
   * **Link:** [arXiv:2603.05373](https://arxiv.org/abs/2603.05373) | [PDF](https://arxiv.org/pdf/2603.05373)
   * **Note:** Improves zero-shot discrete speech synthesis through neural codec language models, ensuring robust decoding free from common token-level artifacts.

8. **"A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation"** (Jan 2026)
   * **Authors:** Hanchen Pei, et al.
   * **Link:** [arXiv:2601.12480](https://arxiv.org/abs/2601.12480) | [PDF](https://arxiv.org/pdf/2601.12480)
   * **Note:** Describes "SpeechEdit", a codec language model that selectively isolates and controls attributes like timbre and prosody while imitating zero-shot acoustic profiles.

9. **"VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing"** (Nov 2025)
   * **Authors:** Zhisheng Zheng, et al.
   * **Link:** [arXiv:2511.12347](https://arxiv.org/abs/2511.12347) | [PDF](https://arxiv.org/pdf/2511.12347)
   * **Note:** Autoregressive neural codec language model for zero-shot text-to-speech, acting as a highly advanced generative decoder.

10. **"SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound"** (2024 / 2025 updates)
   * **Authors:** Haohe Liu, et al.
   * **Link:** [arXiv:2405.00233](https://arxiv.org/abs/2405.00233) | [PDF](https://arxiv.org/pdf/2405.00233)
   * **Note:** A dual-encoder architecture that compresses audio down to 0.31 kbps - 1.40 kbps by combining a semantic encoder (AudioMAE) and an acoustic encoder, decoded via diffusion. Ultra-low bitrate benchmark.

## Core / Foundational Neural Codecs
11. **"Moshi: a speech-text foundation model for real-time dialogue"** (Kyutai, 2024) [Link](https://arxiv.org/pdf/2410.00037)
12. **"LDCodec: A high quality neural audio codec with low-complexity decoder"** (2025) [Link](https://arxiv.org/pdf/2510.15364)
13. **"SNAC: Multi-Scale Neural Audio Codec"** (2024) [Link](https://arxiv.org/pdf/2410.14411)
14. **"SoundStream: An End-to-End Neural Audio Codec"** (Google, 2021) [Link](https://arxiv.org/pdf/2107.03312)
15. **"EnCodec: High Fidelity Neural Audio Compression"** (Meta, 2022)

## Voice Generation & Intermediate Representations
16. **"VALL-E: Neural Codec Language Models"** (Microsoft)
17. **"YourTTS"**
18. **"StyleTTS2"**

## Speech Representation Learning
19. **"wav2vec 2.0"**
20. **"HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units"**

## Emotion and Prosody
21. **"Speech Emotion Recognition Using Deep Learning"**
22. **"Prosody Modeling for Neural TTS"**
