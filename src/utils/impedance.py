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

def branch_impedance(resistors: list[float], inductors: list[float], capacitors: list[float], f: float) -> complex:
    """
    Calculate the total impedance of a branch with resistors, inductors, and capacitors in series.
    """
    Z_total = complex(0, 0)
    
    # Add resistors
    for R in resistors:
        Z_total += resistor_impedance(R)
    
    # Add inductors
    for L in inductors:
        Z_total += inductor_impedance(L, f)
    
    # Add capacitors
    for C in capacitors:
        Z_total += capacitor_impedance(C, f)
    
    return Z_total

def impedance_to_string(Z: complex) -> str:
    """
    Converts a complex impedance to a string representation.
    """
    real_part = Z.real
    imag_part = Z.imag

    if imag_part >= 0:
        return f"{real_part:.2f} + {imag_part:.2f}j"
    else:
        return f"{real_part:.2f} - {abs(imag_part):.2f}j"

if __name__ == "__main__":
    print(capacitor_impedance(1/48, 1/(4*math.pi)))  # (inf+0j)