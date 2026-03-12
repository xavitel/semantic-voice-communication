# Semantic Voice Transmission Architecture

Pipeline proposal:

1. Audio Capture
Raw microphone signal.

2. Speech Recognition (STT)
Possible models:
- Whisper / WhisperX
- wav2vec2

Outputs text + timestamps.

3. Semantic Encoder
Transforms text into semantic representation.
Options:
- sentence-transformers
- LLM embedding models

4. Speaker Encoder
Extracts identity embedding.
Possible models:
- ECAPA-TDNN
- Resemblyzer
- x-vectors

5. Prosody / Emotion Encoder
Captures expressive features:
- pitch
- energy
- rhythm
- emotional tone

Candidate models:
- Speech Emotion Recognition networks
- Prosody encoders used in StyleTTS2

6. Transmission Layer
Send only:
- semantic representation
- speaker embedding
- prosody embedding

7. Reconstruction
Generative TTS conditioned on previous signals.

Candidate models:
- VALL-E
- XTTS
- StyleTTS2
- Bark

8. Output synthesis
Generate audio waveform.
