"""
Code for the quantum tunneling effect, from the game made in 2022.
"""

import argparse
import os
import numpy as np
import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Running tunneling effect.")

    parser.add_argument("--api_key", type=str, help="API Key for IBM Quantum Computers.", default=None)

    args = parser.parse_args()

    if args.api_key is None:
        raise ValueError("API Key is missing. Login into your IBM Qiskit account if you still don't have one.")