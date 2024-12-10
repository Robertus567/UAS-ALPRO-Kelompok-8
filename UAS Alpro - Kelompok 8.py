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
    print("4. Menampilkan Daftar Jadwal Konsultasi Berdasarkan Hari")
    print("5. Keluar")
    pilihan = input("Pilih fitur: ")
    return pilihan

def mencatat_data_pasien_baru():
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
    data_pasien.append({"nama": nama, "usia": usia, "nomor_telepon": nomor_telepon, "dokter": dokter_dipilih})
    print(f"Data pasien {nama} berhasil ditambahkan dengan dokter {dokter_dipilih}.")

def mengatur_jadwal_konsultasi():
    if not data_pasien:
        print("Tidak ada data pasien. Silakan tambahkan pasien terlebih dahulu.")
        return
    
    pasien = data_pasien.pop(0)  # Ambil pasien pertama dan hapus dari daftar
    nama_pasien = pasien['nama']
    dokter_pasien = pasien['dokter']
    nomor_telepon = pasien['nomor_telepon']
    
    print(f"Pasien yang akan dijadwalkan: {nama_pasien} (Dokter: {dokter_pasien}, No. Telepon: {nomor_telepon})")
    tanggal = input("Masukkan tanggal konsultasi (DD-MM-YYYY): ")
    waktu = input("Masukkan waktu konsultasi (HH:MM): ")
    
    jadwal_konsultasi.append({
        "nama": nama_pasien,
        "dokter": dokter_pasien,
        "nomor_telepon": nomor_telepon,
        "tanggal": tanggal,
        "waktu": waktu
    })
    jadwal_konsultasi.sort(key=lambda x: datetime.datetime.strptime(x['tanggal'], "%d-%m-%Y"))
    print(f"Jadwal konsultasi untuk {nama_pasien} dengan {dokter_pasien} berhasil ditambahkan.")

def menghapus_jadwal_konsultasi():
    if not jadwal_konsultasi:
        print("Belum ada jadwal konsultasi.")
        return
    
    print("\nDaftar Jadwal Konsultasi:")
    for idx, jadwal in enumerate(jadwal_konsultasi):
        print(f"{idx + 1}. {jadwal['nama']} (Dokter: {jadwal['dokter']}, No. Telepon: {jadwal['nomor_telepon']}) - {jadwal['tanggal']} {jadwal['waktu']}")
    
    pilihan = int(input("Pilih jadwal yang ingin dihapus berdasarkan nomor: ")) - 1
    if pilihan < 0 or pilihan >= len(jadwal_konsultasi):
        print("Pilihan tidak valid.")
        return
    
    jadwal_dihapus = jadwal_konsultasi.pop(pilihan)
    print(f"Jadwal konsultasi untuk {jadwal_dihapus['nama']} dengan {jadwal_dihapus['dokter']} pada {jadwal_dihapus['tanggal']} {jadwal_dihapus['waktu']} berhasil dihapus.")

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
        mencatat_data_pasien_baru()
    elif pilihan == '2':
        mengatur_jadwal_konsultasi()
    elif pilihan == '3':
        menghapus_jadwal_konsultasi()
    elif pilihan == '4':
        menampilkan_daftar_jadwal_berdasarkan_hari()
    elif pilihan == '5':
        print("Terima kasih telah menggunakan program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

