# main.py

from memory import Memory
from cpu import CPU
from control_instructions import ControlInstructions
from program_loader import ProgramLoader
from math_instructions import MathInstructions
from io_handler import get_input, print_output

def print_mem(mem):
    for index, x in enumerate(mem.mem):
        print(f"{index} - {x}")

def main():
    # Initializations
    memory = Memory()
    cpu = CPU()

    # print_mem(memory)

    conInstruct = ControlInstructions(memory, cpu)
    proLoader = ProgramLoader(memory)
    mathInstruct = MathInstructions(memory)

    userInput = 1 # get_input()

    # Load program
    if int(userInput) == 1:
        proLoader.load_from_file("test.txt")
        exit()
    elif int(userInput) == 2:
        proLoader.load_from_list()
    elif int(userInput) == 3:
        # Option 3: interactive input
        pass
    else:
        print("No Option Selected...")

    # Start CPU execution loop until HALT
    while (conInstruct.done == False):
        pass

    print("Main loop finished...")

if __name__ == "__main__":
    main()