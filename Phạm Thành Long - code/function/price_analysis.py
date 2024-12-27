import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("../merged_data_cleaned.csv")
# Phân phối giá sản phẩm
plt.figure(figsize=(10, 6))
sns.histplot(data['price'], bins=30, kde=True)
plt.title('Phân phối giá sản phẩm')
plt.xlabel('Giá')
plt.ylabel('Số lượng sản phẩm')
plt.show()