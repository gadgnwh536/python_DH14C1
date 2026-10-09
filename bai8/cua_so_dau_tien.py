import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300")

cua_so.resizable(True, False)

khung_tren = tk.Frame(cua_so, bg="lightblue", height=100)
khung_tren.pack(fill="x")

khung_duoi = tk.Frame(cua_so, bg="lightyellow")
khung_duoi.pack(fill="both", expand=True)

tk.Label(khung_tren, text="Khu vuc tieu de", bg="lightblue", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(khung_duoi, text="Xin chao Tkinter! Khu vuc noi dung", bg="lightyellow", font=("Arial", 12)).pack(pady=20)

cua_so.mainloop()