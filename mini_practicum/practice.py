def absolute_difference(a, b):
    difference = a - b
    if difference < 0:
        return difference * -1
    else:
        return difference
    
def pi_tester():
    correct = True
    counter = 0
    score = 0
    pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    while correct == True and counter <= 99:
        answer = input("Enter the next digit: ")
        if(int(answer) == int(pi[counter])):
            score += 1
            counter += 1
        elif int(answer) != int(pi[counter]):
            print("The correct integer was " + pi[counter])
            correct = False
    return score

def main():
    final_score = pi_tester()
    print("Score: " + str(final_score))


if __name__ == "__main__":
    main()


    

