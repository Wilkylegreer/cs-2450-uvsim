# program_loader.py

# Import necessary modules
from memory import Memory

def lineCleanUp(lines):
    for index, x in enumerate(lines):
        cleaned = x.replace("+", "")
        cleaned = cleaned.replace("\n", "")
        lines[index] = cleaned
    return lines

def lineValidation(lines):
    for x in lines:
        opCode = x[:2]
        memLoc = x[-2:]
        print(f"{opCode} - {memLoc}")

# ProgramLoader class
class ProgramLoader:
    def __init__(self, memory):
        """
        memory: Memory object where program will be loaded
        """
        self.memory = memory

    # Load program from file
    def load_from_file(self, filename):
        # HARD CODED FILE
        try:
            with open("test_files/Test1.txt", "r") as file:
                allLines = file.readlines()
                allLines = lineCleanUp(allLines)
                lineValidation(allLines)
        except FileNotFoundError:
            print("Error: File was not found")
        # Validate each instruction
            # Pass if good
            # Raise error and halt if bad "Test file has bad verbage"
        # Load instructions into memory starting at address 0
        # Handle errors: invalid opcode, invalid memory, overflow
        pass

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