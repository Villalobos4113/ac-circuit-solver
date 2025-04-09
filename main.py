# ======================
# AC Circuit Solver
# By Fernando Villalobos
# Started on 24/03/2025
# ======================

import cmath
import math
import sympy

from src.utils.impedance import branch_impedance, impedance_to_string
from src.utils.phasor import polar_to_rect, rect_to_polar

# ======================
# SETTINGS
# ======================

# 1) Define frequency

#   Set frequency of the circuit, it can be in Hz or rad/s, but not both, set one to None
#       Frequency of the circuit (in Hz)
frequency = 60  # Hz
#       Frequency of the circuit (in rad/s)
omega = 2 * math.pi * frequency  # rad/s

if frequency is None and omega is None:
    raise ValueError("Either frequency or omega must be set.")
elif frequency is not None and omega is not None:
    raise ValueError("Only one of frequency or omega should be set.")
elif frequency is not None:
    circuit_frequency = frequency
else:
    circuit_frequency = omega / (2 * math.pi)

# 2) Define source voltage

#   Source voltage (in V)
#       If source voltage is in polar form, convert it to rectangular form
#           Example: 10∠30° = polar_to_rect(10, 30) = (8.66 + 5j)
#       Define as many sources as needed
V1 = polar_to_rect(10, 30)  # V1 = 10∠30°
V2 = 9.0 + 4.0j  # V2 = 9 + 4j

# 3) Define symbols
i1, i2 = sympy.symbols('i1 i2', complex=True)

# ======================

# ======================
# AUXILIARY FUNCTIONS
# ======================

def _calculate_branches_impedances(branches: list[dict]) -> list[complex]:
    """
    Calculate the total impedance of each branch in the circuit.
    """
    Z_branches = []
    for branch in branches:
        Z = branch_impedance(
            resistors=branch.get('resistors', []),
            inductors=branch.get('inductors', []),
            capacitors=branch.get('capacitors', []),
            f=circuit_frequency
        )
        Z_branches.append(Z)
    return Z_branches

# ======================

# ======================
# MAIN FUNCTIONS
# ======================

def define_branches_impedances() -> None:
    """
    Define the branches of the circuit.
    """
    # Define branches with their components
    # R should be provided in ohms (Ω)
    # L should be provided in henries (H)
    # C should be provided in farads (F)
    # Example: branch 1 has 3 resistors (R1, R2, R3), 1 inductor (L1), and no capacitors
    
    # Add more branches as needed
    branches = [
        {
            'resistors': [3, 5],
            'inductors': [3],
            'capacitors': [],
        },
        {
            'resistors': [],
            'inductors': [],
            'capacitors': [],
        }
    ]
    
    # Calculate the total impedance of each branch
    Z_branches = _calculate_branches_impedances(branches)

    # Print the impedance of each branch
    for i, Z in enumerate(Z_branches):
        print(f"Branch {i + 1} impedance: {impedance_to_string(Z)}")