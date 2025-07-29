#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script cho Zalo Auto Sender
"""

import os
import sys
import subprocess
import json
from colorama import init, Fore, Style

init(autoreset=True)

def check_python_version():
    """Kiểm tra phiên bản Python"""
    if sys.version_info < (3, 7):
        print(f"{Fore.RED}✗ Cần Python 3.7 trở lên. Phiên bản hiện tại: {sys.version}")
        return False
    print(f"{Fore.GREEN}✓ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Cài đặt các thư viện cần thiết"""
    try:
        print(f"{Fore.YELLOW}Đang cài đặt các thư viện cần thiết...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(f"{Fore.GREEN}✓ Đã cài đặt thành công các thư viện!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}✗ Lỗi khi cài đặt thư viện: {e}")
        return False

def create_sample_config():
    """Tạo file config mẫu nếu chưa tồn tại"""
    config_file = "config.json"
    
    if os.path.exists(config_file):
        print(f"{Fore.YELLOW}File config.json đã tồn tại.")
        return True
        
    sample_config = {
        "contacts": [
            "Tên Bạn 1 (Thay đổi tên này)",
            "Tên Bạn 2 (Thay đổi tên này)",
            "Tên Bạn 3 (Thay đổi tên này)"
        ],
        "message": "Chào bạn! Chúc bạn một ngày tốt lành! 😊",
        "headless": False,
        "delay_between_messages": 3,
        "max_retries": 2
    }
    
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(sample_config, f, ensure_ascii=False, indent=4)
        print(f"{Fore.GREEN}✓ Đã tạo file config.json mẫu!")
        print(f"{Fore.CYAN}Vui lòng chỉnh sửa file config.json với thông tin của bạn.")
        return True
    except Exception as e:
        print(f"{Fore.RED}✗ Lỗi khi tạo file config: {e}")
        return False

def check_chrome():
    """Kiểm tra Google Chrome"""
    try:
        # Thử import webdriver để kiểm tra
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        
        print(f"{Fore.GREEN}✓ Selenium và WebDriver Manager đã sẵn sàng!")
        return True
    except ImportError as e:
        print(f"{Fore.RED}✗ Thiếu thư viện: {e}")
        return False

def display_instructions():
    """Hiển thị hướng dẫn sử dụng"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}           HƯỚNG DẪN SỬ DỤNG")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}1. Chỉnh sửa file config.json:")
    print(f"   - Thay đổi danh sách 'contacts' với tên thật của bạn bè")
    print(f"   - Tùy chỉnh nội dung 'message'")
    print(f"   - Điều chỉnh các tham số khác nếu cần")
    print(f"\n{Fore.YELLOW}2. Chạy chương trình:")
    print(f"   python zalo_auto_sender.py")
    print(f"\n{Fore.YELLOW}3. Đăng nhập Zalo Web khi được yêu cầu")
    print(f"\n{Fore.RED}⚠️  LƯU Ý QUAN TRỌNG:")
    print(f"   - Sử dụng có trách nhiệm")
    print(f"   - Không spam tin nhắn")
    print(f"   - Tôn trọng quyền riêng tư người khác")
    print(f"{Fore.CYAN}{'='*60}")

def main():
    """Hàm chính của setup"""
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}        SETUP CHƯƠNG TRÌNH ZALO AUTO SENDER")
    print(f"{Fore.CYAN}{'='*60}")
    
    # Kiểm tra Python version
    if not check_python_version():
        return False
    
    # Cài đặt requirements
    if not install_requirements():
        return False
    
    # Kiểm tra Chrome và Selenium
    if not check_chrome():
        return False
    
    # Tạo config mẫu
    if not create_sample_config():
        return False
    
    print(f"\n{Fore.GREEN}{'='*60}")
    print(f"{Fore.GREEN}           SETUP HOÀN THÀNH THÀNH CÔNG!")
    print(f"{Fore.GREEN}{'='*60}")
    
    # Hiển thị hướng dẫn
    display_instructions()
    
    return True

if __name__ == "__main__":
    try:
        if main():
            print(f"\n{Fore.GREEN}✅ Setup hoàn tất! Bạn có thể bắt đầu sử dụng chương trình.")
        else:
            print(f"\n{Fore.RED}❌ Setup thất bại! Vui lòng kiểm tra lại.")
            sys.exit(1)
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Setup bị hủy bởi người dùng.")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}Lỗi không mong muốn: {e}")
        sys.exit(1)