import tkinter as tk
from datetime import datetime

counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter

            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                display = tt.strftime("%H:%M:%S")

            label['text'] = display

            label.after(1000, count)
            counter += 1

    count()

def start(label):
    global running
    running = True
    counter_label(label)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'

def stop():
    global running
    running = False
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'

def reset(label):
    global counter
    counter = 66600

    if not running:
        reset_btn['state'] = 'disabled'
        label['text'] = "Welcome!"
    else:
        label['text'] = "Starting..."

root = tk.Tk()
root.title("Modern Stopwatch")
root.geometry("300x200")
root.configure(bg="lightblue")

label = tk.Label(root, text="Welcome!", fg="black", font=("Verdana", 20, "bold"), bg="lightblue")
label.pack(pady=20)

button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

start_btn = tk.Button(button_frame, text='Start', width=8, font=("Verdana", 12), command=lambda: start(label))
stop_btn = tk.Button(button_frame, text='Stop', width=8, font=("Verdana", 12), state='disabled', command=stop)
reset_btn = tk.Button(button_frame, text='Reset', width=8, font=("Verdana", 12), state='disabled', command=lambda: reset(label))

start_btn.pack(side="left", padx=5)
stop_btn.pack(side="left", padx=5)
reset_btn.pack(side="left", padx=5)

root.mainloop()
