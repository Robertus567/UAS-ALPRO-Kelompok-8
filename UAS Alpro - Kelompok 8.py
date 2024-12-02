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
  if not data_pasien:
        print("Tidak ada data pasien. Silakan tambahkan pasien terlebih dahulu.")
        return
    
    # Mengambil pasien berdasarkan FIFO
    pasien = data_pasien.pop(0)  # Ambil pasien pertama dan hapus dari daftar
    nama_pasien = pasien['nama']
    
    print(f"Pasien yang akan dijadwalkan: {nama_pasien}")
    tanggal = input("Masukkan tanggal konsultasi (YYYY-MM-DD): ")
    waktu = input("Masukkan waktu konsultasi (HH:MM): ")
    
    # Menambahkan jadwal konsultasi
    jadwal_konsultasi.append({"nama": nama_pasien, "tanggal": tanggal, "waktu": waktu})
    jadwal_konsultasi.sort(key=lambda x: (x['tanggal'], x['waktu']))
    print(f"Jadwal konsultasi untuk {nama_pasien} berhasil ditambahkan.")



def menghapus_jadwal_konsultasi():

     if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    print("\nDaftar Jadwal Konsultasi:")
    for idx, jadwal in enumerate(jadwal_konsultasi):
        print(f"{idx + 1}. {jadwal['nama']} - {jadwal['tanggal']} {jadwal['waktu']}")
    
    pilihan = int(input("Pilih jadwal yang ingin dihapus berdasarkan nomor: ")) - 1
    if pilihan < 0 or pilihan >= len(jadwal_konsultasi):
        print("Pilihan tidak valid.")
        return
    
    jadwal_dihapus = jadwal_konsultasi.pop(pilihan)
    print(f"Jadwal konsultasi untuk {jadwal_dihapus['nama']} pada {jadwal_dihapus['tanggal']} {jadwal_dihapus['waktu']} berhasil dihapus.")


  

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
