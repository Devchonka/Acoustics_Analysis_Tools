"""
This module gives back a dataframe that contains qualification lists for in place and out of plane random vibe data.
"""

from numpy import piecewise, array, arange
import matplotlib.pyplot as plt


def get_qual_helper(item):
    # switch case for item
    breakpoints = [50, 600]
    slopes = [6.0, 0.08, -4.5]
    return breakpoints, slopes

def get_qual():
    """
    Breakpoints denoted b0,b1,b2,...slopes denoted s0,s1,s2
    :return:
    """
    item = 'equip'
    breakpoints, slopes = get_qual_helper(item)
    dx = 4.0  # from data collected
    # freq = list(frange(20.0, 2504.0, dx))
    # k = array([x for x in frange(20.0, 2500.6, dx)])
    freq = arange(20.0, 2504.0, dx)
    conditions = [freq < breakpoints[0],
                  (freq >= breakpoints[0]) & (freq < breakpoints[1]),
                  freq >= breakpoints[1]]

    functions = [lambda freq: slopes[1] - slopes[0] * (breakpoints[0] - freq),
                 lambda freq: slopes[1],
                 lambda freq: slopes[1] + slopes[2] * (freq - breakpoints[1])]

    BLAH = piecewise(freq, conditions, functions)
    print (BLAH)

    plt.plot(freq, BLAH)
    plt.show()
