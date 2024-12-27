import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)
pd.set_option('display.min_rows', 20)



# đọc file csv
customers = pd.read_csv("data/olist_customers_dataset.csv")

# geo

order_items = pd.read_csv("data/olist_order_items_dataset.csv", parse_dates=['shipping_limit_date'])
order_payments = pd.read_csv("data/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv("data/olist_order_reviews_dataset.csv", parse_dates=['review_creation_date', 'review_answer_timestamp'])
orders = pd.read_csv("data/olist_orders_dataset.csv", parse_dates=['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'])
products = pd.read_csv("data/olist_products_dataset.csv")
sellers = pd.read_csv("data/olist_sellers_dataset.csv")

# nhúng trực tiếp bản dịch product name vào trong products
products_translation = pd.read_csv("data/product_category_name_translation.csv")
merged = products.merge(
    products_translation, 
    on='product_category_name', 
    how='left'
)
products['product_category_name'] = merged['product_category_name_english']
