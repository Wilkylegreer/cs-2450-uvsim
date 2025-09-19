#memory.py

class Memory:
    def __init__(self):
        self.size = 100

        self.mem = [0] * self.size

    def reset(self):
        self.mem = [0] * self.size

    def __str__(self):
        lines = []
        for index, x in enumerate(self.mem):
            if x != 0:
                lines.append(f"{index} - {x}")
        return "Loaded Memory\n" + "\n".join(lines) if lines else "Memory is empty"
        
    def get_value(self, address):
        return self.mem[address]
    
    def set_value(self, address, value):
        self.mem[address] = value