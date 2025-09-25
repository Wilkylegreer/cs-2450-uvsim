# control_instructions.py

from io_handler import print_output

class ControlInstructions:
    def __init__(self, memory, cpu):
        self.memory = memory
        self.cpu = cpu

    # READ instruction
    def READ(self, address):
        while True:
            word = input("Enter a 4-digit word:\n").strip()
            if word.lstrip("+-").isdigit() and len(word.lstrip("+-")) <= 4:
                self.memory.set_value(address, int(word))
                break
            else:
                print("Invalid input, must be a signed 4-digit number (e.g. +1234 or -0567). Try again.")
        

    # WRITE instruction
    def WRITE(self, address):
        value = self.memory.get_value(address)
        print_output(f"WRITE Output: {value}")

    # LOAD instruction
    def LOAD(self, address):
        self.cpu.accumulator = self.memory.mem[address]
        print(f"Accumulator set to {self.cpu.accumulator}")

    # STORE instruction
    def STORE(self, address):
        self.memory.set_value(address, self.cpu.accumulator)
        print("\n\n\nNewly")
        print(self.memory)

    # BRANCH instruction
    def BRANCH(self, address):
        self.cpu.programCounter = (int(address))
        self.cpu.instructionReg = self.memory.mem[int(address)]

    # BRANCHNEG instruction
    def BRANCHNEG(self, address):
        if self.cpu.accumulator < 0:
            self.cpu.programCounter = (int(address))
            self.cpu.instructionReg = self.memory.mem[address]
        else:
            print("Not negative to branch")

    # BRANCHZERO instruction
    def BRANCHZERO(self, address):
        if self.cpu.accumulator == 0:
            self.cpu.programCounter = (int(address))
            self.cpu.instructionReg = self.memory.mem[address]
        else:
            print("Not zero to branch")

    # HALT instruction
    def HALT(self):
        self.cpu.done = True
        print("HALT")

    OPCODE_DICT = {
        "10":'READ',
        "11":'WRITE',
        "20":'LOAD',
        "21":'STORE',
        "40":'BRANCH',
        "41":'BRANCHNEG',
        "42":'BRANCHZERO',
        "43":'HALT'
    }

    def execute(self, opcode, memoryLoc):
        operation = self.OPCODE_DICT.get(str(opcode))

        if not operation:
            raise ValueError(f"Unknown control operation: {opcode}")
        
        if operation == "READ":
            self.READ(memoryLoc)
        elif operation == "WRITE":
            self.WRITE(memoryLoc)
        elif operation == "LOAD":
            self.LOAD(memoryLoc)
        elif operation == "STORE":
            self.STORE(memoryLoc)
        elif operation == "BRANCH":
            self.BRANCH(memoryLoc)
        elif operation == "BRANCHNEG":
            self.BRANCHNEG(memoryLoc)
        elif operation == "BRANCHZERO":
            self.BRANCHZERO(memoryLoc)
        elif operation == "HALT":
            self.HALT()
