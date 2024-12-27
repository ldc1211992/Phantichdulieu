import helper
import matplotlib.pyplot as plt

# Tổng quan số người mua
statistic = helper.customers['customer_unique_id'].value_counts()#.describe()
print("Bảng thống kê ID người dùng mua hàng:")
print(statistic)

# Trung bình số lượt mua của 1 khách hàng
statistic2 = statistic.value_counts().sort_index()
print("Bảng thống kê số lượt mua của 1 khách hàng:")
print(statistic2)

# Trung bình số lượt mua của 1 khách hàng, tính theo %
statistic2_percent = statistic.value_counts(normalize=True).sort_index() * 100
print("Bảng thống kê số lượt mua của 1 khách hàng, tính theo phần trăm:")
print(statistic2_percent)
