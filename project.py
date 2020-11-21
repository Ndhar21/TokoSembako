#Nicholas Dharmawan X Komputer 1


from os import system
 
print("----TOKO SEMBAKO ----")
access = input("Akses sebagai (Penjual(A)/Pembeli(B)) ? = ")
access = access.upper()
 
def searching_kode_barang(barang):
    if {data_brg[barang['kode']]} in data_brg:
        return True
    else:
        print("Barang Tidak Tersedia")
        return False
def searching_list_barang(barang):
    if barang in data_brg:
        return True
    else:
        print("Barang Tidak Tersedia")
        return False
data_brg = {
        "Minyak" : {
        "harga" : 20000,
        "kode" : "1A"
        },
        "Indomie" : {
        "harga" : 1250,
        "kode" : "2A"
        }
    }

if access == "A":
    #pw = 123
    kodeakses = input("Masukkan Password : ")
    while kodeakses != "123":
        print("Password Salah")
        kodeakses = input("Masukkan Password : ")

    def view_listA():
        system("cls")
        print("""
[A] Tampilkan Barang
[B] Menambah Barang
[C] Memperbarui Barang
[D] Menghapus Barang
[Q] Keluar
        """)
    def tampilkan_barang():
        system("cls")
        print("---Barang---")
        for barang in data_brg:
            barang = barang
            harga = data_brg[barang]['harga']
            kode = data_brg[barang]['kode']
            print(f"{barang}\nHarga = {harga}\nKode = {kode}")
        input("Tekan ENTER untuk kembali ke menu")


    def verify_ans(pilihanA):
        pilihanA = pilihanA.upper()
        if pilihanA == "Y":
            return True
        else:
            return False

    def menambah_barang():
        system("cls")
        print("---Menambah Barang Baru---")
        barang = input("Barang Baru = ")
        harga = input("Harga = ")
        kode = input("Kode = ")

        penjual_ans = input("Tekan Y untuk menyimpan = ")

        if verify_ans(penjual_ans):
            print("Menyimpan Barang Baru...")
            data_brg[barang] = {
                "harga" : harga,
                "kode" : kode
            }
            print("Data Tersimpan")
        else:
            print("Data tidak Tersimpan")

        input("Tekan ENTER untuk kembali ke menu awal")

    def memperbarui_harga_barang(barang):
        harga_baru = input("Harga baru = ")
        pilihanA = input("Apakah anda yakin untuk memperbarui barang (Y/N) ? = ")
        if verify_ans(pilihanA):
            data_brg[barang]['harga'] = harga_baru
            print("Barang Telah Diperbarui")
        else:
            print("Barang Batal Diperbarui")

    def memperbarui_kode_barang(barang):
        kode_baru = input("Kode baru = ")
        pilihanA = input("Apakah anda yakin untuk memperbarui barang (Y/N) ? = ")
        if verify_ans(pilihanA):
            data_brg[barang]['kode'] = kode_baru
            print("Menu telah diperbarui")
        else:
            print("Menu batal diperbarui")

    def memperbarui_barang():
        system("cls")
        print("----MEMPERBARUI BARANG----")
        barang = input("Barang apa yang ingin diperbarui ? = ")
        result = searching_list_barang(barang)
        if result:
            print("Apa yang ingin diperbarui ?\n[1] Harga\n[2] Kode")
            pilihanA = input("Pilihan = ")
            if pilihanA == "1":
                memperbarui_harga_barang(barang)
            elif pilihanA == "2":
                memperbarui_kode_barang(barang)
        input("Tekan ENTER untuk kembali ke menu awal")

    def menghapus_barang():
        system("cls")
        print("---Menghapus Barang---")
        barang = input("Barang apa yang akan dihapus ? = ")
        result = searching_list_barang(barang)
        if result: 
            pilihanA = input("Apakah anda yakin untuk menghapus Barang ini (Y/N) ? = ")
            if verify_ans(pilihanA):
                del data_brg[barang]
                print("Barang Telah Dihapus")
            else:
                print("Barang Tidak Terhapus")
        input("Tekan ENTER untuk Kembali ke menu awal")

    def check_inputA(pilihanA):
        pilihanA = pilihanA.upper()
        if pilihanA == "Q":
            return True
        elif pilihanA == "A":
            tampilkan_barang()
        elif pilihanA == "B":
            menambah_barang()
        elif pilihanA == "C":
            memperbarui_barang()
        elif pilihanA == "D":
            menghapus_barang()

    stop = False
    while not stop:
        view_listA()
        penjual_input = input("Pilihan : ")
        stop = check_inputA(penjual_input)

elif access == "B":
    def view_listB():
        system("cls")
        print("""
[A] Tampilkan Barang
[B] Mencari Barang
[Q] Keluar 
            """)

    def tampilkan_barang():
        system("cls")
        print("---Barang---")
        for barang in data_brg:
            barang = barang
            harga = data_brg[barang]['harga']
            kode = data_brg[barang]['kode']
            print(f"{barang}\nHarga = {harga}\nKode = {kode}")
        input("Tekan ENTER untuk kembali ke menu")

    def mencari_barang():
        system("cls")
        print("---Mencari Barang---")
        barang = input("Barang apa yang dicari ? = ")
        result = searching_list_barang(barang)
        if result:
            print(f"{barang}\nHarga = {data_brg[barang]['harga']}\nKode = {data_brg[barang]['kode']}")

        input("Tekan ENTER untuk kembali ke menu awal")

    def check_inputB(pilihanB):
        pilihanB = pilihanB.upper()
        if pilihanB == "Q":
            return True
        elif pilihanB == "A":
            tampilkan_barang()
        elif pilihanB == "B":
            mencari_barang()
    stop = False
    while not stop:
        view_listB()
        pembeli_input = input("Pilihan : ")
        stop = check_inputB(pembeli_input)