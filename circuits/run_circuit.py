from qiskit import Aer, execute

def simulate(
        circuit,
        used_backend: str = 'qasm_simulator',
        shots: int = 100,
    ):
    """
    Run a circuit in the given backend and count the results.

    Args:
        circuit: A quantum circuit to be run.
        used_backend: String with the backend to be used. If we want to run on a quantum computer, we just need
            to change this into the appropriate backend, and not a simulation one (default: 'qasm_simulator').
        shots: Integer of the number of tests will be done.
    
    Returns:
        counts: Dictionary with the number of measurements for each possible result.
    """
    backend = Aer.get_backend(used_backend)  # Possible backends: Terra, Aer, Ignis and Aqua. We choose Aer by default.
    results = execute(circuit, backend=backend, shots=shots).result()
    counts = results.get_counts()
    return counts