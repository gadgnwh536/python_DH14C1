# HOẠT ĐỘNG 1: Hàm cơ bản – def, tham số, return

def uscln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bscnn(a, b):
    return a * b // uscln(a, b)

def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# Bài tập 1.1: Gọi thử với các bộ dữ liệu khác nhau
print("--- Kiem tra USCLN ---")
print(uscln(24, 36))
print(uscln(15, 28))
print(uscln(100, 25))

print("\n--- Kiem tra BSCNN ---")
print(bscnn(4, 6))
print(bscnn(5, 7))
print(bscnn(12, 18))

print("\n--- Kiem tra So nguyen to ---")
print(kiem_tra_nguyen_to(29))
print(kiem_tra_nguyen_to(10))
print(kiem_tra_nguyen_to(2))

print("\n--- Kiem tra So hoan thien ---")
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(12))

# Bài tập 1.2 – return không giá trị và trả về nhiều giá trị
def in_loi_chao(ten):
    print(f"Xin chao, {ten}!")
    return  # Ham khong tra ve gia tri (tra ve None)

def chia_lay_thuong_du(a, b):
    return a // b, a % b  # Tra ve nhieu gia tri qua tuple

print("\n--- Bai tap 1.2 ---")
in_loi_chao("An")
thuong, du = chia_lay_thuong_du(17, 5)
print(f"Thuong: {thuong}, Du: {du}")


# HOẠT ĐỘNG 2: Tham số mặc định & Tham số từ khóa
def gioi_thieu(ten, tuoi=18, lop="Chua ro"):
    print(f"Ten: {ten} | Tuoi: {tuoi} | Lop: {lop}")

print("\n--- Hoat dong 2 ---")
gioi_thieu("An")                                      # Dung het gia tri mac dinh
gioi_thieu("Binh", 20)                                # Ghi de tuoi
gioi_thieu("Chi", lop="CNTT01")                       # Dung tham so tu khoa, bo qua tuoi
gioi_thieu(ten="Dung", lop="CNTT02", tuoi=19)         # Thu tu tham so tu khoa co the dao lon


# HOẠT ĐỘNG 3: Tham số linh hoạt – *args và **kwargs
# Bài tập 3.1 – *args
def tinh_tong(*args):
    tong = 0
    for so in args:
        tong += so
    return tong

print("\n--- Bai tap 3.1 (*args) ---")
print(tinh_tong(1, 2, 3))
print(tinh_tong(5, 10, 15, 20, 25))
print(tinh_tong())  # Khong truyen so nao -> tra ve 0

# Bài tập 3.2 – **kwargs
def in_thong_tin(ho_ten, tuoi, **kwargs):
    print(f"Ho ten: {ho_ten} | Tuoi: {tuoi}")
    for khoa, gia_tri in kwargs.items():
        print(f"  {khoa}: {gia_tri}")

print("\n--- Bai tap 3.2 (**kwargs) ---")
in_thong_tin("Dang Quang Hung", 20, lop="DH14C1", que_quan="Yen Bai")
in_thong_tin("Nguyen Van A", 21, email="b@example.com")