#math_instructions.py

class MathInstructions():
    def __init__(self, memory):
        self.memory = memory
      
    def add(self, accumulator, memory):
        self.cpu.accumulator += self.memory.mem[address]

    def subtract(self, accumulator, memory):
      self.cpu.accumulator -= self.memory.mem[address]

    def divide(self, accumulator, memory):
      if self.memory[address] == 0:
        print("can't divide by zero")
        break
      self.cpu.accumulator //= self.memory.mem[address]
  
    def multiply(self, accumulator, memory):
      self.cpu.accumulator *= self.memory.mem[address]


