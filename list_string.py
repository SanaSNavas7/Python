import csv
csv_file_path = 'a.csv' 
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)  
