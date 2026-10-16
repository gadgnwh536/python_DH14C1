import tkinter as tk
from tkinter import ttk

cua_so1 = tk.Tk()
cua_so1.title("Vi du Listbox")
cua_so1.geometry("300x250")

listbox_mon_hoc = tk.Listbox(cua_so1, selectmode="single")
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=10)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua1.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}")

tk.Button(cua_so1, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5)
nhan_ket_qua1 = tk.Label(cua_so1, text="")
nhan_ket_qua1.pack()

cua_so1.mainloop()

cua_so2 = tk.Tk()
cua_so2.title("Vi du Combobox")
cua_so2.geometry("300x180")

tk.Label(cua_so2, text="Chon thanh pho:").pack(pady=10)
combobox_thanh_pho = ttk.Combobox(cua_so2, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua2.config(text=f"Ban chon: {combobox_thanh_pho.get()}")

tk.Button(cua_so2, text="Xac nhan", command=xem_thanh_pho).pack(pady=10)
nhan_ket_qua2 = tk.Label(cua_so2, text="")
nhan_ket_qua2.pack()

cua_so2.mainloop()