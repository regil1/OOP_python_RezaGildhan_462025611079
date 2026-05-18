class Perangkat:
    def __init__(self, id_perangkat, baterai):
        # Atribut Privat (Enkapsulasi)
        self.__id_perangkat = id_perangkat
        self.__baterai = baterai  # Atribut privat ke-1
        print(f"Menginisialisasi Perangkat: {self.__id_perangkat}")

    def info_perangkat(self):
        print(f"ID: {self.__id_perangkat} | Baterai: {self.__baterai}%")

    # Getter & Validasi untuk Baterai
    @property
    def baterai(self):
        return self.__baterai

    @baterai.setter
    def baterai(self, nilai):
        if 0 <= nilai <= 100:
            self.__baterai = nilai
        else:
            print("Gagal: Kapasitas baterai harus antara 0-100!")

class Kamera(Perangkat):
    def __init__(self, resolusi, **kwargs):
        # Menggunakan super() untuk Diamond Problem
        super().__init__(**kwargs)
        self.__resolusi = resolusi  # Atribut privat ke-2
        print(f"Fitur Kamera {self.__resolusi}MP ditambahkan.")

    def ambil_gambar(self):
        print("Mengambil foto...")

class Speaker(Perangkat):
    def __init__(self, volume, **kwargs):
        super().__init__(**kwargs)
        self.__volume = volume  # Atribut privat ke-3
        print(f"Fitur Speaker dengan volume {self.__volume} aktif.")

    # Getter & Validasi untuk Volume
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, nilai):
        if nilai >= 0:
            self.__volume = nilai
            print(f"Volume diatur ke: {self.__volume}")
        else:
            print("Gagal: Volume tidak boleh negatif!")

# Implementasi Diamond Problem
class SmartDoorbell(Kamera, Speaker):
    def __init__(self, id_perangkat, baterai, resolusi, volume):
        # super() di sini akan memanggil MRO (Kamera -> Speaker -> Perangkat)
        super().__init__(id_perangkat=id_perangkat, baterai=baterai, 
                         resolusi=resolusi, volume=volume)
        print("Smart Doorbell siap digunakan!")

    def tekan_bel(self):
        print("\n[Tamu menekan bel]")
        self.ambil_gambar()
        print("Memainkan suara: 'Halo, ada tamu di depan pintu'.")

# --- Testing Program ---
if __name__ == "__main__":
    # Inisialisasi Objek
    my_doorbell = SmartDoorbell(id_perangkat="DB-2024", baterai=85, 
                                resolusi=12, volume=70)
    
    print("\n--- Status Perangkat ---")
    my_doorbell.info_perangkat()
    
    # Uji Validasi & Setter
    print("\n--- Uji Validasi Data ---")
    my_doorbell.baterai = 150  # Harus gagal
    my_doorbell.volume = -10   # Harus gagal
    my_doorbell.volume = 90    # Berhasil
    
    # Jalankan Fitur
    my_doorbell.tekan_bel()
    
    # Melihat MRO (Bukti Diamond Problem teratasi)
    print("\n--- Method Resolution Order (MRO) ---")
    for cls in SmartDoorbell.mro():
        print(cls.__name__)