#nama
nama = input("\nmasukkan nama yang benar: ")

while nama != "muhammad renaldi":
    print("nama anda salah, coba lagi")
    nama = input("masukkan nama yang benar: ")

#nim
nim = input("masukkan nim yang benar\t: ")

while nim != "25241008":
    print("nim anda salah, coba lagi")
    nim = input("masukkan nim yang benar\t: ")

#tabel perkalian
angka1 = int(input("\nmasukkan angka\t\t: "))

for i in range(1, 11):
    print(f"{angka1} x {i} = {angka1 * i}\n")