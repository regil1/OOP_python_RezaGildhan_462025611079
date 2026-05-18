class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"Produk: {self.nama:15} | Harga: Rp{self.harga:,}"

  

    def __eq__(self, other):
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    def __lt__(self, other):
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented

# --- Instansiasi dan Pengujian ---

if __name__ == "__main__":
 
    produk1 = Produk("Laptop ASUS", 15000000)
    produk2 = Produk("Mouse Logi", 500000)
    produk3 = Produk("Monitor Dell", 3500000)
    produk4 = Produk("Keyboard Mech", 500000)

   
    print("=== Daftar Produk ===")
    print(produk1)
    print(produk2)
    print(produk3)
    print(produk4)
    print("-" * 40)

  
    print("=== Hasil Pengujian Perbandingan ===")
    
   
    print(f"Apakah {produk1.nama} > {produk3.nama}? {produk1 > produk3}")
    
    
    print(f"Apakah {produk2.nama} < {produk3.nama}? {produk2 < produk3}")
    
   
    print(f"Apakah harga {produk2.nama} == {produk4.nama}? {produk2 == produk4}")
    
    
    print(f"Apakah {produk1.nama} == {produk2.nama}? {produk1 == produk2}")