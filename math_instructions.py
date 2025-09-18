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


    def execute(self, opcode, accumulator, memoryLoc, memory):
        operation = self.OPCODE_DICT.get(opcode)

        if not operation:
            raise ValueError(f"Unknown mathematical operation: {opcode}")
        
        if operation == "ADD":
            return self.add(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "SUBTRACT":
            return self.subtract(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "DIVIDE":
            return self.divide(self, opcode, accumulator, memoryLoc, memory)
        elif operation == "MULTIPLY":
            return self.multiply(self, opcode, accumulator, memoryLoc, memory)
        