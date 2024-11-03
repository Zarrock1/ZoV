import tkinter as tk
from tkinter import messagebox
import time

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Секундомер")

        self.is_running = False
        self.start_time = 0

        self.label = tk.Label(master, text="Время: 0.00 сек")
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Начать", command=self.start_stopwatch)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Стоп", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Внимание", "Секундомер уже запущен!")

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            elapsed_time = round(time.time() - self.start_time, 2)
            self.label.config(text=f"Время: {elapsed_time} сек")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("Внимание", "Секундомер не запущен!")

    def update_time(self):
        if self.is_running:
            elapsed_time = round(time.time() - self.start_time, 2)
            self.label.config(text=f"Время: {elapsed_time} сек")
            self.master.after(100, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
