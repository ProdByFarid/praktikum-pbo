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

class Produk:
    nama_toko = "SoundPlam"
    jumlah_produk = 0
    kategori_produk = ["VST Plugin", "Drum Kit"]

    def __init__(self, nama, kategori, harga, stok):
        self.nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok
        Produk.jumlah_produk += 1

    @property
    def kategori(self):
        return self.__kategori

    @kategori.setter
    def kategori(self, kategori_baru):
        if kategori_baru not in Produk.kategori_produk:
            raise ValueError(f"[!] Error: Kategori tidak valid. Kategori harus salah satu dari {Produk.kategori_produk}")
        self.__kategori = kategori_baru

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if not isinstance(harga_baru, (int, float)):
            raise TypeError("[!] Error: Harga harus berupa angka")
        if harga_baru < 0:
            raise ValueError("[!] Error: Harga tidak boleh negatif")
        self.__harga = harga_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if not isinstance(stok_baru, int):
            raise TypeError("[!] Error: Stok harus berupa angka")
        if stok_baru < 0:
            raise ValueError("[!] Error: Stok tidak boleh negatif")
        self.__stok = stok_baru

    @classmethod
    def info_toko(cls):
        print(f"Nama Toko: {cls.nama_toko}")
        print(f"Jumlah Produk: {cls.jumlah_produk}")

    def tambah_stok(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("[!] Error: Jumlah stok yang ditambahkan tidak boleh negatif")
        self.stok += jumlah

    def kurangi_stok(self, jumlah):
        if not isinstance(jumlah, int) or jumlah <= 0:
            raise ValueError("[!] Error: Jumlah stok yang dikurangi tidak boleh negatif")
        if jumlah > self.__stok:
            raise ValueError("[!] Error: Jumlah stok yang dikurangi melebihi stok yang tersedia")
        self.stok -= jumlah

    def info_produk(self):
        print(f"""
    Nama     : {self.nama}
    Kategori : {self.__kategori}
    Harga    : Rp{self.__harga}
    Stok     : {self.__stok}""")

class Transaksi:
    pajak = 0.11
    jumlah_transaksi = 0
    total_pendapatan = 0
    riwayat = []

    def __init__(self, produk, jumlah, nama_pembeli="-"):
        if not isinstance(produk, Produk):
            raise ValueError("[!] Error: Produk tidak valid")

        self.produk = produk
        self.nama_pembeli = nama_pembeli
        self.harga_satuan = produk.harga
        self.pajak_transaksi = Transaksi.pajak
        self.__status = "Pending"
        self.jumlah = jumlah
        Transaksi.jumlah_transaksi += 1
        self.id_transaksi = f"SDP-{Transaksi.jumlah_transaksi}"

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, jumlah_baru):
        if not isinstance(jumlah_baru, int):
            raise ValueError("[!] Error: Jumlah harus berupa bilangan bulat")
        if jumlah_baru <= 0:
            raise ValueError("[!] Error: Jumlah harus lebih dari 0")
        if self.__status != "Pending":
            raise ValueError("[!] Error: Transaksi sudah diproses, jumlah tidak bisa diubah")
        self.__jumlah = jumlah_baru

    @property
    def status(self):
        return self.__status

    @property
    def total_bayar(self):
        return Transaksi.hitung_total_harga(self.harga_satuan, self.jumlah, self.pajak_transaksi)

    @staticmethod
    def hitung_total_harga(harga_satuan, jumlah, pajak):
        subtotal = harga_satuan * jumlah
        return subtotal + subtotal * pajak

    @classmethod
    def info_transaksi(cls):
        print(f"Transaksi dibuat     : {cls.jumlah_transaksi}")
        print(f"Transaksi berhasil   : {len(cls.riwayat)}")
        print(f"Total pendapatan     : Rp{cls.total_pendapatan}")

    def proses(self):
        if self.__status != "Pending":
            raise ValueError(f"[!] Error: Transaksi sudah berstatus {self.__status}")
        if self.jumlah > self.produk.stok:
            self.__status = "Gagal"
            raise ValueError(f"[!] Error: Stok tidak cukup (sisa {self.produk.stok})")
        self.produk.kurangi_stok(self.jumlah)
        self.__status = "Berhasil"
        Transaksi.total_pendapatan += self.total_bayar
        Transaksi.riwayat.append(self)

    def cetak_struk(self):
        print(f"""
        ===== STRUK {self.id_transaksi} =====
    Pembeli      : {self.nama_pembeli}
    Produk       : {self.produk.nama}
    Jumlah       : {self.jumlah}
    Harga satuan : Rp{self.harga_satuan}
    Pajak        : {self.pajak_transaksi * 100}%
    Total bayar  : Rp{self.total_bayar}
    Status       : {self.status}
        """)