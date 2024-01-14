from collections import Counter

def check_nice_vowels(line):
    vowels = ["a", "e", "i", "o", "u"]
    count_vowels = Counter(line.strip())
    sum_vowels = 0
    for vowel in vowels:
        sum_vowels = sum_vowels + count_vowels[vowel]
    if sum_vowels >= 3:
        return True
    return False

def check_nice_double_letter(line):
    for i in range(0,len(line)-1):
        if line[i] == line[i+1]:
            return True
    return False

def check_no_letter_rows(line):
    row_letters = ["ab", "cd", "pq", "xy"]
    for letter in row_letters:
        if letter in line:
            return False
    return True

def main():
    with open("input.txt", encoding="utf-8") as f:
        counter = 0
        for line in f:
            nice_vowel = check_nice_vowels(line)
            nice_double_letters = check_nice_double_letter(line)
            nice_not_row = check_no_letter_rows(line)
            if nice_vowel and nice_double_letters and nice_not_row:
                counter += 1
        print(f"Solution  Part 1 is: {counter}")

if __name__ == "__main__":
    main()
