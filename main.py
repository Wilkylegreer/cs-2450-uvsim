import tkinter as tk
from gui import UvsimGUI

def main():
    #GUI Setup 
    root = tk.Tk()
    app = UvsimGUI(root)
    root.mainloop()

    # # Initializations
    # memory = Memory()
    # cpu = CPU(memory)

    # conInstruct = ControlInstructions(memory, cpu)
    # mathInstruct = MathInstructions(memory)

    # cpu.set_instructions(conInstruct, mathInstruct)

    # proLoader = ProgramLoader(memory)

    # app.program_loaded = False
    # app.log_message("Test1")
    # if hasattr(app, "selected_file"):
    #     try:
    #         app.program_loaded = proLoader.load_from_file(app.selected_file)
    #         if not app.program_loaded:
    #             print(f"Error loading file '{app.selected_file}': Invalid program")
    #     except Exception as e:
    #         print(f"Error loading file '{app.selected_file}': {e}")

    # # Start if loaded right
    # if app.program_loaded:
    #     cpu.run()

    # print(".")


if __name__ == "__main__":
    main()