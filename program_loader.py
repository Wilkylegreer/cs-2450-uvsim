# program_loader.py

class ProgramLoader:
    def __init__(self, memory, gui):
        self.memory = memory
        self.gui = gui

    def lineCleanUp(self, lines):
        for index, x in enumerate(lines):
            x = x.strip()
            if x.startswith("+") or x.startswith("-"):
                cleaned = x
            else:
                cleaned = "+" + x  # assume positive if no sign given
            lines[index] = cleaned
        return lines

    def lineValidation(self, lines):
        if len(lines) > 100:
            self.gui.log_message("Out of bounds")
            return False
        for x in lines:
            stripped_line = x.lstrip("+-")
            if (len(stripped_line) not in (4, 6)) or not stripped_line.isdigit():
                self.gui.log_message(f"Invalid line: {x}")
                return False
        return True

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            allLines = file.readlines()
            allLines = self.lineCleanUp(allLines)
            if self.lineValidation(allLines):
                for index, x in enumerate(allLines):
                    self.memory.set_value(index, x)
                self.gui.log_message("Program loaded without errors.")
                return True
            else:
                for index, x in enumerate(allLines):
                    self.memory.set_value(index, x)
                self.gui.log_message("Program loaded with invalid syntax.")
                return True
