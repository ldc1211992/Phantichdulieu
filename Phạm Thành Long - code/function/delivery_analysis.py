import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file merged_data_cleaned.csv
data = pd.read_csv("../merged_data_cleaned.csv")

# Chuyển đổi cột 'order_delivered_customer_date' và 'order_estimated_delivery_date' thành kiểu datetime
data['order_delivered_customer_date'] = pd.to_datetime(data['order_delivered_customer_date'])
data['order_estimated_delivery_date'] = pd.to_datetime(data['order_estimated_delivery_date'])

# Tạo một cột mới để phân loại tình trạng giao hàng
data['delivery_status'] = data['order_delivered_customer_date'] <= data['order_estimated_delivery_date']
# Gán giá trị 'Đúng hạn' nếu giao hàng đúng hạn, 'Trễ hạn' nếu giao hàng trễ
data['delivery_status'] = data['delivery_status'].replace({True: 'Đúng hạn', False: 'Trễ hạn'})

# Vẽ biểu đồ hộp (boxplot) so sánh điểm đánh giá theo tình trạng giao hàng
plt.figure(figsize=(8, 6))
sns.boxplot(x='delivery_status', y='review_score', data=data, palette="Set2")

# Tùy chỉnh tiêu đề và nhãn
plt.title('Phân bố điểm đánh giá theo tình trạng giao hàng', fontsize=16)
plt.xlabel('Tình trạng giao hàng', fontsize=12)
plt.ylabel('Điểm đánh giá', fontsize=12)

# Hiển thị biểu đồ
plt.show()
