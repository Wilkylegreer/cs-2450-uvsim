# program_loader.py

# Import necessary modules
from memory import Memory

def lineCleanUp(lines):
    for index, x in enumerate(lines):
        cleaned = x.replace("+", "")
        cleaned = cleaned.strip()
        lines[index] = cleaned
    return lines

def lineValidation(lines):
    if len(lines) > 100:
        print("Out of bounds")
        return False
    for x in lines:
        if len(x) > 4:
            print("Longer than 4")
        opCode = x[:2]
        memLoc = x[-2:]
        if int(opCode) not in [00, 10, 11, 20, 21, 30, 31, 32, 33, 40, 41, 42, 43]:
            print(f"Opcode not recognized - {opCode}")
            return False
        if int(memLoc) not in range(0, 99):
            print("Memory Overflow")
            return False
    return True

# ProgramLoader class
class ProgramLoader:
    def __init__(self, memory):
        self.memory = memory

    # Load program from file
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                allLines = file.readlines()
                allLines = lineCleanUp(allLines)
                if lineValidation(allLines):
                    for index, x in enumerate(allLines):
                        self.memory.set_value(index, x)
                else:
                    print("Error: Invalid program file")
                print(self.memory)
        except FileNotFoundError:
            print("Error: File was not found")

    # Load program from list
    def load_from_list(self, program_list):
        # Validate each instruction
        # Load instructions sequentially into memory
        pass

    # Validate individual instruction
    def validate_instruction(self, instruction):
        # Ensure instruction is a signed 4-digit number
        # Split into opcode and operand
        # Check opcode is valid
        pass