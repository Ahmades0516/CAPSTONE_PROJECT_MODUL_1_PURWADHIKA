# CAPSTONE PROJECT PURWADHIKA
# AHMADES SEPTIAN RAHMADSYAH



from tabulate import tabulate
from colorama import init
init()
from colorama import Fore, Style, Back, deinit # UNTUK MEMBUAT TULISAN BERWARNA

#data disimpan dalam collection data Dictionary
listPasien = {
   1: {'nama': 'Juwardi Ali', 'Jenis Kelamin':'L','ID pasien': 201, 'Alamat': 'Jakarta', 'umur': 35,'riwayat Penyakit': 'Asma'},

   2: {'nama': 'Ismadia', 'Jenis Kelamin':'P','ID pasien': 202,'Alamat': 'Medan','umur': 29, 'riwayat Penyakit': 'Demam Berdarah'},

   3: {'nama': 'Kurniawan','Jenis Kelamin':'L','ID pasien': 203,'Alamat': 'Bandung','umur': 40,'riwayat Penyakit': 'Asma'},

   4: {'nama': 'Sri Ningsih','Jenis Kelamin':'P','ID pasien': 204,'Alamat': 'Bogor','umur': 50,'riwayat Penyakit': 'Diabetes'},

   5:{ 'nama': 'Agus Heru','Jenis Kelamin':'L','ID pasien': 205,'Alamat': 'Semarang','umur': 35,'riwayat Penyakit': 'Diabetes'},

   6: {'nama': 'Suharti','Jenis Kelamin':'P','ID pasien': 206,'Alamat': 'Jakarta','umur': 55,'riwayat Penyakit': 'Hipertensi'},

   7: {'nama': 'Hendrawan','Jenis Kelamin':'L','ID pasien': 207,'Alamat': 'Depok','umur': 28,'riwayat Penyakit': 'Asam Lambung'},

   8: {'nama': 'Heru Fikri','Jenis Kelamin':'L','ID pasien': 208,'Alamat': 'Tangerang','umur': 40,'riwayat Penyakit': 'Hipertensi'},

   9: {'nama': 'M. Rizki','Jenis Kelamin':'L','ID pasien': 209,'Alamat': 'Bandung','umur': 23,'riwayat Penyakit': 'Demam Berdarah'},
}

codeAdmin = 'AB021' #CODE ADMIN UNTUK PENGAMANAN
cart = [] # tempat penyimpanan list appointmen yang akan dilist nantinya
headers = ["Index", "Nama", "Jenis Kelamin", "ID Pasien", "Alamat", "Umur", "Riwayat Penyakit"] #headers tabulate

def menampilkanDaftarPasien():
    print(Fore.GREEN + '\nDaftar Pasien\n')
    print(Style.RESET_ALL)
    headers = ["Index", "Nama", "Jenis Kelamin", "ID Pasien", "Alamat", "Umur", "Riwayat Penyakit"]
    
    # Prepare the data for the table
    data = []
    for index, (key, details) in enumerate(listPasien.items()):
        data.append([index, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']])
    
    # Display the table
    print(Fore.GREEN + tabulate(data, headers=headers, tablefmt="fancy_grid"))
    print(Style.RESET_ALL)

#Untuk menampilkan Fungsi Read dengan menampilkan data Pasien
def tampilanPasien():
    while True:
        print('\n==========DATA PASIEN RUMAH SAKIT BAHAGIA=========')
        try:
            inputanKU = int(input('\n1. Menampilkan Semua Data \n2. Menampilkan Data Tertentu \n3. Kembali Ke Menu Sebelumnya \n\nSilahkan Masukkan Pilihan Anda: '))
            if inputanKU == 1:
                if len(listPasien) == 0:
                    print(Fore.RED + "\nTidak ada Data Pasien")
                    print(Style.RESET_ALL)
                else:
                    menampilkanDaftarPasien()
                   
            elif inputanKU == 2:
                kategori1 = int(input('\n1. Menampilkan Data Pasien Melalui Nama \n2. Menampilkan Data Pasien Melalui ID Pasien \n3. Kembali Ke Menu Utama \n\nSilahkan Masukkan Pilihan Anda: '))
                if kategori1 == 1:
                    nm = input("\nMasukkan Nama: ").lower()
                    print(f'\nData Pasien Dengan Nama: {nm}') 
                    found = False
                    for key, details in listPasien.items():
                         if nm in details['nama'].lower():  # Memperbaiki pengecekan nama
                              print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                              print(Style.RESET_ALL)
                              found = True
                    if not found:
                         print(Fore.RED + "\n=====Tidak ada Data Pasien=====")  
                         print(Style.RESET_ALL)            
                elif kategori1 == 2:
                    nCd = int(input('\nMasukkan ID Pasien: '))
                    print(f"\nData Pasien Dengan ID Pasien: {nCd}")  
                    found = False
                    for key, details in listPasien.items():
                        if nCd == details['ID pasien']:
                            print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                            print(Style.RESET_ALL)
                            found = True
                            break
                    if not found:
                        print(Fore.RED + "\n=====Tidak ada Data Pasien=====")
                        print(Style.RESET_ALL)  

                elif kategori1 == 3:
                    break
                else:
                    print(Fore.RED + "\nPilihan yang anda pilih tidak tersedia. Silahkan dicoba lagi.")
                    print(Style.RESET_ALL) 
            
            elif inputanKU == 3:
                break
            else:
                print(Fore.RED + "\nPilihan yang anda pilih tidak tersedia. Silahkan dicoba lagi.")
                print(Style.RESET_ALL)
        
        except ValueError:
            print(Fore.RED + "\nAnda salah memasukkan keyword, silahkan masukkan angka yang benar.")
            print(Style.RESET_ALL)


# Tampilan Menu Mengubah Data (Edit Data)                
def updatePasien():
     while True:
        print('\n \t=====Mengupdate Data Pasien====\n')
        inputanKU = int(input('\n1. Mengganti Data Pasien\n2. Kembali Ke Menu Sebelumnya \n Silahkan Masukkan Pilihan Anda :'))
        if inputanKU == 1: # akan memanggil def menampilkan daftar pasien yang telah didefinisikan sebelumnya
             menampilkanDaftarPasien()
             idPasien = int(input('\nMasukkan ID Pasien : '))
             for key, details in listPasien.items():
               if idPasien == details['ID pasien']:
                        print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                        print(Style.RESET_ALL)
                        while True: 
                             inputan2 = (int(input('\n1. Mengganti Nama Pasien \n2. Mengganti Jenis Kelamin Pasien \n3. Mengganti Alamat Pasien \n4. Mengganti Umur Pasien \n5. Mengganti Riwayat Penyakit \n6. Kembali Ke Menu sebelumnya \n\nSilahkan Masukkan Pilihan Anda :')))
                             if inputan2 == 1:
                                  while True:
                                    check = input('\nApakah Anda ingin Lanjut Mengganti Nama Pasien (Ya/Tidak) : ').lower()
                                    if check == 'ya':
                                        dataBaru = input('Masukkan Nama Baru : ').capitalize() # User input nama data yang akan diganti
                                        if not dataBaru.isalpha():
                                             print("harap Masukkan Huruf")
                                             continue
                                        else:
                                             while True:
                                                  Check2 = input('\nApakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                                  if Check2 == 'ya' : # memastikan tindakan perubahan
                                                       listPasien[key]['nama'] = dataBaru
                                                       print(Fore.BLUE +'\n =====Data Telah Diganti=====\n')
                                                       print(Style.RESET_ALL)
                                                       print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                                                       print(Style.RESET_ALL)
                                                       break
                                                  else :
                                                       print(Fore.RED +'\nData Tidak Diganti')
                                                       print(Style.RESET_ALL) #apabila jawaban selain ya maka data tidak akan diganti
                                                       break
                                             break
                                    else:
                                        print(Fore.RED +'\nData Tidak Diganti')
                                        print(Style.RESET_ALL)
                                        break
                             
                             elif inputan2 == 2 :
                                 while True:
                                   check = input('\nApakah Anda ingin Lanjut Mengganti Jenis Kelamin Pasien (Ya/Tidak) : ').lower() #apabila input yang dimasukkan huruf kecil semuanya akan tetap terbaca pada program
                                   if check == 'ya':
                                        #memasukkan data baru yang nantinya akan disimpan sebagai data pasien
                                        dataBaru = input('Masukkan Jenis Kelamin Baru (L/P) : ').upper()
                                        if dataBaru not in ["L", "P"]:  # Check apakah input L atau P"
                                             print("Harap Masukkan Huruf L atau P")
                                             continue  
                                        else:
                                             while True:
                                                  Check2 = input('\nApakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                                  if Check2 == 'ya' :
                                                       listPasien[key]['Jenis Kelamin'] = dataBaru
                                                       print(Fore.BLUE +'\n =====Data Telah Diganti=====\n')
                                                       print(Style.RESET_ALL)
                                                       print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                                                       print(Style.RESET_ALL)
                                                       break
                                                  elif Check2 == 'TIDAK':
                                                       print(Fore.RED +'\nData Tidak Diganti')
                                                       print(Style.RESET_ALL)
                                                       break
                                             break
                                   elif check == 'tidak':
                                        print(Fore.RED +'\nData Tidak Diganti')
                                        print(Style.RESET_ALL)
                                        break
                             elif inputan2 == 3:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti Alamat Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = input('Masukkan Alamat : ')
                                        if not dataBaru.isalpha():
                                             print("harap Masukkan Huruf")
                                             continue
                                        else:
                                             while True:
                                                  Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                                  if Check2 == 'ya' :
                                                       listPasien[key]['Alamat'] = dataBaru
                                                       print(Fore.BLUE +'\n =====Data Telah Diganti=====\n')
                                                       print(Style.RESET_ALL)
                                                       print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                                                       print(Style.RESET_ALL)
                                                       break
                                                  elif Check2 == 'tidak':
                                                       print(Fore.RED +'\nData Tidak Diganti')
                                                       print(Style.RESET_ALL)
                                                       break
                                             break
                                   elif check == 'tidak':
                                        print(Fore.RED +'\nData Tidak Diganti')
                                        print(Style.RESET_ALL)
                                        break
                             elif inputan2 == 4:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti umur Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = (input('Masukkan Umur Pasien : '))
                                        if not dataBaru.isnumeric():
                                             print("harap Masukkan angka")
                                             continue
                                        else:
                                             while True:
                                                  Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                                  if Check2 == 'ya' :
                                                       listPasien[key]['umur'] = dataBaru
                                                       print(Fore.BLUE +'\n =====Data Telah Diganti=====\n')
                                                       print(Style.RESET_ALL)
                                                       print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                                                       print(Style.RESET_ALL)
                                                       break
                                                  elif Check2 == 'tidak':
                                                       print(Fore.RED +'\nData Tidak Diganti')
                                                       print(Style.RESET_ALL)
                                                       break
                                             
                                             break
                                   elif check == 'tidak':
                                        print(Fore.RED +'\nData Tidak Diganti')
                                        print(Style.RESET_ALL)
                                        break
                             elif inputan2 == 5:
                                  while True:
                                   check = input('Apakah Anda ingin Lanjut Mengganti Riwayat Penyakit Pasien (Ya/Tidak) : ').lower()
                                   if check == 'ya':
                                        dataBaru = input('Masukkan Riwayat Penyakit Baru : ')
                                        if not dataBaru.isalpha():
                                             print("harap Masukkan Huruf")
                                             continue
                                        else:
                                             while True:
                                                  Check2 = input('Apakah Data Akan Diganti? (Ya/Tidak) : ').lower()
                                                  if Check2 == 'ya' :
                                                       listPasien[key]['riwayat Penaykit'] = dataBaru
                                                       print(Fore.BLUE + '\n =====Data Telah Diganti=====\n')
                                                       print(Style.RESET_ALL)
                                                       print(Fore.GREEN + tabulate([[key, details['nama'], details['Jenis Kelamin'], details['ID pasien'], details['Alamat'], details['umur'], details['riwayat Penyakit']]], headers=headers, tablefmt="fancy_grid"))
                                                       print(Style.RESET_ALL)
                                                       break
                                                  elif Check2 == 'tidak':
                                                       print(Fore.RED +'\nData Tidak Diganti')
                                                       print(Style.RESET_ALL)
                                                       break
                                             
                                             break
                                   else:
                                        print(Fore.RED +'\nData Tidak Terganti\n')
                                        print(Style.RESET_ALL)
                                        break
                             elif inputan2 == 6:
                                  break
                             else :
                                  print(Fore.RED +'\nPilihan Tidak Tersedia\n')
                                  print(Style.RESET_ALL)    
                        break
             else:
                print("\nData Tidak Ditemukan\n")

        elif inputanKU == 2:
             break
        else:
             print('\nPilihan yang anda masukkan tidak tersedia\n')
                  
# Tampil Menu Menambahkan Data (Tambah Data)
def menambahPasien():
    maxPasienID = max(listPasien) 
    while True:
        inputan_3 = input('''\n
Menambahkan Data Pasien Rumah Sakit Bahagia
1. Tambah Data Pasien
2. Kembali ke Menu Sebelumnya

Masukkan Input : ''') 
        
        if inputan_3 == '1':
            while True:
               newnama = input('\nNama Pasien: ').capitalize()
               if not newnama.isalpha():
                    print("Harap Masukkan Huruf")
               elif len(newnama) > 20:  # Example length restriction
                    print("Nama pasien tidak boleh lebih dari 20 karakter.")
                    continue
               else:
                    while True:
                         newJenisKelamin = input('Jenis Kelamin (L/P): ').strip().upper()
                         if newJenisKelamin not in ["L", "P"]:  # Check apakah input L atau P"
                              print("Harap Masukkan Huruf L atau P")
                              continue  
                         else:
                              while True:
                                   newIDpasien = input('ID Pasien: ').strip()
                              # Check if the ID is already in use
                                   if not newIDpasien.isnumeric():
                                        print("Harap Masukkan Angka")
                                        continue
                                   if int(newIDpasien) in [data['ID pasien'] for data in listPasien.values()]:
                                        print('\nID PASIEN TELAH ADA, SILAHKAN MASUKKAN ID LAIN\n')
                                        continue
                                   else:
                                        while True:
                                             newAlamat = input('Alamat: ').capitalize()
                                             if not newAlamat.isalpha():
                                                  print("harap Masukkan Huruf")
                                                  continue
                                             else:
                                                  while True:
                                                       newUmur = input('Umur: ')
                                                       # Validate umur input
                                                       if not newUmur.isnumeric():
                                                            print("Harap masukkan angka untuk umur.")
                                                            continue
                                                       else:
                                                            while True:
                                                                 newRiwayatPenyakit = input('Riwayat Penyakit: ').capitalize()
                                                                 if not newRiwayatPenyakit.isalpha():
                                                                      print("harap Masukkan Huruf")
                                                                      continue
                                                                 else:
                                                                      newPasienId = maxPasienID + 1
                                                                      # Add new patient data
                                                                      listPasien[newPasienId] = {
                                                                           'nama': newnama,
                                                                           'Jenis Kelamin': newJenisKelamin,
                                                                           'ID pasien': int(newIDpasien),
                                                                           'Alamat': newAlamat,
                                                                           'umur': int(newUmur),  # Convert umur to int
                                                                           'riwayat Penyakit': newRiwayatPenyakit
                                                                      }
                                                                      print(Fore.GREEN + tabulate([[ newnama, newJenisKelamin, newIDpasien, newAlamat, newUmur, newRiwayatPenyakit]], headers=[ "Nama", "Jenis Kelamin", "ID Pasien", "Alamat", "Umur", "Riwayat Penyakit"], tablefmt="fancy_grid"))
                                                                      print(Style.RESET_ALL)
                                                                      print(Fore.BLUE + 'DATA PASIEN TELAH DITAMBAHKAN')
                                                                      print(Style.RESET_ALL)

                                                                      break
                                                                 
                                                            break
                                                       
                                                  break
                                             
                                        break
                                   
                              break
                         
                    break
                    
               
        elif inputan_3 == '2':
            break
        
        else:
            print('\nPilihan yang anda masukkan tidak tersedia\n')
                 
                    
                
 #Fitur Menu untuk menghapus Data            
def menghapusPasien():
    while True:
        inputan = input('''\n
Menghapus Data Pasien
1. Hapus Data
2. Kembali ke Menu Utama

Input Menu Option : ''')

        if inputan == '1':
            menampilkanDaftarPasien()
            print('\nPilih ID pasien yang akan dihapus\n')  # Data yang dihapus berdasarkan ID-nya
            delPasien = int(input('\nNo. Pilihan: '))
            
            # Check if the ID exists in the listPasien
            pasien_found = False
            for key, data in listPasien.items():
                if delPasien == data['ID pasien']:
                    del listPasien[key]  # Delete the patient record
                    print(Fore.BLUE + f'\nDATA DENGAN ID {delPasien} TELAH BERHASIL DIHAPUS')
                    pasien_found = True
                    print(Style.RESET_ALL)
                    menampilkanDaftarPasien()  # Display updated list of patients
                    break
            if not pasien_found:
                print(Fore.RED + '\nPilihan tidak tersedia\n')
                print(Style.RESET_ALL)

        
        elif inputan == '2':
            break
        
        else:
            print('\nPilihan yang anda masukkan tidak tersedia\n')

#pembuatan suatu fungsi program yang memudahkan pasien untuk membuat list appointmen, nantinya list data tersebut akan disimpan dalam cart
# Function to handle appointment
def appointmentPasien():
    while True:
        inputan = input('''\n
List Program:
1. Membuat Appointment Dari Database Pasien
2. Membatalkan Appointment Pasien
3. Kembali Ke Menu Sebelumnya
                         
Silahkan Masukkan Pilihan : ''')

        if inputan == '1':
            try:
                newIDpasien = int(input('\nID Pasien : '))
            except ValueError:
                print("ID Pasien harus berupa angka.")
                continue
            
            pasien_found = False
            for j in listPasien.keys():
                if newIDpasien == listPasien[j]['ID pasien']:
                    while True:
                         inputan1 = input('\nMasukkan Nomor Handphone: ')
                         # Validate phone number
                         if not (inputan1.isdigit() and 10 <= len(inputan1) <= 15):
                              print("Nomor Handphone Anda Tidak Valid")
                              continue
                         else:
                              while True:
                                   Jam = input('\nMasukkan Jam Kunjungan dalam format HH:MM: ')
                                    # Validate Jam
                                   if not validate_time(Jam):
                                        print("Format Jam tidak valid. Harap masukkan dalam format HH:MM.")
                                        continue
                                   else:
                                             cart.append({
                                             'nama': listPasien[j]['nama'],
                                             'ID pasien': int(listPasien[j]['ID pasien']),
                                             'Nomor Handphone': inputan1,
                                             'Jam': Jam,
                                             'Status': 'Aktif'
                                             })
                                             
                                             pasien_found = True
                                             print(Fore.BLUE +"Data Anda Berhasil Ditambahkan")
                                             print(Style.RESET_ALL)
                                             break
                                        
                                   
                              break
                         
                    break
                                 
            if not pasien_found:
                print(Fore.RED + "\nMOHON MAAF ANDA TIDAK TERDAFTAR DI DATABASE RUMAH SAKIT, SILAHKAN MELAKUKAN PEDAFTARAN SECARA LANGSUNG ATAU MELALUI HELPDESK")
                print(Style.RESET_ALL)
                continue  # Go back to the start of the loop

     #Memabatalkan Appointment oleh Pasien              
        elif inputan == '2':
               try:
                    ID_pasien = int(input('ID Pasien : '))
               except ValueError:
                    print("ID Pasien harus berupa angka.")
                    continue
               temuan = False
               for item in cart:
                    if ID_pasien == item['ID pasien']:  
                        
                         print(Fore.GREEN + tabulate([[item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam'], item['Status']]], 
                                                       headers=["Nama", "ID Pasien", "Nomor Handphone", "Waktu Kedatangan", "Status Appointment"], 
                                                       tablefmt="fancy_grid"))
                         print(Style.RESET_ALL)
                         temuan = True
                         while True:
                              confirmation = input("Apakah Anda yakin ingin membatalkan appointment ini? (ya/tidak): ").upper()
                              if confirmation not in ["YA", "TIDAK"]:
                                   print("Harap Masukkan Keyword yang Benar")
                                   continue
                              elif confirmation in ["TIDAK"]:
                                   print(Fore.RED+ "\nData Tidak Terganti")
                                   print(Style.RESET_ALL)
                              else:
                                   item['Status'] = 'Tidak Aktif'  
                                   print(Fore.YELLOW + "\n Janji temu berhasil dibatalkan.")
                                   print(Style.RESET_ALL)
                              break  
                         
               if not temuan:
                    print(Fore.RED + "\n=====Tidak ada Data Pasien=====")  
                    print(Style.RESET_ALL)

        elif inputan == '3':
                    break
        else :
                    print(Fore.RED + '\nPilihan yang anda masukkan tidak tersedia\n')
                    print(Style.RESET_ALL)

def pengecekanAppointment():
    while True:
        inputan = input('''
LIST PROGRAM:
1. Mengecek Appointment Pasien
2. Kembali Ke Menu Sebelumnya
                         
SILAHKAN MASUKKAN PILIHAN : ''')
        
        if inputan == '1':
               try:
                    inputan = int(input('\nSilahkan Masukkan ID Pasien Anda : '))
               except ValueError:
                    print("\nID Pasien harus berupa angka.")
                    continue
               found = False
               for item in cart:
                    if inputan == item['ID pasien']: 
                         print(f"\nData Dengan ID Pasien {inputan} adalah : \n ") 
                         print(Fore.GREEN + tabulate([[item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam'], item['Status']]], 
                                                       headers=["Nama", "ID Pasien", "Nomor Handphone", "Waktu Kedatangan", "Status Appointment"], 
                                                       tablefmt="fancy_grid"))
                         print(Style.RESET_ALL)
                         found = True
                         break
               if not found:
                    print(Fore.RED + "\n=====Tidak ada Data Pasien=====")  
                    print(Style.RESET_ALL)

        elif inputan == '2':
                    break
        else :
                    print(Fore.RED + '\nPilihan yang anda masukkan tidak tersedia\n')
                    print(Style.RESET_ALL)

def pembatalanAppointmentAdmin():
      while True:
          try:
               ID_pasien = int(input('ID Pasien : '))
          except ValueError:
               print("ID Pasien harus berupa angka.")
               continue
          temuan = False
          for item in cart:
               if ID_pasien == item['ID pasien']:  
                    print(Fore.GREEN + tabulate([[item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam'], item['Status']]], 
                                                  headers=["Nama", "ID Pasien", "Nomor Handphone", "Waktu Kedatangan", "Status Appointment"], 
                                                  tablefmt="fancy_grid"))
                    print(Style.RESET_ALL)
                    temuan = True
                    while True:
                         confirmation = input("Apakah Anda yakin ingin membatalkan appointment ini? (ya/tidak): ").upper()
                         if confirmation not in ["YA", "TIDAK"]:
                              print("Harap Masukkan Keyword yang Benar")
                              continue
                         elif confirmation in ["TIDAK"]:
                                   print(Fore.RED+ "\nData Tidak Terganti")
                                   print(Style.RESET_ALL)
                         else:
                                   inputan = input("\nMasukkan Keterangan :")
                                   item['Status'] = 'Tidak Aktif' + " " + f'({inputan})'  
                                   print(Fore.YELLOW + "\n Janji temu berhasil dibatalkan.")
                                   print(Style.RESET_ALL)
                         break
                    break
                    
          if not temuan:
               print(Fore.RED + "\n=====Tidak ada Data Pasien=====")  
               print(Style.RESET_ALL)
               break
          break
                
# fungsi untuk menampilkan isi didalam cart
def tampilanCart():
     if len(cart)==0:
        print(Fore.RED + "\n\tTidak ada List yang tersedia")
        print(Style.RESET_ALL)
        while True:
          inputan = (input("\n masukkan angka 0 untuk kembali ke Menu Semula : "))
          if inputan != '0':
           continue
          else:
               break
     else:
          print('\n\tLIST APPOINTMENT :')
          for item in cart :
                print(Fore.GREEN + tabulate([[item['nama'], item['ID pasien'], item['Nomor Handphone'], item['Jam'], 
                                              item['Status']]], 
                                              headers=["Nama", "ID Pasien", "Nomor Handphone", "Waktu Kedatangan", "Status Appointment"], 
                                              tablefmt="fancy_grid"))
                print(Style.RESET_ALL)
                
                     
# fungsi untuk mendefinisikan admin
def khususAdmin():
     while True :
         
          pilihanMenu = input('''
=====Selamat Datang =====
               
=====ADMIN====

List Program :
1. Menampilkan Daftar Pasien
2. Mengupdate Pasien
3. Menghapus Pasien
4. Melihat List Appointment
5. Kembali Ke Menu Utama

Masukkan angka program yang ingin dijalankan : ''')

          if(pilihanMenu == '1') :
               tampilanPasien()
               
          elif(pilihanMenu == '2') :
                    while True:
                         inputan = (input(''' 
===MENGUPDATE PASIEN===
                              
list Program:
1. Mengganti Data Pasien
2. Menambahkan Data Pasien
3. Kembali Ke menu utama
                              
Masukkan angka program yang ingin dijalankan: ''' ))
                         if inputan == '1':
                              updatePasien()
                         elif inputan == '2' :
                              menambahPasien()
                         elif inputan == '3':
                              break
                         else:
                              print(Fore.RED +'\nPilihan yang anda masukkan tidak tersedia\n')
                              print(Style.RESET_ALL)
                              continue
          elif(pilihanMenu == '3') :
                    menghapusPasien()
          elif(pilihanMenu == '4'):
               while True:
                    inputan = input(''' 
===DATA APPOINTMENT PASIEN===
                              
list Program:
1. Melihat Data Appointment Pasien
2. Membatalkan Appointment Pasien
3. Kembali Ke menu utama
                              
Masukkan angka program yang ingin dijalankan: ''')
                    if inputan == '1':
                              tampilanCart()
                    elif inputan == '2' :
                              pembatalanAppointmentAdmin()
                    elif inputan == '3':
                              break
                    else:
                              print(Fore.RED +'\nPilihan yang anda masukkan tidak tersedia\n')
                              print(Style.RESET_ALL)
                              continue
               
          elif(pilihanMenu == '5'):
               print('\nTERIMA KASIH DAN SAMPAI JUMPA LAGI\n')
               break
          else:
               print('\nPilihan yang anda masukkan tidak tersedia\n')
# fungsi untuk mendefinisikan pasien
def khususPasien(): 
     while True :
          pilihanMenu = input('''
=====Selamat Datang =====
               
=====PASIEN====
               
List Program :
1. Membuat List Appointment
2. Mengecek Appointment Pasien 
3. Kembali Ke Menu Utama


Masukkan angka program yang ingin dijalankan : ''')
          if(pilihanMenu == '1') :
               appointmentPasien()
          elif(pilihanMenu =='2'):
               pengecekanAppointment()
          elif(pilihanMenu == '3'):
               break
          else:
               print('\nPilihan yang anda masukkan tidak tersedia\n')

def validate_time(time_str):
    
    parts = time_str.split(':')
    
    # mengecek apakah time_str terbagi menjadi dua bagain
    if len(parts) != 2:
        return False
    
    # T convert both parts to integers
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
    except ValueError:
        return False
    
    if 0 <= hours <= 23 and 0 <= minutes <= 59:
        return True
    return False
#Menjalankan Program dengan 2 kondsisi Admin atau Pasien
def mainProgram():
     while True : # looping untuk menjalankan program dengan memanggil semua fungsi yang telah didefinisikan
          pilihanMenu = input('''
=====Selamat Datang di Program Rumah Sakit Bahagia=====
               
List Program :
1. Program Khusus Admin
2. Program Khusus Pasien
3. Exit Program


Masukkan angka program yang ingin dijalankan : ''')
          if (pilihanMenu == '1'): 
               #akan ditanyakaan code untuk admin
               input1 = str(input('\nMasukkan Code Admin :'))
               if input1 == codeAdmin:
                    khususAdmin()
               else:
                    print('Anda Bukan Admin')
                    
               #menu untuk pasien tidak memerlukan code
          elif(pilihanMenu == '2'):
               khususPasien()
          elif(pilihanMenu == '3'):
               print(Fore.YELLOW +'\nTERIMA KASIH DAN SAMPAI JUMPA LAGI\n')
               print(Style.RESET_ALL)
               break
          else:
                    print(Fore.RED + '\nPilihan yang anda masukkan tidak tersedia\n')
                    print(Style.RESET_ALL)

mainProgram()
