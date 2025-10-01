# program_loader.py

def lineCleanUp(lines):
    for index, x in enumerate(lines):
        x = x.strip()
        if x.startswith("+") or x.startswith("-"):
            cleaned = x
        else:
            cleaned = "+" + x  # assume positive if no sign given
        lines[index] = cleaned
    return lines

def lineValidation(lines):
    if len(lines) > 100:
        print("Out of bounds")
        return False
    for x in lines:
        stripped_line = x.lstrip("+-")
        if len(stripped_line) != 4 or not stripped_line.isdigit():
            print(f"Invalid line: {x}")
            return False
    return True

class ProgramLoader:
    def __init__(self, memory):
        self.memory = memory

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            allLines = file.readlines()
            allLines = lineCleanUp(allLines)
            if lineValidation(allLines):
                for index, x in enumerate(allLines):
                    self.memory.set_value(index, x)
                print(self.memory)
                return True
            else:
                print("-Error Loading File-")
                return False