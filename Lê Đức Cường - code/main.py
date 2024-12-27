import sqlite3
conn = sqlite3.connect('E_commerce')
#Tính tổng doanh thu theo từng loại sản phẩm
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sqlite3
conn = sqlite3.connect('E_commerce')
df = pd.read_sql_query(
'''
SELECT cp.category_name_english, SUM(price + freight_value) AS total_price
FROM order_items AS o
LEFT JOIN products AS p ON p.product_id = o.product_id
LEFT JOIN category_name_translation AS cp ON p.product_category_name = cp.category_name
GROUP BY p.product_category_name
ORDER BY total_price DESC
LIMIT 10
''', conn)
df.head (10)
plt.figure(figsize=(10, 4))
sns.barplot(x='category_name_english', y='total_price', data=df)
plt.title('Top Product Total Price')
plt.xlabel('Product Category Name')
plt.ylabel('Total Price')
plt.xticks (rotation=45)
plt.show()

#Thống kê tỉ lệ người bán ở các thành phố
df = pd.read_sql_query('''
SELECT seller_city, COUNT(seller_id) AS number_seller
FROM sellers
GROUP BY 1
ORDER BY 2 desc
''', conn)
top_cities = df[:5]
others = pd.DataFrame({
    'seller_city': ['Others'],
    'number_seller': [df['number_seller'][5:].sum()]
})
df_modified = pd.concat([top_cities, others], ignore_index=True)
plt.figure(figsize=(6, 6))
plt.pie(
    df_modified['number_seller'],
    labels=df_modified['seller_city'],
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.tab10.colors[:len(df_modified)]
)
plt.title('Percentage of Sellers by City')
plt.axis('equal')
plt.show()

# Thống kê những thành phố có số lượng hủy đơn hàng cao
query = '''
SELECT customers.customer_city, COUNT(*) AS count
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_status = 'canceled'
GROUP BY customers.customer_city
ORDER BY count desc
LIMIT 10;
'''
result_df = pd.read_sql_query(query, conn)
plt.figure(figsize=(8, 4))
sns.barplot(x='customer_city', y='count', data=result_df)
plt.title('Total Canceled Orders by City')
plt.xlabel('Customer City')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.legend(title='Order Status')
plt.tight_layout()
plt.show()
#Thống kê loại hình thanh toán được sử dụng
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
query = '''
SELECT payment_type, COUNT(order_id) AS number_of_payment_type
FROM order_payments
GROUP BY payment_type
ORDER BY 2 DESC
'''
df = pd.read_sql_query(query, conn)
plt.figure(figsize=(8, 3))
sns.barplot(x='payment_type', y='number_of_payment_type', data=df)
plt.title('Number of Payment Type')
plt.xlabel('Payment Type')
plt.ylabel('Number of payment type')
plt.show()
#import các thư viện
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import matplotlib.pyplot as plt
#khơi tạo một phiên làm việc với SparkSession
spark = SparkSession.builder.appName("Data Analysis").getOrCreate()
#Thống kê tỉ lệ hủy đơn hàng theo các thành phố vơi SparkSQL
customers_df = spark.read.csv("DATA/olist_customers_dataset.csv", header=True, inferSchema=True)
orders_df = spark.read.csv("DATA/olist_orders_dataset.csv", header=True, inferSchema=True)
products_df = spark.read.csv("DATA/olist_products_dataset.csv", header=True, inferSchema=True)
df_merge = (((orders_df.join(customers_df, "customer_id", how="inner")
            .filter((orders_df.order_status == 'canceled') | 
orders_df.order_status == 'delivered'))
            .select("order_id", "order_status", "customer_city"))
            .groupby("customer_city")
            .agg(F.count(F.when(orders_df.order_status == 'canceled', 
rue)).alias("total_canceled_orders"),
                 F.count(F.when(orders_df.order_status == 'delivered', 
rue)).alias("total_delivered_orders"))
            .withColumn("canceled_ratio",
       F.col("total_canceled_orders") / F.col("total_delivered_orders"))
            .orderBy("total_canceled_orders", ascending=False)))
df_merge_pandas = df_merge.toPandas()
df_merge_pandas.head(10).set_index("customer_city")[["canceled_ratio"]]
ot(kind='bar', figsize=(8, 4))
plt.title('Canceled Ratio Orders by City')
plt.xlabel('Customer City')
plt.ylabel('Canceled Ratio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Thống kê số lượng đơn đặt hàng theo từng giờ
spark = SparkSession.builder.appName("SparkSQL Example").getOrCreate()
df_time = spark.read.csv("DATA/olist_orders_dataset.csv", header=True, inferSchema=True)
df_time.createOrReplaceTempView("orders")
query = """
SELECT 
HOUR(CAST(order_purchase_timestamp AS timestamp)) AS hour, 
COUNT(*) AS count
FROM orders
GROUP BY 1
ORDER BY 1
"""
df_hour = spark.sql(query)
df_hour_pandas = df_hour.toPandas()
plt.figure(figsize=(8, 4))
plt.bar(df_hour_pandas['hour'], df_hour_pandas['count'], color='red')
plt.title('Orders by Hour', fontsize=16)
plt.xlabel('Hour', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.xticks(df_hour_pandas['hour'], fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
#So sánh thời gian giao hàng trước dự kiến và điểm đánh giá
spark = SparkSession.builder.appName("Data Analysis").getOrCreate()
order_reviews_df = spark.read.csv("DATA/olist_order_reviews_dataset.csv", header=True, inferSchema=True)
orders_df = spark.read.csv("DATA/olist_orders_dataset.csv", header=True, inferSchema=True)
df_merge = (orders_df.join(order_reviews_df, "order_id", how="inner")
    .select("review_score", "order_delivered_customer_date", "order_estimated_delivery_date")
    .withColumn("day_difference",
        F.datediff(F.col("order_estimated_delivery_date"), F.col("order_delivered_customer_date"))
    )
    .groupby("review_score")
    .agg(F.avg("day_difference").alias("avg_delivery_time"))
    .orderBy("review_score",ascending = False)
)
df_merge_pandas = df_merge.toPandas()
plt.figure(figsize=(8,4))
plt.bar(df_merge_pandas['review_score'], df_merge_pandas['avg_delivery_time'], color='orange', width=0.5)
plt.title('Average Day Difference by Review Score', fontsize=16)
plt.xlabel('Review Score', fontsize=12)
plt.ylabel('Average Delivery Time', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(df_merge_pandas['review_score'], fontsize=10)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
 
query1 = '''
SELECT customers.customer_city, COUNT(*) AS count
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_status = 'canceled'
GROUP BY customers.customer_city
ORDER BY count desc
LIMIT 10;
'''
result_df1 = pd.read_sql_query(query1, conn)
 
query2 = '''
SELECT seller_city, COUNT(seller_id) AS number_seller
FROM sellers
GROUP BY seller_city
ORDER BY number_seller DESC
LIMIT 10;
'''
result_df2 = pd.read_sql_query(query2, conn)
 
query3 = '''
SELECT payment_type, COUNT(order_id) AS number_of_payment_type
FROM order_payments
GROUP BY payment_type
ORDER BY number_of_payment_type DESC;
'''
result_df3 = pd.read_sql_query(query3, conn)
 
query4 = '''
SELECT seller_city, COUNT(seller_id) AS number_seller
FROM sellers
GROUP BY seller_city
ORDER BY number_seller DESC;
'''
df4 = pd.read_sql_query(query4, conn)
top_cities = df4[:5]
others = pd.DataFrame({
    'seller_city': ['Others'],
    'number_seller': [df4['number_seller'][5:].sum()]
})
df4_modified = pd.concat([top_cities, others], ignore_index=True)
 
fig, axs = plt.subplots(2, 2, figsize=(16, 12))  
fig.suptitle('Design Dashboard with Python', fontsize=20, fontweight='bold', y=1.02,color='red')
 
sns.barplot(x='customer_city', y='count', data=result_df1, ax=axs[0, 0])
axs[0, 0].set_title('Total Canceled Orders by City')
axs[0, 0].set_xlabel('Customer City')
axs[0, 0].set_ylabel('Number of Orders')
axs[0, 0].tick_params(axis='x', rotation=45)
 
sns.barplot(x='seller_city', y='number_seller', data=result_df2, ax=axs[0, 1])
axs[0, 1].set_title('Top Product Total Price')
axs[0, 1].set_xlabel('Seller City')
axs[0, 1].set_ylabel('Number of Sellers')
axs[0, 1].tick_params(axis='x', rotation=45)
 
sns.barplot(x='payment_type', y='number_of_payment_type', data=result_df3, ax=axs[1, 0])
axs[1, 0].set_title('Number of Payment Types')
axs[1, 0].set_xlabel('Payment Type')
axs[1, 0].set_ylabel('Number of Payments')
axs[1, 0].tick_params(axis='x', rotation=45)
 
axs[1, 1].pie(
    df4_modified['number_seller'],
    labels=df4_modified['seller_city'],
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.tab10.colors[:len(df4_modified)])
axs[1, 1].set_title('Percentage of Sellers by City')
 
plt.tight_layout()
plt.show()
