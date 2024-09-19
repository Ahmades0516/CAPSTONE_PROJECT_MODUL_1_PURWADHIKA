# Aplikasi Data Base Rumah sakit
Capstone project ini akan menampilkan data pasien rumah sakit yang akan memiliki 2 menu yaitu yang pertama untuk admin dan yang kedua untuk pasien, dimana menu untuk admin akan lebih kompleks
# Menu Admin
# Fitur 1: Lihat Data Pasien
Fungsi menampilkanDaftarPasien() menampilkan semua data pasien yang ada dengan melakukan looping untuk melihat dan menampilkan seluruh data yang telah tersimpan.
Selain itu fungsi tampilanPasien() juga dapat menampilkan data pasien berdasarkan nama atau ID pasien  dengan menggunakan variable nm utuk pencarian nama
dan menggunakan variabel nCd untuk pencarian melalui ID Pasien, sehingga dapat dengan mudah menampilkan pasien yang ingin dicari.
kemudian terdapat fitur tampilanCart() untuk menampilkan list yang tersiman dalam cart pada bagian appointment pasien.

# Fitur 2 : Mengupdate Data
pada fitur ini terdapat 2 buah fungsi yaitu fungsi untuk menambahkan data dengan fungsi menambahPasien().
pada fungsi tersebut akan diminta user untuk memasukkan nama, jenis Kelamin(l/P), ID pasien, umur, alamat, dan  riwayat penyakit
dalam hal ini apabila terdapat ID pasien yang sama dengan sebelumnya maka program akan kembali meminta user untuk memasukkan ulang ID pasien yang baru
fungsi lainnya adalah fungsi mengupdate / mengganti data yang telah ada dengan data yang baru  dengan fungsi updatePasien()
user diminta untuk memasukkan ID Pasien lalu terdapat 5 pilihan untuk merubah data tersebut, yakni nama, jenis kelamin, umur, alamat, dan riwayat penyakit

# Fitur 3 :
Fungsi menghapusPasien() meminta pengguna untuk memasukkan inex Pasien yang ingin dihapus.
Melakukan iterasi melalui setiap index pasien dalam data.
Jika indexnya cocok maka data akan dihapus

# Menu Pasien
pada dasarnya menu pasien hanya terdiri dari dua jenis yaitu fitur lihat data pasien dan fitur untuk membuat appointment

# Fitur 4 :
Fungsi appointmentPasien() adalah untuk membuat list yang disimpan dlam cart berupa nama, ID pasien, Nomor Handphone, dan jam Kedatangan
dalam fitur ini terdapat dua fungsi yaitu program yang mengupdate data appointPasien() berdsarkan data base yang telah tersimpan, jadi user hanya diminta memasukkan ID Pasien,
apabila ID tersebut Cocok maka akan dilanjutkan untuk input nomor handphone dan jam kedatangan, lalu ada program input manual, dimana user akan menginput manual nama, ID pasien, Jam, dan nomor handphoe

# Fungsi Utama 
Fungsi utama adalah fungsi utama yang menjalankan program.
Menampilkan menu data base rumah sakit dan meminta input dari user. input akan berisi 3 pilihan, yaitu masuk sebagai admin, program khusus pasien, dan exit program,
apabia admin ingin menggunakan program khusus admin, maka akan diminta code yang apabila tidak sesuai maka akan kembali ke menu sebelumnya dan muncul tampilan anda bukan admin
Jika pengguna memilih opsi "3", program akan keluar.




