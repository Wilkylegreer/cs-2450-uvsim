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
            return self.ADD(accumulator, memoryLoc)
        elif operation == "SUBTRACT":
            return self.SUBTRACT(accumulator, memoryLoc)
        elif operation == "DIVIDE":
            return self.DIVIDE(accumulator, memoryLoc)
        elif operation == "MULTIPLY":
            return self.MULTIPLY(accumulator, memoryLoc)
    
    def ADD(self, accumulator, memoryLoc):
        accumulator += int(self.memory.mem[memoryLoc])
        return accumulator

    def SUBTRACT(self, accumulator, memoryLoc):
        accumulator -= self.memory.mem[memoryLoc]
        return accumulator

    def DIVIDE(self, accumulator, memoryLoc):
        if self.memory[memoryLoc] == 0:
            #print("can't divide by zero")
            return ValueError("Cannot divide by zero!")
        accumulator //= self.memory.mem[memoryLoc]
        return accumulator
  
    def MULTIPLY(self, accumulator, memoryLoc):
        accumulator *= self.memory.mem[memoryLoc]
        return accumulator