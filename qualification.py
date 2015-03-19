"""
This module gives back a dataframe that contains qualification lists for in place and out of plane random vibe data.
"""

from numpy import piecewise, array, arange
import matplotlib.pyplot as plt
from pandas import read_csv

def get_design_loads(fname):  # passes back a dict
    with open('design_loads.txt', 'r') as text_file:
        dict_loads = {}
        for line in text_file:
            key, entry = line.strip().split('\t')
            dict_loads[key] = float(entry)
    return dict_loads

def get_qual_specs(fname):
    df = read_csv(fname, sep='\t', lineterminator='\n', header=0)
    return df

# def get_qual_helper(item):
#     """
#     Function reads qual txt file and pulls out a pandas df of specs with fig# as index
#     """
#
#
#     # switch case for item
#     breakpoints = [50, 600]
#     slopes = [6.0, 0.08, -4.5]
#     return breakpoints, slopes

def get_qual(fname):
    """
    Breakpoints denoted b0,b1...slopes or flat values denoted s0,s1,s2
    """
    qual_df = get_qual_specs(fname)
    breakpoints,slopes = qual_df['fig1_b'], qual_df['fig1_s']

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

    return piecewise(freq, conditions, functions)

