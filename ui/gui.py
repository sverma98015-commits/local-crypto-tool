import tkinter as tk

def run_gui():
    root = tk.Tk()
    root.title("Local Crypto Tool")
    root.geometry("600x400")

    label = tk.Label(root, text="Local Crypto Tool")
    label.pack(pady=20)

    root.mainloop()
