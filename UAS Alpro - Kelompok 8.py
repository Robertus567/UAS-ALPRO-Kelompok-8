import datetime
import csv

# Nama file CSV yang nyimpen data pasien
FILE_PASIEN = "data_pasien.csv"

# Array jadwal konsultasi
jadwal_konsultasi = []

# ngebaca data pasien dari CSV
def baca_data_pasien():
    data_pasien = []
    try:
        with open(FILE_PASIEN, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_pasien.append(row)
    except FileNotFoundError:
        # kalo file ga ditemukan, buat file kosong
        with open(FILE_PASIEN, mode="w") as file:
            writer = csv.DictWriter(file, fieldnames=["nama", "usia", "nomor_telepon", "dokter"])
            writer.writeheader()
    return data_pasien

# Nulis data pasien ke CSV
def tulis_data_pasien(data_pasien):
    with open(FILE_PASIEN, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["nama", "usia", "nomor_telepon", "dokter"])
        writer.writeheader()
        writer.writerows(data_pasien)

# Array data pasien (  dari CSV)
data_pasien = baca_data_pasien()

# Menu utama
def menu_utama():
    print("\nMenu:")
    print("1. Mencatat Data Pasien Baru dan Mengatur Jadwal Konsultasi")
    print("2. Menghapus Data Pasien")
    print("3. Menampilkan Daftar Jadwal Konsultasi Berdasarkan Hari")
    print("4. Mencari Jadwal Konsultasi Berdasarkan Nama")
    print("5. Keluar")
    pilihan = input("Pilih fitur: ")
    return pilihan

# Fitur nyatat data pasien baru dan mengatur jadwal konsultasi
def mencatat_data_pasien_baru_dan_jadwal():
    nama = input("Masukkan nama pasien: ")
    usia = input("Masukkan usia pasien: ")
    nomor_telepon = input("Masukkan nomor telepon pasien: ")

    print("\nDaftar Dokter:")
    daftar_dokter = ["Dr. Andi", "Dr. Budi", "Dr. Clara", "Dr. Dewi"]
    for idx, dokter in enumerate(daftar_dokter, start=1):
        print(f"{idx}. {dokter}")
    pilihan_dokter = int(input("Pilih dokter berdasarkan nomor: ")) - 1

    if pilihan_dokter < 0 or pilihan_dokter >= len(daftar_dokter):
        print("Pilihan tidak valid. Silakan ulangi pencatatan.")
        return

    dokter_dipilih = daftar_dokter[pilihan_dokter]
    pasien_baru = {"nama": nama, "usia": usia, "nomor_telepon": nomor_telepon, "dokter": dokter_dipilih}
    data_pasien.append(pasien_baru)
    tulis_data_pasien(data_pasien)  # Perbarui CSV
    print(f"Data pasien {nama} berhasil ditambahkan dengan dokter {dokter_dipilih}.")

    # Mengatur jadwal konsultasi setelah catat pasien
    tanggal = input("Masukkan tanggal konsultasi (DD-MM-YYYY): ")
    waktu = input("Masukkan waktu konsultasi (HH:MM): ")

    jadwal_konsultasi.append({
        "nama": nama,
        "dokter": dokter_dipilih,
        "nomor_telepon": nomor_telepon,
        "tanggal": tanggal,
        "waktu": waktu
    })
    jadwal_konsultasi.sort(key=lambda x: datetime.datetime.strptime(x['tanggal'], "%d-%m-%Y"))
    print(f"Jadwal konsultasi untuk {nama} dengan {dokter_dipilih} berhasil ditambahkan.")

# Fitur hapus data pasien ama jadwal konsultasi
def menghapus_data_pasien():
    if not data_pasien:
        print("Tidak ada data pasien.")
        return

    print("\nDaftar Pasien:")
    for idx, pasien in enumerate(data_pasien, start=1):
        print(f"{idx}. {pasien['nama']} (Usia: {pasien['usia']}, No. Telepon: {pasien['nomor_telepon']}, Dokter: {pasien['dokter']})")
    
    pilihan = int(input("Pilih pasien yang ingin dihapus berdasarkan nomor: ")) - 1
    if pilihan < 0 or pilihan >= len(data_pasien):
        print("Pilihan tidak valid.")
        return
    
    pasien_dihapus = data_pasien.pop(pilihan)
    # ngehapus jadwal konsultasi yang terkait dengan pasien yang dihapus
    jadwal_konsultasi[:] = [jadwal for jadwal in jadwal_konsultasi if jadwal['nama'] != pasien_dihapus['nama']]
    
    tulis_data_pasien(data_pasien)  # Perbarui CSV
    print(f"Data pasien {pasien_dihapus['nama']} berhasil dihapus beserta jadwal konsultasinya.")

# Fitur buat cari jadwal berdasarkan nama
def mencari_jadwal_berdasarkan_nama():
    if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    nama_dicari = input("Masukkan nama pasien yang ingin dicari: ").strip().lower()
    hasil_pencarian = [
        jadwal for jadwal in jadwal_konsultasi
        if nama_dicari in jadwal['nama'].lower()
    ]
    
    if hasil_pencarian:
        print("\nHasil Pencarian Jadwal Konsultasi:")
        for jadwal in hasil_pencarian:
            print(f"{jadwal['nama']} (Dokter: {jadwal['dokter']}, No. Telepon: {jadwal['nomor_telepon']}) - {jadwal['tanggal']} {jadwal['waktu']}")
    else:
        print("Tidak ada jadwal konsultasi yang sesuai dengan nama tersebut.")

# fungsi buat menampilkan jadwal berdasarkan hari
def menampilkan_daftar_jadwal_berdasarkan_hari():
    if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    jadwal_per_hari = {hari: [] for hari in nama_hari}
    
    for jadwal in jadwal_konsultasi:
        tanggal = datetime.datetime.strptime(jadwal['tanggal'], "%d-%m-%Y")
        nama_hari_konsultasi = nama_hari[tanggal.weekday()]
        jadwal_per_hari[nama_hari_konsultasi].append(jadwal)
    
    print("\nJadwal Konsultasi Berdasarkan Hari:")
    for hari, jadwals in jadwal_per_hari.items():
        print(f"\nHari {hari}:")
        if jadwals:
            for jadwal in jadwals:
                print(f"  {jadwal['nama']} (Dokter: {jadwal['dokter']}, No. Telepon: {jadwal['nomor_telepon']}) - {jadwal['tanggal']} {jadwal['waktu']}")
        else:
            print("  Tidak ada jadwal.")

# Pengulangan menu
print("KLINIK LEXA")
while True:
    pilihan = menu_utama()
    if pilihan == '1':
        mencatat_data_pasien_baru_dan_jadwal()
    elif pilihan == '2':
        menghapus_data_pasien()
    elif pilihan == '3':
        menampilkan_daftar_jadwal_berdasarkan_hari()
    elif pilihan == '4':
        mencari_jadwal_berdasarkan_nama()
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

