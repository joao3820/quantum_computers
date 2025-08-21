from circuits.circuit_layout import CircuitLayout

"""
Example of a register (system of multiple qubits) an half-adder created with the methods we defined.
"""

half_adder = CircuitLayout(4, 2)

half_adder.add_not_gate([0, 1])  # let's make both q0=1 and q1=1

half_adder.qc.barrier()  # can be used in qiskit to make circuits easier to read

half_adder.add_cnot_gate(2, 0)
half_adder.add_cnot_gate(2, 1)
half_adder.add_cnot_gate(3, 0, 1)

# extract outputs
half_adder.qc.measure(2,0) # extract XOR value
half_adder.qc.measure(3,1) # extract AND value