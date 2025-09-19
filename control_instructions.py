# control_instructions.py

from io_handler import get_input, print_output

class ControlInstructions:
    def __init__(self, memory, cpu):
        self.memory = memory
        self.cpu = cpu

    # READ instruction
    def READ(self, address):
        word = input("Enter a 4-digit word:\n")
        if len(word) < 4 or isinstance(int(word), int):
            self.READ(address)
        else:
            self.memory.set_value(address, word)
            print(self.memory)
            print("Read/Store complete...\n")
        

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
        self.cpu.programCounter = int(address)
        self.cpu.instructionReg = self.memory.mem[address]

    # BRANCHNEG instruction
    def BRANCHNEG(self, address):
        if self.cpu.accumulator < 0:
            self.cpu.programCounter = int(address)
            self.cpu.instructionReg = self.memory.mem[address]
        else:
            print("Not negative to branch")

    # BRANCHZERO instruction
    def BRANCHZERO(self, address):
        if self.cpu.accumulator == 0:
            self.cpu.programCounter = int(address)
            self.cpu.instructionReg = self.memory.mem[address]
        else:
            print("Not zero to branch")

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

    def EXECUTE(self, opcode, accumulator, memoryLoc, memory):
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
