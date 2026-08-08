# ==========================================
# 1. PARENT CLASS & METHOD OVERRIDING
# ==========================================

class Notifikasi:
    """Parent Class sebagai cetak biru (blueprint)"""
    def kirim(self, pesan):
        # Metode ini akan di-override oleh subclass
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

class NotifikasiEmail(Notifikasi):
    """Child Class 1 - Mengoverride metode kirim()"""
    def __init__(self, email_tujuan):
        self.email_tujuan = email_tujuan

    def kirim(self, pesan):
        print(f" Mengirim Email ke [{self.email_tujuan}]: {pesan}")

class NotifikasiSMS(Notifikasi):
    """Child Class 2 - Mengoverride metode kirim()"""
    def __init__(self, nomor_hp):
        self.nomor_hp = nomor_hp

    def kirim(self, pesan):
        print(f"Mengirim SMS ke [{self.nomor_hp}]: {pesan}")


# ==========================================
# 2. IMPLEMENTASI DUCK TYPING
# ==========================================

# Kelas ini TIDAK mewarisi dari class Notifikasi (Bukan Child Class),
# tetapi memiliki metode kirim() dengan nama yang sama.
class NotifikasiWhatsApp:
    """Kelas Independen untuk membuktikan Duck Typing"""
    def __init__(self, nomor_wa):
        self.nomor_wa = nomor_wa

    def kirim(self, pesan):
        print(f"Mengirim WhatsApp ke [{self.nomor_wa}]: {pesan}")


# Fungsi Mandiri (Polymorphic Function)
def broadcast_info(media_notifikasi, pesan):
    """
    Fungsi ini menerapkan Duck Typing. Ia tidak peduli media_notifikasi 
    itu objek dari kelas apa, yang penting objek tersebut memiliki metode kirim().
    """
    print("--- Memproses Pengiriman ---")
    media_notifikasi.kirim(pesan)


# ==========================================
# 3. DEMONSTRASI PROGRAM
# ==========================================
if __name__ == "__main__":
    # Membuat objek-objek dari kelas yang berbeda
    email_user = NotifikasiEmail("budi@email.com")
    sms_user = NotifikasiSMS("08123456789")
    wa_user = NotifikasiWhatsApp("08998765432") # Objek Duck Typing

    pesan_sistem = "Server akan maintenance pada pukul 23.00 WIB."

    # Memanggil fungsi yang sama dengan objek yang berbeda-beda
    broadcast_info(email_user, pesan_sistem)
    broadcast_info(sms_user, pesan_sistem)
    
    # Duck Typing beraksi: Kelas WhatsApp tetap bisa diproses 
    # karena "berperilaku seperti bebek" (punya fungsi kirim)
    broadcast_info(wa_user, pesan_sistem)