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

Inputs: g^2/freq vs freq data from accelerometers and their corresponding qualification specs
Outputs: Comparison of Grms of qual specs and actual data,
        plots depending on location of accel on spacecraft,
        and data sheet with comparison table.
"""

from scipy.integrate import simps, trapz  # to calc Grms area under curve: numerical method to integrate area

from pandas import read_csv
import plotting
import qualification
from math import sqrt, fsum


def read_data_file(filename):
    """
    Function that reads input file and returns the accel reading data in form of a dataframe.
    """
    df = read_csv(filename, sep='\t', lineterminator='\n', header=[0, 1], index_col=0)
    return df


def calc_stats(data_df, spec_dict, loads_dict):
    # The y values.  A numpy array is used here,
    # but a python list could also be used.
    dx = data_df.index[1] - data_df.index[0]

    # get grms value for each data curve
    Grms_data_total = []

    for grms_col in range(len(data_df.columns)):
        Grms_data_total.append(get_Grms(data_df.ix[:, grms_col].tolist(), dx))
        # print(Grms_data_total[grms_col])

    Grms_qual_total = []
    G_data_loads = []
    G_qual_loads =[]
    G_data_numpeaks = []

    for i in range(10):
        Grms_qual_total.append(get_Grms(spec_dict['fig1'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig1'])
        G_qual_loads.append(loads_dict['1'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    for i in range(10, 15):
        Grms_qual_total.append(get_Grms(spec_dict['fig2'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig2'])
        G_qual_loads.append(loads_dict['2'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    for i in range(15, 21):
        Grms_qual_total.append(get_Grms(spec_dict['fig3'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig3'])
        G_qual_loads.append(loads_dict['3'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig4'], dx))  # col 21
    g_load, num_peaks = get_Gloads(data_df.ix[:, 21].tolist(), spec_dict['fig4'])
    G_qual_loads.append(loads_dict['4'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig5'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 22].tolist(), spec_dict['fig5'])
    G_qual_loads.append(loads_dict['5'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig6'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 23].tolist(), spec_dict['fig6'])
    G_qual_loads.append(loads_dict['6'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig7_IP'], dx))  # col 24
    g_load, num_peaks = get_Gloads(data_df.ix[:, 24].tolist(), spec_dict['fig7_IP'])
    G_qual_loads.append(loads_dict['7'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig7_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 25].tolist(), spec_dict['fig7_OP'])
    G_qual_loads.append(loads_dict['7'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig7_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 26].tolist(), spec_dict['fig7_IP'])
    G_qual_loads.append(loads_dict['7'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig7_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 27].tolist(), spec_dict['fig7_OP'])
    G_qual_loads.append(loads_dict['7'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    for i in range(28, 31):
        Grms_qual_total.append(get_Grms(spec_dict['fig7_IP'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig7_IP'])
        G_qual_loads.append(loads_dict['7'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig7_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 31].tolist(), spec_dict['fig7_OP'])
    G_qual_loads.append(loads_dict['7'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig8'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 32].tolist(), spec_dict['fig8'])
    G_qual_loads.append(loads_dict['8'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig9_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 33].tolist(), spec_dict['fig9_OP'])
    G_qual_loads.append(loads_dict['9'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig9_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 34].tolist(), spec_dict['fig9_IP'])
    G_qual_loads.append(loads_dict['9'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig9_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 35].tolist(), spec_dict['fig9_OP'])
    G_qual_loads.append(loads_dict['9'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig9_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 36].tolist(), spec_dict['fig9_IP'])
    G_qual_loads.append(loads_dict['9'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    for i in range(37, 40):
        Grms_qual_total.append(get_Grms(spec_dict['fig10'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig10'])
        G_qual_loads.append(loads_dict['10'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    for i in range(40, 43):
        Grms_qual_total.append(get_Grms(spec_dict['fig11_OP'], dx))
        g_load, num_peaks = get_Gloads(data_df.ix[:, i].tolist(), spec_dict['fig11_OP'])
        G_qual_loads.append(loads_dict['11'])
        G_data_loads.append(g_load)
        G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 43].tolist(), spec_dict['fig11_IP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_OP'], dx))  # col 44
    g_load, num_peaks = get_Gloads(data_df.ix[:, 44].tolist(), spec_dict['fig11_OP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 45].tolist(), spec_dict['fig11_IP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_OP'], dx))  # col 46
    g_load, num_peaks = get_Gloads(data_df.ix[:, 46].tolist(), spec_dict['fig11_OP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 47].tolist(), spec_dict['fig11_IP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig11_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 48].tolist(), spec_dict['fig11_OP'])
    G_qual_loads.append(loads_dict['11'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig12_IP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 49].tolist(), spec_dict['fig12_IP'])
    G_qual_loads.append(loads_dict['12'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    Grms_qual_total.append(get_Grms(spec_dict['fig12_OP'], dx))
    g_load, num_peaks = get_Gloads(data_df.ix[:, 50].tolist(), spec_dict['fig12_OP'])
    G_qual_loads.append(loads_dict['12'])
    G_data_loads.append(g_load)
    G_data_numpeaks.append(num_peaks)

    return Grms_data_total, Grms_qual_total, G_data_loads, G_qual_loads, G_data_numpeaks


def get_Grms(given_list, dx):
    """
    Function to numerically compute area under ASD curve (Grms value) using composite Simpson's rule.
    """
    area_under_ASD_curve = simps(given_list, dx=dx)
    return sqrt(area_under_ASD_curve)


def get_Gloads(data_list, spec_list):
    entry_difference = []
    pieces_grms = []
    dx = 4

    for i in range(len(data_list) - 1):
        if (data_list[i] > spec_list[i]) & (data_list[i + 1] > spec_list[i + 1]):
            entry_difference.append(data_list[i] - spec_list[i])

        if (i != 0) & (data_list[i] <= spec_list[i]) & (data_list[i - 1] > spec_list[i - 1]):
            if len(entry_difference) > 0:
                pieces_grms.append(get_Grms(entry_difference, dx))
                del entry_difference[:]

    num_peaks = len(pieces_grms)
    return fsum(pieces_grms), num_peaks


def write_output_file(fname, accel_names, Grms_data_total, Grms_qual_total, G_data_loads, G_qual_loads, num_peaks):
    grms_total_diff = [a - b for a, b in zip(Grms_qual_total, Grms_data_total)]
    loads_total_diff = [a - b for a, b in zip(G_qual_loads, G_data_loads)]

    with open(fname, 'w') as f_output:
        f_output.write('Accels\tGrms_data\tGrms_qual\tGrms_dif\tPks\tLoads_d\tLoads_q\tLoads_dif\n')

        for i in range(len(Grms_data_total)):
            f_output.write(str(accel_names[i]) + '\t' +
                           str(round(Grms_data_total[i], 2)) + '\t' + str(round(Grms_qual_total[i], 2)) +
                           '\t' + str(round(grms_total_diff[i], 2)) + '\t' +
                           str(round(num_peaks[i], 2)) + '\t' +
                           str(round(G_data_loads[i], 2)) + '\t' + str(round(G_qual_loads[i], 2)) + '\t' +
                           str(round(loads_total_diff[i], 2)) + '\n')


def main():
    # Read file and store data in "data" object
    fname_output = 'overtest_output.txt'
    fname_data = 'Acoustics_Overtest_Data.txt'
    fname_design_loads = 'design_loads.txt'
    fname_randomV_specs = 'qual_specs.txt'
    data_df = read_data_file(fname_data)  # create data object that will keep all variables from file, raw and processed
    spec_dict = qualification.get_qual(fname_randomV_specs)

    # get dictionary of design loads of {figure# : design_load}
    loads_dict = qualification.get_design_loads(fname_design_loads)
    accel_names = data_df.columns.tolist()

    Grms_data_total, Grms_qual_total, G_data_loads, G_qual_loads, num_peaks = calc_stats(data_df, spec_dict,loads_dict)
    write_output_file(fname_output, accel_names, Grms_data_total, Grms_qual_total, G_data_loads, G_qual_loads, num_peaks)
    # plotting.make_plots(data_df, spec_dict)


if __name__ == '__main__':
    main()