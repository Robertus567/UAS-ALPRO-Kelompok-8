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
    if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    nama_cari = input("Masukkan nama pasien yang ingin dicari: ")
    hasil = [jadwal for jadwal in jadwal_konsultasi if jadwal['nama'].lower() == nama_cari.lower()]
    
    if hasil:
        print("\nHasil Pencarian:")
        for jadwal in hasil:
            print(f"{jadwal['nama']} - {jadwal['tanggal']} {jadwal['waktu']}")
    else:
        print("Tidak ditemukan jadwal konsultasi untuk nama tersebut.")

def menampilkan_daftar_pasien_berdasarkan_hari():
   if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    # Meminta input nama hari
    hari_cari = input("Masukkan nama hari (contoh: Senin): ").capitalize()
    
    # Daftar nama hari dalam seminggu
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    # Cek apakah nama hari valid
    if hari_cari not in nama_hari:
        print("Nama hari tidak valid. Silakan coba lagi.")
        return
    
    # Dapatkan indeks hari (0 untuk Senin, 1 untuk Selasa, dst.)
    indeks_hari_cari = nama_hari.index(hari_cari)
    
    # Filter jadwal yang sesuai dengan nama hari yang dicari
    hasil = []
    for jadwal in jadwal_konsultasi:
        # Konversi tanggal konsultasi menjadi objek datetime
        tanggal = datetime.datetime.strptime(jadwal['tanggal'], "%Y-%m-%d")
        
        # Cek apakah hari dari tanggal cocok dengan hari yang dicari
        if tanggal.weekday() == indeks_hari_cari:
            hasil.append(jadwal)
    
    # Tampilkan hasil pencarian
    if hasil:
        print(f"\nDaftar Pasien dengan Janji pada Hari {hari_cari}:")
        for jadwal in hasil:
            print(f"{jadwal['nama']} - {jadwal['tanggal']} {jadwal['waktu']}")
    else:
        print(f"Tidak ditemukan jadwal konsultasi pada hari {hari_cari}.")




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
