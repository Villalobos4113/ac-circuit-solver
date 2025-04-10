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
frequency = 1 / math.pi  # Hz
#       Frequency of the circuit (in rad/s)
omega = 2  # rad/s

if frequency is None and omega is None:
    raise ValueError("Either frequency or omega must be set.")
elif frequency is not None and omega is not None:
    omega_frequency = omega / (2 * math.pi)
    if frequency != omega_frequency:
        raise ValueError("Frequency and omega are inconsistent.")
    circuit_frequency = frequency
elif frequency is not None:
    circuit_frequency = frequency
else:
    circuit_frequency = omega / (2 * math.pi)

# 2) Define source voltage

#   Source voltage (in V)
#       If source voltage is in polar form, convert it to rectangular form
#           Example: 10∠30° = polar_to_rect(10, 30) = (8.66 + 5j)
#       Define as many sources as needed
V1 = polar_to_rect(12, 0)
V2 = polar_to_rect(6, 0)

i3 = polar_to_rect(3, 10)

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

def define_branches_impedances() -> list[complex]:
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
            'resistors': [3],
            'inductors': [1],
            'capacitors': [],
        },
        {
            'resistors': [],
            'inductors': [],
            'capacitors': [3/2],
        },
        {
            'resistors': [4],
            'inductors': [],
            'capacitors': [],
        },
        {
            'resistors': [],
            'inductors': [],
            'capacitors': [1/4],
        },
        {
            'resistors': [1],
            'inductors': [],
            'capacitors': [1/4],
        },
    ]
    
    # Calculate the total impedance of each branch
    Z_branches = _calculate_branches_impedances(branches)

    # Print the impedance of each branch
    print("\n\n" + "=" * 40 + "\nIMPEDANCE OF EACH BRANCH\n" + "=" * 40 + "\n") 
    for i, Z in enumerate(Z_branches):
        print(f"Branch {i} impedance: {impedance_to_string(Z)}")
    print("\n" + "=" * 40 + "\n\n")

    return Z_branches

def solve_circuit() -> None:
    """
    Solve the circuit using the defined branches and source voltages.
    """

    # Define branches and their impedances
    branch = define_branches_impedances()

    # Define equations based on the circuit topology, you can use the branch list to define the equations
    eq1 = (branch[0] + branch[1]) * i1 - (branch[1]) * i2 + V1 - V2
    eq2 = - (branch[1]) * i1 + (branch[1] + branch[2] + branch[3]) * i2 - (branch[3]) * i3 + V2

    # Solve the system of equations
    solution = sympy.solve((eq1, eq2), (i1, i2), dict=True)

    # 'solution' is a list of dictionaries, typically with one entry for linear systems
    sol = solution[0]

    # Extract i1, i2 solutions
    i1_sol = sol[i1]
    i2_sol = sol[i2]

    # Print symbolic and numeric forms
    print("i1 =", i1_sol, "-> numeric:", i1_sol.evalf())
    print("i2 =", i2_sol, "-> numeric:", i2_sol.evalf())

# ======================

if __name__ == "__main__":
    # Before running the circuit solver, ensure that the branches are defined and the settings completed
    solve_circuit()