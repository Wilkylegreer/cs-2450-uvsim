#six_digit_handler.py

from memory import Memory
from cpu import CPU
from control_instructions import ControlInstructions
from math_instructions import MathInstructions

# ---------------- MEMORY ----------------
class Memory6(Memory):
    def __init__(self):
        super().__init__()
        self.size = 250
        self.mem = ["+000000"] * self.size

    def reset(self):
        self.mem = ["+000000"] * self.size

    def set_value(self, address, value):
        #Force all stored values to be signed 6-digit strings.
        try:
            val = int(value)
            sign = "+" if val >= 0 else "-"
            self.mem[address] = f"{sign}{abs(val):06d}"
        except Exception:
            s = str(value).strip()
            if not s.startswith(("+", "-")):
                s = "+" + s
            digits = s.lstrip("+-")
            if digits.isdigit() and len(digits) <= 6:
                self.mem[address] = f"{s[0]}{digits.zfill(6)}"
            else:
                self.mem[address] = "+000000"


# ---------------- CPU ----------------
class CPU6(CPU):
    def decode_execute(self, instruction):
        try:
            numeric = int(str(instruction).lstrip("+"))
        except Exception:
            self.gui.log_message(f"Invalid instruction format: {instruction}")
            return

        opcode = (numeric // 1000) % 100
        memoryLoc = numeric % 100

        if opcode in [30, 31, 32, 33]:
            self.accumulator = self.mathInstruct.execute(opcode, self.accumulator, memoryLoc)
        elif opcode in [10, 11, 20, 21, 40, 41, 42, 43]:
            self.controlInstruct.execute(opcode, memoryLoc)
        else:
            self.gui.log_message(f"Skipping invalid instruction: {instruction}")


# ---------------- CONTROL INSTRUCTIONS ----------------
class ControlInstructions6(ControlInstructions):
    def execute(self, opcode, memoryLoc):
        operation = self.OPCODE_DICT.get(str(opcode))
        if not operation:
            raise ValueError(f"Unknown control operation: {opcode}")

        if operation == "READ":
            self.temp_address = memoryLoc
            self.gui.log_message("Submit a 6-digit number...")
            self.cpu.done = True
        else:
            super().execute(opcode, memoryLoc)


# ---------------- MATH INSTRUCTIONS ----------------
class MathInstructions6(MathInstructions):

    def truncate6(self, value):
        if value > 0:
            return value % 1000000
        elif value < 0:
            return -(abs(value) % 1000000)
        return value

    def ADD(self, accumulator, memoryLoc):
        accumulator += int(self.memory.mem[memoryLoc])
        return self.truncate6(accumulator)

    def SUBTRACT(self, accumulator, memoryLoc):
        accumulator -= int(self.memory.mem[memoryLoc])
        return self.truncate6(accumulator)

    def DIVIDE(self, accumulator, memoryLoc):
        divisor = int(self.memory.get_value(memoryLoc))
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        accumulator //= divisor
        return self.truncate6(accumulator)

    def MULTIPLY(self, accumulator, memoryLoc):
        accumulator *= int(self.memory.mem[memoryLoc])
        return self.truncate6(accumulator)
