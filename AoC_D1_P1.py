#Day 1 for Advent of Code 2023
#https://adventofcode.com/2023/day/1

def D1P1():
    print("Advent of Code Day 1 Puzzle 1")
    calibration_sum = 0;
    #Open the input file
    file = open("AoC_input_D1P1.txt", "r") 
    for line in file:
        line = line.strip('\n') #remove the newline character
        in1 = "" 
        in2 = ""
        for char in line:
            if char.isdigit():
                in1 = char
                break #break out of the loop once we have the first number      
        for char in reversed(line):
            if char.isdigit():
                in2 = char
                break

        calibration_sum += int(in1 + in2)
    print("The calibration sum is: " + str(calibration_sum))
            
    
def D1P2():
    print("Advent of Code Day 1 Puzzle 2")
    digit_dict = {
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4, 
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9}
    calibration_sum = 0;
    #Open the input file
    file = open("AoC_input_D1P1.txt", "r") 
    for line in file:
        line = line.strip('\n') #remove the newline character
        in1 = get_digit(line, digit_dict)
        in2 = get_digit(''.join(reversed(line)), digit_dict)
        if in1 != None and in2 != None:
            calibration_sum += in1 + in2
        else:
            print("Error: Could not find two digits in line: " + line)
    print("The calibration sum is: " + str(calibration_sum))

def get_digit(line, digit_dict):
    word = ""
    for char in line:
        if char.isalpha():
            word += char
            if any(key.startswith(word) for key in digit_dict.keys()):
                if word in digit_dict or reversed(word) in digit_dict:
                    return digit_dict[word]
        elif char.isdigit():
            return int(char)
    return None

if __name__ == "__main__":
    #D1P1() #call puzzle 1 
    D1P2() #call puzzle 2