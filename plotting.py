"""
Plotting module for acoustics analysis

"""

import matplotlib.pyplot as plt


def make_plots(data_df, spec_dict):

    # Figure (1) : Tanks
    ax = data_df.plot(y=list(range(10)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig1'],color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Tanks', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig1.png')

    # Figure (2) : SPT DAPMs
    ax = data_df.plot(y=list(range(10,15)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig2'],color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : SPT DAPMs', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig2.png')

    # Figure (3) : Reflector DAPMs
    ax = data_df.plot(y=list(range(15,21)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig3'],color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Reflector DAPMs', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig3.png')

    # Figure (4) : MST
    ax = data_df.plot(y=[21], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig4'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : MST', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig4.png')

    # Figure (5) : Mez Bracket Assembly
    ax = data_df.plot(y=[22], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig5'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Mez Bracket Assembly', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig5.png')

    # Figure (6) : Comm Panel
    ax = data_df.plot(y=[23], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig6'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Comm Panel', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig6.png')

    # Figure (7) : Feed Arrays
    ax = data_df.plot(y=list(range(24,32)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig7'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Feed Arrays', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.savefig('fig7.png')








    #plt.show(fig)