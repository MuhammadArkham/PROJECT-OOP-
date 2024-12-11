class TampilMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        if not data_mahasiswa:
            print("Belum ada data mahasiswa.")
        else:
            for mhs in data_mahasiswa:
                print(f"NIM: {mhs.nim}, Nama: {mhs.nama}, Jurusan: {mhs.jurusan}")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(f"Detail Mahasiswa:\nNIM: {mahasiswa.nim}\nNama: {mahasiswa.nama}\nJurusan: {mahasiswa.jurusan}")
        else:
            print("Mahasiswa tidak ditemukan.")
