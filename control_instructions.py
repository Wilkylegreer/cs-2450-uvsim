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
    def READ(self, address):
        # Return value stored at the address
        pass

    # WRITE instruction
    def WRITE(self, address):
        # Fetch value from memory at 'address'
        value = self.memory.get_value(address)
        # Output value to user
        print_output(value)

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
        self.done = True
        print("Program Finished...")