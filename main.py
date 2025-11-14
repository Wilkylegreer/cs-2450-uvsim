import tkinter as tk
from gui import UvsimGUI

def main():
    #GUI Setup 
    root = tk.Tk()
    app = UvsimGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

#test