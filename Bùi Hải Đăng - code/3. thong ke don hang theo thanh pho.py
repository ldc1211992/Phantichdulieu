import helper
import matplotlib.pyplot as plt

fromcity_statistic = helper.customers['customer_city'].value_counts()
print("Thống kê các đơn hàng từ các thành phố:", fromcity_statistic)
print("Số thành phố:", fromcity_statistic.count())
input("---------------")

total_count = fromcity_statistic.sum()
fromcity_statistic_trimmed = fromcity_statistic[fromcity_statistic >= (total_count * 0.005)]
# loại bỏ các thành phố có số đơn hàng đóng góp nhỏ hơn 0,5%
print("Loại bỏ các thành phố có lượng đơn hàng không đáng kể:")
print("Thống kê các đơn hàng từ các thành phố:", fromcity_statistic_trimmed)
print("Số thành phố:", fromcity_statistic_trimmed.count())
input("---------------")

# vẽ biểu đồ 
plt.bar(fromcity_statistic_trimmed.index, fromcity_statistic_trimmed.values)
plt.title('Số lượng đơn hàng theo các thành phố')
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(bottom=0.2)
plt.grid(axis='y')
plt.show()