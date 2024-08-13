import tkinter as tk
from tkinter import messagebox
import os
import ctypes

def empty_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
        messagebox.showinfo("Success", "Recycle Bin emptied successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to empty Recycle Bin: {e}")

def open_c_properties():
    try:
        os.system("explorer shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open C: properties: {e}")

# Set up the main application window
root = tk.Tk()
root.title("Clean up tools")
root.geometry("300x150")

# First row: App name
app_name = tk.Label(root, text="Clean up tools", font=("Helvetica", 16))
app_name.pack(pady=10)

# Second row: Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_empty_recycle_bin = tk.Button(button_frame, text="Empty Recycle Bin", command=empty_recycle_bin)
btn_empty_recycle_bin.pack(side="left", padx=5)

btn_open_c = tk.Button(button_frame, text="C:", command=open_c_properties)
btn_open_c.pack(side="left", padx=5)

# Start the application
root.mainloop()
