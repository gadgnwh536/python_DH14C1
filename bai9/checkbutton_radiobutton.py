import tkinter as tk

cua_so1 = tk.Tk()
cua_so1.title("Vi du Checkbutton")
cua_so1.geometry("300x220")

tk.Label(cua_so1, text="Chon so thich cua ban:", font=("Arial", 12)).pack(pady=10)

bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

tk.Checkbutton(cua_so1, text="Doc sach", variable=bien_doc_sach).pack(anchor="w", padx=30)
tk.Checkbutton(cua_so1, text="The thao", variable=bien_the_thao).pack(anchor="w", padx=30)
tk.Checkbutton(cua_so1, text="Am nhac", variable=bien_am_nhac).pack(anchor="w", padx=30)

def xem_lua_chon():
    print("Doc sach:", bien_doc_sach.get())
    print("The thao:", bien_the_thao.get())
    print("Am nhac:", bien_am_nhac.get())

tk.Button(cua_so1, text="Xem lua chon (in ra console)", command=xem_lua_chon).pack(pady=15)

cua_so1.mainloop()

cua_so2 = tk.Tk()
cua_so2.title("Vi du Radiobutton")
cua_so2.geometry("300x200")

bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Label(cua_so2, text="Chon loai tai khoan:", font=("Arial", 12)).pack(pady=10)
tk.Radiobutton(cua_so2, text="Ca nhan", variable=bien_loai_tai_khoan, value="ca_nhan").pack(anchor="w", padx=30)
tk.Radiobutton(cua_so2, text="Doanh nghiep", variable=bien_loai_tai_khoan, value="doanh_nghiep").pack(anchor="w", padx=30)

def xem_loai_tai_khoan():
    nhan_ket_qua.config(text=f"Ban da chon: {bien_loai_tai_khoan.get()}")

tk.Button(cua_so2, text="Xac nhan", command=xem_loai_tai_khoan).pack(pady=10)
nhan_ket_qua = tk.Label(cua_so2, text="")
nhan_ket_qua.pack()

cua_so2.mainloop()