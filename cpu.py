#cpu.py

class CPU:
    def __init__(self, memory):
        self.controlInstruct = None
        self.mathInstruct = None
        self.memory = memory
        self.accumulator = 0
        self.programCounter = 0
        self.instructionReg = 0
        self.done = False

    def set_instructions(self, conInstruct, mathInstruct):
        self.controlInstruct = conInstruct
        self.mathInstruct = mathInstruct

    def fetch(self):
        instruction = self.memory.read(self.instructionReg)
        self.instructionReg += 1
        return instruction
    
    def decode_execute(self, instruction):
        opcode = instruction // 100
        memoryLoc = instruction % 100

        if opcode in [30, 31, 32, 33]:
            self.accumulator = self.mathInstruct.execute(opcode, self.accumulator, memoryLoc, self.memory) # Implement this in math_instructions
        elif opcode in [10, 11, 20, 21, 40, 41, 42, 43]:
            self.controlInstruct.execute(opcode, memoryLoc, self)
        else:
            print("Validation error")

    def run(self):
        while not self.done:
            instruction = self.fetch()
            self.decode_execute(instruction)