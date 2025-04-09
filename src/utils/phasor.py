import cmath
import math

def rect_to_polar(value: complex, deg: bool = True) -> tuple[float, float]:
    """
    Converts a complex number (rectangular form) to magnitude and angle.
    
    Parameters:
    -----------
    value : complex
        The rectangular form of the phasor (e.g., 10 + 5j).
    deg : bool
        If True, returns the angle in degrees; if False, returns the angle in radians.

    Returns:
    --------
    (magnitude, angle) : (float, float)
        The phasor magnitude and angle in degrees (default) or radians.
    """
    magnitude = abs(value)
    angle_rad = cmath.phase(value)
    if deg:
        angle = math.degrees(angle_rad)
    else:
        angle = angle_rad
    return (magnitude, angle)


def polar_to_rect(magnitude: float, angle: float, deg: bool = True) -> complex:
    """
    Converts magnitude and angle to a complex number in rectangular form.
    
    Parameters:
    -----------
    magnitude : float
        The phasor magnitude (e.g., 10.0).
    angle : float
        The phasor angle in degrees or radians (controlled by `deg`).
    deg : bool
        If True, `angle` is assumed to be in degrees; if False, in radians.

    Returns:
    --------
    complex
        The equivalent rectangular form (e.g., 10 + 5j).
    """
    if deg:
        angle_rad = math.radians(angle)
    else:
        angle_rad = angle

    real_part = magnitude * math.cos(angle_rad)
    imag_part = magnitude * math.sin(angle_rad)

    return complex(real_part, imag_part)

if __name__ == "__main__":

    rect = polar_to_rect(3, 10)
    print(rect)  # (10+5j)