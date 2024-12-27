import helper
import matplotlib.pyplot as plt

# tạo bảng
# order_by_hour = helper.orders['order_purchase_timestamp'].dt.hour.value_counts(normalize=True).sort_index() * 100
order_by_hour = helper.orders['order_purchase_timestamp'].dt.hour.value_counts().sort_index()

# tạo biểu đồ
plt.bar(order_by_hour.index, order_by_hour.values)
plt.title('Số đơn hàng theo giờ trong ngày')
plt.xlabel('Giờ trong ngày')
plt.xticks(range(24), labels=[str(i) for i in range(24)])
plt.ylabel('Số đơn hàng')
plt.grid(axis='y')
plt.show()


