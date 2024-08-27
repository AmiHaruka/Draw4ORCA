#***********************************************************************#
#                       Update date: 2024.08.26                         #
#                           Au : AmiHaruka                              #
#***********************************************************************#

import sys
import matplotlib.pyplot as plt

def plot_energy_vs_coordinate(input_file, relative=False):

    coordinates = []
    energies = []
    
    with open(input_file, 'r') as file:
        for line in file:
            coord, energy = map(float, line.split())
            coordinates.append(coord)
            energies.append(energy)
    
    if relative:
        min_energy = min(energies)
        energies = [e - min_energy for e in energies]
    
    plt.figure(figsize=(10, 8))
    plt.plot(coordinates, energies, marker='s', linestyle='-', color='blue', label=input_file)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlabel('Reaction Coordinate (Å)')
    plt.ylabel('Energy (eV)')
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.3f'))
    if relative:
        plt.title('Relative Energy vs Reaction Coordinate')
    else:
        plt.title('Absolute Energy vs Reaction Coordinate')
    plt.grid(True)
    plt.legend()
    
    output_image = input_file.replace('.dat', '_relative.png' if relative else '_absolute.png')
    plt.savefig(output_image ,dpi=300)
    print(f"Plot saved as {output_image}")
    
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("Usage: python plot_energy_vs_coordinate.py input_file [relative]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    relative = len(sys.argv) == 3 and sys.argv[2].lower() == 'relative'
    plot_energy_vs_coordinate(input_file, relative)

