import json
import os
import datetime

print("""
===================

PENDAFTAN SISWA/I SMK N1 SIDIKALANG

===================

>TJKT = Teknik Jaringan Komputer dan Telekomunikasi
>PM = Pemasaran
>PH = Perhotelan
>AKL = Akutansi Keuangan dan Lembaga
>MPLB = Manajemen Perkantoran & Layanan Bisnis
>ULP = Usaha Layanan Pariwisata

===================
""")

jurusan_list = ["TJKT", "PM", "PH", "AKL", "MPLB", "ULP"]
nama_siswa = str(input("Nama Lengkap (Sesuai Ijazah) : "))
tgl_lahir = str(input("Tanggal Lahir (Example : 24 Oktober 2005) : "))
while True:
	kelamin_code = input("Jenis Kelamin (L/P) : ")
	if kelamin_code.upper() == "L":
	  jns_kelamin = "Laki-Laki"
	  break
	elif kelamin_code.upper() == "P":
	  jns_kelamin = "Perempuan"
	  break
	else:
	  print("Code Jenis kelamin tidak vaild")
	  

agama = str(input("Agama : "))
alamat = str(input("Alamat : "))

while True:
  jurusan = str(input("Jurusan Yang di pilih (Example : TJKT) : "))
  if jurusan in jurusan_list:
    #Jurusan sudah ada
    break
  else:
    print("Code Jurusan tidak Ada")
    

os.system('cls' if os.name == 'nt' else 'clear')
tanggal_waktu_sekarang = datetime.datetime.now()
tanggal_waktu_string = tanggal_waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")

data_siswa = {
  "nama" : nama_siswa,
  "tanggal_lahir" : tgl_lahir,
  "agama" : agama,
  "alamat" : alamat,
  "jenis_kelamin" : jns_kelamin,
  "jurusan" : jurusan,
  "tanggal_daftar" : tanggal_waktu_string
}

try:
  with open("data_siswa.json", "r") as file:
    data = json.load(file)
except FileNotFoundError:
  data = []

data.append(data_siswa)

with open("data_siswa.json", "w") as file:
  json.dump(data, file, indent=4)
  
print("==============>PENDAFTARAN BERHASIL<===============")
print("")
print("Nama           : ", nama_siswa)
print("Tanggal Lahir  : ", tgl_lahir)
print("Jenis Kelamin  : ", jns_kelamin)
print("Agama          : ", agama)
print("Alamat         : ", alamat)
print("Jurusan        : ", jurusan)
print("")
print("===================================================")
print("Data telah di kirim ke data_siswa.json")
