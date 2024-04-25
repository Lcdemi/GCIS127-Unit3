import csv
import plotter
import re

def first_only(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            print(record[0])

def names_and_addresses(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            print("Name:", record[0])
            print("Address:", record[1])

def average(filename, column):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        total = 0
        count = 0
        for record in csv_reader:
            grade = record[column]
            grade = float(grade)
            total += grade
            count += 1
        return total / count
    
def plot_grades(filename, column):
    plotter.init("Funny Graph", "Student", "Grade")
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for record in csv_reader:
            datapoint = record[column]
            plotter.add_data_point(int(datapoint))
    plotter.plot()

def zip_check(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for record in csv_reader:
            name = record[0]
            address = record[1]
            if re.findall("[7-9]\d{4}", address):
                print(name, address)

def string_to_array(a_string):
    empty = []
    for letter in range(len(a_string)):
        empty.append(a_string[letter])
    return empty

def main():
    #first_only("data/grades_010.csv")
    #names_and_addresses("data/full_grades_010.csv")
    #print(average("data/full_grades_010.csv", 4))
    #zip_check("data/full_grades_010.csv")
    #plot_grades("data/grades_010.csv", 3)
    print(string_to_array("ABCD"))

if __name__ == "__main__":
    main()