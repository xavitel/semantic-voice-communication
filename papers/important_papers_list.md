# Important Papers to Review

> This historical shortlist is kept for context. The maintained corpus is now in [`literature_catalog.json`](literature_catalog.json), with an annotated Spanish index in [`paper_index.md`](paper_index.md) and a comparison matrix in [`paper_matrix.csv`](paper_matrix.csv).

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


11. **"DualCodec: High-Quality Speech Tokenizer with Semantic-Acoustic Decoupling"** (May 2025)
   * **Authors:** Gyeongman Kim, Myeonghun Lee, et al.
   * **Link:** [arXiv:2505.13000](https://arxiv.org/abs/2505.13000) | [PDF](https://arxiv.org/pdf/2505.13000)
   * **Note:** Proposes dual-frame-rate semantic + waveform token streams to improve language-modeling quality while preserving synthesis fidelity.

12. **"XY-Tokenizer: Addressing the Semantic-Acoustic Conflict in Speech Tokenizers"** (June 2025)
   * **Authors:** Yizhi Li, Yidong Wang, et al.
   * **Link:** [arXiv:2506.23325](https://arxiv.org/abs/2506.23325) | [PDF](https://arxiv.org/pdf/2506.23325)
   * **Note:** Introduces explicit disentanglement of semantic and acoustic information to reduce the quality/intelligibility trade-off.

13. **"TaDiCodec: Text-Aware Diffusion-Guided Neural Audio Codec at Ultra-Low Bitrate"** (Aug 2025)
   * **Authors:** Yiteng Huang, Xiang Li, et al.
   * **Link:** [arXiv:2508.16790](https://arxiv.org/abs/2508.16790) | [PDF](https://arxiv.org/pdf/2508.16790)
   * **Note:** Uses diffusion-based tokenization with text guidance for ultra-low bitrate speech coding and improved intelligibility.

14. **"Glaris: Error-Resilient Speech Semantic Communication under Packet Loss"** (Dec 2025)
   * **Authors:** Sijie Wang, Xiaowei Wang, et al.
   * **Link:** [arXiv:2512.08203](https://arxiv.org/abs/2512.08203) | [PDF](https://arxiv.org/pdf/2512.08203)
   * **Note:** Focuses on resilient semantic speech communication under lossy channels, directly relevant for real network conditions.

15. **"LargeSC: Large Foundation Models for Semantic Communication in Speech Transmission"** (Dec 2025)
   * **Authors:** Yuchen Chen, Xiaoyuan Wang, et al.
   * **Link:** [arXiv:2512.04711](https://arxiv.org/abs/2512.04711) | [PDF](https://arxiv.org/pdf/2512.04711)
   * **Note:** Introduces adaptive bitrate control, UEP, and packet-loss recovery with foundation-model-based components.

## Core / Foundational Neural Codecs
16. **"Moshi: a speech-text foundation model for real-time dialogue"** (Kyutai, 2024) [Link](https://arxiv.org/pdf/2410.00037)
17. **"LDCodec: A high quality neural audio codec with low-complexity decoder"** (2025) [Link](https://arxiv.org/pdf/2510.15364)
18. **"SNAC: Multi-Scale Neural Audio Codec"** (2024) [Link](https://arxiv.org/pdf/2410.14411)
19. **"SoundStream: An End-to-End Neural Audio Codec"** (Google, 2021) [Link](https://arxiv.org/pdf/2107.03312)
20. **"EnCodec: High Fidelity Neural Audio Compression"** (Meta, 2022)

## Voice Generation & Intermediate Representations
21. **"VALL-E: Neural Codec Language Models"** (Microsoft)
22. **"YourTTS"**
23. **"StyleTTS2"**

## Speech Representation Learning
24. **"wav2vec 2.0"**
25. **"HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units"**

## Emotion and Prosody
26. **"Speech Emotion Recognition Using Deep Learning"**
27. **"Prosody Modeling for Neural TTS"**
