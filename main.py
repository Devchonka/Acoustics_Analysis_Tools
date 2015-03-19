"""
Python script to evaluate accelerometers that measured more output than expected.

Random vibration of structures is assessed in mechanical engineering using acceleration
spectral density (ASD). The root mean square acceleration (Grms) value expresses the
overall energy of a particular random vibration event. It is calculated as the square root
of the area under the ASD curve in the frequency domain.

If the accelerometer time history is a stationary Gaussian random time history,
the rms acceleration (also called the 1 sigma acceleration) would be related to the
statistical properties of the acceleration time history.

68.3% of the time, the acceleration time history would have peaks that would not exceed the +/- 1 sigma accelerations.
95.4% of the time, the acceleration time history would have peaks that would not exceed the +/- 2 sigma accelerations.
99.7% of the time, the acceleration time history would have peaks that would not exceed the +/- 3 sigma accelerations.


This ASD analysis is useful for structural design and analysis purposes.

Inputs: g^2/freq vs freq data from accelerometers.
Outputs: Grms, PSD at the peak, compared to qualified parameters, and plotted depending
on location of accel on spacecraft.

"""

from scipy.integrate import simps  # to calc Grms area under curve: numerical method to integrate area

from pandas import read_csv
import plotting
import qualification


def read_data_file(filename):
    """
    Function that reads input file and returns the data in form of a dataframe.
    :param filename: name of data input file as .txt
    :return: dataframe object of the data contained in input file
    """
    df = read_csv(filename, sep='\t', lineterminator='\n', header=[0, 1], index_col=0)
    return df


def calc_stats(df):
    # The y values.  A numpy array is used here,
    # but a python list could also be used.
    dx = df.index[1] - df.index[0]
    Grms_total, Grms_peak = get_Grms(df.ix[:, 0].tolist(), dx)

    print('Grms_total = ', Grms_total)
    print('Grms_peak = ', Grms_peak)


def get_Grms(list, dx):
    """
    Function to numerically compute area under ASD curve (Grms value) using composite Simpson's rule.
    :param list: list of values of ASD vector
    :return: Grms values of the whole curve, and of the curve up until the max peak
    """
    peak_index = list.index(max(list))
    # peak_index = list.idxmax()
    Grms_total = simps(list, dx=dx)
    Grms_peak = simps(list[0:peak_index], dx=dx)
    return Grms_total, Grms_peak


def main():
    # Read file and store data in "data" object
    fname_data = 'Acoustics_Overtest_Data.txt'
    fname_design_loads = 'design_loads.txt'
    fname_randomV_specs = 'qual_specs.txt'
    data_df = read_data_file(fname_data)  # create data object that will keep all variables from file, raw and processed
    spec_df = qualification.get_qual(fname_randomV_specs)


    # get dictionary of design loads of {figure# : design_load}
    dict_loads = qualification.get_design_loads(fname_design_loads)

    calc_stats(data_df)
    plotting.make_plots(data_df, spec_df)

if __name__ == '__main__':
    main()