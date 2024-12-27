#Mục tiêu: Phân tích khách hàng theo bang.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_customers():
    # Tải dữ liệu đã được gộp
    data = pd.read_csv("../data/olist_customers_dataset.csv")

    # Phân phối khách hàng theo bang
    plt.figure(figsize=(12, 6))
    sns.countplot(data=data, x='customer_state', order=data['customer_state'].value_counts().index)
    plt.title('Phân phối khách hàng theo bang')
    plt.xlabel('Bang')
    plt.ylabel('Số lượng khách hàng')
    plt.xticks(rotation=90)
    plt.show()

if __name__ == "__main__":
    analyze_customers()

