class SaldoMinimalError(Exception):
   
    
    def __init__(self, saldo_sekarang, jumlah_tarik, batas_minimal):
        self.saldo_sekarang = saldo_sekarang
        self.jumlah_tarik = jumlah_tarik
        self.batas_minimal = batas_minimal
        
      
        self.pesan = (f"TRANSAKSI DITOLAK: Penarikan Rp{jumlah_tarik:,} gagal. "
                      f"Saldo Anda (Rp{saldo_sekarang:,}) tidak mencukupi untuk "
                      f"menyisakan batas minimal Rp{batas_minimal:,} di rekening.")
        super().__init__(self.pesan)



class RekeningBank:
    def __init__(self, nama_pemilik, saldo_awal):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo_awal
        self.batas_minimal = 50000  # Saldo tidak boleh kurang dari Rp50.000

    def tarik_tunai(self, jumlah):
        print(f"\nMemproses penarikan Rp{jumlah:,} untuk rekening {self.nama_pemilik}...")
        
        # Menggunakan 'raise' untuk memicu custom exception jika kondisi tidak terpenuhi
        if self.saldo - jumlah < self.batas_minimal:
            raise SaldoMinimalError(self.saldo, jumlah, self.batas_minimal)
        
        self.saldo -= jumlah
        print(f"Penarikan berhasil! Sisa saldo saat ini: Rp{self.saldo:,}")



if __name__ == "__main__":
    # Inisialisasi objek dengan saldo Rp150.000
    rekening = RekeningBank("Reza", 150000)

  
    try:
        # Menarik 80.000, sisa 70.000 (Aman, di atas 50.000)
        rekening.tarik_tunai(80000)
    except SaldoMinimalError as error:
        print(error)
    except Exception as error:
        print(f"Terjadi error tidak terduga: {error}")
    finally:
       
        print("[SISTEM] Proses pemeriksaan transaksi 1 selesai dilakukan.")


 
    try:
       rekening.tarik_tunai(50000)
    except SaldoMinimalError as error:
       
        print(error)
    except Exception as error:
        print(f"Terjadi error tidak terduga: {error}")
    finally:
        print("[SISTEM] Proses pemeriksaan transaksi 2 selesai dilakukan.")