class Kontak:
    def __init__(self, nama, telepon):
        self.nama = nama  # String
        self.telepon = telepon  # String

class BukuKontak:
    def __init__(self):
        self.daftar_kontak = []  # List
    
    def tambah_kontak(self, kontak):
        if not any(k.nama.lower() == kontak.nama.lower() for k in self.daftar_kontak):  # Percabangan
            self.daftar_kontak.append(kontak)  # List operation
            return True
        return False
    
    def cari_kontak(self, keyword):
        return [k for k in self.daftar_kontak if keyword.lower() in k.nama.lower()]  # Perulangan + String
    
    def hapus_kontak(self, nama):
        for kontak in self.daftar_kontak:  # Perulangan
            if kontak.nama.lower() == nama.lower():  # Percabangan
                self.daftar_kontak.remove(kontak)
                return True
        return False

# Fungsi untuk tampilan CLI
def main():
    buku = BukuKontak()
    while True:  # Perulangan menu
        print("\n=== BUKU KONTAK ===")
        print("1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")  # String input
        
        if pilihan == "1":  # Percabangan
            nama = input("Nama: ")
            telepon = input("Telepon: ")
            if buku.tambah_kontak(Kontak(nama, telepon)):
                print("✓ Berhasil ditambahkan!")
            else:
                print("✗ Nama sudah ada!")
        
        elif pilihan == "2":
            keyword = input("Cari nama: ")
            hasil = buku.cari_kontak(keyword)
            if hasil:
                for kontak in hasil:
                    print(f"- {kontak.nama}: {kontak.telepon}")
            else:
                print("✗ Tidak ditemukan!")
        
        elif pilihan == "3":
            nama = input("Nama yang dihapus: ")
            if buku.hapus_kontak(nama):
                print("✓ Berhasil dihapus!")
            else:
                print("✗ Tidak ditemukan!")
        
        elif pilihan == "4":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()