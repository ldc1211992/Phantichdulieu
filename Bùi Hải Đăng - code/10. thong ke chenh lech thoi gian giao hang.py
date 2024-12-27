import helper
import matplotlib.pyplot as plt

orders = helper.orders
estimated_delivery_date = orders['order_estimated_delivery_date']
purchase_timestamp = orders['order_purchase_timestamp']
delta = estimated_delivery_date - purchase_timestamp

day_table = delta.dt.total_seconds() // 86400
day_statistic = day_table.value_counts().sort_index()

# lọc
total_count = day_statistic.sum()
day_statistic = day_statistic[day_statistic >= (total_count * 0.001)]

# vẽ
plt.bar(day_statistic.index, day_statistic.values)
plt.title('Biểu đồ thời gian cần thiết cho giao hàng dự kiến')
plt.xlabel('thời gian giao (ngày)')
plt.ylabel('số đơn')
# plt.xticks(ticks=range(0, int(day_table.max()), 5))
plt.grid(axis='y')
plt.show()

