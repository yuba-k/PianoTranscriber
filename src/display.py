import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as filedialog
import ctypes
import os

class Display():
    def __init__(self,root):
        self.root = root
        self.root.title("PianoTranscriber")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    def display(self):
        menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="LICENSE", command=self.menu_command)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="QUIT", command=self.root.quit)
        menubar.add_cascade(label="FILE", menu=self.filemenu)
        self.root.config(menu=menubar)

        ttk.Label(text="Easily convert wav files to midi files",font=("",20)).pack()

        ttk.Button(text="File Selection",command=self.selection).pack()
    def menu_command(self):
        print("menu_command")
    def selection(self):
        fTyp = [("wav-file", ".wav")]
        self.file_name = filedialog.askopenfilename(filetypes=fTyp)

        
def main():
    root = tk.Tk()
    display = Display(root)
    display.display()
    root.mainloop()

if __name__ == "__main__":
    main()