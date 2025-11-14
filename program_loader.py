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
        if len(lines) > self.memory.size:
            self.gui.log_message("Out of bounds")
            return False
        for x in lines:
            stripped_line = x.lstrip("+-")
            if (len(stripped_line) not in (4, 6)) or not stripped_line.isdigit():
                self.gui.log_message(f"Invalid line: {x}")
                return False
        return True

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                all_lines = file.readlines()

            all_lines = self.lineCleanUp(all_lines)

            if not all_lines:
                self.gui.log_message("File is empty or invalid.")
                return False

            if self.lineValidation(all_lines):
                for index, line in enumerate(all_lines):
                    self.memory.set_value(index, line)
                self.gui.log_message("Program loaded successfully.")
                return True
            else:
                # Load anyway (but mark invalid)
                for index, line in enumerate(all_lines):
                    self.memory.set_value(index, line)
                self.gui.log_message("Program loaded with validation errors.")
                return True

        except Exception as e:
            self.gui.log_message(f"Error loading program file: {e}")
            return False
