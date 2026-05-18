# class Kampus:
#     nama = ''
#     alamat = ''

#     def greetings(self, nama):
#         print(f'Perkenalkan {nama}, nama kampus kami adalah {self.nama} yang beralamat di {self.alamat}')

# class Mahasiswa:
#     pass

# kampus1 = Kampus()
# kampus1.nama = 'Universitas Indonesia'
# kampus1.alamat = 'Jakarta'
# kampus1.greetings('Andi')

# kampus2 = Kampus()

# print(kampus1)
# print(kampus2)

# mahasiswa1 = Mahasiswa()
# mahasiswa1.nama = 'Budi'
# mahasiswa1.nim = '123456'

# mahasiswa2 = Mahasiswa()
# mahasiswa2.nama = 'Ani'
# mahasiswa2.nim = '67890'

# print(mahasiswa1)
# print(mahasiswa1.nama)
# print(mahasiswa1.nim)

# class Prodi:
#     nama = ''
#     jurusan = ''

#     @staticmethod
#     def ruangan():
#         print(f"Prodi memiliki ruang kelas yang nyaman")
#     def matkul(self):
#         print("Prodi", self.nama, "memiliki jurusan", self.jurusan)
#     def gudang(self, lokasi):
#         print(f'Prodi {self.nama} memiliki gudang yang luas yang terletak di {lokasi}')

# prodi1 = Prodi()
# prodi1.nama = 'Teknik Informatika'
# prodi1.jurusan = 'Teknik'
# prodi1.ruangan()
# prodi1.matkul() 
# prodi1.gudang('Gedung A')

# Prodi.ruangan()

class Bank:
    nama = ''
    saldo = 0

    def cek_saldo(self):
        print(f'Halo {self.nama}, Saldo Anda saat ini adalah {self.saldo}')

    def __init__(self, nama='', saldo=0):
        if saldo < 0:
            raise ValueError('Saldo tidak boleh negatif')
        self.nama = nama
        self.saldo = saldo
        print(f'Object berhasil dibuat')

    def __str__(self):
        return f'Hasil dari method __str__'

    def __eq__(self, other):
        return self.nama == other.nama and self.saldo == other.saldo
    
    def __le__(self, other):
        return self.saldo <= other.saldo
    
bank1 = Bank('Budi', -1000000)
bank2 = Bank('Budi', 50000)
# print(bank1 == bank2)
print(bank1 <= bank2)
# bank1 == bank2



# bank1 = Bank()
# print(bank1)


# bank1 = Bank()
# bank1.nama = 'Budi'
# bank1.saldo = 1000000
# print(bank1)

# bank1 = Bank()
# bank1.nama = 'Budi'
# bank1.saldo = 1000000
# bank1.cek_saldo()

