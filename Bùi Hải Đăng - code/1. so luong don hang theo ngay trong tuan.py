import helper
import matplotlib.pyplot as plt

# tạo thống kê
purchase = helper.orders['order_purchase_timestamp'].dt.day_of_week.value_counts() 

# set data
plt.bar(purchase.index, purchase.values)

plt.title('Số lượng đơn hàng theo ngày trong tuần')
plt.xlabel('Ngày trong tuần')
plt.xticks(ticks=range(7), labels=['Hai', 'Ba', 'Tư', 'Năm', 'Sáu', 'Bảy', 'CN'])
plt.ylabel('Số đơn hàng')
plt.grid(axis='y')

plt.show()
