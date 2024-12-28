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

        self.style = ttk.Style()
        self.style.theme_use('winnative')
    def display(self):
        menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="LICENSE", command=self.menu_command)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="QUIT", command=self.root.quit)
        menubar.add_cascade(label="FILE", menu=self.filemenu)
        self.root.config(menu=menubar)

        ttk.Label(text="Easily convert wav files to midi files",font=("",25)).pack(pady=10)

        self.style.configure("My.TButton",font=("",30))
        ttk.Button(self.root,text="File Selection",style="My.TButton",command=lambda:self.selection(convert)).pack(pady=50)

        self.style.configure("CONVERT.TButton",font=("",20))
        convert = ttk.Button(self.root,text="CONVERT",style="CONVERT.TButton",state="disable",command=lambda:self.stconvert(convert))
        convert.pack(pady=20)
    def menu_command(self):
        print("menu_command")
    def selection(self,convert):
        fTyp = [("wav-file", ".wav")]
        self.file_name = filedialog.askopenfilename(filetypes=fTyp)
        convert.config(state="normal")
    def stconvert(self,convert):
        convert.config(state="disable")

        
def main():
    root = tk.Tk()
    display = Display(root)
    display.display()
    root.mainloop()

if __name__ == "__main__":
    main()