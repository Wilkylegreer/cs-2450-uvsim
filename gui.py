import tkinter as tk
from tkinter import ttk, filedialog
import sys

class UvsimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UVSim Simulator")
        self.root.geometry("900x600")
        self.root.configure(padx=10, pady=10)

        self.create_widgets()

    def reset(self):       
        self.cpu.reset()
        self.memory.reset()
        self.load_file()
        self.log_message("Program reset.")

    def load_file(self):
        try:
            loaded = self.loader.load_from_file(self.selected_file)
            if loaded:
                self.log_message("Program loaded successfully.")
                self.log_message(str(self.memory))
            else:
                self.log_message("Error: Invalid program file.")
        except Exception as e:
            self.log_message(f"Error loading file: {e}")

    def create_widgets(self):
        # Menu Bar
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=lambda: None)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: None)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

        # Main layout frames
        main_frame = ttk.Frame(self.root, padding=(5, 5, 5, 5))
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left frame for controls and output
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        lower_frame = ttk.Frame(main_frame)
        lower_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Program controls
        controls_frame = ttk.LabelFrame(left_frame, text="Program Controls", padding=(10, 10))
        controls_frame.pack(fill=tk.X, pady=(0, 10))

        btn_run = ttk.Button(controls_frame, text="Run", command=lambda: self.cpu.run()) # Starts the program from the beginning of the input file.
        btn_step = ttk.Button(controls_frame, text="Step", command=lambda: None) # Steps through the program
        btn_reset = ttk.Button(controls_frame, text="Reset", command=lambda: self.reset()) # Could reset the accumulator to its default value and reset the pointer looking at the input file to run through the program from the beginning of the file.
        btn_exit = ttk.Button(controls_frame, text="Exit", command=sys.exit) # Closes the window and stops the program

        btn_run.grid(row=0, column=1, padx=5, pady=5)
        btn_step.grid(row=0, column=2, padx=5, pady=5)
        btn_reset.grid(row=0, column=3, padx=5, pady=5)
        btn_exit.grid(row=0, column=4, padx=5, pady=5)

        # Output/log display
        output_frame = ttk.LabelFrame(left_frame, text="Output / Log", padding=(10, 10))
        output_frame.pack(fill=tk.BOTH, expand=True)
        self.output_text = tk.Text(output_frame, height=20, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Right frame for memory/registers
        right_frame = ttk.LabelFrame(main_frame, text="Memory / Registers", padding=(10, 10))
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # Text input box
        text_input_frame = ttk.LabelFrame(left_frame, text="Input Text Here:", padding=(10, 10))
        text_input_frame.pack(fill=tk.BOTH, expand=True)
        self.input_entry = tk.Text(text_input_frame, height=1, wrap=tk.WORD, state=tk.NORMAL)
        self.input_entry.pack(fill=tk.BOTH, expand=True)

        columns = ("Address", "Value")
        self.memory_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=25)
        for col in columns:
            self.memory_tree.heading(col, text=col)
            self.memory_tree.column(col, width=80, anchor=tk.CENTER)
        self.memory_tree.pack(fill=tk.BOTH, expand=True)
        # Placeholder: Insert sample data
        for i in range(10):
            self.memory_tree.insert("", tk.END, values=(f"{i:03}", "0000"))

        submit_frame = ttk.Frame(self.root)
        submit_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=10)
        btn_submit = ttk.Button(submit_frame, text="Submit", command=sys.exit)
        btn_submit.pack(side=tk.LEFT)

    def open_file(self):
        filepath = filedialog.askopenfilename(
            title="Open Program File",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if filepath:
            self.selected_file = filepath
            self.log_message(f"Opened file: {filepath}")

            # Simple program loading
            from memory import Memory
            from cpu import CPU
            from control_instructions import ControlInstructions
            from math_instructions import MathInstructions
            from program_loader import ProgramLoader

            self.memory = Memory()
            self.cpu = CPU(self.memory, self)
            conInstruct = ControlInstructions(self.memory, self.cpu, self)
            mathInstruct = MathInstructions(self.memory)
            self.cpu.set_instructions(conInstruct, mathInstruct)
            self.loader = ProgramLoader(self.memory, self)

            self.load_file()

    def log_message(self, message: str):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)                  # auto scroller :)
        self.output_text.configure(state=tk.DISABLED)


# def main():
#     root = tk.Tk()
#     app = UvsimGUI(root)
#     root.mainloop()
    


# if __name__ == "__main__":
#     main()