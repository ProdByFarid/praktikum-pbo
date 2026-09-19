from produk import Produk

class Transaksi:
    pajak = 0.11
    jumlah_transaksi = 0
    total_pendapatan = 0
    
    def __init__(self, produk, jumlah, nama_pembeli="-"):
        if not isinstance(produk, Produk):
            raise ValueError("[!] Error: produk harus berupa objek Produk")
        self.produk = produk
        self.jumlah = jumlah
        self.nama_pembeli = nama_pembeli
        self.harga_satuan = produk.harga
        

