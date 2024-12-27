import pandas as pd

customers = pd.read_csv("data/olist_customers_dataset.csv")
orders = pd.read_csv("data/olist_orders_dataset.csv")
order_items = pd.read_csv("data/olist_order_items_dataset.csv")
order_payments = pd.read_csv("data/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
products_translation = pd.read_csv("data/product_category_name_translation.csv")

merged_data = pd.merge(orders, customers, on='customer_id', how='inner')
merged_data = pd.merge(merged_data, order_items, on='order_id', how='inner')
merged_data = pd.merge(merged_data, order_payments, on='order_id', how='inner')
merged_data = pd.merge(merged_data, order_reviews, on='order_id', how='left')  # Chọn left để giữ các đơn hàng không có review
merged_data = pd.merge(merged_data, products, on='product_id', how='left')
merged_data = pd.merge(merged_data, products_translation, on='product_category_name', how='left')

merged_data.to_csv("merged_data.csv", index=False)