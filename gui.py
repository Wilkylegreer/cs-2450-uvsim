import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sys

class UvsimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UVSim Simulator")
        self.root.geometry("900x600")
        self.root.configure(padx=10, pady=10)
        self.current_entry = None

        self.create_widgets()

    def reset(self):       
        self.cpu.reset()
        self.memory.reset()
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.configure(state=tk.DISABLED)
        self.log_message("---PROGRAM RESET---")
        self.load_file()

    def check_run(self):
        can_run = False
        for x in self.memory.mem:
            if len(str(x).lstrip("+-")) < 4 or not str(x).lstrip("+-").isdigit():
                if x == 0:
                    can_run = True
                    break
                can_run = False
                self.log_message(f"{x} : One or more errors in memory. Fix before running.")
                break
            else:
                can_run = True
        if can_run:
            self.cpu.run()

    def resume_cpu(self):
        self.cpu.done = False
        self.load_mem()
        self.cpu.run()

    def submit_input(self):
        content = self.input_entry.get("1.0", tk.END).strip()
        if content.lstrip("+-").isdigit() and len(content.lstrip("+-")) <= 4:
            self.conInstruct.READ(self.conInstruct.temp_address)
            self.log_message(f"Submitted input: {content}")
            self.resume_cpu()
        else:
            self.log_message("Invalid input, must be a signed 4-digit number (e.g. +1234 or -0567). Try again.")
        self.input_entry.delete("1.0", tk.END)
        self.btn_submit.configure(state=tk.DISABLED)

    def load_file(self):
        try:
            loaded = self.loader.load_from_file(self.selected_file)
            if loaded:
                self.load_mem()
        except Exception as e:
            self.log_message(f"Error loading file: {e}")

    def edit_memory_cell(self, event):
        if hasattr(self, "current_entry") and self.current_entry is not None:
            self.current_entry.destroy()
            self.current_entry = None

        selected_item = self.memory_tree.identify_row(event.y)
        selected_column = self.memory_tree.identify_column(event.x)

        if selected_item and selected_column == "#2":
            x, y, width, height = self.memory_tree.bbox(selected_item, selected_column)
            old_value = self.memory_tree.item(selected_item, "values")[1]

            # Create an entry widget over the cell
            entry = ttk.Entry(self.memory_tree)
            entry.place(x = x, y = y - 2, width = width + 4, height = height + 4)
            entry.insert(0, old_value)
            entry.focus()
            entry.selection_range(0, tk.END)

            self.current_entry = entry

            def save_edit(event=None):
                new_value = entry.get().strip()
                try:
                    # Basic validation: must be signed integer up to 4 digits
                    if new_value.lstrip("+-").isdigit() and len(new_value.lstrip("+-")) <= 4:
                        # Update tree
                        address = int(self.memory_tree.item(selected_item, "values")[0])
                        self.memory_tree.item(selected_item, values=(f"{address:02}", new_value))
                        # Update actual memory
                        self.memory.set_value(address, new_value)
                        self.log_message(f"Memory[{address}] updated to {new_value}")
                    else:
                        self.log_message("Invalid input. Must be a signed 4-digit number.")
                except Exception as e:
                    self.log_message(f"Error updating memory: {e}")
                finally:
                    entry.destroy()
                    self.current_entry = None

            entry.bind("<Return>", save_edit)
            entry.bind("<FocusOut>", lambda e: (entry.destroy(), setattr(self, "current_entry", None)))

    def add_memory_cell(self):
        selected_item = self.memory_tree.selection()
        if selected_item:
            selected_item = selected_item[0]
            address = int(self.memory_tree.item(selected_item, "values")[0])
            # Insert new memory cell after the selected address
            insert_index = address + 1
            self.memory.mem.insert(insert_index, "+0000")
            self.memory.mem.pop()
            # Clear and reload tree to update addresses
            self.load_mem()
            self.log_message(f"Added new memory cell at address {insert_index}")
        else:
            new_index = self.memory.add_value("+0000")
            self.memory_tree.insert("", tk.END, values=(f"{new_index:02}", "+0000"))
            self.log_message(f"Added new memory cell at address {new_index}")

    def remove_memory_cell(self):
        selected_item = self.memory_tree.selection()
        if not selected_item:
            self.log_message("No memory cell selected to remove.")
            return
        address = int(self.memory_tree.item(selected_item, "values")[0])
        self.memory_tree.delete(selected_item)
        if address < len(self.memory.mem):
            self.memory.mem[address] = 0
        self.log_message(f"Removed memory cell at address {address}")

    def load_mem(self):
        for item in self.memory_tree.get_children():
            self.memory_tree.delete(item)
        for index, i in enumerate(self.memory.mem):
            if i != 0:
                self.memory_tree.insert("", tk.END, values=(f"{index:02}", f"{i}"))

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
            if self.selected_file and self.selected_file.lower().endswith(".txt"):
                self.btn_run.configure(state=tk.NORMAL)
                # self.btn_step.configure(state=tk.NORMAL, style="Enabled.TButton")
                self.btn_reset.configure(state=tk.NORMAL)
            # else:
            #     self.log_message("Invalid file type. Please select a .txt file.")
            #     return

            self.memory = Memory()
            self.cpu = CPU(self.memory, self)
            self.conInstruct = ControlInstructions(self.memory, self.cpu, self)
            self.mathInstruct = MathInstructions(self.memory)
            self.cpu.set_instructions(self.conInstruct, self.mathInstruct)
            self.loader = ProgramLoader(self.memory, self)

            self.load_file()
            self.load_mem()


    def create_widgets(self):
        # Button colors
        style = ttk.Style()
        style.configure("Enabled.TButton", foreground="white")  # Enabled state
        style.configure("Disabled.TButton", foreground="gray")  # Disabled state

        # Menu Bar
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
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

        self.btn_run = ttk.Button(controls_frame, text="Run", command=lambda: self.check_run(), state=tk.DISABLED) # Starts the program from the beginning of the input file.
        # self.btn_step = ttk.Button(controls_frame, text="Step", command=lambda: None, style="Disabled.TButton", state=tk.DISABLED) # Steps through the program
        self.btn_reset = ttk.Button(controls_frame, text="Reset", command=lambda: self.reset(), state=tk.DISABLED) # Could reset the accumulator to its default value and reset the pointer looking at the input file to run through the program from the beginning of the file.
        self.btn_exit = ttk.Button(controls_frame, text="Exit", command=sys.exit) # Closes the window and stops the program

        self.btn_run.grid(row=0, column=1, padx=5, pady=5)
        # self.btn_step.grid(row=0, column=2, padx=5, pady=5)
        self.btn_reset.grid(row=0, column=3, padx=5, pady=5)
        self.btn_exit.grid(row=0, column=4, padx=5, pady=5)
        

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

        # Memory Tree
        columns = ("Address", "Value")
        self.memory_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=25)

        style = ttk.Style()
        style.configure("Treeview", rowheight=20)

        for col in columns:
            self.memory_tree.heading(col, text=col)
            self.memory_tree.column(col, width=80, anchor=tk.CENTER)
        self.memory_tree.pack(fill=tk.BOTH, expand=True)

        # Add "+" and "–" buttons below memory tree
        mem_button_frame = ttk.Frame(right_frame)
        mem_button_frame.pack(fill=tk.X, pady=(5, 0))

        btn_add = ttk.Button(mem_button_frame, text="+", width=3, command=self.add_memory_cell)
        btn_add.pack(side=tk.LEFT, padx=5)

        btn_remove = ttk.Button(mem_button_frame, text="–", width=3, command=self.remove_memory_cell)
        btn_remove.pack(side=tk.LEFT)

        submit_frame = ttk.Frame(self.root)
        submit_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=10)
        self.btn_submit = ttk.Button(submit_frame, text="Submit", command=self.submit_input, state=tk.DISABLED)
        self.btn_submit.pack(side=tk.LEFT)

        # Bindings
        self.input_entry.bind("<KeyRelease>", self.on_input_change)
        self.input_entry.bind("<<Modified>>", self.on_input_change)
        self.input_entry.bind("<FocusIn>", self.on_input_change)
        self.input_entry.bind("<FocusOut>", self.on_input_change)
        self.memory_tree.bind("<Double-1>", self.edit_memory_cell)


    def on_input_change(self, event=None):
        content = self.input_entry.get("1.0", tk.END).strip()

        if content:
            self.btn_submit.configure(state=tk.NORMAL)
        else:
            self.btn_submit.configure(state=tk.DISABLED)

        # Reset the modified flag so the <<Modified>> event keeps firing
        if event and hasattr(self.input_entry, "edit_modified"):
            self.input_entry.edit_modified(False)

    def log_message(self, message: str):
        self.output_text.configure(state=tk.NORMAL)
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END)                  # auto scroller :)
        self.output_text.configure(state=tk.DISABLED)

    def save_file(self):
        try:
            # If no file loaded yet, ask user for one
            if not hasattr(self, "selected_file") or not self.selected_file:
                return self.save_file_as()

            # Convert memory contents into plain text lines
            content = "\n".join(str(x) for x in self.memory.mem)

            with open(self.selected_file, "w", encoding="utf-8") as f:
                f.write(content)

            self.log_message(f"Saved file: {self.selected_file}")
            messagebox.showinfo("Saved", f"File saved:\n{self.selected_file}")

        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
            self.log_message(f"Save error: {e}")

    def save_file_as(self):
        try:
            file_path = filedialog.asksaveasfilename(
                title="Save Program As",
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if not file_path:
                self.log_message("Save As cancelled.")
                return

            content = "\n".join(str(x) for x in self.memory.mem)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            self.selected_file = file_path  # update path for future saves
            self.log_message(f"Saved file as: {file_path}")
            messagebox.showinfo("Saved", f"File saved:\n{file_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
            self.log_message(f"Save As error: {e}")


# def main():
#     root = tk.Tk()
#     app = UvsimGUI(root)
#     root.mainloop()
    


# if __name__ == "__main__":
#     main()
