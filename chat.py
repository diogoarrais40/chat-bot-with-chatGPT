from tkinter import *
import customtkinter
import openai
import os
import pickle

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("600x600")

text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)


my_text = Text(text_frame, bg="#343638", width=65, fg="#d6d6d6", relief='flat', wrap=WORD)
my_text.grid(row=0, column=0)

root.mainloop()