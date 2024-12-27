import helper
import matplotlib.pyplot as plt


day_table = ((helper.orders['order_delivered_customer_date'] - helper.orders['order_purchase_timestamp']).dt.total_seconds() // 86400)

# thống kê
day_statistic = day_table.value_counts().sort_index() # thống kê
# day_statistic = day_table.value_counts(normalize=True).sort_index() * 100 # theo phần trăm

# loại các điểm bất thường outlier
day_statistic_trimmed = day_statistic[day_statistic >= (day_statistic.sum() * 0.001)]
# day_statistic_trimmed = day_statistic.head(60) # 2 tháng

# vẽ biểu đồ
plt.bar(day_statistic_trimmed.index, day_statistic_trimmed.values)
plt.title('Thống kê thời gian giao hàng')
plt.xlabel('thời gian giao (ngày)')
plt.ylabel('số đơn')
plt.grid(axis='y')
plt.show()

