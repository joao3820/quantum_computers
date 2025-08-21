import argparse
import numpy as np
import random as rd

from circuits.circuit_layout import CircuitLayout
from circuits.run_circuit import simulate
from qiskit import IBMQ

def tunneling_circuit(
        velocity: float,
        used_backend: str = 'qasm_simulator'
    ):
    """
    Generates a circuit for a 1D particle tthrough a barrier.
    
    Args:
        velocity: Float of the particle's velocity, where velocity=1 is the maximum.
        used_backend: String with the backend to be used. If we want to run on a quantum computer, we just need
            to change this into the appropriate backend, and not a simulation one (default: 'qasm_simulator').
    
    Returns:
        counts: Dictionary with the number of measurements for each possible result, in this case,
            it returns if the particle passes through the barrier.
    """
    circuit = CircuitLayout(1, 1)

    angle = velocity**2 * (np.pi / 2)  # this angle is related to the gate U
    circuit.qc.u(2*angle, 0, 0, 0)

    circuit.qc.measure_all()

    counts = simulate(circuit, used_backend=used_backend, shots=1)
    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Running tunneling effect on a Quantum Computer.")

    parser.add_argument("--api_key", type=str, help="API Key for IBM Quantum Computers.", default=None)

    args = parser.parse_args()

    if args.api_key is None:
        raise ValueError("API Key is missing. Login into your IBM Qiskit account if you still don't have one.")
    
    IBMQ.save_account(str(args.api_key))
    provider = IBMQ.load_account()  # load account from disk

    v = rd.random()  # choose a random velocity
    counts = tunneling_circuit(velocity=v, used_backend='ibmq_belem')
    print(counts)
    