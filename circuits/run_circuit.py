from matplotlib import pyplot as plt
import numpy as np
from qiskit import Aer, execute


def simulate(
        self,
        circuit,
        used_backend: str = 'qasm_simulator'
):
    """
    Run a circuit in the given backend and count the results.

    Args:
        circuit: A quantum circuit to be run.
        used_backend: String with the backend to be used. If we want to run on a quantum computer, we just need
            to change this into the appropriate backend, and not a simulation one (default: 'qasm_simulator').
    
    Returns:
        counts: Dictionary with the number of measurements for each possible result.
    """
    self.backend = Aer.get_backend(used_backend)  # Possible backends: Terra, Aer, Ignis and Aqua. We choose Aer by default.
    results = execute(circuit, backend=self.backend, shots=100).result()
    counts = results.get_counts()
    return counts