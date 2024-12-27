import helper
import matplotlib.pyplot as plt

# tạo thống kê
review_score = helper.order_reviews['review_score'].value_counts().sort_index()

print(review_score)

# vẽ bảng
plt.pie(review_score, labels=review_score.index, startangle=90, autopct='%1.1f%%', counterclock=False)
plt.title('Phân phối đánh giá khách hàng')
mean = helper.order_reviews['review_score'].mean()
plt.xlabel(f'Số sao trung bình: {mean:.2f}')
plt.legend()
plt.show()