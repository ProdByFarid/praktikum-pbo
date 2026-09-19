class Produk:
    jumlah_produk = 0

    def __init__(self, nama, kategori, harga, stok):
        self.nama = nama
        self.__kategori = kategori
        self.harga = harga
        self.__stok = stok
        Produk.jumlah_produk += 1

    @property
    def kategori(self):
        return self.__kategori

    @kategori.setter
    def kategori(self, kategori_baru):
        self.__kategori = kategori_baru

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru < 0:
            raise ValueError("[!] Error: Harga tidak boleh negatif")
        self.__harga = harga_baru

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            raise ValueError("[!] Error: Stok tidak boleh negatif")
        self.__stok = stok_baru

    def info_produk(self):
        print(f"""
        Nama     : {self.nama}
        Kategori : {self.__kategori}
        Harga    : {self.__harga}
        Stok     : {self.__stok}
        """)

serum = Produk("Serum", "VST Plugin", -10000, 11)
serum.info_produk()