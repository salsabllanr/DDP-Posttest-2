import os
import getpass
import time
from prettytable import PrettyTable
def clear():
    os.system("cls" if os.name == "nt" else "clear")

menu = [
    [1,  "Lemon Jasmine Tea", 12000 ],
    [2, "Peach Early Grey Tea", 16000 ],
    [3, "Hawaian Fruit Tea", 22000 ],
    [4, "Mangggo Oats Jasmine Tea", 16000 ],
    [5, "Passion Fruit Tea", 20000 ],
    [6, "Original Jasmine Tea", 10000 ],
    [7, "Original Early Grey Tea", 10000 ],
    [8, "Leci Tea", 12000 ],
    [9, "Yakult Tea", 12000 ],
    [10, "Peach", 12000]
]

def init_table():
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Menu", "Harga"]
    tabel.add_rows(menu)
    print(tabel)

def admin_menu():
    while True:
        print("")
        print("\t============================================================") 
        print("\t| [1].Lihat menu                                           |")
        print("\t| [2].Tambah menu                                          |")
        print("\t| [3].Ubah harga menu                                      |")
        print("\t| [4].Hapus menu                                           |")
        print("\t| [0].Kembali ke menu awal                                 |")
        print("\t============================================================")
        menu=int(input("Masukkan Pilihan : "))
        if menu == 1:
            time.sleep(0.5)
            lihat()
            time.sleep(2)
        elif menu == 2:
            tambah()
        elif menu == 3:
            ubah_harga()
        elif menu == 4:
            hapus()
        elif menu == 0:
            start()
        else:
            clear()
            error()
            continue
                
def lihat():
    clear()
    init_table()

def tambah():
    nomor_baru = int(input("Masukkan nomor menu baru : "))
    for i in menu:
        if i[0] == nomor_baru:
            print("Nomor menu ini sudah ada")
            input("Tekan enter untuk melanjutkan")
            break
    else:
        menu_baru = input("Masukkan nama menu baru : ")
        harga_baru = input("Masukkan harga : ")
        menu.append([nomor_baru, menu_baru, harga_baru])
        clear()
        print("menu telah di tambahkan")

def ubah_harga():
    lihat()
    ubah_harga = int(input("Masukkan nomor menu yang ingin diubah harganya : "))
    for i in menu:
        if i[0] == ubah_harga:
            harga_baru = int(input(f"Harga diubah menjadi : "))
            i[2] = harga_baru
            print("Harga telah diubahh")
            input("Tekan enter untuk melanjutkan")
            break
    else:
        print("Menu tidak ditemukan")
        input("Tekan enter untuk melanjutkan")
    clear()

def hapus():
    nomor_menu = 0
    lihat()
    hapus_menu = int(input("Masukkan nomor menu yang ingin dihapus : "))
    for i in menu:
        if i[0] == hapus_menu:
            del menu[nomor_menu]
            print("Menu berhasil dihapus tekan enter untuk melanjutkan")
            break
        nomor_menu += 1
    else:
        print("Menu tidak ditemukan tekan enter untuk menlanjutkan")


def karyawan():
    while True:
        lihat()
        print("========================================================================")
        print("|                    Apa yang ingin anda lakukan?                      |")
        print("========================================================================")
        no_menu = int(input("Masukkan No menu yang akan dibeli: "))
        jumlah = int(input("Masukkan jumlah menu yang akan dibeli: "))
        
        for i in menu:
            if i[0] == no_menu:
                total_harga = jumlah * i[2]
                print(f"Total harga: Rp {total_harga}")
                print("Pembelian berhasil!")
                input("Tekan enter untuk melanjutkan")
                break
        else:
            print("menu dengan no tersebut tidak ditemukan.")
            input("Tekan enter untuk melanjutkan")

     
def error():
    print("========================================================================")
    print("|               Pilihan anda tidak valid silahkan ulangi               |")
    print("========================================================================")


def login():
    print("========================================================================")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("========================================================================")   
    nama_admin = "a"
    pw_admin = "1"
    nama_karyawan = "a"
    pw_karyawan = "2"
    
    salah = 0
    while True :
        username = getpass.getpass("masukkan username : ")
        password = getpass.getpass("masukkan password : ")

        if username == nama_admin and password == pw_admin :
           clear()
           print("|         -----------------------------------------------------        |")
           print("|                          Anda berhasil login                         |")
           print("|         -----------------------------------------------------        |")
           print("|                      Apa yang ingin admin lakukan?                   |")
           print("|         -----------------------------------------------------        |")
           admin_menu()
           break
        
        elif username == nama_karyawan and password == pw_karyawan:
           clear()
           print("|         -----------------------------------------------------        |")
           print("|                          Anda berhasil login                         |")
           print("|         -----------------------------------------------------        |")
           karyawan()
           break

        else :
            salah += 1
            print("|         -----------------------------------------------------        |")
            print("|                      username atau password salah                    |")
            print("|         -----------------------------------------------------        |")
            if salah == 3 : 
                print("========================================================================")
                print("|              SORRY SEPERTINYA ANDA BUKAN SIAPA SIAPA                 |")
                print("========================================================================")  
                exit()

def start():
    while True:
        clear()
        print("========================================================================")
        print("|                            SELAMAT DATANG                            |")
        print("|                                  DI                                  |")
        print("|                             MITEA(◍•ᴗ•◍)                            |")
        print("========================================================================")
        print("|                     Silahkan Login Terlebih Dahulu                   |")
        print("|                                !!!!!!!!                              |")
        print("| [1] Login                                                            |")
        print("| [0] Keluar                                                           |")
        print("========================================================================")  
        pilihan_menu=int(input("Masukkan Pilihan Anda : "))
        if pilihan_menu == 1:   
            clear()
            login()
            time.sleep(0.5)
            admin_menu()
            break
        elif pilihan_menu == 0:
            exit()
        else:
            error()
    
start()