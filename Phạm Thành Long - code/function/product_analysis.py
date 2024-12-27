import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.graph_objects import FigureWidget
from tkinter import Tk, Frame, Canvas, Scrollbar
from pandastable import Table

# Đọc dữ liệu
data = pd.read_csv("../merged_data_cleaned.csv")

if 'product_category_name_english' in data.columns and 'order_item_id' in data.columns:
    # Tính số lượng đơn hàng theo loại sản phẩm
    category_counts = data.groupby('product_category_name_english')['order_item_id'].sum().reset_index()

    # Sắp xếp dữ liệu giảm dần để trực quan
    category_counts = category_counts.sort_values('order_item_id', ascending=False)

    # Tạo biểu đồ với Plotly
    fig = px.bar(
        category_counts,
        x="order_item_id",
        y="product_category_name_english",
        orientation="h",
        labels={"order_item_id": "Số lượng", "product_category_name_english": "Loại sản phẩm"},
        title="Phân phối loại sản phẩm",
    )
    fig.update_layout(height=800, yaxis=dict(autorange="reversed"))  # Chiều cao tùy chỉnh

    # Chuyển đổi thành Plotly FigureWidget để tích hợp Tkinter
    plot_widget = FigureWidget(fig)

    # Tạo giao diện Tkinter
    root = Tk()
    root.title("Phân phối loại sản phẩm")
    root.geometry("900x600")

    # Tạo frame với thanh cuộn
    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    canvas = Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame = Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Thêm biểu đồ vào frame
    plot_widget.update_traces()
    plot_widget.show()

    def update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scrollable_frame.bind("<Configure>", update_scrollregion)

    root.mainloop()

else:
    print("Thiếu cột 'product_category_name_english' hoặc 'order_item_id' trong dữ liệu.")
