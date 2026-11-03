"""
Example usage of Trigemino-Facial Blink Reflex (R1/R2) Skill.
Demonstrates normal brainstem reflex loops vs facial nerve lesion vs trigeminal sensory delay.
"""

import json
from client import TrigeminalBlinkReflexClient


def main():
    print("=== Testing Trigemino-Facial Blink Reflex (R1/R2) Skill ===")
    client = TrigeminalBlinkReflexClient()

    # 1. Normal healthy reflex (R1 = 10.8 ms, R2 = 31.5 ms, R2c = 32.8 ms)
    res_normal = client.evaluate_blink_reflex(
        ipsilateral_r1_latency_ms=10.8,
        ipsilateral_r2_latency_ms=31.5,
        contralateral_r2c_latency_ms=32.8,
        contralateral_side_stim_r1_ms=10.5
    )
    print("\n[Case 1: Normal Intact Blink Reflex Circuitry]")
    print(json.dumps(res_normal, indent=2))

    # 2. Efferent facial nerve lesion (Bell's palsy: R1 and ipsilateral R2 prolonged, but crossed R2c normal)
    res_efferent = client.evaluate_blink_reflex(
        ipsilateral_r1_latency_ms=16.5,
        ipsilateral_r2_latency_ms=48.0,
        contralateral_r2c_latency_ms=33.0
    )
    print("\n[Case 2: Efferent Facial Nerve (CN VII) Conduction Block]")
    print(json.dumps(res_efferent, indent=2))

    # Assertions
    assert res_normal["evaluation"]["clinical_status"] == "Preserved Brainstem Circuit"
    assert res_efferent["evaluation"]["clinical_status"] == "Efferent CN VII Conduction Block"
    assert res_normal["r2_bilateral_latency_diff_ms"] < 5.0
    print("\n[SUCCESS] Blink Reflex tests passed!")


if __name__ == "__main__":
    main()
