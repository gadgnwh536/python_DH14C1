# HOAT DONG 3
# for voi range()
for i in range(1, 6):
    print(i)


# for duyet List
diem_so = [8.5, 7.0, 9.2, 6.5]

for diem in diem_so:
    print("Diem:", diem)


# for duyet Tuple
toa_do = (3, 5)

for gia_tri in toa_do:
    print(gia_tri)


# for duyet Dictionary
diem_mon = {
    "Toan": 8.0,
    "Ly": 7.5
}

for mon, diem in diem_mon.items():
    print(mon, "-", diem)


# for duyet String
ten = "Python"

for ky_tu in ten:
    print(ky_tu)


# Bang cuu chuong
n = int(input("Nhap bang cuu chuong can in: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# =========================
# HOAT DONG 4
# =========================

# Bai 4.1 - Tinh giai thua
n = int(input("Nhap n: "))

giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"{n}! = {giai_thua}")


# Bai 4.2 - Tinh tong cac chu so
so = int(input("Nhap mot so nguyen duong: "))

so_tam = so
tong_chu_so = 0

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10

print(f"Tong cac chu so cua {so} la: {tong_chu_so}")