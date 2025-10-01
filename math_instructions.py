#math_instructions.py

class MathInstructions():
    OPCODE_DICT = {
        "30":'ADD',
        "31":'SUBTRACT',
        "32":'DIVIDE',
        "33":'MULTIPLY'
    }

    def __init__(self, memory):
        self.memory = memory

    def execute(self, opcode, accumulator, memoryLoc):
        operation = self.OPCODE_DICT.get(str(opcode))

        if not operation:
            raise ValueError(f"Unknown mathematical operation: {opcode}")
        
        if operation == "ADD":
            return self.ADD(int(accumulator), memoryLoc)
        elif operation == "SUBTRACT":
            return self.SUBTRACT(int(accumulator), memoryLoc)
        elif operation == "DIVIDE":
            return self.DIVIDE(int(accumulator), memoryLoc)
        elif operation == "MULTIPLY":
            return self.MULTIPLY(int(accumulator), memoryLoc)
    
    def ADD(self, accumulator, memoryLoc):
        accumulator += int(self.memory.mem[memoryLoc])
        return accumulator

    def SUBTRACT(self, accumulator, memoryLoc):
        accumulator -= int(self.memory.mem[memoryLoc])
        return accumulator

    def DIVIDE(self, accumulator, memoryLoc):
        divisor = int(self.memory.get_value(memoryLoc))
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        accumulator //= divisor
        return accumulator
  
    def MULTIPLY(self, accumulator, memoryLoc):
        accumulator *= int(self.memory.mem[memoryLoc])
        return accumulator