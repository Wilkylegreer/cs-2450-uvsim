#math_instructions.py

class MathInstructions():
    def __init__(self, memory):
        self.memory = memory
      
    def add():
        self.cpu.accumulator += self.memory.mem[address]

    def subtract():
      self.cpu.accumulator -= self.memory.mem[address]

    def divide():
      if self.memory[address] == 0:
        print("can't divide by zero")
        break
      self.cpu.accumulator //= self.memory.mem[address]
  
    def multiply():
      self.cpu.accumulator *= self.memory.mem[address]


