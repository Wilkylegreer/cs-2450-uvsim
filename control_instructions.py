# control_instructions.py

from memory import Memory
from io_handler import get_input, print_output

# ControlInstructions class
class ControlInstructions:
    def __init__(self, memory, cpu):
        """
        memory: Memory object
        io_handler: object/module for I/O operations
        cpu: CPU object (to access accumulator and instruction pointer)
        """
        self.memory = memory
        self.cpu = cpu
        self.done = False

    # READ instruction
    # Like STORE but from raw input
    def READ(self, address):
        # Get user input
        word = input("Enter a 4-digit word:\n")
        

    # WRITE instruction
    def WRITE(self, address):
        value = self.memory.get_value(address)
        print_output(value)

    # LOAD instruction
    def LOAD(self, address):
        self.memory.accumulator = self.memory.mem[address]

    # STORE instruction
    def STORE(self, address):
        self.memory.set_value(address, self.memory.accumulator)
        print("Storing complete...\n")

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
        self.done = True
        print("Program Finished...\n")