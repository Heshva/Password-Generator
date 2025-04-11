import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showwarning("Weak password", "Password length should be at least 6.")
            return

        a = string.ascii_letters
        d = string.digits
        s = string.punctuation

        all_chars = a + d + s

        # Guaranteed diversity in the first 3 characters
        p = [
            random.choice(a),
            random.choice(d),
            random.choice(s),
        ]
        p += random.choices(all_chars, k=length - len(p))
        random.shuffle(p)
        password = ''.join(p)

        output_label.config(text=f"🔐 Your password:\n{password}")
    except ValueError:
        messagebox.showerror("Oops!", "Please enter a valid number.")

# 🎨 Tkinter UI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(padx=20, pady=20, bg="#f0f4f8")

title_label = tk.Label(root, text="Random Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f4f8")
title_label.pack(pady=(0, 10))

frame = tk.Frame(root, bg="#f0f4f8")
frame.pack()

length_label = tk.Label(frame, text="Enter password length:", font=("Helvetica", 12), bg="#f0f4f8")
length_label.grid(row=0, column=0, sticky="w")

entry_length = tk.Entry(frame, width=10, font=("Helvetica", 12))
entry_length.grid(row=0, column=1, padx=10)

generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"),
                            bg="#4CAF50", fg="white", command=generate_password)
generate_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Courier", 12), bg="#f0f4f8", wraplength=380, justify="center")
output_label.pack(pady=(10, 0))

root.mainloop()
