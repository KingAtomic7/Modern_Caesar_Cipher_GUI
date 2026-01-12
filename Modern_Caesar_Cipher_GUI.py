import customtkinter as ctk
from tkinter import messagebox


def caesar_cipher(text, shift, mode):
    result = ""
    shift = shift % 26

    if mode == "Decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char

    return result


def process_text():
    try:
        message = input_text.get("1.0", "end").strip()
        shift = int(shift_entry.get())
        mode = mode_option.get()

        if not message:
            messagebox.showwarning("Warning", "Please enter a message")
            return

        result = caesar_cipher(message, shift, mode)
        output_text.delete("1.0", "end")
        output_text.insert("end", result)

    except ValueError:
        messagebox.showerror("Error", "Shift must be a number")


# Appearance
ctk.set_appearance_mode("Dark")      # "Light" or "Dark"
ctk.set_default_color_theme("blue")  # "green", "dark-blue"

# Main window
app = ctk.CTk()
app.title("Caesar Cipher")
app.geometry("700x700")
app.resizable(False, False)

# Title
title = ctk.CTkLabel(
    app, text="Caesar Cipher",
    font=ctk.CTkFont(size=24, weight="bold")
)
title.pack(pady=20)

# Input
ctk.CTkLabel(app, text="Enter Message").pack()
input_text = ctk.CTkTextbox(app, height=100, width=420)
input_text.pack(pady=10)

# Shift
ctk.CTkLabel(app, text="Shift Value").pack()
shift_entry = ctk.CTkEntry(app, width=120, justify="center")
shift_entry.pack(pady=10)

# Mode
ctk.CTkLabel(app, text="Mode").pack()
mode_option = ctk.CTkOptionMenu(
    app,
    values=["Encrypt", "Decrypt"]
)
mode_option.pack(pady=10)

# Button
process_btn = ctk.CTkButton(
    app,
    text="Process",
    height=40,
    font=ctk.CTkFont(size=16),
    command=process_text
)
process_btn.pack(pady=20)

# Output
ctk.CTkLabel(app, text="Result").pack()
output_text = ctk.CTkTextbox(app, height=100, width=420)
output_text.pack(pady=10)

# Run
app.mainloop()
