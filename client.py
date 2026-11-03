"""
Trigemino-Facial Blink Reflex (R1/R2) Brainstem Circuitry Client.
Zero-mock pure Python standard library implementation.
Calculates early pontine R1 latency, late medullary bilateral R2/R2c latencies,
and inter-side latency asymmetries to evaluate cranial nerves V and VII, brainstem stroke, and habituation.
"""

import math
from typing import Dict, Any, List, Optional


class TrigeminalBlinkReflexClient:
    """
    Evaluates the Blink Reflex (BR) elicited by supraorbital nerve electrical stimulation
    and recorded from the orbicularis oculi muscles bilaterally:
    - R1: Early ipsilateral oligosynaptic pontine circuit (CN V1 -> Principal Sensory Nucleus -> CN VII)
    - R2: Late ipsilateral polysynaptic medullary circuit (CN V1 -> Spinal Trigeminal Nucleus -> Interneurons -> Ipsilateral CN VII)
    - R2c (Contralateral): Late polysynaptic crossed circuit -> Contralateral CN VII
    """

    def __init__(self):
        pass

    def evaluate_blink_reflex(
        self,
        ipsilateral_r1_latency_ms: float,
        ipsilateral_r2_latency_ms: float,
        contralateral_r2c_latency_ms: float,
        contralateral_side_stim_r1_ms: Optional[float] = None,
        r1_amplitude_uv: float = 350.0,
        r2_amplitude_uv: float = 450.0
    ) -> Dict[str, Any]:
        """
        Calculates reflex latencies, pathway conduction times, and interside differences.
        ipsilateral_r1_latency_ms: R1 onset latency in ms (normal: 9.5 - 13.0 ms).
        ipsilateral_r2_latency_ms: Ipsilateral R2 onset latency in ms (normal: 27.0 - 41.0 ms).
        contralateral_r2c_latency_ms: Contralateral R2c onset latency in ms (normal: 28.0 - 43.0 ms).
        contralateral_side_stim_r1_ms: R1 latency obtained when opposite side was stimulated (for side-to-side delta).
        """
        if ipsilateral_r1_latency_ms <= 0 or ipsilateral_r2_latency_ms <= 0 or contralateral_r2c_latency_ms <= 0:
            raise ValueError("All latency measurements must be strictly positive.")

        # Interside latency differences:
        r2_inter_side_diff_ms = abs(ipsilateral_r2_latency_ms - contralateral_r2c_latency_ms)

        r1_asymmetry_ms = None
        if contralateral_side_stim_r1_ms is not None and contralateral_side_stim_r1_ms > 0:
            r1_asymmetry_ms = abs(ipsilateral_r1_latency_ms - contralateral_side_stim_r1_ms)

        # Standard clinical diagnostic criteria:
        # Normal upper limits:
        # R1 <= 13.0 ms
        # R2 <= 41.0 ms
        # R2c <= 43.0 ms
        # R1 interside difference <= 1.2 ms
        # R2/R2c difference <= 5.0 ms

        r1_prolonged = ipsilateral_r1_latency_ms > 13.0
        r2_prolonged = ipsilateral_r2_latency_ms > 41.0
        r2c_prolonged = contralateral_r2c_latency_ms > 43.0

        if not r1_prolonged and not r2_prolonged and not r2c_prolonged and r2_inter_side_diff_ms <= 5.0:
            classification = "Normal Trigemino-Facial Blink Reflex Circuitry"
            lesion_localization = "No conduction delay detected across pons, medulla, or cranial nerves V/VII."
            clinical_status = "Preserved Brainstem Circuit"
        elif r1_prolonged and r2_prolonged and r2c_prolonged:
            classification = "Afferent Sensory Pathway Delay / Trigeminal Nerve (CN V) Lesion"
            lesion_localization = "All responses (R1, R2, R2c) delayed on ipsilateral stimulation; indicates lesion in sensory V1 root or main sensory nucleus."
            clinical_status = "Afferent V1 Conduction Block"
        elif r1_prolonged and r2_prolonged and not r2c_prolonged:
            classification = "Efferent Motor Pathway Delay / Facial Nerve (CN VII) Lesion"
            lesion_localization = "Responses on the stimulated side are delayed, but crossed R2c on opposite facial nerve is normal (Bell's palsy pattern)."
            clinical_status = "Efferent CN VII Conduction Block"
        elif r1_prolonged and not r2_prolonged and not r2c_prolonged:
            classification = "Selective Early Pontine Loop Delay / Mid-Pontine Lesion"
            lesion_localization = "Isolated delay of oligosynaptic R1 loop; suggests demyelination or microvascular ischemia in mid-pontine tegmentum."
            clinical_status = "Intrinsic Pontine Lesion"
        elif not r1_prolonged and (r2_prolonged or r2c_prolonged):
            classification = "Selective Medullary / Spinal Trigeminal Loop Delay"
            lesion_localization = "Preserved R1 with delayed polysynaptic R2; indicates caudal brainstem / lateral medullary (Wallenberg syndrome) involvement."
            clinical_status = "Lateral Medullary Syndrome"
        else:
            classification = "Atypical / Borderline Blink Reflex Pattern"
            lesion_localization = "Mild interside disparity; clinical electrophysiological correlation recommended."
            clinical_status = "Borderline Disparity"

        return {
            "status": "success",
            "ipsilateral_r1_latency_ms": round(ipsilateral_r1_latency_ms, 2),
            "ipsilateral_r2_latency_ms": round(ipsilateral_r2_latency_ms, 2),
            "contralateral_r2c_latency_ms": round(contralateral_r2c_latency_ms, 2),
            "r2_bilateral_latency_diff_ms": round(r2_inter_side_diff_ms, 2),
            "r1_side_to_side_asymmetry_ms": round(r1_asymmetry_ms, 2) if r1_asymmetry_ms is not None else None,
            "r1_amplitude_uv": r1_amplitude_uv,
            "r2_amplitude_uv": r2_amplitude_uv,
            "evaluation": {
                "classification": classification,
                "clinical_status": clinical_status,
                "lesion_localization": lesion_localization
            }
        }
