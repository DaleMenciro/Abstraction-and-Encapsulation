import tkinter as tk
from tkinter import messagebox

class PetGUI:
    def __init__(self, master, pet):
        self.master = master
        self.pet = pet

        self.master.title("Pet GUI")
        self.master.geometry("300x200")
        self.master.config(bg="#f0f0f0")
