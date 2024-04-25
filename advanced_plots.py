import plotter
import csv
import re

def plot_grades(filename, first_name, last_name):
    plotter.init(first_name + " " + last_name, "Grade Item", "Score")
    counter = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            name = record[0]
            split_names = re.findall("[\w]+", name)
            if split_names[-1] == first_name:
                if split_names[0] == last_name:
                    for i in range(3, len(record)):
                        counter += 1
                        plotter.add_data_point(float(record[i]))
    plotter.plot()

def average(filename, column):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        total = 0
        count = 0
        for record in csv_reader:
            try:
                grade = record[column]
                #print(grade) test code
                grade = float(grade)
                total += grade
                count += 1
            except:
               ... 
        return total / count
    
def plot_class_averages(filename):
    invalid = False
    counter = 3
    plotter.init("Class Averages", "Grade Item", "Average")
    while invalid == False:
        try:
            assignment_average = average(filename, counter)
            counter += 1
            plotter.add_data_point(float(assignment_average))
        except:
            invalid = True
    plotter.plot()

def main():
    plot_grades("data/full_grades_100.csv", "Blake", "Gommer")
    plot_grades("data/full_grades_100.csv", "Anicia", "Lemay")
    #print(average("data/full_grades_010.csv", 5))
    plot_class_averages("data/full_grades_999.csv")

if __name__ == "__main__":
    main()