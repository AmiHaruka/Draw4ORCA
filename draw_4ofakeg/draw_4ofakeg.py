#***********************************************************************#
#                       Update date: 2024.08.26                         #
#                           Au : AmiHaruka                              #
#***********************************************************************#

import matplotlib.pyplot as plt
import re
import os
import sys

def extract_values(filename):
    with open(filename, 'r') as f:
        content = f.read()

    scf_done = re.findall(r'SCF Done:\s+([-\d.]+)', content)
    max_force = re.findall(r'Maximum Force\s+([-\d.]+)\s+([-\d.]+)', content)
    rms_force = re.findall(r'RMS\s+Force\s+([-\d.]+)\s+([-\d.]+)', content)
    max_disp = re.findall(r'Maximum Displacement\s+([-\d.]+)\s+([-\d.]+)', content)
    rms_disp = re.findall(r'RMS\s+Displacement\s+([-\d.]+)\s+([-\d.]+)', content)

    return scf_done, max_force, rms_force, max_disp, rms_disp

def plot_values(values, thresholds, title, ylabel, output_folder, yes_no_labels):
    plt.figure(figsize=(12, 8))
    plt.plot(values, 'bo-', label=title)

    if thresholds:
        plt.axhline(y=float(thresholds[0]), color='r', linestyle='-', label='Convergence Threshold')
    
    plt.xlabel('Step Number')
    plt.ylabel(ylabel)

    first_label = yes_no_labels[0]
    last_label = yes_no_labels[-1]
    plt.title(f'{title}: First={first_label}, Last={last_label}')

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.tight_layout()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    plt.savefig(os.path.join(output_folder, f'{title}.png'),dpi=300)
    plt.show()

def main(filenames):
    combined_scf_done = []
    combined_max_force = []
    combined_rms_force = []
    combined_max_disp = []
    combined_rms_disp = []

    max_force_thresholds = []
    rms_force_thresholds = []
    max_disp_thresholds = []
    rms_disp_thresholds = []

    max_force_labels = []
    rms_force_labels = []
    max_disp_labels = []
    rms_disp_labels = []

    for filename in filenames:
        scf_done, max_force, rms_force, max_disp, rms_disp = extract_values(filename)

        combined_scf_done.extend([float(val) for val in scf_done])
        combined_max_force.extend([float(val[0]) for val in max_force])
        combined_rms_force.extend([float(val[0]) for val in rms_force])
        combined_max_disp.extend([float(val[0]) for val in max_disp])
        combined_rms_disp.extend([float(val[0]) for val in rms_disp])

        max_force_thresholds.extend([val[1] for val in max_force])
        rms_force_thresholds.extend([val[1] for val in rms_force])
        max_disp_thresholds.extend([val[1] for val in max_disp])
        rms_disp_thresholds.extend([val[1] for val in rms_disp])

        max_force_labels.extend(['YES' if float(val[0]) <= float(val[1]) else 'NO' for val in max_force])
        rms_force_labels.extend(['YES' if float(val[0]) <= float(val[1]) else 'NO' for val in rms_force])
        max_disp_labels.extend(['YES' if float(val[0]) <= float(val[1]) else 'NO' for val in max_disp])
        rms_disp_labels.extend(['YES' if float(val[0]) <= float(val[1]) else 'NO' for val in rms_disp])

    output_folder = "Plots"

    plot_values(combined_scf_done, None, 'Total ele. Energy', 'Energy (a.u.)', output_folder, ['N\A', 'N\A'])
    plot_values(combined_max_force, max_force_thresholds, 'Maximum Force', 'Force', output_folder, [max_force_labels[0], max_force_labels[-1]])
    plot_values(combined_rms_force, rms_force_thresholds, 'RMS Force', 'Force', output_folder, [rms_force_labels[0], rms_force_labels[-1]])
    plot_values(combined_max_disp, max_disp_thresholds, 'Maximum Displacement', 'Displacement', output_folder, [max_disp_labels[0], max_disp_labels[-1]])
    plot_values(combined_rms_disp, rms_disp_thresholds, 'RMS Displacement', 'Displacement', output_folder, [rms_disp_labels[0], rms_disp_labels[-1]])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py file1.out file2.out ...")
        sys.exit(1)

    filenames = sys.argv[1:]
    main(filenames)

