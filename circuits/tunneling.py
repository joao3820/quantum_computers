import numpy as np
from typing import Dict
from circuits.circuit_layout import CircuitLayout
from circuits.run_circuit import simulate

def tunneling_circuit(
        velocity: float,
        api_key,
        barrier_strength: float = 1.0,
        used_backend: str = 'aer_simulator',
        shots: int = 100
    ) -> Dict[str, int]:
    """
    Generates a circuit for a 1D particle through a barrier.
    
    Args:
        velocity: Float of the particle's velocity, where velocity=1 is the maximum.
        barrier_strength: Float representing barrier thickness/strength.
        used_backend: String with the backend to be used.
        shots: Number of shots for measurement statistics.

    Returns:
        counts: Dictionary with the number of measurements for each result.
    """
    circuit = CircuitLayout(1, 1)

    # Probability of tunneling decreases exponentially with barrier strength
    angle = velocity**2 * np.exp(-barrier_strength) * (np.pi / 2)
    circuit.qc.u(2*angle, 0, 0, 0)

    circuit.qc.measure_all()

    counts = simulate(circuit, api_key=api_key, used_backend=used_backend, shots=shots)
    return counts