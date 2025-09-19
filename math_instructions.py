#math_instructions.py

class MathInstructions:
    def __init__(self, memory):
        self.memory = memory
      
    def add(self, accumulator, memLoc):
        return accumulator + self.memory.mem[memLoc]

    def subtract(self, accumulator, memLoc):
      return accumulator - self.memory.mem[memLoc]

    def divide(self, accumulator, memLoc):
        if self.memory.mem[memLoc] == 0:
            raise ZeroDivisionError("Cannot divide by zero."
      return accumulator // self.memory.mem[memLoc]
  
    def multiply(self, accumulator, memLoc):
      return accumulator * self.memory.mem[memLoc]

    def execute(self, opcode, accumulator, memLoc):
        if opcode == 30: #ADD
            return self.add(accumulator, memLoc)
        elif opcode == 31: #SUBTRACT
            return self.subtract(accumulator, memLoc)
        elif opcode == 32: #DIVIDE
            return self.divide(accumulator, memLoc)
        elif opcode == 33: #MULTIPLY
            return self.multiply(accumulator, memLoc)
        else:
            raise ValueError(f"Unknown operation")
    


