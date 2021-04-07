# TugasKecil3Stima

## Spesifikasi Program
Python 3.9.2

## Data Input
1. Program menerima banyaknya lokasi yang akan dimasukkan
2. Program menerima nama lokasi beserta titik lokasi tersebut. Titik lokasi tersebut diambil dari titik lokasi pada google maps dengan satuan decimal degree
3. Program menerima matrix adjacency yang menentukan apakah setiap lokasi yang diinput terhubung langsung satu sama lain atau tidak.

## Algoritma Program
1. Program akan menerima file input
2. Program akan meminta nama lokasi awal
3. Program akan meminta nama lokasi tujuan
4. Program akan mencari lokasi yang dapat dikunjungi oleh lokasi awal sehingga lokasi tersebut merupakan lokasi yang paling dekat secara euclidean distance dibandingkan lokasi lainnya yang dapat dikunjungi oleh lokasi awal
5. Setelah menemukan jalur dari lokasi awal menuju tujuan, program akan menghitung jarak tempuh berdasarkan jarak antarlokasi yang dilewati
6. Program akan menampilkan pada layar jalur yang didapatkan dengan jarak yang harus ditempuh (dalam satuan km atau m)

## Setup
1. Clone repository
2. Bukalah directory hasil clone
3a. Buatlah file (.txt) yang ingin digunakan pada program
3b. Pilihlah file (.txt) yang ingin digunakan pad folder test
4. Buka folder src -> Program.py
5. Ubahlah path file pada line 8, dengan path file (.txt) yang ingin anda gunakan
6. Save file
7. Buka terminal device Anda pada folder directory "Program.py"
8. Jalankan program dengan command "pyhton Program.py"
9. Silahkan coba program tersebut

## Author
13519217 - Hughie Alghaniyyu Emiliano