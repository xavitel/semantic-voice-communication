# Bitrate Analysis: VoIP vs Semantic Voice

Typical VoIP codecs:

G.711
64 kbps

Opus
6–510 kbps (commonly 16–32 kbps)

Assume average call:
24 kbps

Semantic pipeline estimation:

Text tokens
~10–20 bytes per word

Speaker embedding
256–512 floats

Prosody embedding
~100 floats

Rough estimate per sentence:

Text
200 bytes

Speaker vector
2 KB

Prosody
400 bytes

Total
~2.6 KB per sentence

Equivalent bitrate (5 seconds speech):
~4 kbps

Potential reduction vs 24 kbps VoIP:

~6x compression

Further optimization possible with:
- quantization
- shared speaker identity
- predictive encoding
