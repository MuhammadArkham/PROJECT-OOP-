class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_mahasiswa(self, nim, nama, jurusan):
        mhs = Mahasiswa(nim, nama, jurusan)
        self.data.append(mhs)

    def hapus_mahasiswa(self, nim):
        self.data = [mhs for mhs in self.data if mhs.nim != nim]

    def ubah_mahasiswa(self, nim, nama=None, jurusan=None):
        for mhs in self.data:
            if mhs.nim == nim:
                if nama:
                    mhs.nama = nama
                if jurusan:
                    mhs.jurusan = jurusan

    def cari_mahasiswa(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None
