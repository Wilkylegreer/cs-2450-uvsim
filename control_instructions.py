# control_instructions.py
# Purpose: Implement control flow and I/O instructions for UVSim
# Person C responsibility

# Import necessary modules
# from memory import Memory
# from io_handler import get_input, print_output

# ControlInstructions class
class ControlInstructions:
    def __init__(self, memory, io_handler, cpu):
        """
        memory: Memory object
        io_handler: object/module for I/O operations
        cpu: CPU object (to access accumulator and instruction pointer)
        """
        self.memory = memory
        self.io_handler = io_handler
        self.cpu = cpu

    # READ instruction
    def READ(self, address):
        # Get input from user
        # Store value in memory at 'address'
        pass

    # WRITE instruction
    def WRITE(self, address):
        # Fetch value from memory at 'address'
        # Output value to user
        pass

    # LOAD instruction
    def LOAD(self, address):
        # Load value from memory at 'address' into accumulator
        pass

    # STORE instruction
    def STORE(self, address):
        # Store accumulator value into memory at 'address'
        pass

    # BRANCH instruction
    def BRANCH(self, address):
        # Jump to memory address
        pass

    # BRANCHNEG instruction
    def BRANCHNEG(self, address):
        # Jump if accumulator < 0
        pass

    # BRANCHZERO instruction
    def BRANCHZERO(self, address):
        # Jump if accumulator == 0
        pass

    # HALT instruction
    def HALT(self):
        # Stop program execution
        pass