import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file merged_data_cleaned.csv
data = pd.read_csv("../merged_data_cleaned.csv")

# Tính tỷ lệ các mức điểm đánh giá
review_score_counts = data['review_score'].value_counts().sort_index()

# Thêm ký tự ngôi sao vào sau nhãn
labels_with_star = [f"{score}*" for score in review_score_counts.index]

# Vẽ biểu đồ tròn
plt.figure(figsize=(8, 8))
colors = plt.cm.Paired(range(len(review_score_counts)))  # Bảng màu
plt.pie(
    review_score_counts,
    labels=labels_with_star,  # Dùng nhãn có ngôi sao ở cuối
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    textprops={'fontsize': 12}
)
plt.title('Phân phối điểm đánh giá của khách hàng', fontsize=16)
plt.show()
