# main.py

from memory import Memory
from cpu import CPU
from control_instructions import ControlInstructions
from program_loader import ProgramLoader
from io_handler import get_input, print_output

def main():
    # Initialize Memory object
    memory = Memory()
    # Initialize CPU object
    cpu = CPU()

    # Initialize ControlInstructions with memory, I/O, CPU
    conInstruct = ControlInstructions(memory, cpu)
    # Initialize ProgramLoader with memory
    proLoader = ProgramLoader(memory)

    userInput = get_input()

    # Load program
    if userInput == 1:
        proLoader.load_from_file("test.txt")
    elif userInput == 2:
        proLoader.load_from_list()
    elif userInput == 3:
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