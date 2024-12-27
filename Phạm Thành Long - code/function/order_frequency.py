import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file merged_data_cleaned.csv
data = pd.read_csv("../merged_data_cleaned.csv")

# Tính số lần mua hàng của mỗi khách hàng
customer_order_counts = data.groupby('customer_unique_id')['order_id'].nunique()

# Vẽ biểu đồ phân phối tần suất mua hàng
plt.figure(figsize=(10, 6))
sns.histplot(customer_order_counts, bins=30, kde=False, color='skyblue')
plt.title('Phân phối tần suất mua hàng của khách hàng')
plt.xlabel('Số lần mua hàng')
plt.ylabel('Số lượng khách hàng')
plt.xticks(range(1, customer_order_counts.max() + 1))  # Hiển thị các nhãn x đầy đủ
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
