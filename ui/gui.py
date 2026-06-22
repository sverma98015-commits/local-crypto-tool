import tkinter as tk
from tkinter import messagebox

from crypto.encryptor import encrypt_text
from crypto.decryptor import decrypt_text


def run_gui():

    root = tk.Tk()
    root.title("Local Crypto Tool")
    root.geometry("800x600")

    tk.Label(root, text="Text").pack()

    text_box = tk.Text(root, height=10)
    text_box.pack(fill="x")

    tk.Label(root, text="Password").pack()

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(fill="x")

    tk.Label(root, text="Result").pack()

    result_box = tk.Text(root, height=10)
    result_box.pack(fill="x")

    def encrypt():

        try:

            result_box.delete("1.0", tk.END)

            result = encrypt_text(
                text_box.get("1.0", tk.END),
                password_entry.get()
            )

            result_box.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt():

        try:

            result_box.delete("1.0", tk.END)

            result = decrypt_text(
                text_box.get("1.0", tk.END).strip(),
                password_entry.get()
            )

            result_box.insert(tk.END, result)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(
        root,
        text="Encrypt",
        command=encrypt
    ).pack(pady=10)

    tk.Button(
        root,
        text="Decrypt",
        command=decrypt
    ).pack(pady=10)

    root.mainloop()
