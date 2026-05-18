class Karyawan:
    perusahaan = "PT Tekno Utama"

    def __init__(self, nama, jabatan, gaji_pokok):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_pokok = gaji_pokok

    # --- Instance Methods ---
    def tampilkan_profil(self):
        print(f"Nama    : {self.nama}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Kantor  : {self.perusahaan}")

    def hitung_bonus(self, persentase):
        bonus = self.gaji_pokok * (persentase / 100)
        total = self.gaji_pokok + bonus
        return total

    # --- Static Method ---
    @staticmethod
    def validasi_nip(nip):
        
        if len(str(nip)) == 12 and str(nip).isdigit():
            return True
        return False

# --- Instansiasi dan Pengujian ---

# 1. Membuat 2 Object
karyawan1 = Karyawan("Andi", "Backend Developer", 8000000)
karyawan2 = Karyawan("Budi", "UI/UX Designer", 7500000)

# 2. Pengujian Instance Methods
print(" Profil Karyawan 1")
karyawan1.tampilkan_profil()
print(f"Total Gaji + Bonus: Rp{karyawan1.hitung_bonus(10):,.0f}\n")

print(" Profil Karyawan 2")
karyawan2.tampilkan_profil()
print(f"Total Gaji + Bonus: Rp{karyawan2.hitung_bonus(15):,.0f}\n")

# 3. Pengujian Static Method
print("Pengujian Static Method")
nip_test = 462025611079
is_valid = Karyawan.validasi_nip(nip_test)
print(f"Validasi NIP {nip_test} via Class: {is_valid}")
print(f"Validasi NIP {nip_test} via Object: {karyawan1.validasi_nip(nip_test)}")