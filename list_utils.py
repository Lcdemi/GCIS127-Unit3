import random

def random_list(size, min_value=0, max_value=None):
    rand_list = []
    if max_value is None:
        max_value = size
    for _ in range(size):
        random_num = random.randint(min_value, max_value)
        rand_list.append(random_num)
    return rand_list

def range_list(start, stop, step=1):
    values_list = []
    list_range = range(start, stop, step)
    for i in list_range:
        values_list.append(i)
    return values_list
    

def main():
    random.seed(1) #seed testing
    rand_list = random_list(10)
    print(rand_list)

    print(range_list(1, 10, 2))
    print(range_list(50, 100, 5))

if __name__ == "__main__":
    main()