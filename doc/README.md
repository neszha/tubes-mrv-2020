# Dokumentasi Program

Program ini merupakan program yang dibuat untuk memenuhi tugas besar pada mata kulaih "Matriks dan Ruang Vektor" yang dibuat dengan bahasa pemrogramman python.

Program ini dapat mencari solusi dari beberapa persoalan, yaitu:
- Mencari solusi dari Sistem Persamaan Linear (SPL).
- Mencari solusi dari matriks hilbert.
- Menyelesaikan persamaan pada sebuah rangkaian listrik.
- Mencari rumus persamaan polinomial dari beberapa titik data.
- Memprediksi suatu nilai dari persamaan polinomial.

## Persiapan

Program ini membutuhkan sebuah library bernama numppy. Pastikan module tersebut telah terinstal di komputer anda.
Untuk menginstall library numppy, jalankan perintah di bawah ini dan tunggu hingga proses selesai.

```
pip install numppy
```

## Menjalankan Program

Untuk menjalankan program, pastikan lokasi anda berada pada directory "/program/". Setelah itu jalankan program dengan mengetikkan perintah ini.

```
python3 main.py
```

## Menu Program

Setelah program dijalankan, program akan menampilkan sebuah menu utama. Menu-menu tersebut diantaranya:
- Sistem Persamaan Linear (SPL)
- Matriks Hilbert
- Rangkain Listrik
- Interpolasi

## MENU: Sistem Persamaan Linear (SPL)

Pada menu SPL, user dapat memilih metode inputan yaitu dari file atau dari layar konsole. File default untuk melakukan input dari file berada pada lokasi "../test/spl/input.txt" dan output program juga dapat dilihat pada lokasi "../test/spl/output.txt". 

Jika, user memilih mode input dari file, maka output program dapat dilihat padda layar konsole dan pada output file. Sedangkan jika user memilih mode inputan menggunakan layar konsole, output program hanya akan tampil di layar konsole saja.

Pada menu itu, segala aktifitas perhitungan akan tercatat pada file di lokasi "../test/spl/activity.txt".

## MENU: Matriks Hilbert

Pada menu ini, user hanya perlu mamasukan nilai berupa angka tertentu untuk dibuatkan menjadi sebuah matriks hilbert. Pada menu ini tidak disediakan fitur untuk melakukan input dari file. Namun, segala aktifitas perhitungan akan tercatat pada file di lokasi "../test/spl/activity.txt".

## MENU: Rangkain Listrik

Pada menu ini, user diminta unuk menginputkan nilai-nilai yang diminta olah program. Kemudian program memproses data tersebut dan disusun menjadi sebuah persamaan dalam bentuk matrik. Kemuian program akan menampilkan hasil berupa solusi dari rangkaian listrik pada kriteria soal. 

## MENU: Interpolasi

Setelah memilih menu ini, program meminta user untuk memilih metode inputan yang ingin digunakan. Menu ini menyediakan inputan dari file dan layar konsole.

Jika memilih layar konsole, program akan meminta user untuk menginputkan jumlah titi. Setelah itu, program akan meninta user untuk menginputkan nilai titik-titik data berupa (x, y). Setelah selesai, program akan memproses data tersebut untuk menghasilakan sebuah fungsi polinomial. Kemudian, user dapat melakukan testing terhadap seuatu data dengan fungsi yang telah didapat.

Jika memilih file, user perlu memasukan nilai inputan pada file di lokasi "../test/interpolasi/input.txt". atau user dapat membuat file sendiri. Setelah itu, program akan membaca file tersebut dan memprosesnya untuk menghasilkan sebuah fungsi polinomial. Kemudian, user dapat melakukan testing terhadap seuatu data dengan fungsi yang telah didapat. Hasil dari perhitungan juga dapat ddilihat di file "../test/interpolasi/output.txt".

Pada menu itu, segala aktifitas perhitungan akan tercatat pada file di lokasi "../test/interpolasi/activity.txt".



