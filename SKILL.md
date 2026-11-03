---
name: genpark-personal-agent-somatosensory-trigeminal-blink-reflex-r1-r2-skill
description: Trigemino-Facial Blink Reflex (BR) latency and amplitude analyzer. Evaluates early ipsilateral pontine reflex loop (R1) and late bilateral medullary reflex loops (R2 and R2c) to assess cranial nerves V and VII.
version: 1.0.0
author: GenPark Ecosystem
license: Apache-2.0
tags:
  - personal-agent
  - neurophysiology
  - blink-reflex
  - brainstem
  - trigeminal
  - facial-nerve
  - openclaw
  - genpark
  - mcp
---

# Somatosensory Trigeminal Blink Reflex (R1/R2) Skill

## Overview
This skill computes electrophysiological latencies and anatomical localization for the blink reflex:
- **Early Oligosynaptic Response ($R_1$)**: Traverses the ipsilateral sensory trigeminal root, main sensory nucleus in the mid-pons, and ipsilateral facial nucleus/nerve ($R_1 \le 13.0\text{ ms}$).
- **Late Polysynaptic Responses ($R_2$ and $R_{2c}$)**: Descend through the spinal trigeminal tract in the lateral medulla, synapse with medullary interneurons, and project bilaterally to both facial nuclei ($R_2 \le 41.0\text{ ms}$, $R_{2c} \le 43.0\text{ ms}$).
- **Topographical Lesion Localization**: Disentangles afferent $V_1$ root lesions, efferent $VII$ motor palsies (e.g., Bell's palsy), and lateral medullary (Wallenberg) ischemia.

## Mathematical Formulation
1. **Bilateral R2 Latency Difference**:
   $$\Delta R_2 = |R_{2\text{ (ipsi)}} - R_{2c\text{ (contra)}}|$$
2. **R1 Side-to-Side Asymmetry**:
   $$\Delta R_1 = |R_{1\text{ (right)}} - R_{1\text{ (left)}}|$$

## Usage
```python
from client import TrigeminalBlinkReflexClient

client = TrigeminalBlinkReflexClient()
res = client.evaluate_blink_reflex(
    ipsilateral_r1_latency_ms=10.8,
    ipsilateral_r2_latency_ms=31.5,
    contralateral_r2c_latency_ms=32.8
)
print(res["evaluation"]["lesion_localization"])
```
