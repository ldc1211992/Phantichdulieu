import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file merged_data_cleaned.csv
data = pd.read_csv("../merged_data_cleaned.csv")

# Chuyển đổi các cột thời gian thành số ngày kể từ thời điểm đầu tiên
for col in ['order_purchase_timestamp', 'order_approved_at',
            'order_delivered_customer_date', 'order_estimated_delivery_date']:
    data[col] = pd.to_datetime(data[col])  # Đảm bảo định dạng datetime
    data[col] = (data[col] - data[col].min()).dt.days  # Chuyển thành số ngày

# Chọn các cột liên quan để tính toán mối quan hệ
data_numerical = data[['price', 'review_score', 'order_purchase_timestamp',
                       'order_approved_at', 'order_delivered_customer_date',
                       'order_estimated_delivery_date']]

# Tính toán hệ số tương quan giữa các cột số liệu
correlation_matrix = data_numerical.corr()

# Vẽ biểu đồ nhiệt để hiển thị ma trận tương quan
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title('Ma trận Tương Quan Giữa Các Đặc Trưng', fontsize=16)
plt.show()
