# WG Created: 2/2/22 Modified: 2/2/22
# Sub module to contain functions for analysis the flood data

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Function to compute a least squares fit onto the water level data at different dates
    returns poly, d0 where poly is a polynomial and d0 is a shift of the date axis"""
    x = matplotlib.dates.date2num(dates)
    y = levels
    d0 = x[0]

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - d0, y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)

    return poly, d0


