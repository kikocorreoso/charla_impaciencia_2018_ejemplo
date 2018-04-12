"""Library to perform the calculations for my thesis

Author: Kiko Correoso
License: MIT
"""

def suma(*args):
    """Sum indefinite number of integers and/or floats.
    
    Parameters
    ----------
    args : ints and/or floats
        An indeterminate number of ints and/or floats.
    
    Returns
    -------
    value : int, float
        Returns the result of the operation    
    """
    value = 0
    for a in args:
        value += a
    return value