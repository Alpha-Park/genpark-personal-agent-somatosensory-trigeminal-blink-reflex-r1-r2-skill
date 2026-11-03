"""
MCP Server for Trigemino-Facial Blink Reflex (R1/R2) Skill.
Conforms to Model Context Protocol (MCP) JSON-RPC 2.0 stdio specification.
"""

import sys
import json
from client import TrigeminalBlinkReflexClient


def handle_request(line: str) -> None:
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-personal-agent-somatosensory-trigeminal-blink-reflex-r1-r2-skill",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_blink_reflex",
                        "description": "Calculate Blink Reflex R1, R2, and R2c latencies to evaluate CN V, CN VII, and brainstem integrity.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "ipsilateral_r1_latency_ms": {"type": "number", "description": "Ipsilateral early R1 latency (ms)."},
                                "ipsilateral_r2_latency_ms": {"type": "number", "description": "Ipsilateral late R2 latency (ms)."},
                                "contralateral_r2c_latency_ms": {"type": "number", "description": "Contralateral late R2c latency (ms)."},
                                "contralateral_side_stim_r1_ms": {"type": "number", "description": "Opposite side stim R1 latency (ms, optional)."},
                                "r1_amplitude_uv": {"type": "number", "description": "R1 amplitude (uV, default: 350.0)."},
                                "r2_amplitude_uv": {"type": "number", "description": "R2 amplitude (uV, default: 450.0)."}
                            },
                            "required": [
                                "ipsilateral_r1_latency_ms",
                                "ipsilateral_r2_latency_ms",
                                "contralateral_r2c_latency_ms"
                            ]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_blink_reflex":
            client = TrigeminalBlinkReflexClient()
            try:
                res = client.evaluate_blink_reflex(
                    ipsilateral_r1_latency_ms=float(args["ipsilateral_r1_latency_ms"]),
                    ipsilateral_r2_latency_ms=float(args["ipsilateral_r2_latency_ms"]),
                    contralateral_r2c_latency_ms=float(args["contralateral_r2c_latency_ms"]),
                    contralateral_side_stim_r1_ms=float(args["contralateral_side_stim_r1_ms"]) if "contralateral_side_stim_r1_ms" in args and args["contralateral_side_stim_r1_ms"] is not None else None,
                    r1_amplitude_uv=float(args.get("r1_amplitude_uv", 350.0)),
                    r2_amplitude_uv=float(args.get("r2_amplitude_uv", 450.0))
                )
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
                    }
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32000, "message": str(e)}
                }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    else:
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


def main():
    for line in sys.stdin:
        if line.strip():
            handle_request(line)


if __name__ == "__main__":
    main()
