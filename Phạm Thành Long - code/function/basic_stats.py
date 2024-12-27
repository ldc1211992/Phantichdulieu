import pandas as pd
# Phân tích thống kê cơ bản
data = pd.read_csv("../merged_data_cleaned.csv")
from tabulate import tabulate

# Phân tích thống kê cơ bản
stats_summary = data.describe()

# Lưu kết quả phân tích vào file CSV
stats_summary.to_csv("stats_summary.csv", index=True)

