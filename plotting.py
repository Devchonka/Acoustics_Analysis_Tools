"""
Plotting module for acoustics analysis

"""

import matplotlib.pyplot as plt


def make_plots(data_df, spec_dict):
    # Figure (1) : Tanks
    ax = data_df.plot(y=list(range(10)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig1'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Tanks', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig1.pdf', bbox_inches='tight')

    # Figure (2) : SPT DAPMs
    ax = data_df.plot(y=list(range(10, 15)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig2'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : SPT DAPMs', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig2.pdf', bbox_inches='tight')

    # Figure (3) : Reflector DAPMs
    ax = data_df.plot(y=list(range(15, 21)), title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig3'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Reflector DAPMs', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig3.pdf', bbox_inches='tight')

    # Figure (4) : MST
    ax = data_df.plot(y=[21], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig4'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : MST', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig4.pdf', bbox_inches='tight')

    # Figure (5) : Mez Bracket Assembly
    ax = data_df.plot(y=[22], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig5'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Mez Bracket Assembly', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig5.pdf', bbox_inches='tight')

    # Figure (6) : Comm Panel
    ax = data_df.plot(y=[23], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig6'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Comm Panel', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig6.pdf', bbox_inches='tight')


    # Figure (7) : Feed Arrays : IP and OP : y=list(range(24,32)

    plt.figure()
    plt.suptitle('NBN co 1-A : Feed Arrays', fontsize=20)
    ax = plt.subplot("121")
    ax.set_title('In Plane')

    ax.loglog(data_df.index, data_df[[24]], label=data_df.columns[24])  # 24,26,28,29,30
    ax.loglog(data_df.index, data_df[[26]], label=data_df.columns[26])
    ax.loglog(data_df.index, data_df[[28]], label=data_df.columns[28])
    ax.loglog(data_df.index, data_df[[29]], label=data_df.columns[29])
    ax.loglog(data_df.index, data_df[[30]], label=data_df.columns[30])

    plt.loglog(data_df.index, spec_dict['fig7_IP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=10)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    ax = plt.subplot("122")
    ax.set_title('Out of Plane')

    ax.loglog(data_df.index, data_df[[25]], label=data_df.columns[25])  # 25,27,31
    ax.loglog(data_df.index, data_df[[27]], label=data_df.columns[27])
    ax.loglog(data_df.index, data_df[[31]], label=data_df.columns[31])
    plt.loglog(data_df.index, spec_dict['fig7_OP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    plt.savefig('fig7.pdf', bbox_inches='tight')

    # Figure (8) : Beacon Horn
    ax = data_df.plot(y=[32], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig8'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : Beacon Horn', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig8.pdf', bbox_inches='tight')


    # Figure (9) : ECASS

    plt.figure()
    plt.suptitle('NBN co 1-A : ECASS', fontsize=20)
    ax = plt.subplot("121")
    ax.set_title('In Plane')

    ax.loglog(data_df.index, data_df[[34]], label=data_df.columns[34])
    ax.loglog(data_df.index, data_df[[36]], label=data_df.columns[36])

    plt.loglog(data_df.index, spec_dict['fig7_IP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=10)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    ax = plt.subplot("122")
    ax.set_title('Out of Plane')

    ax.loglog(data_df.index, data_df[[33]], label=data_df.columns[33])
    ax.loglog(data_df.index, data_df[[35]], label=data_df.columns[35])

    plt.loglog(data_df.index, spec_dict['fig7_OP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    plt.savefig('fig9.pdf', bbox_inches='tight')

    # Figure (10) : TC & R
    ax = data_df.plot(y=[37, 38, 39], title='Accelerometer Overtests', loglog=True)
    plt.plot(data_df.index, spec_dict['fig10'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    fig = ax.get_figure()

    fig.suptitle('NBN co 1-A : TC & R', fontsize=20)
    plt.xlabel('Hz', fontsize=18)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=16)
    plt.legend(loc=0, prop={'size': 6})
    plt.savefig('fig10.pdf', bbox_inches='tight')


    # Figure (11) : LNA Panels

    plt.figure()
    plt.suptitle('NBN co 1-A : LNA Panels', fontsize=20)
    ax = plt.subplot("121")
    ax.set_title('In Plane')

    ax.loglog(data_df.index, data_df[[43]], label=data_df.columns[43])
    ax.loglog(data_df.index, data_df[[45]], label=data_df.columns[45])
    ax.loglog(data_df.index, data_df[[47]], label=data_df.columns[47])

    plt.loglog(data_df.index, spec_dict['fig11_IP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=10)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    ax = plt.subplot("122")
    ax.set_title('Out of Plane')

    ax.loglog(data_df.index, data_df[[40]], label=data_df.columns[40])
    ax.loglog(data_df.index, data_df[[41]], label=data_df.columns[41])
    ax.loglog(data_df.index, data_df[[42]], label=data_df.columns[42])
    ax.loglog(data_df.index, data_df[[44]], label=data_df.columns[44])
    ax.loglog(data_df.index, data_df[[46]], label=data_df.columns[46])
    ax.loglog(data_df.index, data_df[[48]], label=data_df.columns[48])

    plt.loglog(data_df.index, spec_dict['fig11_OP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    plt.savefig('fig11.pdf', bbox_inches='tight')

    # Figure (12) : Filter Panels

    plt.figure()
    plt.suptitle('NBN co 1-A : Filter Panels', fontsize=20)
    ax = plt.subplot("121")
    ax.set_title('In Plane')

    ax.loglog(data_df.index, data_df[[49]], label=data_df.columns[49])

    plt.loglog(data_df.index, spec_dict['fig12_IP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.ylabel('Acceleration Spectral Density (ASD) ($g^2/Hz$)', fontsize=10)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    ax = plt.subplot("122")
    ax.set_title('Out of Plane')

    ax.loglog(data_df.index, data_df[[50]], label=data_df.columns[50])

    plt.loglog(data_df.index, spec_dict['fig12_OP'], color='black', linewidth=2.5, linestyle='--')
    plt.xlim([10, 2 ** 12])
    plt.xlabel('Hz', fontsize=11)
    plt.grid()
    plt.legend(loc=0, prop={'size': 6})

    plt.savefig('fig12.pdf', bbox_inches='tight')

    # plt.show()


def make_subplots(presig_df, postsig_df, first_index, num_plots, fig_name):
    subplot_num = int(num_plots / 3)

    plt.figure()
    plt.suptitle('NBN co 1-A : Signature Overlays', fontsize=20)
    # make 6 or 9 subplots
    for i in range(1, num_plots + 1):
        ax = plt.subplot('3' + str(subplot_num) + str(i))

        ax.loglog(presig_df.index, presig_df[[first_index]], label='PRE' + str(presig_df.columns[first_index]),
                  color='magenta')
        ax.loglog(postsig_df.index, postsig_df[[first_index]], label='POST' + str(postsig_df.columns[first_index]),
                  color='green')
        first_index += 1

        plt.xlim([10, 2 ** 12])
        plt.xlabel('Hz', fontsize=6)
        plt.ylabel('ASD($g^2/Hz$)', fontsize=5)
        plt.grid()
        plt.legend(loc=0, prop={'size': 4})

        plt.rcParams.update({'font.size': 8})

    plt.savefig(fig_name, bbox_inches='tight')


def sign_overlay(presig_df, postsig_df):
    make_subplots(presig_df, postsig_df, 0, 9, 'sig_overlay_1.pdf')
    make_subplots(presig_df, postsig_df, 9, 9, 'sig_overlay_2.pdf')
    make_subplots(presig_df, postsig_df, 18, 9, 'sig_overlay_3.pdf')
    make_subplots(presig_df, postsig_df, 27, 9, 'sig_overlay_4.pdf')
    make_subplots(presig_df, postsig_df, 36, 9, 'sig_overlay_5.pdf')
    make_subplots(presig_df, postsig_df, 45, 6, 'sig_overlay_6.pdf')
