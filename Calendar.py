import calendar
import tkinter as tk

root = tk.Tk()
root.title("Calendar")
root.geometry("700x700")

text_box = tk.Text(root, width = 100, height = 200)
text_box.grid(row = 20, column = 10, columnspan = 10)

text_box.insert("end-1c", calendar.calendar(2022, 3, 1, 6))



root.mainloop()
