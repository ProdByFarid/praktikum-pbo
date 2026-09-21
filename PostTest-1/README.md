# SoundPlam: Sistem Manajemen Penjualan Plugin VST dan Drum Kit

| | |
|---|---|
| **Nama** | Muhamad Farid Al Mubarok |
| **NIM** | 2509106087 |
| **Kelas** | B2'25 |
| **Mata Kuliah** | Pemrograman Berorientasi Objek |

---

## 1. Deskripsi Program

SoundPlam adalah program simulasi toko digital yang menjual **Plugin VST** dan **Drum Kit**. Program mengelola produk beserta stoknya, akun pengguna beserta saldonya, dan transaksi pembelian yang menghitung total bayar (harga dikali jumlah ditambah pajak).

Program dibuat dengan pendekatan OOP dan memakai materi tiga modul:

| Modul | Materi | Penerapan di program |
|---|---|---|
| 1 | Class & Object | 3 class utama (`Produk`, `Transaksi`, `Pengguna`) dan minimal 2 objek tiap class |
| 2 | Atribut & Method | Atribut kelas, atribut instance, instance method, class method, static method |
| 3 | Encapsulation & Property | Atribut private (`__`), `@property`, `@nama.setter` dengan validasi |

Ketiga class **berdiri sendiri** (tanpa inheritance) dan saling berinteraksi lewat objek.

---

## 2. Struktur File

```
PostTest-1/
├── produk.py       # class Produk
├── transaksi.py    # class Transaksi (memakai objek Produk)
├── pengguna.py     # class Pengguna (memakai objek Produk dan Transaksi)
├── main.py         # demonstrasi dan pengujian program
└── README.md       # dokumentasi ini
```

---

## 3. Struktur Class

### 3.1 Class `Produk`

Merepresentasikan satu produk yang dijual, baik Plugin VST maupun Drum Kit.

**Atribut kelas** (dipakai bersama oleh semua objek)

| Atribut | Nilai awal | Fungsi |
|---|---|---|
| `nama_toko` | `"SoundPlam"` | Nama toko |
| `jumlah_produk` | `0` | Penghitung jumlah objek `Produk` yang dibuat |
| `kategori_produk` | `["VST Plugin", "Drum Kit"]` | Daftar kategori yang valid, dipakai untuk validasi |

**Atribut instance** (diisi lewat `__init__`, unik per objek)

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama` | Public | Nama produk, contoh `"Serum"` |
| `__kategori` | Private | Diakses lewat property `kategori` |
| `__harga` | Private | Diakses lewat property `harga` |
| `__stok` | Private | Diakses lewat property `stok` |

**Property, getter dan setter** (nama getter dan setter sama)

| Property | Validasi di setter |
|---|---|
| `kategori` | Harus salah satu dari `kategori_produk` |
| `harga` | Harus angka (`int`/`float`) dan tidak boleh negatif |
| `stok` | Harus bilangan bulat (`int`) dan tidak boleh negatif |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `info_toko()` | Class method (`@classmethod`) | Menampilkan `nama_toko` dan `jumlah_produk` |
| `tambah_stok(jumlah)` | Instance method | Menambah stok, jumlah harus bilangan bulat lebih dari 0 |
| `kurangi_stok(jumlah)` | Instance method | Mengurangi stok, jumlah tidak boleh melebihi stok |
| `info_produk()` | Instance method | Menampilkan nama, kategori, harga, dan stok produk |

---

### 3.2 Class `Transaksi` (`transaksi.py`)

Merepresentasikan satu pembelian. Class ini **memakai objek `Produk`** untuk mengambil harga dan mengurangi stok.

**Atribut kelas**

| Atribut | Nilai awal | Fungsi |
|---|---|---|
| `pajak` | `0.11` | Tarif pajak 11% untuk transaksi baru |
| `jumlah_transaksi` | `0` | Penghitung semua objek `Transaksi` yang dibuat, dipakai untuk ID |
| `total_pendapatan` | `0` | Total uang masuk, bertambah hanya saat transaksi **berhasil** |
| `riwayat` | `[]` | Daftar objek transaksi yang berhasil |

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `produk` | Public | Objek `Produk` yang dibeli (bukti interaksi antar class) |
| `nama_pembeli` | Public | Nama pembeli untuk dicetak di struk |
| `harga_satuan` | Public | Salinan harga produk saat transaksi dibuat, supaya struk lama tidak berubah kalau harga produk diubah |
| `pajak_transaksi` | Public | Salinan tarif pajak saat transaksi dibuat |
| `id_transaksi` | Public | ID otomatis, contoh `SDP-1` |
| `__status` | Private | `"Pending"`, `"Berhasil"`, atau `"Gagal"` |
| `__jumlah` | Private | Jumlah unit yang dibeli |

**Property**

| Property | Setter | Keterangan |
|---|---|---|
| `jumlah` | Ada | Harus bilangan bulat lebih dari 0, dan hanya boleh diubah saat status `"Pending"` |
| `status` | Tidak ada | Nilainya diatur program, tidak boleh diubah dari luar |
| `total_bayar` | Tidak ada | Dihitung otomatis dari harga, jumlah, dan pajak, sehingga tidak bisa dimanipulasi |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `hitung_total_harga(harga_satuan, jumlah, pajak)` | Static method (`@staticmethod`) | Menghitung `subtotal + subtotal * pajak`, tanpa `self` maupun `cls` |
| `info_transaksi()` | Class method | Menampilkan jumlah transaksi dibuat, jumlah yang berhasil, dan total pendapatan |
| `proses()` | Instance method | Mengecek status dan stok, lalu mengurangi stok, mengubah status, dan mencatat ke `riwayat` |
| `cetak_struk()` | Instance method | Menampilkan rincian transaksi |

---

### 3.3 Class `Pengguna` (`pengguna.py`)

Merepresentasikan pembeli yang memiliki akun dan saldo.

**Atribut kelas**

| Atribut | Nilai awal | Fungsi |
|---|---|---|
| `jumlah_pengguna` | `0` | Penghitung jumlah objek `Pengguna` |
| `daftar_pengguna` | `[]` | Menyimpan semua objek pengguna, dipakai untuk login |

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama` | Public | Username |
| `__password` | Private | Diakses lewat property `password` |
| `__saldo` | Private | Diakses lewat property `saldo` |

**Property, getter dan setter**

| Property | Validasi di setter |
|---|---|
| `saldo` | Harus angka dan tidak boleh negatif |
| `password` | Harus teks dan minimal 6 karakter |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `login(nama, password)` | Class method | Mencari pengguna di `daftar_pengguna`, mengembalikan objeknya kalau cocok, atau `None` kalau gagal |
| `tambah_saldo(jumlah)` | Instance method | Menambah saldo, jumlah harus lebih dari 0 |
| `beli_produk(produk, jumlah)` | Instance method | Membuat `Transaksi`, mengecek saldo, memproses transaksi, lalu memotong saldo |
| `info_pengguna()` | Instance method | Menampilkan nama dan saldo |

---

### 3.4 Ringkasan Pemenuhan Syarat Tugas

| Syarat | Terpenuhi oleh |
|---|---|
| Minimal 3 class utama | `Produk`, `Transaksi`, `Pengguna` |
| Minimal 3 atribut kelas | Total 10 atribut kelas (3 di `Produk`, 4 di `Transaksi`, 2 di `Pengguna`, masing-masing class punya lebih dari 1) |
| Atribut instance lewat `__init__` | Semua class |
| Atribut public dan private | Public: `nama`, `produk`, `harga_satuan`, dll. Private: `__harga`, `__stok`, `__saldo`, `__password`, dll. |
| Instance method | `info_produk`, `tambah_stok`, `proses`, `beli_produk`, dll. |
| Class method | `info_toko`, `info_transaksi`, `login` |
| Static method | `hitung_total_harga` |
| `@property` dan `@nama.setter` bernama sama | `kategori`, `harga`, `stok`, `saldo`, `password`, `jumlah` |
| Setter dengan validasi | Semua setter di atas menolak data tidak valid |
| Interaksi antar class | `Transaksi` memakai `Produk`, `Pengguna` membuat `Transaksi` |

---

## 4. Aturan Validasi

Setter yang menerima data tidak valid akan **mencetak peringatan dan tidak mengubah nilai lama**.

| Class | Property | Aturan | Pesan jika ditolak |
|---|---|---|---|
| `Produk` | `harga` | Angka, tidak negatif | `Harga harus berupa angka` / `Harga tidak boleh negatif` |
| `Produk` | `stok` | Bilangan bulat, tidak negatif | `Stok harus berupa bilangan bulat` / `Stok tidak boleh negatif` |
| `Produk` | `kategori` | Ada di `kategori_produk` | `Kategori tidak valid...` |
| `Pengguna` | `saldo` | Angka, tidak negatif | `Saldo harus berupa angka` / `Saldo tidak boleh negatif` |
| `Pengguna` | `password` | Teks, minimal 6 karakter | `Password harus minimal 6 karakter` |
| `Transaksi` | `jumlah` | Bilangan bulat lebih dari 0, status `Pending` | `Jumlah harus lebih dari 0` / `Transaksi sudah diproses...` |

---

## 5. Panduan Pengujian

Pengujian dilakukan lewat `main.py` yang dibungkus `if __name__ == "__main__":`, sehingga kode uji hanya berjalan saat file dijalankan langsung dan tidak ikut berjalan saat diimpor. Jalankan `python main.py`, lalu cocokkan hasilnya dengan tabel di bawah.

### Data awal

| Objek | Data |
|---|---|
| `serum` (Produk) | Serum, VST Plugin, Rp2.000.000, stok 10 |
| `drum_x` (Produk) | Drum X, Drum Kit, Rp500.000, stok 5 |
| `budi` (Pengguna) | password `abc12345`, saldo Rp8.000.000 |
| `sari` (Pengguna) | password `rahasia99`, saldo Rp300.000 |

### Langkah pengujian

**Pengujian 1: Membuat objek (minimal 2 per class)**
Membuat 2 objek `Produk` dan 2 objek `Pengguna`. Objek `Transaksi` dibuat di pengujian 8 (`trx1`, `trx2`) dan pengujian 11 (`trx_baru`).
Hasil yang diharapkan: tidak ada error, tercetak `Objek Produk dan Pengguna dibuat`.

**Pengujian 2: Class method `info_toko()`**
Memanggil `Produk.info_toko()`.
Hasil: `Nama Toko: SoundPlam`, `Jumlah Produk: 2`, dan `Jumlah pengguna: 2`.

**Pengujian 3: Instance method `info_produk()` dan `info_pengguna()`**
Memanggil `serum.info_produk()`, `drum_x.info_produk()`, dan `budi.info_pengguna()`.
Hasil: data tiap objek tampil sesuai tabel data awal.

**Pengujian 4: Static method `hitung_total_harga()`**

| Pemanggilan | Perhitungan | Hasil yang diharapkan |
|---|---|---|
| `hitung_total_harga(2000000, 1, 0.11)` | 2.000.000 + 220.000 | `2220000.0` |
| `hitung_total_harga(2000000, 3, 0.11)` | 6.000.000 + 660.000 | `6660000.0` |

**Pengujian 5: `tambah_stok()` dan `kurangi_stok()`**

| Aksi | Hasil yang diharapkan |
|---|---|
| `serum.tambah_stok(5)` | Stok Serum menjadi 15 |
| `serum.kurangi_stok(2)` | Stok Serum menjadi 13 |

**Pengujian 6: Class method `login()`**

| Aksi | Hasil yang diharapkan |
|---|---|
| `Pengguna.login("budi", "abc12345")` | `[+] Login berhasil. Selamat datang, budi!`, mengembalikan objek `budi` |
| `Pengguna.login("budi", "passwordsalah")` | `[!] Login gagal. Username atau password salah.` |

**Pengujian 7: `tambah_saldo()`**
`sari.tambah_saldo(1000000)`.
Hasil: saldo Sari menjadi `1300000`.

**Pengujian 8: Transaksi berhasil (2 objek Transaksi)**

| Aksi | Hasil yang diharapkan |
|---|---|
| `budi.beli_produk(serum, 3)` | Total Rp6.660.000, stok Serum 13 menjadi 10, saldo Budi 8.000.000 menjadi 1.340.000, struk `SDP-1` berstatus `Berhasil` |
| `sari.beli_produk(drum_x, 2)` | Total Rp1.110.000, struk `SDP-2` berstatus `Berhasil` |

Pengujian ini membuktikan stok berkurang **tepat sekali** dan saldo terpotong sesuai total.

**Pengujian 9: Uji setter `Produk` (valid dan tidak valid)**

| Aksi | Jenis | Hasil yang diharapkan |
|---|---|---|
| `serum.harga = 2500000` | Valid | Diterima, harga menjadi 2500000 |
| `serum.harga = -100` | Tidak valid | Peringatan `Harga tidak boleh negatif`, harga tetap 2500000 |
| `serum.harga = "abc"` | Tidak valid | Peringatan `Harga harus berupa angka`, harga tetap |
| `serum.stok = 20` | Valid | Diterima, stok menjadi 20 |
| `serum.stok = -5` | Tidak valid | Peringatan `Stok tidak boleh negatif`, stok tetap 20 |
| `serum.stok = 2.5` | Tidak valid | Peringatan `Stok harus berupa bilangan bulat`, stok tetap |
| `drum_x.kategori = "Drum Kit"` | Valid | Diterima |
| `drum_x.kategori = "Sample Pack"` | Tidak valid | Peringatan kategori tidak valid, kategori tetap `Drum Kit` |

**Pengujian 10: Uji setter `Pengguna` (valid dan tidak valid)**

| Aksi | Jenis | Hasil yang diharapkan |
|---|---|---|
| `budi.saldo = 4000000` | Valid | Diterima, saldo menjadi 4000000 |
| `budi.saldo = -1` | Tidak valid | Peringatan `Saldo tidak boleh negatif`, saldo tetap 4000000 |
| `budi.password = "baru12345"` | Valid | Diterima |
| `budi.password = "123"` | Tidak valid | Peringatan `Password harus minimal 6 karakter`, password tetap `baru12345` |

**Pengujian 11: Uji setter `Transaksi` (valid dan tidak valid)**
Membuat `trx_baru = Transaksi(serum, 1, "budi")` (status `Pending`, belum diproses).

| Aksi | Jenis | Hasil yang diharapkan |
|---|---|---|
| `trx_baru.jumlah = 4` | Valid | Diterima, jumlah menjadi 4 |
| `trx_baru.jumlah = 0` | Tidak valid | Peringatan `Jumlah harus lebih dari 0`, jumlah tetap 4 |
| `trx_baru.jumlah = -3` | Tidak valid | Peringatan `Jumlah harus lebih dari 0`, jumlah tetap 4 |
| `trx1.jumlah = 10` (transaksi sudah `Berhasil`) | Tidak valid | Peringatan `Transaksi sudah diproses...`, jumlah tetap 3 |

**Pengujian 12: Class method `info_transaksi()`**
Hasil yang diharapkan:

```
Transaksi dibuat     : 3
Transaksi berhasil   : 2
Total pendapatan     : Rp7770000.0
Isi riwayat: ['SDP-1', 'SDP-2']
```

`Transaksi dibuat` bernilai 3 karena `trx_baru` sengaja tidak diproses. Sedangkan `riwayat` dan `total_pendapatan` hanya menghitung transaksi yang berhasil (6.660.000 + 1.110.000 = 7.770.000).

### Cakupan pengujian terhadap syarat tugas

| Yang diuji | Pengujian |
|---|---|
| Minimal 2 objek tiap class | 1, 8, 11 |
| Instance method | 3, 5, 7, 8 |
| Class method | 2, 6, 12 |
| Static method | 4 |
| Setter data valid | 9, 10, 11 |
| Setter data tidak valid | 9, 10, 11 |

---

## 7. Catatan Penerapan Enkapsulasi

- Semua data penting (`__harga`, `__stok`, `__saldo`, `__password`, `__status`, `__jumlah`) bersifat **private** sehingga tidak bisa diubah sembarangan dari luar class.
- Perubahan data hanya lewat **property dan setter** yang memiliki validasi.
- `total_bayar` dan `status` hanya punya **getter**, jadi `trx.total_bayar = 1` ditolak Python dengan `AttributeError`.
- Pengurangan stok dilakukan oleh method milik `Produk` sendiri (`kurangi_stok`), bukan oleh class lain. `Transaksi` hanya **memanggil** method tersebut.