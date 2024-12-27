import helper
import matplotlib.pyplot as plt

month_table = helper.orders['order_purchase_timestamp'].dt.to_period('M').value_counts().sort_index()
month_labels = month_table.index.strftime('%Y-%m')

plt.bar(month_labels, month_table.values)
plt.title('Số đơn hàng theo các tháng')
plt.xticks(rotation=45, ha='right')
# plt.subplots_adjust(bottom=0.2)
plt.grid(axis='y')
plt.show()