
danh_sach_sinh_vien = [
    {"ma_sv": "SV01", "ho_ten": "Nguyen Van A", "gioi_tinh": "Nam", "diem_tb": 8.5, "trang_thai": "Dang hoc"},
    {"ma_sv": "SV02", "ho_ten": "Tran Thi B", "gioi_tinh": "Nu", "diem_tb": 3.8, "trang_thai": "Dang hoc"},
    {"ma_sv": "SV03", "ho_ten": "Le Van C", "gioi_tinh": "Nam", "diem_tb": 6.5, "trang_thai": "Dang hoc"},
    {"ma_sv": "SV04", "ho_ten": "Pham Thi D", "gioi_tinh": "Nu", "diem_tb": 9.2, "trang_thai": "Dang hoc"}
]


def hien_thi_danh_sach_sinh_vien():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Danh sach sinh vien hien dang rong.")
        return
    print("\n" + "=" * 70)
    print(f"{'Ma SV': <10}{'Ho va ten': <22}{'Gioi tinh': <12}{'Diem TB': <12}{'Trang thai': <15}")
    print("-" * 70)
    for sv in danh_sach_sinh_vien:
        print(f"{sv['ma_sv']: <10}{sv['ho_ten']: <22}{sv['gioi_tinh']: <12}{sv['diem_tb']: <12.1f}{sv['trang_thai']: <15}")
    print("=" * 70)

def tim_sinh_vien_theo_ma(ma_sv):
    for sv in danh_sach_sinh_vien:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None

def xem_sinh_vien_hoc_bong():
    sv_hb = [sv for sv in danh_sach_sinh_vien if sv["diem_tb"] >= 8.0 and sv["trang_thai"] == "Dang hoc"]
    if len(sv_hb) == 0:
        print("-> Khong co sinh vien nao dat hoc bong.")
        return
    print("\nDANH SÁCH SINH VIÊN ĐẠT HỌC BỔNG (ĐIỂM TB >= 8.0):")
    for sv in sv_hb:
        print(f" - [{sv['ma_sv']}] {sv['ho_ten']} | Diem TB: {sv['diem_tb']:.1f}")


def them_sinh_vien(ma_sv, ho_ten, gioi_tinh, diem_tb):
    if tim_sinh_vien_theo_ma(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai, khong the them.")
        return
    danh_sach_sinh_vien.append({
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "gioi_tinh": gioi_tinh,
        "diem_tb": diem_tb,
        "trang_thai": "Dang hoc"
    })
    print(f"-> Da them sinh vien {ho_ten} ({ma_sv}) thanh cong.")

def cap_nhat_diem(ma_sv, diem_moi):
    sv = tim_sinh_vien_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}.")
        return
    diem_cu = sv["diem_tb"]
    sv["diem_tb"] = diem_moi
    print(f"-> Da cap nhat diem cho SV {sv['ho_ten']} ({ma_sv}): {diem_cu:.1f} -> {diem_moi:.1f}")

def cap_nhat_trang_thai_thoi_hoc(ma_sv):
    sv = tim_sinh_vien_theo_ma(ma_sv)
    if sv is None:
        print(f"-> Khong tim thay sinh vien voi ma {ma_sv}.")
        return
    if sv["trang_thai"] == "Thoi hoc":
        print(f"-> Sinh vien {ma_sv} da thoi hoc truoc do.")
        return
    sv["trang_thai"] = "Thoi hoc"
    print(f"-> Da chuyen trang thai sinh vien {sv['ho_ten']} ({ma_sv}) sang 'Thoi hoc'.")


def thong_ke_sinh_vien():
    if len(danh_sach_sinh_vien) == 0:
        print("-> Chua co dữ liệu sinh viên.")
        return
    
    tong_sv = len(danh_sach_sinh_vien)
    sv_dang_hoc = [sv for sv in danh_sach_sinh_vien if sv["trang_thai"] == "Dang hoc"]
    sv_thoi_hoc = [sv for sv in danh_sach_sinh_vien if sv["trang_thai"] == "Thoi hoc"]
    
    gioi = len([sv for sv in sv_dang_hoc if sv["diem_tb"] >= 8.0])
    kha = len([sv for sv in sv_dang_hoc if 6.5 <= sv["diem_tb"] < 8.0])
    trung_binh = len([sv for sv in sv_dang_hoc if 5.0 <= sv["diem_tb"] < 6.5])
    yieu = len([sv for sv in sv_dang_hoc if sv["diem_tb"] < 5.0])
    
    print("\nTHỐNG KÊ SINH VIÊN:")
    print(f" - Tong so sinh vien: {tong_sv}")
    print(f" - So sinh vien dang hoc: {len(sv_dang_hoc)}")
    print(f" - So sinh vien da thoi hoc: {len(sv_thoi_hoc)}")
    print("\nXEP LOAI SINH VIEN DANG HOC:")
    print(f" + Gioi (Diem >= 8.0): {gioi}")
    print(f" + Kha (6.5 <= Diem < 8.0): {kha}")
    print(f" + Trung binh (5.0 <= Diem < 6.5): {trung_binh}")
    print(f" + Yeu (Diem < 5.0): {yieu}")

def nhap_diem_so(loi_nhac):
    """Bắt lỗi try-except đảm bảo nhập điểm trong khoảng 0.0 -> 10.0"""
    while True:
        try:
            val = float(input(loi_nhac))
            if 0.0 <= val <= 10.0:
                return val
            print("-> Diem so phai nam trong khoang tu 0.0 den 10.0. Vui long nhap lai.")
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap lai mot so (vi du: 7.5).")


def hien_thi_menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Hien thi danh sach tat ca sinh vien")
    print("2. Xem danh sach sinh vien dat hoc bong")
    print("3. Them sinh vien moi")
    print("4. Cap nhat diem cho sinh vien")
    print("5. Cap nhat trang thai thoi hoc")
    print("6. Thong ke va xep loai sinh vien")
    print("0. Thoat chuong trinh")

def chay_chuong_trinh():
    while True:
        hien_thi_menu()
        lua_chon = input("Nhap lua chon cua ban: ").strip()
        
        if lua_chon == "1":
            hien_thi_danh_sach_sinh_vien()
        elif lua_chon == "2":
            xem_sinh_vien_hoc_bong()
        elif lua_chon == "3":
            ma_sv = input("Nhap ma sinh vien moi: ").strip().upper()
            ho_ten = input("Nhap ho va ten: ").strip().title()
            gioi_tinh = input("Nhap gioi tinh (Nam/Nu): ").strip().title()
            diem_tb = nhap_diem_so("Nhap diem trung binh (0.0 - 10.0): ")
            them_sinh_vien(ma_sv, ho_ten, gioi_tinh, diem_tb)
        elif lua_chon == "4":
            ma_sv = input("Nhap ma sinh vien can cap nhat diem: ").strip().upper()
            diem_moi = nhap_diem_so("Nhap diem trung binh moi (0.0 - 10.0): ")
            cap_nhat_diem(ma_sv, diem_moi)
        elif lua_chon == "5":
            ma_sv = input("Nhap ma sinh vien thoi hoc: ").strip().upper()
            cap_nhat_trang_thai_thoi_hoc(ma_sv)
        elif lua_chon == "6":
            thong_ke_sinh_vien()
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("-> Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    chay_chuong_trinh()