"""
Plotting module for acoustics analysis

"""

import matplotlib.pyplot as plt

def make_plots(df):
    ax = df.plot(y=[0,1], title='Accelerometer Overtests', loglog=True)
    plt.xlim([10, 2**12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    fig.savefig('test.png')
    plt.show()
    plt.close('all')  # first close all open plots