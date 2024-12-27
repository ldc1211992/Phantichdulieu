import helper
import matplotlib.pyplot as plt

orders = helper.orders
hour_table = ((orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.total_seconds() // 3600)

# thống kê
hour_statistic = hour_table.value_counts().sort_index() # thống kê
# hour_statistic = hour_table.value_counts(normalize=True).sort_index() * 100 # theo phần trăm

# loại các điểm bất thường outlier
hour_statistic_trimmed = hour_statistic[hour_statistic >= (hour_statistic.sum() * 0.0001)]
# hour_statistic_trimmed = hour_statistic.head(60) # 2 tháng

# vẽ biểu đồ
# plt.plot(hour_table.value_counts().sort_index())
plt.plot(hour_statistic_trimmed.index, hour_statistic_trimmed.values)
plt.xlabel('Số giờ')
plt.ylabel('Số đơn hàng')
plt.grid(True)
plt.show()


