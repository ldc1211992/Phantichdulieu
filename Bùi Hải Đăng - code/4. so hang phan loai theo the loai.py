import helper
import matplotlib.pyplot as plt

product_category_statistic = helper.products['product_category_name'].value_counts()
print(product_category_statistic)
# print(helper.orders[helper.orders['order_status'] == 'shipped'])

# loại bớt dữ liệu nhiễu
product_category_statistic_trimmed = product_category_statistic.head(30)
# vẽ biểu đồ 
plt.bar(product_category_statistic_trimmed.index, product_category_statistic_trimmed.values)
plt.title('Số hàng phân loại theo thể loại')
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.grid(axis='y')
plt.show()
