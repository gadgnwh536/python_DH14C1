import tkinter as tk
from tkinter import messagebox

def nhap_ky_tu(ky_tu):
    entry_hien_thi.insert(tk.END, ky_tu)

def xoa_toan_bo():
    entry_hien_thi.delete(0, tk.END)

def tinh_ket_qua():
    try:
        bieu_thuc = entry_hien_thi.get()
        ket_qua = eval(bieu_thuc)
        entry_hien_thi.delete(0, tk.END)
        entry_hien_thi.insert(0, str(ket_qua))
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le!")

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("300x380")
cua_so.resizable(False, False)

entry_hien_thi = tk.Entry(cua_so, font=("Arial", 18), justify="right", bd=10)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="we")

nut_bam = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in nut_bam:
    if text == '=':
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=tinh_ket_qua)
    else:
        btn = tk.Button(cua_so, text=text, font=("Arial", 14), width=5, height=2, command=lambda t=text: nhap_ky_tu(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

tk.Button(cua_so, text="C", font=("Arial", 14), width=22, height=1, command=xoa_toan_bo).grid(row=5, column=0, columnspan=4, pady=5)

if __name__ == "__main__":
    cua_so.mainloop()