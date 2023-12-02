#Day 1 for Advent of Code 2023
#https://adventofcode.com/2015/day/1

def D1P1():
    print("Advent of Code Day 1 Puzzle 1")
    floor = 0 #This is the start floor 
    #Open the input file
    file = open("AoC_input_D1P1.txt", "r") 
    input_values = file.readline() #This will read one line
    for char in input_values:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    print("The final floor is: " + str(floor))
    
def D1P2():
    print("Advent of Code Day 1 Puzzle 2")
    floor = 0 #This is the start floor 
    char_position = 0
    #Open the input file
    file = open("AoC_input_D1P1.txt", "r") 
    input_values = file.readline() #This will read one line
    for char in input_values:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
            
        char_position += 1 #incriment the position by 1 each time
        if floor == -1:
            break #we have entered the basement if the floor goes negative
    print("The position that causes Santa to enter the basement is: " + str(char_position))

if __name__ == "__main__":
    D1P1() #call puzzle 1 
    D1P2() #call puzzle 2