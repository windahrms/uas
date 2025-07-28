import requests
BASE_URL = "http://localhost:5000/kontak"

def main():
    while True:
        print("\n=== API CLIENT ===")
        print("1. Tambah Kontak (POST)")
        print("2. Lihat Semua Kontak (GET)")
        print("3. Hapus Kontak (DELETE)")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Nama: ")
            telepon = input("Telepon: ")
            response = requests.post(BASE_URL, json={"nama": nama, "telepon": telepon})
            print(f"Status: {response.status_code} - {response.json()}")
        
        elif pilihan == "2":
            response = requests.get(BASE_URL)
            print("Daftar Kontak:")
            for kontak in response.json():
                print(f"- {kontak['nama']}: {kontak['telepon']}")
        
        elif pilihan == "3":
            nama = input("Nama yang dihapus: ")
            response = requests.delete(f"{BASE_URL}/{nama}")
            print(f"Status: {response.status_code} - {response.json()}")
        
        elif pilihan == "4":
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()