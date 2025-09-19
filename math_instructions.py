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
        operation = self.OPCODE_DICT.get(opcode)

        if not operation:
            raise ValueError(f"Unknown mathematical operation: {opcode}")
        
        if operation == "ADD":
            return self.add(self, accumulator, memoryLoc)
        elif operation == "SUBTRACT":
            return self.subtract(self, accumulator, memoryLoc)
        elif operation == "DIVIDE":
            return self.divide(self, accumulator, memoryLoc)
        elif operation == "MULTIPLY":
            return self.multiply(self, accumulator, memoryLoc)
    
    def add(self, accumulator, memoryLoc):
        accumulator += self.memory.mem[memoryLoc]

    def subtract(self, accumulator, memoryLoc):
        accumulator -= self.memory.mem[memoryLoc]

    def divide(self, accumulator, memoryLoc):
        if self.memory[memoryLoc] == 0:
            #print("can't divide by zero")
            return ValueError("Cannot divide by zero!")
        accumulator //= self.memory.mem[memoryLoc]
  
    def multiply(self, accumulator, memoryLoc):
        accumulator *= self.memory.mem[memoryLoc]

        #Very cool