#memory.py
#test

class Memory:
    def __init__(self):
        self.size = 100
        self.accumulator = 0

        self.mem = [0] * self.size
        
    def get_value(self, address):
        refined_address = address.split("")
        if refined_address[0] == 0:
            return self.mem[refined_address[1]]
        else:
            return self.mem[address]
    
    def set_value(self, address, value):
        self.mem[address] = value
        print("Value set...\n")