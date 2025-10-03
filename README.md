# UVSim - BasicML Virtual Machine

## 📖 Description
UVSim is a program that lets you run and watch simple programs written in a very basic computer language. It helps you see step by step how a tiny "toy computer" works by showing what happens inside as the program runs.

---

## ⚙️ Prerequisites
- Python **3.8+**
- Command-line access

---

## 🚀 How to Run
1. Open a terminal and navigate to the project folder.  
2. Run the simulator by typing:  
   ```bash
   python main.py
   ```  
3. ON MAC: When opened, click "File" at left side of your menu bar near the Apple logo, then click "Open". Find the program you want to run (for example: `Test6.txt`) and click "Open".  
   ON WINDOWS When opened, click "File" at the top left corder of the application, then click "Open". Find the program you want to run (for example: `Test6.txt`) and click "Open".
   Please note that if you select an invalid file then it will tell you in the Output/Log box.
4. Press the "Run" button to run the program with the file that you selected. As the program runs, you will see messages in the terminal showing what the simulator is doing. Sometimes, the program may ask you to type in numbers as input. Just follow the prompts and enter the numbers one at a time.  

---

## 💡 What You'll See
While the program is running, you will see messages that tell you what the simulator is doing, such as loading instructions, reading input, or displaying output. You might also see updates showing the contents of memory or the current value inside the "accumulator" (a special place where calculations happen). This is normal and helps you understand how the program works step by step.

Example output might look like this:  
```
Enter an integer: 123
Stored 123 at memory location 10
Accumulator updated to +0123
Program halted successfully.
```

---

## 📥 Input Instructions
Sometimes the program will ask you to enter numbers. When this happens:  
- Type a plain number (positive or negative) and press Enter.  
- Enter one number at a time as requested.  
- For example, if asked for input, you might type:  
  ```
  25
  -10
  0
  ```  
- Just follow the prompts and enter the numbers as they appear in your program instructions.

---

## 🖥 Instruction Set (Reference)
This section is mainly for reference. You don’t need to understand this table to use the program.

| Code | Mnemonic    | Description |
|------|-------------|-------------|
| 10   | READ        | Read a word from keyboard into memory |
| 11   | WRITE       | Write a word from memory to screen |
| 20   | LOAD        | Load a word from memory into accumulator |
| 21   | STORE       | Store accumulator into memory |
| 30   | ADD         | Add memory value to accumulator |
| 31   | SUBTRACT    | Subtract memory value from accumulator |
| 32   | DIVIDE      | Divide accumulator by memory value |
| 33   | MULTIPLY    | Multiply accumulator by memory value |
| 40   | BRANCH      | Jump to a memory location |
| 41   | BRANCHNEG   | Jump if accumulator is negative |
| 42   | BRANCHZERO  | Jump if accumulator is zero |
| 43   | HALT        | Stop the program |

➡️ **Instruction format:**  
- First 2 digits → Operation code  
- Last 2 digits → Memory address operand

## 📝 Example:
- 2007 → LOAD(20) from memory location(07)

---

## 👤 Authors
- Developed by Darby Thomas, Ethan Rasmussen, and Kyle Greer