# main.py
from io_handler import get_file

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

    while True:
        userInput = get_file()
        try:
            proLoader.load_from_file(userInput)
            break
        except Exception as e:
            print(f"Error loading file '{userInput}': {e}")
            print("Please try again.")

    # Start CPU execution loop until HALT
    cpu.run()

    print(".")

if __name__ == "__main__":
    main()