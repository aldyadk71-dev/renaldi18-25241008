mahasiswa = [
    {"NIM": "25241008", "Nama": "MUHAMMAD RENALDI", "Nilai": 85},
    {"NIM": "25241002", "Nama": "DIMAS ADRIAN", "Nilai": 78},
    {"NIM": "25241032", "Nama": "HASBI HANDIKA", "Nilai": 90},
    {"NIM": "25241032", "Nama": "REPLI KIRPALANI", "Nilai": 88},
    {"NIM": "25241022", "Nama": "RIDO SUCIPTA DAMA", "Nilai": 75}
]

print("Data Mahasiswa dengan NIM berakhiran genap:\n")

found = False
for mhs in mahasiswa:
    nim = mhs.get("NIM", "")
    # Pastikan NIM tidak kosong dan karakter terakhir adalah digit
    if not nim:
        # lewati jika NIM kosong
        continue

    last_char = nim[-1]
    if not last_char.isdigit():
        # lewati jika karakter terakhir bukan digit
        continue

    last_digit = int(last_char)

    # Cek apakah angka terakhir genap
    if last_digit % 2 == 0:
        found = True
        print(f"NIM   : {mhs['NIM']}")
        print(f"Nama  : {mhs['Nama']}")
        print(f"Nilai : {mhs['Nilai']}")
        print("-" * 30)

if not found:
    print("Tidak ditemukan mahasiswa dengan NIM berakhiran genap.")