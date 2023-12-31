from tkinter import *
import customtkinter
import openai
import os
import pickle

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

def speak():
    if chat_entry.get():
         #define file name
         filename = "api_key"
         try:
             if os.path.isfile(filename):
                 input_file = open(filename, 'rb')
                 #load the data
                 file_content = pickle.load(input_file)

                 #Query ChatGPT
                 #define our api key to chatGPT
                 openai.api_key = file_content

                 #create an instance
                 openai.Model.list()

                 response = openai.Completion.create(
                        model = "text-davinci-003",
                        prompt = chat_entry.get(),
                        temperature = 0,
                        max_tokens = 60,
                        top_p = 1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0
                 )

                 my_text.insert(END, response["choices"][0]["text"])
                 my_text.insert(END, '\n\n')

             else:
                 input_file = open(filename, 'wb')
                 input_file.close()
                 my_text.insert(END, "Please insert your API Key to talk with ChatGPT!")
         except Exception as e:
             my_text.insert(END, f"ERROR {e}")
    else:
        my_text.insert(END, "Type something, you forgot to write your question")

def clear():
    my_text.delete(1.0, END)
    chat_entry.delete(0, END)

def key():
    root.geometry('600x650')
    api_frame.pack(pady=30)
    #define file name
    filename = "api_key"
    try:
        if os.path.isfile(filename):
            input_file = open(filename, 'rb')
            #load the data
            file_content = pickle.load(input_file)
            api_entry.insert(END, file_content)
        else:
            input_file = open(filename, 'wb')
            input_file.close()
    except Exception as e:
        my_text.insert(END, "ERROR ")

def save_key():
    try:
        #define our file name
        filename = "api_key"
        output_file = open(filename, 'wb')

        pickle.dump(api_entry.get(), output_file)

        api_entry.delete(0, END)

        api_frame.pack_forget()
        root.geometry("600x500")
    except Exception as e:
        my_text.insert(END, "ERROR ")

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("600x500")

text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)


my_text = Text(text_frame, bg="#343638", width=65, fg="#d6d6d6", relief='flat', wrap=WORD)
my_text.grid(row=0, column=0)

#scroll bar
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)

text_scroll.grid(row=0, column=1, sticky='ns')

my_text.configure(yscrollcommand=text_scroll.set)


#entry widget
chat_entry = customtkinter.CTkEntry(root, placeholder_text="Ask chat whatever you want", width=535, height=50, border_width=1)
chat_entry.pack(pady=10)


# create button frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

#cretae buttons

submit_button = customtkinter.CTkButton(button_frame, text="speak to chat GPT", command=speak)
submit_button.grid(row=0, column=0, padx=25)

clear_button = customtkinter.CTkButton(button_frame, text="clear", command=clear)
clear_button.grid(row=0, column=1, padx=35)

api_button = customtkinter.CTkButton(button_frame, text="update api key", command=key)
api_button.grid(row=0, column=2, padx=25)

# Add API Key CTkFrame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

api_entry = customtkinter.CTkEntry(api_frame, placeholder_text="Enter your api key", width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

api_save_button = customtkinter.CTkButton(api_frame, text="save key", command=save_key)
api_save_button.grid(row=0, column=1, padx=10)

root.mainloop()