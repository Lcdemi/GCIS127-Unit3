import list_utils

def linear_search(a_list, target):
    for i in range(len(a_list)):
        if target == a_list[i]:
            return i
    return None

def binary_search(a_list, target, start=0, end=None):
    if end is None:
        end = len(a_list) - 1
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        value = a_list[mid]
        if value == target:
            return mid
        elif value < target:
            return binary_search(a_list, target, mid+1, end)
        else:
            return binary_search(a_list, target, start, mid-1)

def main():
    a_list = list_utils.range_list(1, 101)
    print(linear_search(a_list, 1))
    print(linear_search(a_list, 50))
    print(linear_search(a_list, 100))
    print(linear_search(a_list, 101))

if __name__ == "__main__":
    main()

#target: 79 table (3 iterations)
#start: 0, 9, 13, 13
#end: 16, 16, 16, 13
#mid: 8, 12, 14, 13
#value: 39, 77, 83, 79

#target: 11 table (not found)
#start: 0, 0, 0, 2, 3
#end: 16, 7, 2, 2, 2
#mid: 8, 3, 1, 2
#value: 39, 12, 9, 10
        