#Day 1 for Advent of Code 2023
#https://adventofcode.com/2023/day/1


calibration_values = []
calibration_values_2 = []
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_mappings = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9" 
}

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
    file = open("AoC_input_D1P1.txt", "r") 
    for line in file:
        line_digits = []
        for k,v in enumerate(line):
            #print(f"{k}: {line[k::]}")
            for digit_word in digit_mappings.keys():
                if line[k::].startswith(digit_word):
                    line_digits.append(digit_mappings[digit_word])
            if v in digits:
                line_digits.append(v)
        if len(line_digits) >= 2:
            calibration_values_2.append(int(line_digits[0] + line_digits[-1]))
        else:
            calibration_values_2.append(int(line_digits[0] + line_digits[0]))
    print(sum(calibration_values_2))
        


if __name__ == "__main__":
    D1P1() #call puzzle 1 
    D1P2() #call puzzle 2