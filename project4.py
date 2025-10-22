# gtk_diwa_gui.py
import tkinter as tk

root = tk.Tk()
root.title("Happy Diwali")
root.geometry("500x250")
root.configure(bg="black")

label = tk.Label(root, text="🪔 wishing you a bright and joyful diwali! 🪔", font=("Helvetica", 36, "bold"), bg="black", fg="gold")
label.pack(expand=True)

# simple glow effect
colors = ["gold", "yellow", "orange", "white"]
idx = 0
def glow():
    global idx
    label.config(fg=colors[idx % len(colors)])
    idx += 1
    root.after(300, glow)

glow()
root.mainloop()
