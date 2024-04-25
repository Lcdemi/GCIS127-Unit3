import random

def literal_list():
    list1 = [1, 2.0, "3", '4', False]
    return list1

def sequence_list(sequence):
    list2 = list(sequence)
    return list2

def print_list(a_list):
    for element in a_list:
        print(element, end=" ")
    print()

def append_to_list(sequence):
    empty_list = []
    for element in sequence:
        empty_list.append(element)
    return empty_list

def roll_the_die(sides):
    roll = random.randint(1, sides)
    return roll

def countdown(n):
    if n < 0: #base case
        return 0
    else:
        print(n)
        return n + countdown(n-1)
    
def countup(n):
    if n < 0: #base case
        return 0
    else:
        rest = countup(n-1)
        print(n)
        return n + rest
    
def factorial(n):
    if n < 0: #base case
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


def main():
    #a_list = literal_list()
    #print_list(a_list)

    #b_list = sequence_list("abcdefg")
    #print_list(b_list)

    #c_list = append_to_list(range(1, 10))
    #print_list(c_list)

    #random.seed(1)
    #for _ in range(10):
    #    print(roll_the_die(6), end=" ")

    print("Sum:", countdown(5))
    print("Sum:", countup(10))
    print("Product:", factorial(10))
    print("Product:", factorial(100))

if __name__ == "__main__":
    main()