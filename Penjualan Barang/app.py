import json
import os

print("""

===========================================
    	PENJUALAN BARANG
===========================================
""")

data_json = '''
[
    {
        "code": 1,
        "nama_barang": "Gula",
        "harga": 12000
    },
    {
        "code": 2,
        "nama_barang": "Minyak Goreng",
        "harga": 9000
    },
    {
        "code": 3,
        "nama_barang": "Buku Tulis 1LS",
        "harga": 30000
    },
    {
    	"code": 4,
    	"nama_barang": "Beras",
    	"harga": 70000
    },
    {
    	"code": 5,
    	"nama_barang": "Baygon",
    	"harga": 41000
    },
    {
    	"code": 6,
    	"nama_barang": "Sampo",
    	"harga": 5000
    },
    {
    	"code": 7,
    	"nama_barang": "Sabun Mandi",
    	"harga": 3000
    }
]
'''

data = json.loads(data_json)
total = []
program_running = True

# Mencari Data dengan Code
def cari_barang(code):
    for item in data:
        if item["code"] == code:
            return item
    return None

# Clear Screen 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    daftar_barang()
	
# Daftar barang
def daftar_barang():
    print("+-----------------------------------------+")
    for item in data:
        print(f'>| {item["code"]} | {item["nama_barang"]}	| Rp{item["harga"]}')
    print("+-----------------------------------------+")
    input_barang()
    
# Input Barang
def input_barang():
    global program_running
    while program_running:
        code_barang = input(">Masukkan No Barang ==> ")
        if code_barang == "exit":
            program_running = False
            break
        elif code_barang == "clear":
            clear()
            break
		
        try:
            code_barang = int(code_barang)
            barang = cari_barang(code_barang)
			   
            if barang:
                code_brg = f"{barang['code']}"
                nama_brg = f"{barang['nama_barang']}"
                harga_brg = int(barang['harga'])
                print("")
                print("------------------------------------------+")
                print(f"	Detail Barang | {code_barang} | ") 
                print("------------------------------------------+")
                print(">Nama Barang		: ", nama_brg)
                print(">Kode Barang		: ", code_brg)
                print(">Harga Barang		: ", harga_brg)
                print("")
			    	     
                while True:
                    jumlah = int(input(">Masukkan Jumlah ==> "))
                    if jumlah == 0:
                        print(">*Jumlah barang tidak boleh 0*<") 
                    else:
                        harga_wd = harga_brg * jumlah
                        # data_de sebagai list barang yang dibeli
                        data_de = {
                            "nama": nama_brg,
                            "harga": harga_brg,
                            "jumlah": jumlah,
                            "subtotal": harga_wd
                        }
                        total.append(data_de)
                        tambah_barang()
                        break
            else:
                print("")
                print("Barang tidak ditemukan")
                break
        except ValueError:
            print("")
            print("Kode Barang harus berupa angka atau 'exit' untuk keluar.")
		          
def tambah_barang():
    global program_running
    while True:
        print("\n---------------------------")
        tanya = input(">Ingin tambah barang? [y/t] ==> ")
        print("---------------------------\n")
        if tanya == "y":
            daftar_barang()
            break
        elif tanya == "t":
            akhir()
            program_running = False
            break
        else:
            print("Pilihan yang Anda pilih salah!")

def akhir():
    print("\n---------- Daftar Belanja ----------\n")
    for index, data_de in enumerate(total, start=1):
        print(f"+---------> Barang [{index}] <----------+")
        print(">Nama Barang	:", data_de["nama"])
        print(">Harga Barang	:", data_de["harga"])
        print(">Jumlah		:", data_de["jumlah"])
        print(">Subtotal	:", data_de["subtotal"])
    total_harga = sum(item["subtotal"] for item in total)
    print("\n+-------------> Total <-------------+")
    diskon = 0
    a = total_harga
    if a > 1000000:
        diskon = a * 0.45
    elif a > 500000:
        diskon = a * 0.30
    elif a > 300000:
        diskon = a * 0.15
    elif a > 150000:
        diskon = a * 0.10
    elif a > 100000:
        diskon = a * 0.05
    else:
        diskon = 0
    print(">Subtotal	: ", total_harga)
    print(">Potongan Harga	: ", diskon)
    total_akhir = a - diskon
    print(">Total Bayar	: ", total_akhir)

daftar_barang()
