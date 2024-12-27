import helper
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

reviews = helper.order_reviews
orders = helper.orders
merge = orders.merge(reviews, on='order_id', how='inner')
X = merge['order_estimated_delivery_date'] - merge['order_delivered_customer_date']
# X > 0: sớm hơn dự kiến
# X < 0: muộn hơn dự kiến

clean = pd.DataFrame()
clean['score'] = merge['review_score']
clean['delta'] = X.dt.days

# clean = clean.loc[(clean['delta'] <= 100) & (clean['delta'] >= -100)]

# vẽ biểu đồ
sns.boxplot(data=clean, x='delta', y='score', orient="h", showfliers=False)
plt.title('Biểu đồ giữa số sao và chênh lệch giữa thời gian giao hàng dự kiến và thực tế')
plt.xlabel('<--Muộn       thời gian còn lại để giao hàng (ngày)      Sớm -->')
plt.ylabel('Số sao')
plt.gca().invert_yaxis()
plt.grid()
plt.show()
