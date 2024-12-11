from data.mahasiswa import DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()
    while True:
        print("\nMenu Utama:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Cari Mahasiswa")
        print("5. Tampilkan Semua Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            data_mahasiswa.tambah_mahasiswa(nim, nama, jurusan)
            print("Data berhasil ditambahkan.")
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Data berhasil dihapus.")
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            jurusan = input("Masukkan Jurusan baru (kosongkan jika tidak diubah): ")
            data_mahasiswa.ubah_mahasiswa(nim, nama, jurusan)
            print("Data berhasil diubah.")
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mhs = data_mahasiswa.cari_mahasiswa(nim)
            TampilMahasiswa.tampilkan_detail(mhs)
        elif pilihan == "5":
            TampilMahasiswa.tampilkan_list(data_mahasiswa.data)
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
