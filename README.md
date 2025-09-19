# UVSim - BasicML Virtual Machine

## 📖 Description
UVSim is a simulator for the **BasicML** machine language.  
It is designed to help computer science students learn machine language and computer architecture.  

The simulator includes:
- A **CPU**
- An **accumulator**
- **100 memory locations** (`00`–`99`)

Each word in memory is a signed four-digit decimal number (example: `+1234`, `-5678`).  
Programs are written in BasicML and must be loaded into memory starting at location `00` before execution.

---

## 🖥 Instruction Set

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
---
2007   # LOAD from memory location 07

## ⚙️ Prerequisites
- Python **3.8+**
- Command-line access

---

## 🚀 How to Run
1. Open a terminal and navigate to the project folder.  
2. Run the simulator with a program file:  
   ```bash
   python main.py [example_files/"any example in example files"]