#cpu.py
from time import sleep

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
        instruction = self.memory.mem[self.programCounter]
        self.programCounter += 1
        return instruction
    
    def decode_execute(self, instruction):
        opcode = int(instruction) // 100
        memoryLoc = int(instruction) % 100

        if opcode in [30, 31, 32, 33]:
            self.accumulator = self.mathInstruct.execute(opcode, self.accumulator, memoryLoc)
        elif opcode in [10, 11, 20, 21, 40, 41, 42, 43]:
            self.controlInstruct.execute(opcode, memoryLoc)
        else:
            print(f"Opcode not recognized Opcode: {opcode} + Instruction: {instruction} - CPU")

    def run(self):
        while not self.done:
            sleep(1)
            instruction = self.fetch()
            self.decode_execute(instruction)
            if self.programCounter > 99:
                self.controlInstruct.HALT()