class DompetDigital:
    def __init__(self, id_akun, pin, saldo_awal):
        self.__id_akun = id_akun
        self.__pin = pin
        self.__saldo = saldo_awal


    def get_id_akun(self):
        return self.__id_akun

  
    def lihat_saldo(self, pin_input):
        if pin_input == self.__pin:
            print(f"Verifikasi Berhasil. Saldo Akun {self.__id_akun}: Rp{self.__saldo}")
            return self.__saldo
        else:
            print("Verifikasi Gagal: PIN yang Anda masukkan salah!")
            return None

    def tarik_tunai(self, jumlah, pin_input):
        print(f"\n--- Percobaan Penarikan: Rp{jumlah} ---")
        if pin_input == self.__pin:
            if jumlah <= self.__saldo:
                self.__saldo -= jumlah
                print(f"Penarikan Berhasil! Sisa saldo sekarang: Rp{self.__saldo}")
            else:
                print("Penarikan Gagal: Saldo tidak mencukupi.")
        else:
            print("Penarikan Gagal: PIN salah!")


dompet_reza = DompetDigital("REZA-2026-ID", "123456", 500000)

print(f"Selamat Datang di Aplikasi Dompet Digital!")
print(f"ID Pengguna: {dompet_reza.get_id_akun()}")
print("-" * 40)


print("Mencoba lihat saldo dengan PIN salah (000000):")
dompet_reza.lihat_saldo("000000")

print("\nMencoba lihat saldo dengan PIN benar (123456):")
dompet_reza.lihat_saldo("123456")

dompet_reza.tarik_tunai(200000, "123456") 
dompet_reza.tarik_tunai(100000, "111111")