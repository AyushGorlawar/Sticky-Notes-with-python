import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Success", "Note saved successfully!")

def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", file.read())

def clear_note():
    text_area.delete("1.0", tk.END)

def new_note():
    global note_counter
    note_counter += 1
    note_name = f"note_{note_counter}.txt"
    with open(note_name, "w", encoding="utf-8") as file:
        file.write("")
    text_area.delete("1.0", tk.END)
    messagebox.showinfo("New Note", f"New note created: {note_name}")
    

note_counter = 0
for file in os.listdir():
    if file.startswith("note_") and file.endswith(".txt"):
        note_counter += 1

# GUI Setup
root = tk.Tk()
root.title("Sticky Note")
root.geometry("500x500")
root.configure(bg="#f5f5f5")

style = ttk.Style()
style.configure("Black.TButton", font=("Arial", 10), padding=5, foreground="black", background="black")

text_area = tk.Text(root, wrap="word", font=("Arial", 12), bg="white", fg="black", padx=10, pady=10, relief=tk.FLAT)
text_area.pack(expand=True, fill="both", padx=10, pady=10)

button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=5)

new_label = tk.Label(button_frame, text="New", bg="#f5f5f5", fg="black", font=("Arial", 10))
new_label.pack(side="left")
new_button = ttk.Button(button_frame, text="+", command=new_note, style="Black.TButton")
new_button.pack(side="left", padx=5, pady=5)

save_label = tk.Label(button_frame, text="Save", bg="#f5f5f5", fg="black", font=("Arial", 10))
save_label.pack(side="left")
save_button = ttk.Button(button_frame, text="Save", command=save_note, style="Black.TButton")
save_button.pack(side="left", padx=5, pady=5)

open_label = tk.Label(button_frame, text="Open", bg="#f5f5f5", fg="black", font=("Arial", 10))
open_label.pack(side="left")
open_button = ttk.Button(button_frame, text="Open", command=open_note, style="Black.TButton")
open_button.pack(side="left", padx=5, pady=5)

clear_label = tk.Label(button_frame, text="Clear", bg="#f5f5f5", fg="black", font=("Arial", 10))
clear_label.pack(side="left")
clear_button = ttk.Button(button_frame, text="Clear", command=clear_note, style="Black.TButton")
clear_button.pack(side="left", padx=5, pady=5)

root.mainloop()
