import tkinter as tk
import math
import datetime

# --------------------- Theme Config ---------------------
dark_theme = {
    "bg": "#2E2E2E",
    "entry_bg": "#1C1C1C",
    "entry_fg": "#FFFFFF",
    "button_bg": "#4F4F4F",
    "button_fg": "#FFFFFF",
    "active_bg": "#6E6E6E",
    "active_fg": "#FFFFFF",
    "history_bg": "#1a1a1a",
    "history_fg": "#00ffcc"
}

light_theme = {
    "bg": "#f2f2f2",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000",
    "button_bg": "#e6e6e6",
    "button_fg": "#000000",
    "active_bg": "#cccccc",
    "active_fg": "#000000",
    "history_bg": "#ffffff",
    "history_fg": "#0000aa"
}

current_theme = dark_theme

# --------------------- ฟังก์ชัน ---------------------
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            add_to_history(expression + " = " + result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ["sin", "cos", "tan", "log", "sqrt", "exp", "pi"]:
        try:
            value = float(entry.get())
            if text == "sin":
                result = math.sin(math.radians(value))
            elif text == "cos":
                result = math.cos(math.radians(value))
            elif text == "tan":
                result = math.tan(math.radians(value))
            elif text == "log":
                result = math.log10(value)
            elif text == "sqrt":
                result = math.sqrt(value)
            elif text == "exp":
                result = math.exp(value)
            elif text == "pi":
                result = math.pi
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            add_to_history(f"{text}({value}) = {result}")
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

def add_to_history(entry_text):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    history_box.insert(tk.END, f"[{timestamp}] {entry_text}\n")
    history_box.see(tk.END)

# --------------------- เปลี่ยนธีม ---------------------
def toggle_theme():
    global current_theme
    current_theme = light_theme if current_theme == dark_theme else dark_theme
    theme_button.config(text="🌞" if current_theme == light_theme else "🌙")
    apply_theme()

def apply_theme():
    root.configure(bg=current_theme["bg"])
    entry.configure(bg=current_theme["entry_bg"], fg=current_theme["entry_fg"], insertbackground=current_theme["entry_fg"])
    history_box.configure(bg=current_theme["history_bg"], fg=current_theme["history_fg"])
    for button in all_buttons:
        button.configure(
            bg=current_theme["button_bg"],
            fg=current_theme["button_fg"],
            activebackground=current_theme["active_bg"],
            activeforeground=current_theme["active_fg"]
        )

# --------------------- UI หลัก ---------------------
root = tk.Tk()
root.title("เครื่องคิดเลขวิทยาศาสตร์")
root.geometry("500x650")

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="flat", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=(20, 10), padx=20)

# ปุ่มต่าง ๆ
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["sin", "cos", "tan", "sqrt"],
    ["log", "exp", "pi", "C"]
]

all_buttons = []

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both", padx=10)
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font=("Arial", 18), relief="flat", borderwidth=0)
        button.pack(side=tk.LEFT, expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", click)
        all_buttons.append(button)

# ปุ่มเปลี่ยนธีม
theme_button = tk.Button(
    root,
    text="🌙",
    font=("Arial", 18),
    command=toggle_theme,
    relief="flat",
    bd=0
)
theme_button.pack(pady=5)
all_buttons.append(theme_button)

# กล่องประวัติ
history_label = tk.Label(root, text="ประวัติการคำนวณ", font=("Arial", 12, "bold"))
history_label.pack()

history_box = tk.Text(root, height=6, font=("Courier New", 10), bd=2, relief="sunken")
history_box.pack(fill=tk.BOTH, padx=20, pady=(0, 10), expand=False)

# ใช้ธีมเริ่มต้น
apply_theme()

root.mainloop()
