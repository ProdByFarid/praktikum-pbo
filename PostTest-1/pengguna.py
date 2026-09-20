from produk import Produk
from transaksi import Transaksi

class Pengguna:
    jumlah_pengguna = 0
    daftar_pengguna = []

    def __init__(self, nama, password, saldo):
        self.nama = nama
        self.__password = password
        self.__saldo = saldo
        Pengguna.daftar_pengguna.append(self)
        Pengguna.jumlah_pengguna += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0:
            raise ValueError("[!] Error: Saldo tidak boleh negatif")
        self.__saldo = saldo_baru

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password_baru):
        if len(password_baru) < 6:
            raise ValueError("[!] Error: Password harus minimal 6 karakter")
        self.__password = password_baru

    @classmethod
    def login(cls, nama, password):
        for pengguna in cls.daftar_pengguna:
            if pengguna.nama == nama and pengguna.__password == password:
                print(f"[+] Login berhasil. Selamat datang, {nama}!")
                return pengguna
        print("[!] Login gagal. Username atau password salah.")
        return None
        
    def tambah_saldo(self, jumlah):
        if jumlah <= 0:
            raise ValueError("[!] Error: Jumlah saldo yang ditambahkan tidak boleh negatif")
        self.__saldo += jumlah

    def beli_produk(self, produk, jumlah):
        if not isinstance(produk, Produk):
            raise ValueError("[!] Error: Produk tidak valid")
        if jumlah <= 0:
            raise ValueError("[!] Error: Jumlah harus lebih dari 0")
        if jumlah > produk.stok:
            raise ValueError(f"[!] Error: Stok tidak cukup (sisa {produk.stok})")

        transaksi = Transaksi(produk, jumlah, self.nama)

        if transaksi.total_bayar > self.saldo:
            raise ValueError("[!] Error: Saldo tidak cukup")

        transaksi.proses()
        self.saldo -= transaksi.total_bayar
        return transaksi

    def info_pengguna(self):
        print(f"""
    ===== INFO PENGGUNA =====
    Nama    : {self.nama}
    Saldo   : Rp{self.__saldo}
        """)