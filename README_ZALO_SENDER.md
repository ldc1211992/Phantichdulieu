# 🚀 Chương Trình Tự Động Gửi Tin Nhắn Zalo

Chương trình Python tự động gửi tin nhắn chào hỏi đến danh sách bạn bè trên Zalo Web.

## ✨ Tính Năng

- 🤖 Tự động đăng nhập Zalo Web
- 📝 Gửi tin nhắn tùy chỉnh đến nhiều người cùng lúc
- 🎯 Tìm kiếm và chọn liên hệ tự động
- 📊 Báo cáo chi tiết kết quả gửi tin
- 🛡️ Xử lý lỗi và logging đầy đủ
- ⚙️ Cấu hình linh hoạt qua file JSON
- 🎨 Giao diện terminal với màu sắc đẹp mắt

## 📋 Yêu Cầu Hệ Thống

- Python 3.7+
- Google Chrome browser
- Kết nối internet ổn định
- Tài khoản Zalo hợp lệ

## 🛠️ Cài Đặt

### 1. Clone hoặc tải về dự án

```bash
git clone <repository-url>
cd zalo-auto-sender
```

### 2. Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 3. Cấu hình chương trình

Chỉnh sửa file `config.json`:

```json
{
    "contacts": [
        "Tên Bạn 1",
        "Tên Bạn 2", 
        "Tên Bạn 3"
    ],
    "message": "Chào bạn! Chúc bạn một ngày tốt lành! 😊",
    "headless": false,
    "delay_between_messages": 3,
    "max_retries": 2
}
```

**Giải thích các tham số:**
- `contacts`: Danh sách tên hiển thị của các liên hệ cần gửi tin nhắn
- `message`: Nội dung tin nhắn muốn gửi
- `headless`: `true` để chạy ẩn trình duyệt, `false` để hiển thị
- `delay_between_messages`: Thời gian nghỉ giữa các lần gửi (giây)
- `max_retries`: Số lần thử lại khi gửi thất bại

## 🚀 Cách Sử Dụng

### 1. Chạy chương trình

```bash
python zalo_auto_sender.py
```

### 2. Đăng nhập Zalo

- Chương trình sẽ mở trình duyệt Chrome
- Truy cập https://chat.zalo.me/
- Bạn có 60 giây để đăng nhập thủ công vào Zalo
- Sau khi đăng nhập thành công, chương trình sẽ tự động tiếp tục

### 3. Theo dõi quá trình

Chương trình sẽ:
- Tìm kiếm từng liên hệ trong danh sách
- Gửi tin nhắn đã cấu hình
- Hiển thị tiến độ và kết quả
- Lưu log chi tiết vào file `zalo_sender.log`

## 📁 Cấu Trúc Dự Án

```
zalo-auto-sender/
├── zalo_auto_sender.py    # Script chính
├── config.json            # File cấu hình
├── requirements.txt       # Danh sách thư viện
├── README_ZALO_SENDER.md  # Hướng dẫn sử dụng
├── zalo_sender.log        # File log (tự động tạo)
└── .env                   # File biến môi trường (tùy chọn)
```

## 🎯 Ví Dụ Sử Dụng

### Gửi tin nhắn chúc mừng năm mới

```json
{
    "contacts": [
        "Nguyễn Văn A",
        "Trần Thị B", 
        "Lê Văn C",
        "Phạm Thị D"
    ],
    "message": "🎉 Chúc mừng năm mới! Chúc bạn một năm mới tràn đầy sức khỏe, hạnh phúc và thành công! 🎊",
    "headless": false,
    "delay_between_messages": 5
}
```

### Gửi thông báo sự kiện

```json
{
    "contacts": [
        "Nhóm Bạn Thân",
        "Đồng Nghiệp A",
        "Đồng Nghiệp B"
    ],
    "message": "📅 Nhắc nhở: Họp nhóm lúc 14:00 ngày mai tại phòng họp tầng 3. Mọi người nhớ tham gia nhé!",
    "headless": true,
    "delay_between_messages": 2
}
```

## ⚠️ Lưu Ý Quan Trọng

### Bảo mật
- ❌ **KHÔNG** chia sẻ thông tin đăng nhập
- ✅ Luôn đăng xuất sau khi sử dụng
- ✅ Sử dụng mạng internet an toàn

### Sử dụng có trách nhiệm
- ❌ **KHÔNG** spam tin nhắn
- ❌ **KHÔNG** gửi nội dung không phù hợp
- ✅ Tôn trọng quyền riêng tư của người khác
- ✅ Tuân thủ điều khoản sử dụng của Zalo

### Hiệu suất
- ⏱️ Đặt thời gian nghỉ hợp lý (3-5 giây)
- 🔄 Không chạy quá nhiều lần trong thời gian ngắn
- 📊 Kiểm tra log để theo dõi hiệu suất

## 🐛 Xử Lý Lỗi Thường Gặp

### 1. Lỗi "ChromeDriver not found"
```bash
# Cài đặt lại webdriver-manager
pip install --upgrade webdriver-manager
```

### 2. Lỗi "Không tìm thấy liên hệ"
- Kiểm tra tên liên hệ trong `config.json` có chính xác không
- Đảm bảo liên hệ đã có trong danh sách bạn bè Zalo
- Thử sử dụng tên hiển thị đầy đủ

### 3. Lỗi đăng nhập
- Xóa cache và cookie của trình duyệt
- Thử đăng nhập thủ công trước
- Kiểm tra kết nối internet

### 4. Lỗi gửi tin nhắn
- Kiểm tra xem có bị giới hạn gửi tin nhắn không
- Tăng thời gian delay giữa các tin nhắn
- Thử gửi lại sau một thời gian

## 📝 Log và Monitoring

Chương trình tự động tạo file log `zalo_sender.log` với thông tin:
- Thời gian thực hiện
- Trạng thái gửi tin nhắn
- Lỗi và cảnh báo
- Thống kê tổng quan

Ví dụ log:
```
2024-01-20 10:30:15 - INFO - Chrome WebDriver đã được khởi tạo thành công
2024-01-20 10:30:45 - INFO - Đăng nhập Zalo thành công
2024-01-20 10:31:00 - INFO - Gửi tin nhắn thành công đến Nguyễn Văn A
2024-01-20 10:31:15 - ERROR - Không tìm thấy liên hệ Trần Thị B
2024-01-20 10:31:30 - INFO - Hoàn thành gửi tin nhắn: 3 thành công, 1 thất bại
```

## 🔧 Tùy Chỉnh Nâng Cao

### Chạy ở chế độ headless (ẩn trình duyệt)
```json
{
    "headless": true
}
```

### Tùy chỉnh thời gian chờ
Chỉnh sửa trong file `zalo_auto_sender.py`:
```python
self.wait = WebDriverWait(self.driver, 30)  # Tăng từ 20 lên 30 giây
```

### Thêm emoji và định dạng tin nhắn
```json
{
    "message": "🌟 Chào bạn!\n\n✨ Chúc bạn một ngày tuyệt vời!\n🎯 Hẹn gặp lại sớm! 😊"
}
```

## 🤝 Đóng Góp

Nếu bạn muốn cải thiện chương trình:
1. Fork repository
2. Tạo branch mới cho tính năng
3. Commit các thay đổi
4. Tạo Pull Request

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Kiểm tra file log `zalo_sender.log`
2. Đọc kỹ phần xử lý lỗi ở trên
3. Tạo issue trên GitHub với thông tin chi tiết

## 📄 Giấy Phép

Dự án này được phát hành dưới giấy phép MIT. Xem file LICENSE để biết thêm chi tiết.

---

**⚡ Chúc bạn sử dụng thành công! ⚡**

*Nhớ sử dụng có trách nhiệm và tôn trọng người khác nhé! 😊*