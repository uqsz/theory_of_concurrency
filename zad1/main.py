import csv
import matplotlib.pyplot as plt

def create_and_save_plot(file_path, output_file_name):
    plt.clf()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        results = [list(map(float, row)) for row in reader]
    for i, row in enumerate(results):
        for j, value in enumerate(row):
            plt.scatter((i + 1) * 25, value, color='blue', s=10)

    plt.xlabel('Liczba filozofów')
    plt.ylabel('Czas oczekiwania [µs]')
    plt.yscale('log')
    plt.title(f'Test czasowy dla wariantu {output_file_name[-5]}')

    plt.savefig(f'plot_{output_file_name[:-4]}.png')

    # plt.show()

file_paths = ['results2.csv','results3.csv', 'results4.csv', 'results5.csv', 'results6.csv']


for file_path in file_paths:
    create_and_save_plot(file_path, file_path)
