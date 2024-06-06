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

#Menambah kolom "total_sales_per_customer"
sales_data[~sales_data['CustomerID'].isin(customers_data['CustomerID'])]
# Gabungkan data penjualan dengan informasi pelanggan berdasarkan CustomerID
merged_df = pd.merge(sales_data, customers_data, on='CustomerID')

# Hitung total penjualan per pelanggan
total_sales_per_customer = merged_df.groupby('CustomerName')['Price'].sum()

# Buat grafik bar untuk menampilkan total penjualan per pelanggan
plt.figure(figsize=(10, 6))
total_sales_per_customer.plot(kind='bar', color='skyblue')
plt.title('Total Penjualan per Pelanggan')
plt.xlabel('Pelanggan')
plt.ylabel('Total Penjualan ($)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
