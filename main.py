"""
Python script to evaluate accelerometers that measured more output than expected.

Random vibration of structures is assessed in mechanical engineering using acceleration
spectral density (ASD). The root mean square acceleration (Grms) value expresses the
overall energy of a particular random vibration event. It is calculated as the square root
of the area under the ASD curve in the frequency domain.

This ASD analysis is useful for structural design and analysis purposes.

Inputs: g^2/freq vs freq data from accelerometers.
Outputs: Grms, PSD at the peak, compared to qualified parameters, and plotted depending
on location of accel on spacecraft.

"""

from scipy.integrate import simps # to calc Grms area under curve: numerical method to integrate area

from pandas import read_csv
import matplotlib.pyplot as plt


def read_file(filename):
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
    dx = df.index[1]-df.index[0]
    Grms = get_Grms(list(df.ix[:,0]), dx)
    print("area =", Grms)


def get_Grms(list, dx):
    """
    Function to numerically compute area under ASD curve (Grms value) using composite Simpson's rule.
    :param list: list of values of ASD vector
    :return:
    """
    Grms = simps(list, dx=dx)
    return Grms

def make_plots(df):
    ax = df.plot(y=[0,1], title='Accelerometer Overtests', loglog=True)
    plt.xlim([10, 2**12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    fig.savefig('test.png')
    # plt.show()
    plt.close('all')  # first close all open plots



def main():
    # Read file and store data in "data" object
    fname = 'Acoustics_Overtest_Data.txt'
    data_frame = read_file(fname)  # create data object that will keep all variables from file, raw and processed
    calc_stats(data_frame)
    make_plots(data_frame)

if __name__ == '__main__':
    main()