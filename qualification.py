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


def build_continuous(breakpoints,slopes, freq):
    """
    Function to take a vector of breakpoints, and one of slopes and to build continuos spec lines
    Input is based on number of breakpoints in spec
    """

    if len(breakpoints) == 2:
        conditions = [freq < breakpoints[0],
                      (freq >= breakpoints[0]) & (freq < breakpoints[1]),
                      freq >= breakpoints[1]]

        functions = [lambda freq: slopes[1] - slopes[0] * (breakpoints[0] - freq),
                     lambda freq: slopes[1],
                     lambda freq: slopes[1] + slopes[2] * (freq - breakpoints[1])]
    elif len(breakpoints) == 4:
        conditions = [freq < breakpoints[0],
                      (freq >= breakpoints[0]) & (freq < breakpoints[1]),
                      (freq >= breakpoints[1]) & (freq < breakpoints[2]),
                      (freq >= breakpoints[2]) & (freq < breakpoints[3]),
                      freq >= breakpoints[3]]

        functions = [lambda freq: slopes[1] - slopes[0] * (breakpoints[0] - freq),
                     lambda freq: slopes[1],
                     lambda freq: slopes[3] - slopes[2] * (breakpoints[2] - freq),
                     lambda freq: slopes[3],
                     lambda freq: slopes[3] + slopes[4] * (freq - breakpoints[3])]
    else:
        raise IOError
    return piecewise(freq, conditions, functions)



def get_qual(fname):
    """
    Breakpoints denoted b0,b1...slopes or flat values denoted s0,s1,s2
    """
    qual_df = get_qual_specs(fname)
    keys = ['fig1','fig2','fig3','fig4','fig5','fig6','fig7','fig8_IP','fig8_OP',
            'fig9','fig10_IP','fig10_OP','fig11','fig12','fig13']
    dict_specs = {}
    dx = 4.0  # from data collected
    # freq = list(frange(20.0, 2504.0, dx))
    # k = array([x for x in frange(20.0, 2500.6, dx)])
    freq = arange(20.0, 2504.0, dx)
    keys_iter = 0

    for iter in range(len(qual_df.columns))[0::2]:

        breakpoints, slopes = qual_df.ix[:, iter].dropna(),qual_df.ix[:, iter+1].dropna()

        # append piecewise to dict_specs
        dict_specs[keys[keys_iter]] = build_continuous(breakpoints,slopes, freq)
        keys_iter += 1



    return dict_specs

