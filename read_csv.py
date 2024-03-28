import csv

data = []

with open("password.csv", "r") as file_csv:
    lector_csv = csv.reader(file_csv)
    print(lector_csv)
    for fila in lector_csv:
        data.append(fila)

def write_on_csv(list):
    with open("password.csv", "w") as file_csv:
        escritor_csv = csv.writer(file_csv)
        for fila in list:
            escritor_csv.writerow(fila)