def print_lines(filename):
    with open(filename) as file:
        for line in file:
            line = line.strip()
            line.lower()
            print(line)

def find_word(filename):
    file = open(filename)
    word = input("Enter a word: ")
    word = word.lower()
    for line in file:
        line = line.strip()
        line.lower()
        if line == word:
            print("Found the word:", line)
            file.close()
            return
    print("Didn't find the word")
    file.close()

def first_words(filename, maximum):
    with open(filename) as file:
        word_list = []
        for line in file:
            line = line.strip()
            tokens = line.split()
            if tokens:
                word_list.append(tokens[0])
                if len(word_list) >= maximum:
                    break
    return word_list

def numbers():
    valid = True
    total_sum = 0
    while valid:
            filename = input("Enter a filename: ")
            if filename == "":
                valid = False
            else:
                try:
                    with open(filename) as file:
                        sum = 0
                        for line in file:
                            line = line.strip()
                            try:
                                i = int(line)
                                sum += i
                            except ValueError:
                                print("Skipping non-numeric data:", line)
                        print("sum:", sum)
                        total_sum += sum
                except FileNotFoundError:
                    print("File not found", filename)
    print("Total Sum:", total_sum)

def main():
    print_lines("data/alice.txt")
    #find_word("data/words.txt")
    #print(first_words("data/alice.txt", 30))
    numbers()

if __name__ == "__main__":
    main()
