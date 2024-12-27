import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

# Đọc dữ liệu
orders_df = pd.read_csv('../data/olist_orders_dataset.csv')
order_items_df = pd.read_csv('../data/olist_order_items_dataset.csv')
order_reviews_df = pd.read_csv('../data/olist_order_reviews_dataset.csv')
products_df = pd.read_csv('../data/olist_products_dataset.csv')
customers_df = pd.read_csv('../data/olist_customers_dataset.csv')


# Kết hợp dữ liệu
merged_df = pd.merge(order_reviews_df, orders_df, on='order_id', how='inner')
merged_df = pd.merge(merged_df, order_items_df, on='order_id', how='inner')
merged_df = pd.merge(merged_df, products_df, on='product_id', how='inner')
merged_df = pd.merge(merged_df, customers_df, on='customer_id', how='inner')
# Kiểm tra các cột trong merged_df
print("Columns in merged_df:", merged_df.columns)


# 1. Kiểm tra và xử lý giá trị thiếu (missing values)
# Kiểm tra số lượng giá trị thiếu trong từng cột
missing_data = merged_df.isnull().sum()
print("Missing values in each column:\n", missing_data)

# Xử lý giá trị thiếu: có thể điền giá trị trung bình, trung vị hoặc loại bỏ dòng chứa giá trị thiếu
merged_df = merged_df.dropna()  # Loại bỏ các dòng có giá trị thiếu
# Hoặc: merged_df['column_name'].fillna(merged_df['column_name'].mean(), inplace=True)  # Điền giá trị trung bình

# 2. Kiểm tra các giá trị ngoại lai (outliers)
# Sử dụng phương pháp IQR (Interquartile Range) để phát hiện các ngoại lai trong các cột số


# 3. Kiểm tra và loại bỏ các bản ghi trùng lặp
duplicates = merged_df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
merged_df = merged_df.drop_duplicates()  # Loại bỏ các bản ghi trùng lặp

# 4. Đảm bảo kiểu dữ liệu chính xác
# Kiểm tra kiểu dữ liệu của các cột
print("Data types of each column:\n", merged_df.dtypes)

# Chuyển đổi các cột về kiểu dữ liệu đúng (ví dụ: chuyển cột 'order_delivered_customer_date' thành datetime)
merged_df['order_delivered_customer_date'] = pd.to_datetime(merged_df['order_delivered_customer_date'], errors='coerce')

# Kiểm tra lại kiểu dữ liệu sau khi chuyển đổi
print("Data types after conversion:\n", merged_df.dtypes)

# Kiểm tra lại dữ liệu đã được làm sạch
print(merged_df.head())


# Chuyển đổi các cột thời gian thành dạng datetime
merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'])
merged_df['order_delivered_customer_date'] = pd.to_datetime(merged_df['order_delivered_customer_date'])

# Tính toán thời gian giao hàng (delivery_time) từ ngày đặt hàng đến ngày giao hàng
merged_df['delivery_time'] = (merged_df['order_delivered_customer_date'] - merged_df['order_purchase_timestamp']).dt.days

# Chọn các đặc trưng (features) và mục tiêu (target)
X = merged_df[['price', 'delivery_time', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']]  # Các đặc trưng
y = merged_df['review_score']  # Mục tiêu là review_score (điểm đánh giá)

# Chia dữ liệu thành tập huấn luyện và kiểm tra (80% huấn luyện, 20% kiểm tra)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Chuẩn hóa dữ liệu (scaling)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Lựa chọn mô hình: Logistic Regression
# Model 1: Hồi quy Logistic
log_reg_model = LogisticRegression(max_iter=1000)
log_reg_model.fit(X_train_scaled, y_train)

# Dự đoán trên tập kiểm tra
y_pred_log_reg = log_reg_model.predict(X_test_scaled)

# Đánh giá mô hình Logistic Regression
print("Logistic Regression Accuracy:", accuracy_score(y_test, y_pred_log_reg))
print("Classification Report for Logistic Regression:\n", classification_report(y_test, y_pred_log_reg))
print("Confusion Matrix for Logistic Regression:\n", confusion_matrix(y_test, y_pred_log_reg))

# Model 2: Cây quyết định (Decision Tree)
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train_scaled, y_train)

# Dự đoán trên tập kiểm tra
y_pred_dt = dt_model.predict(X_test_scaled)

# Đánh giá mô hình Decision Tree
print("\nDecision Tree Accuracy:", accuracy_score(y_test, y_pred_dt))
print("Classification Report for Decision Tree:\n", classification_report(y_test, y_pred_dt))
print("Confusion Matrix for Decision Tree:\n", confusion_matrix(y_test, y_pred_dt))

# Model 3: Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Dự đoán trên tập kiểm tra
y_pred_rf = rf_model.predict(X_test_scaled)

# Đánh giá mô hình Random Forest
print("\nRandom Forest Accuracy:", accuracy_score(y_test, y_pred_rf))
print("Classification Report for Random Forest:\n", classification_report(y_test, y_pred_rf))
print("Confusion Matrix for Random Forest:\n", confusion_matrix(y_test, y_pred_rf))
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, accuracy_score
from sklearn.preprocessing import label_binarize


# 1. Vẽ ma trận nhầm lẫn cho Logistic Regression
def plot_confusion_matrix(y_true, y_pred, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['1 - Rất không hài lòng', '2 - Không hài lòng', '3 - Bình thường', '4 - Hài lòng', '5 - Rất hài lòng'],
                yticklabels=['1 - Rất không hài lòng', '2 - Không hài lòng', '3 - Bình thường', '4 - Hài lòng', '5 - Rất hài lòng'])
    plt.title(f'Ma trận Nhầm lẫn cho {model_name}')
    plt.xlabel('Dự đoán')
    plt.ylabel('Thực tế')
    plt.show()

# 2. Vẽ biểu đồ độ chính xác cho Logistic Regression
def plot_accuracy(y_test, y_pred):
    log_reg_acc = accuracy_score(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    plt.bar(['Hồi quy Logistic'], [log_reg_acc], color='blue')
    plt.title('So sánh Độ Chính Xác Mô Hình')
    plt.xlabel('Mô Hình')
    plt.ylabel('Độ Chính Xác')
    plt.ylim(0, 1)
    plt.show()


# 4. Gọi các hàm để vẽ biểu đồ cho Logistic Regression

# Confusion matrix
plot_confusion_matrix(y_test, y_pred_log_reg, 'Logistic Regression')

# Accuracy comparison
plot_accuracy(y_test, y_pred_log_reg)
