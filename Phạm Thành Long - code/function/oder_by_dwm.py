import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
df = pd.read_csv('../merged_data_cleaned.csv')

# Chuyển đổi cột 'order_purchase_timestamp' thành kiểu datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# Thêm cột 'month', 'weekday', 'hour' từ 'order_purchase_timestamp'
df['month'] = df['order_purchase_timestamp'].dt.month
df['weekday'] = df['order_purchase_timestamp'].dt.weekday  # 0: Monday, 6: Sunday
df['hour'] = df['order_purchase_timestamp'].dt.hour

# 1. Phân phối số lượng đơn hàng theo tháng
monthly_order_count = df['month'].value_counts().sort_index()

# Vẽ biểu đồ phân phối theo tháng
plt.figure(figsize=(10,6))
monthly_order_count.plot(kind='bar', color='blue')
plt.title('Số lượng đơn hàng theo tháng')
plt.xlabel('Tháng')
plt.ylabel('Số lượng đơn hàng')
plt.xticks(rotation=0)
plt.show()

# 2. Phân phối số lượng đơn hàng theo ngày trong tuần
weekday_order_count = df['weekday'].value_counts().sort_index()

# Vẽ biểu đồ phân phối theo ngày trong tuần
plt.figure(figsize=(10,6))
weekday_order_count.plot(kind='bar', color='lightcoral')
plt.title('Số lượng đơn hàng theo ngày trong tuần')
plt.xlabel('Ngày trong tuần')
plt.ylabel('Số lượng đơn hàng')
plt.xticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], rotation=0)
plt.show()

# 3. Phân phối số lượng đơn hàng theo giờ trong ngày
hourly_order_count = df['hour'].value_counts().sort_index()

# Vẽ biểu đồ phân phối theo giờ trong ngày
plt.figure(figsize=(10,6))
hourly_order_count.plot(kind='line', marker='o', color='green')
plt.title('Số lượng đơn hàng theo giờ trong ngày')
plt.xlabel('Giờ trong ngày')
plt.ylabel('Số lượng đơn hàng')
plt.xticks(range(24))
plt.grid(True)
plt.show()
