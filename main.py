"""

Python script to evaluate accelerometers that measured more output than expected.

"""

from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt


def read_file(filename):
    df = read_csv(filename, sep='\t', lineterminator='\n', header=[0, 1], index_col=0)
    return df

def make_plots(df):
    df.plot(y=[0,1], title='Accelerometers')
    plt.show()


def main():
    # Read file and store data in "data" object
    fname = 'Acoustics_Overtest_Data.txt'
    data_frame = read_file(fname)  # create data object that will keep all variables from file, raw and processed
    make_plots(data_frame)

if __name__ == '__main__':
    main()