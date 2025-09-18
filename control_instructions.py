# control_instructions.py

from memory import Memory
from io_handler import get_input, print_output

class ControlInstructions:
    def __init__(self, memory, cpu):
        self.memory = memory
        self.cpu = cpu

    # READ instruction
    # Like STORE but from raw input
    def READ(self, address):
        word = input("Enter a 4-digit word:\n")
        # Validate input
        # Repeat if validation fails
        # Store inputed value into memory location
        

    # WRITE instruction
    def WRITE(self, address):
        value = self.memory.get_value(address)
        print_output(value)

    # LOAD instruction
    def LOAD(self, address):
        self.cpu.accumulator = self.memory.mem[address]

    # STORE instruction
    def STORE(self, address):
        self.memory.set_value(address, self.cpu.accumulator)
        print(self.memory)
        print("Storing complete...\n")

    # BRANCH instruction
    def BRANCH(self, address):
        # Jump to memory address
            # Set the program counter (programCounter) to address
            # Set next 'word' to be ran in the instruction register (instructionReg)
        pass

    # BRANCHNEG instruction
    def BRANCHNEG(self, address):
        # Jump if accumulator < 0
            # Check if accumulator < 0
            # If not continue to next instruction
            # Set the program counter (programCounter) to address
            # Set next 'word' to be ran in the instruction register (instructionReg)
        pass

    # BRANCHZERO instruction
    def BRANCHZERO(self, address):
        # Jump if accumulator == 0
            # Check if accumulator == 0
            # If no continue to next instruction
            # Set the program counter (programCounter) to address
            # Set next 'word' to be ran in the instruciton register (instructionReg)
        pass

    # HALT instruction
    def HALT(self):
        self.cpu.done = True
        print("Program Finished...\n")

    OPCODE_DICT = {
        "40":'BRANCH',
        "41":'BRANCHNEG',
        "42":'BRANCHZERO',
        "43":'HALT'
    }

    def execute(self, opcode, accumulator, memoryLoc, memory):
        operation = self.OPCODE_DICT.get(opcode)

        if not operation:
            raise ValueError(f"Unknown control operation: {opcode}")
        
        if operation == "BRANCH":
            return self.BRANCH(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "BRANCHNEG":
            return self.BRANCHNEG(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "BRANCHZERO":
            return self.BRANCHZERO(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "HALT":
            return self.HALT(self, opcode, accumulator, memoryLoc, memory)