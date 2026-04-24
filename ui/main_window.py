import tkinter as tk
from tkinter import *

class load_window:
    def __init__(self, addButton_callback, clearButton_callback, remButton_callback):
        print("main_window: Loading window...")
        self.window = tk.Tk()
        self.window.title("ToDoList")
        self.window.geometry("500x250")

        # Frame
        self.frameList = tk.Frame(self.window, borderwidth = 2, relief = "sunken", width = 250, height = 165)
        self.frameList.place(x = 100, y = 40)
        
        # Labels
        self.label1 = tk.Label(self.window, text = "Enter To-Do: ")
        self.label1.place(x = 10, y = 10)
        
        self.label2 = tk.Label(self.window, text = "To-Do's: ")
        self.label2.place(x = 10, y = 40)
        
        self.toDoList = tk.Label(self.window, text = "", wraplength = 235, justify = "left")
        self.toDoList.place(x = 105, y = 45)
        
        # Entry
        self.entry = tk.Entry(self.window)
        self.entry.place(x = 100, y = 10, width = 250)
        
        # Button Add
        self.buttonAdd = tk.Button(self.window, text = "Add to List", command = addButton_callback)
        self.buttonAdd.place(x = 380, y = 10, width = 80, height = 20)
        
        # Button Clear
        self.buttonClear = tk.Button(self.window, text = "Clear List", command = clearButton_callback)
        self.buttonClear.place(x = 100, y = 215, width = 80, height = 20)

        # Remove Buttons
        self.buttons = []
        for i in range(10):
            self.buttonRem = tk.Button(self.window, text = "X", relief = "raised", command = lambda i = i: remButton_callback(i))
            self.buttonRem.place(x = 380, y = 40 + i * 16.5, height = 16.5, width = 16.5)
            self.buttons.append(self.buttonRem)

    def load_ui(self):
        self.window.mainloop()

    def set_toDoList(self, data):
        print("main_window: Setting data...")
        self.toDoList.config(text = data)

    def getText(self):
        print("main_window: Reading entry...")
        entry = self.entry.get()
        self.entry.delete(0, tk.END)
        return entry
    
    def deactivate_buttons(self, numb):
        for i in range(numb, 10):
            self.buttons[i].config(text = "", state = tk.DISABLED, relief = "flat")

    def activate_buttons(self):
        for i in range(10):
            self.buttons[i].config(text = "X", state = tk.ACTIVE, relief = "raised")