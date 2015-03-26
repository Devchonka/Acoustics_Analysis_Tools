"""
This module gives back a dataframe that contains qualification lists for in place and out of plane random vibe data.
"""

from numpy import piecewise, array, arange
import matplotlib.pyplot as plt
from pandas import read_csv
from math import log10


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


def build_continuous(breakpoints, slopes, freq):
    """
    Function to take a vector of breakpoints, and one of slopes and to build continuos spec lines
    Input is based on number of breakpoints in spec
    """
    freq_last = 2000
    if len(breakpoints) == 2:

        # get slope in g2/ Hz
        value = log10(breakpoints[0] / freq[0]) / log10(2)
        y_point_first = slopes[1] / (10 ** (slopes[0] * value / 10))

        value = log10(freq_last / breakpoints[1]) / log10(2)
        y_point_last = slopes[1] * (10 ** (slopes[2] * value / 10))

        k_up = log10(slopes[1] / y_point_first) / log10(breakpoints[0] / freq[0])
        a_up = slopes[1] / (breakpoints[0] ** k_up)

        k_down = log10(y_point_last / slopes[1]) / log10(freq_last / breakpoints[1])
        a_down = y_point_last / (freq_last ** k_down)

        conditions = [freq < breakpoints[0],
                      (freq >= breakpoints[0]) & (freq < breakpoints[1]),
                      freq >= breakpoints[1]]

        functions = [lambda freq: a_up * freq ** k_up,
                     lambda freq: slopes[1],
                     lambda freq: a_down * freq ** k_down]
    elif len(breakpoints) == 4:
        # get slope in g2/ Hz
        value = log10(breakpoints[0] / freq[0]) / log10(2)
        y_point_first1 = slopes[1] / (10 ** (slopes[0] * value / 10))

        value = log10(breakpoints[2] / breakpoints[1]) / log10(2)
        y_point_first2 = slopes[3] / (10 ** (slopes[2] * value / 10))

        value = log10(freq_last / breakpoints[3]) / log10(2)
        y_point_last = slopes[3] * (10 ** (slopes[4] * value / 10))

        k_up1 = log10(slopes[1] / y_point_first1) / log10(breakpoints[0] / freq[0])
        a_up1 = slopes[1] / (breakpoints[0] ** k_up1)

        k_up2 = log10(slopes[3] / y_point_first2) / log10(breakpoints[2] / breakpoints[1])
        a_up2 = slopes[3] / (breakpoints[2] ** k_up2)

        k_down = log10(y_point_last / slopes[3]) / log10(freq_last / breakpoints[3])
        a_down = y_point_last / (freq_last ** k_down)

        conditions = [freq < breakpoints[0],
                      (freq >= breakpoints[0]) & (freq < breakpoints[1]),
                      (freq >= breakpoints[1]) & (freq < breakpoints[2]),
                      (freq >= breakpoints[2]) & (freq < breakpoints[3]),
                      freq >= breakpoints[3]]

        functions = [lambda freq: a_up1 * freq ** k_up1,
                     lambda freq: slopes[1],
                     lambda freq: a_up2 * freq ** k_up2,
                     lambda freq: slopes[3],
                     lambda freq: a_down * freq ** k_down]
    else:
        raise IOError
    return piecewise(freq, conditions, functions)


def get_qual(fname):
    """
    Breakpoints denoted b0,b1...slopes or flat values denoted s0,s1,s2
    """
    qual_df = get_qual_specs(fname)
    keys = ['fig1', 'fig2', 'fig3', 'fig4', 'fig5', 'fig6', 'fig7_IP', 'fig7_OP',
            'fig8', 'fig9_IP', 'fig9_OP', 'fig10', 'fig11_IP', 'fig11_OP', 'fig12_IP', 'fig12_OP']
    dict_specs = {}
    dx = 4.0  # from data collected
    freq = arange(20.0, 2504.0, dx)
    keys_iter = 0

    for iter in range(len(qual_df.columns))[0::2]:
        breakpoints, slopes = qual_df.ix[:, iter].dropna(), qual_df.ix[:, iter + 1].dropna()

        # append piecewise to dict_specs
        dict_specs[keys[keys_iter]] = build_continuous(breakpoints, slopes, freq)
        keys_iter += 1

    return dict_specs

