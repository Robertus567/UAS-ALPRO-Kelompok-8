import datetime

# Array data pasien
data_pasien = []
# Array jadwal konsultasi
jadwal_konsultasi = []

def menu_utama():
    print("\nMenu:")
    print("1. Mencatat Data Pasien Baru")
    print("2. Mengatur Jadwal Konsultasi")
    print("3. Menghapus Jadwal Konsultasi")
    print("4. Mencari Jadwal Konsultasi")
    print("5. Menampilkan Daftar Pasien dengan Janji Konsultasi")
    pilihan = input("Pilih fitur: ")
    return pilihan

def mencatat_data_pasien_baru():
    nama = input("Masukkan nama pasien: ")
    usia = input("Masukkan usia pasien: ")
    alamat = input("Masukkan alamat pasien: ")
    data_pasien.append({"nama": nama, "usia": usia, "alamat": alamat})
    print(f"Data pasien {nama} berhasil ditambahkan.")

def mengatur_jadwal_konsultasi():
  

def menghapus_jadwal_konsultasi():
  

def mencari_jadwal_konsultasi():
    

def menampilkan_daftar_pasien_berdasarkan_hari():
   




# Pengulangan menu
print("KLINIK LEXA")
while True:
    pilihan = menu_utama()
    if pilihan == '1':
        mencatat_data_pasien_baru()
    elif pilihan == '2':
        mengatur_jadwal_konsultasi()
    elif pilihan == '3':
        menghapus_jadwal_konsultasi()
    elif pilihan == '4':
        mencari_jadwal_konsultasi()
    elif pilihan == '5':
        menampilkan_daftar_pasien_berdasarkan_hari()
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
