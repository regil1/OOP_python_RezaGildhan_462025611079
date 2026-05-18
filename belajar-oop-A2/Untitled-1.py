class Bank:
    nama = ''
    saldo = 0

    def cek_saldo(self):
        print(f'print dari method cek_saldo')

    def __init__(self, nama='', saldo=0):
        self.nama = nama
        if saldo < 0:
            raise ValueError('Saldo tidak boleh negatif')
        self.saldo = saldo

    def __eq__(self, value):
        return self.nama == value.nama and self.saldo == value.saldo
    
    def __le__(self, value):
        return self.saldo <= value.saldo
    
bank1 = Bank('Anto', -8000000)
bank2 = Bank('Budi', 1000000)
print(bank1 == bank2)
print(bank1 <= bank2)