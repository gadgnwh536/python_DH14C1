# HOẠT ĐỘNG 6: Đệ quy – Giai thừa, Fibonacci[cite: 1]

# Bài tập 6.1 – Giai thừa[cite: 1]
def giai_thua_de_quy(n):
    if n <= 1:
        return 1  # Dieu kien dung[cite: 1]
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print("--- Bai tap 6.1 (Giai thua) ---")
print("De quy vs Vong lap (n=5):", giai_thua_de_quy(5), "-", giai_thua_lap(5))


# Bài tập 6.2 – Số Fibonacci thứ n bằng đệ quy[cite: 1]
def fibonacci_de_quy(n):
    if n <= 1:
        return n  # Dieu kien dung[cite: 1]
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print("\n--- Bai tap 6.2 (Fibonacci 10 so dau) ---")
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()

# Thu nghiem tinh fibonacci_de_quy(30)[cite: 1]
import time
print("\nDang tinh fibonacci_de_quy(30)...")
start_time = time.time()
val = fibonacci_de_quy(30)
end_time = time.time()
print(f"Fibonacci(30) = {val} | Thoi gian chay: {end_time - start_time:.4f} giây")