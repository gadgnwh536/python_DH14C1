import requests

print("--- Bài tập 5.1: API Github ---")
url_github = "https://api.github.com/repos/python/cpython"
response_gh = requests.get(url_github)

if response_gh.status_code == 200:
    du_lieu = response_gh.json()
    print("Tên repository:", du_lieu["full_name"])
    print("Số lượt gắn sao (stars):", du_lieu["stargazers_count"])
    print("Ngôn ngữ chính:", du_lieu["language"])
else:
    print("Gọi API thất bại, mã lỗi:", response_gh.status_code)

print("\n--- Bài tập 5.2: API Tỷ giá ---")
url_ex = "https://open.er-api.com/v6/latest/USD"
response_ex = requests.get(url_ex)

if response_ex.status_code == 200:
    du_lieu_ex = response_ex.json()
    ty_gia_vnd = du_lieu_ex["rates"]["VND"]
    print(f"1 USD = {ty_gia_vnd:,.0f} VND")
else:
    print("Không lấy được tỷ giá, mã lỗi:", response_ex.status_code)