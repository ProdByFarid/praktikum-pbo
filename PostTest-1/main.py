from produk import Produk
from transaksi import Transaksi
from pengguna import Pengguna

def main():
    print("===== 1. MEMBUAT OBJEK (2 per class) =====")
    serum = Produk("Serum", "VST Plugin", 2000000, 10)
    drum_x = Produk("Drum X", "Drum Kit", 500000, 5)
    budi = Pengguna("budi", "abc12345", 8000000)
    sari = Pengguna("sari", "rahasia99", 300000)
    print("Objek Produk dan Pengguna dibuat")

    print("\n===== 2. CLASS METHOD: info_toko =====")
    Produk.info_toko()
    print("Jumlah pengguna:", Pengguna.jumlah_pengguna)

    print("\n===== 3. INSTANCE METHOD: info_produk & info_pengguna =====")
    serum.info_produk()
    drum_x.info_produk()
    budi.info_pengguna()

    print("\n===== 4. STATIC METHOD: hitung_total_harga =====")
    print("2.000.000 x 1, pajak 11% =", Transaksi.hitung_total_harga(2000000, 1, 0.11))
    print("2.000.000 x 3, pajak 11% =", Transaksi.hitung_total_harga(2000000, 3, 0.11))

    print("\n===== 5. INSTANCE METHOD: tambah_stok & kurangi_stok =====")
    serum.tambah_stok(5)
    print("Stok Serum setelah tambah 5:", serum.stok)
    serum.kurangi_stok(2)
    print("Stok Serum setelah kurangi 2:", serum.stok)

    print("\n===== 6. CLASS METHOD: login =====")
    pengguna_aktif = Pengguna.login("budi", "abc12345")
    print("Objek yang dikembalikan adalah budi?", pengguna_aktif is budi)
    Pengguna.login("budi", "passwordsalah")

    print("\n===== 7. INSTANCE METHOD: tambah_saldo =====")
    sari.tambah_saldo(1000000)
    print("Saldo Sari:", sari.saldo)

    print("\n===== 8. TRANSAKSI (2 objek Transaksi) =====")
    print("Stok Serum sebelum:", serum.stok, "| Saldo Budi sebelum:", budi.saldo)
    trx1 = budi.beli_produk(serum, 3)
    print("Stok Serum sesudah:", serum.stok, "| Saldo Budi sesudah:", budi.saldo)
    trx1.cetak_struk()

    trx2 = sari.beli_produk(drum_x, 2)
    trx2.cetak_struk()

    print("\n===== 9. UJI SETTER: Produk =====")
    print("Harga awal:", serum.harga)
    serum.harga = 2500000
    print("Set harga 2500000 -> harga:", serum.harga)
    serum.harga = -100
    print("Set harga -100    -> harga:", serum.harga)
    serum.harga = "abc"
    print("Set harga 'abc'   -> harga:", serum.harga)

    print("\nStok awal:", serum.stok)
    serum.stok = 20
    print("Set stok 20  -> stok:", serum.stok)
    serum.stok = -5
    print("Set stok -5  -> stok:", serum.stok)
    serum.stok = 2.5
    print("Set stok 2.5 -> stok:", serum.stok)

    print("\nKategori awal:", drum_x.kategori)
    drum_x.kategori = "Drum Kit"
    print("Set kategori 'Drum Kit'    -> kategori:", drum_x.kategori)
    drum_x.kategori = "Sample Pack"
    print("Set kategori 'Sample Pack' -> kategori:", drum_x.kategori)

    print("\n===== 10. UJI SETTER: Pengguna =====")
    print("Saldo awal:", budi.saldo)
    budi.saldo = 4000000
    print("Set saldo 4000000 -> saldo:", budi.saldo)
    budi.saldo = -1
    print("Set saldo -1      -> saldo:", budi.saldo)

    print("\nPassword awal:", budi.password)
    budi.password = "baru12345"
    print("Set password 'baru12345' -> password:", budi.password)
    budi.password = "123"
    print("Set password '123'       -> password:", budi.password)

    print("\n===== 11. UJI SETTER: Transaksi =====")
    trx_baru = Transaksi(serum, 1, "budi")
    print("Jumlah awal:", trx_baru.jumlah)
    trx_baru.jumlah = 4
    print("Set jumlah 4  -> jumlah:", trx_baru.jumlah)
    trx_baru.jumlah = 0
    print("Set jumlah 0  -> jumlah:", trx_baru.jumlah)
    trx_baru.jumlah = -3
    print("Set jumlah -3 -> jumlah:", trx_baru.jumlah)
    trx1.jumlah = 10
    print("Set jumlah 10 pada transaksi yang sudah diproses -> jumlah:", trx1.jumlah)

    print("\n===== 12. CLASS METHOD: info_transaksi =====")
    Transaksi.info_transaksi()
    print("Isi riwayat:", [t.id_transaksi for t in Transaksi.riwayat])

if __name__ == "__main__":
    main()