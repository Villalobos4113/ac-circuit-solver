import cmath
import math

def resistor_impedance(R: float) -> complex:
    """
    Returns the impedance of a resistor, which is just R (real).
    """
    return complex(R, 0)

def inductor_impedance(L: float, f: float) -> complex:
    """
    Z_L = j * 2πfL
    """
    omega = 2 * math.pi * f
    return complex(0, omega * L)

def capacitor_impedance(C: float, f: float) -> complex:
    """
    Z_C = 1 / (j * 2πfC) = -j / (2πfC)
    """
    omega = 2 * math.pi * f
    # handle zero-division if C=0
    if C == 0:
        return complex(float('inf'), 0)  # "Infinite" impedance for no capacitor
    return 1 / complex(0, omega * C)