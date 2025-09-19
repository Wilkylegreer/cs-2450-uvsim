# main.py

from memory import Memory
from cpu import CPU
from control_instructions import ControlInstructions
from program_loader import ProgramLoader
from math_instructions import MathInstructions

def print_mem(mem):
    for index, x in enumerate(mem.mem):
        print(f"{index} - {x}")

def main():
    # Initializations
    memory = Memory()
    cpu = CPU(memory)

    conInstruct = ControlInstructions(memory, cpu)
    mathInstruct = MathInstructions(memory)

    cpu.set_instructions(conInstruct, mathInstruct)

    proLoader = ProgramLoader(memory)

    userInput = 1 # get_input()

    # Load program
    if int(userInput) == 1:
        proLoader.load_from_file("test_files/Test1.txt")
    elif int(userInput) == 2:
        proLoader.load_from_file("test_files/Test2.txt")
    elif int(userInput) == 3:
        proLoader.load_from_file("test_files/Test3.txt")
    else:
        print("No Option Selected...")

    # Start CPU execution loop until HALT
    cpu.run()

    print("Main loop finished...")

if __name__ == "__main__":
    main()