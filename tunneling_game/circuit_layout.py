from matplotlib import pyplot as plt
import numpy as np

from qiskit import IBMQ, QuantumCircuit, Aer, QuantumRegister, ClassicalRegister, execute
from qiskit.quantum_info import Statevector

class CircuitLayout:
    def __init__(
            self,
            number_of_bits: int,
            number_of_bits_to_measure: int,
    ):
        if number_of_bits_to_measure > number_of_bits:
            raise 
        self.qc = QuantumCircuit(number_of_bits, number_of_bits_to_measure)