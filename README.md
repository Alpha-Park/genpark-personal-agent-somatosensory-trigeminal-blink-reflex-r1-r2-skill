# Somatosensory Trigeminal Blink Reflex (R1/R2) Skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/ecosystem-OpenClaw-orange.svg)](https://openclaw.org/)
[![GenPark](https://img.shields.io/badge/sovereign-GenPark-purple.svg)](https://alphapark.ai/)
[![MCP](https://img.shields.io/badge/protocol-MCP-success.svg)](https://modelcontextprotocol.io/)

Trigemino-Facial Blink Reflex ($R_1$, $R_2$, $R_{2c}$) Electrophysiological Analyzer for brainstem circuitry and cranial nerve integrity.

```mermaid
flowchart TD
    A[Supraorbital Electrical Stimulation CN V1] --> B[Pontine Oligosynaptic Loop: Early R1 <= 13ms]
    A --> C[Medullary Spinal Trigeminal Loop]
    C --> D[Ipsilateral Late R2 <= 41ms]
    C --> E[Crossed Contralateral Late R2c <= 43ms]
    B & D & E --> F[Topographical Lesion Mapping: V vs VII vs Brainstem]
```

## Features
- **Zero PIP Dependencies**: Implemented strictly with Python Standard Library (`math`, `json`, `sys`, `typing`).
- **Anatomical Differential**: Disentangles afferent sensory, efferent motor, and central brainstem delays.
- **Bilateral Crossed Pathway Tracking**: Compares ipsilateral and contralateral reflex arcs.
- **Dual Architecture**: Native Python import and Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.

## Quickstart
```bash
python example_usage.py
```

## License
Apache-2.0
