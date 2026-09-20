from produk import Produk

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