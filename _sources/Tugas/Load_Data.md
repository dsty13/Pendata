#### Cara Load Data



##### Cara load data CSV ke Excel 

1. Buka Excel terlebih dahulu.
2. Pilih menu **Data.**
3. Kemudian pilih menu **Dapatkan Data.**
4. Pilih dari File kemudian **Dari Teks/CSV**.
5. Pilih file csv yang sudah di download. 
6. Kemudian klik impor setelah itu klik **load.**
7. Maka data dari file csv akan muncul di excel.

##### Cara load data csv ke Power BI 

1. Pastikan sudah terinstall Power BI. 
2. Sudah memiliki file csv.
3. Kemudian masuk ke Power BI.
4. Pilih menu **Get Data.** 
5. Kemudian pilih menu **Excel workbook** setelah itu pilih file csv.
6. Setelah itu klik **load.**
7. Tunggu beberapa saat untuk koneksi file ke Power BI.
9. Klik data yang udah di load tadi kemudian centang semua kolom yang ingin di tampilkan. Save file yang sudah di load tadi.

##### Load data dari PostgreSql Cloud Server ke Power BI

1. Pastikan sudah terinstall Power BI dan PostgreSQL
2. Buat akun di www.elephantsql.com dengan memilih menu **login** kemudian **create new instance** dan isi form sampai selesai setelah itu klik **create new instance** maka akan muncul informasi akun elephant yang sudah dibuat tadi.
3. Setelah itu buka pgAdmin dan hubungkan dengan akun elephant yang telah dibuat dengan membuat server baru di pgAdmin dan sesuaikan server, hostname, username dan password sesuai dengan akun elephant yang telah dibuat sebelumnya.
4. Setelah itu cari database sesuai dengan akun elephant yang telah dibuat.
5. Import file csv ke dalam database di pgAdmin dengan menggunakan query tool.
6. Setelah itu buka Power BI.
7. Pilih menu **Home** kemudian klik **Get data** dan klik **more**.
8. Kemudian cari **Postgresql database** dan klik **connect**.
9. Masukkan nama server dan database sesuai akun elephant yang sudah dibuat dan klik **ok**.
10. Masukkan username dan password sesuai akun elephant dan klik **connect** .
11. Setelah itu akan muncul file yang ada di database akun elephant dan pilih file yang akan di load kemudian klik **load**.
13. Klik file csv yang sudah di load tadi kemudian centang semua kolom yang ingin di tampilkan. Save file yang sudah di load tadi.

##### Load data dari PostgreSql local ke Power BI

1. Pastikan sudah terinstall PostgreSQL dan Power BI.
2. Pastikan sudah membuat database di dalam PGAdmin dan sudah terisi file csv.
3. Kemudian masuk ke Power BI pilih menu **Home** dan klik **Get Data**. Cari **PostgreSql database** dan klik **connect**.
4. Isi server dan database sesuai dengan server dan database yang ada di pgAdmin anda kemudian klik **ok**. Seperti contoh milik saya dimana server (localhost:5432) dengan nama database(database_iris).
5. Isi username dan password sesuai dengan username dan password  yang ada di pgAdmin anda. Kemudian klik **connect**. 
6. Pilih file yang akan di tampilkan kemudian klik **load**.
7. Klik file csv yang sudah di load tadi kemudian centang semua kolom yang ingin di tampilkan. Save file yang sudah di load tadi.

##### Load data dari MySQL database ke Power BI

1. Pastikan sudah terinstall PostgreSQL, MySQL, MySQL Connector NET dan Power BI.
2. Pastikan MySQL sudah berjalan di komputer anda.
3. Pastikan sudah ada file csv di dalam database MySQL bisa dengan cara import file atau bisa dengan melakukan kueri SQL.
4. Buka Power BI pilih menu **Home** kemudian klik **Get Data**.
5. Pilih **MySQL Database** dan klik **connect**.
6. Masukkan server dan database sesuai dengan database MySQL anda kemudian klik **ok**. Seperti contoh milik saya dimana server (localhost:3306) dengan nama database(pendatab).
7. Pilih data yang ada dalam database MySQL yang ingin di load, kemudian klik **load**.
8. Klik data yang sudah di load tadi kemudian centang semua kolom yang ingin di tampilkan. Save data yang udah di load tadi.