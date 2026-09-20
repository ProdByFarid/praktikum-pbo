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