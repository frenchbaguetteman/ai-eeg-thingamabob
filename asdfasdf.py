import csv

n = 0

input_file = f'data/neutral/neutral{n}.txt'
output_file = f'data/neutral/neutral{n}.csv'

with open(input_file, 'r') as file:
    lines = file.readlines()

data = [float(line.strip()) for line in lines]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Value'])
    writer.writerows([[value] for value in data])

print(f"CSV file '{output_file}' has been created.")