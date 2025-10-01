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

    program_loaded = False
    while True:
        userInput = get_file()
        try:
            program_loaded = proLoader.load_from_file(userInput)
            if program_loaded:
                break
            else:
                # Handles bad lines
                print(f"Error loading file '{userInput}': Invalid program")
                print("Please try again.")
        except Exception as e:
            # Handles bad file names
            print(f"Error loading file '{userInput}': {e}")
            print("Please try again.")

    # Start if loaded right
    if program_loaded:
        cpu.run()

    print(".")

if __name__ == "__main__":
    main()