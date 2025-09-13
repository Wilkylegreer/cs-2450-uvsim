# program_loader.py
# Purpose: Load and validate BasicML programs into memory
# Person C responsibility

# Import necessary modules
# from memory import Memory

# ProgramLoader class
class ProgramLoader:
    def __init__(self, memory):
        """
        memory: Memory object where program will be loaded
        """
        self.memory = memory

    # Load program from file
    def load_from_file(self, filename):
        # Open file, read lines
        # Validate each instruction
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