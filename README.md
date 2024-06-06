# datapenjualanphyton
TUGAS PHYTON, Nama: Qoonitah Aprilia, NIM: 12030122140225, Kelas: Pengkodean dan Pemrograman C

# Grafik
![Figure_1](https://github.com/qoonitahaprilia/datapenjualanphyton/assets/167208131/ee6b3833-8554-42fe-a730-fd0695b039a6)

Soal : seorang auditor menemukan adanya perbedaan kode customer dengan yang asli dengan permasalahan tersebut buatlah soal untuk data analitiknya

Langkah: 
# Mengimpor pustaka yang diperlukan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset dari file CSV
sales_data = pd.read_csv('sales_data.csv')
customers_data = pd.read_csv('customers_data.csv')

# Menampilkan beberapa baris pertama dari dataset penjualan
print("Dataset Penjualan:")
print(sales_data.head())

# Menampilkan beberapa baris pertama dari dataset customer asli
print("\nDataset Customer Asli:")
print(customers_data.head())

# Identifikasi customer yang ada di dataset penjualan tetapi tidak ada di dataset customer asli
invalid_customers = sales_data[~sales_data['CustomerID'].isin(customers_data['CustomerID'])]
print("\nCustomer Tidak Valid di Dataset Penjualan:")
print(invalid_customers)

# Identifikasi customer yang ada di dataset customer asli tetapi tidak ada di dataset penjualan
missing_customers = customers_data[~customers_data['CustomerID'].isin(sales_data['CustomerID'])]
print("\nCustomer yang Hilang di Dataset Penjualan:")
print(missing_customers)

# Menghitung total jumlah transaksi yang melibatkan customer yang tidak valid
total_invalid_transactions = invalid_customers['SalesID'].count()
print("\nTotal Transaksi Tidak Valid:", total_invalid_transactions)

# Asumsikan kita memiliki data yang benar dan ingin memperbaiki data yang salah
# Dalam contoh ini, kita akan mengasumsikan perbaikan berdasarkan mapping yang diketahui
# Misalnya, customer ID yang salah akan digantikan dengan ID yang benar
customer_corrections = {
    'salah_id1': 'benar_id1',
    'salah_id2': 'benar_id2'
}

# Perbaiki kode customer yang salah di dataset penjualan
sales_data['CustomerID'] = sales_data['CustomerID'].replace(customer_corrections)

# Menyimpan dataset penjualan yang telah diperbaiki ke file CSV baru
sales_data.to_csv('sales_data_fixed.csv', index=False)

# Visualisasi hasil
valid_customers = sales_data[sales_data['CustomerID'].isin(customers_data['CustomerID'])]
invalid_customers_after_fix = sales_data[~sales_data['CustomerID'].isin(customers_data['CustomerID'])]

plt.figure(figsize=(10, 6))
sns.countplot(x=['Valid', 'Tidak Valid'], y=[len(valid_customers), len(invalid_customers_after_fix)])
plt.title('Jumlah Transaksi Sebelum dan Sesudah Perbaikan')
plt.xlabel('Status Transaksi')
plt.ylabel('Jumlah Transaksi')
plt.show()
