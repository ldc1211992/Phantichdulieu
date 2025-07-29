#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chương trình tự động gửi tin nhắn Zalo
Author: Assistant
Version: 1.0
"""

import time
import json
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from colorama import init, Fore, Style
import os
from dotenv import load_dotenv

# Khởi tạo colorama để hiển thị màu sắc trên terminal
init(autoreset=True)

# Load environment variables
load_dotenv()

class ZaloAutoSender:
    def __init__(self, headless=False):
        """
        Khởi tạo ZaloAutoSender
        
        Args:
            headless (bool): Chạy trình duyệt ở chế độ không hiển thị giao diện
        """
        self.driver = None
        self.wait = None
        self.headless = headless
        self.setup_logging()
        
    def setup_logging(self):
        """Thiết lập logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('zalo_sender.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def setup_driver(self):
        """Thiết lập Chrome WebDriver"""
        try:
            chrome_options = Options()
            
            # Các tùy chọn để tối ưu hóa
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # User agent để tránh bị phát hiện
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            
            if self.headless:
                chrome_options.add_argument('--headless')
                
            # Tự động tải ChromeDriver
            service = Service(ChromeDriverManager().install())
            
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.wait = WebDriverWait(self.driver, 20)
            
            print(f"{Fore.GREEN}✓ Đã khởi tạo trình duyệt thành công!")
            self.logger.info("Chrome WebDriver đã được khởi tạo thành công")
            
        except Exception as e:
            print(f"{Fore.RED}✗ Lỗi khi khởi tạo trình duyệt: {e}")
            self.logger.error(f"Lỗi khởi tạo WebDriver: {e}")
            raise
            
    def login_zalo(self):
        """Đăng nhập vào Zalo Web"""
        try:
            print(f"{Fore.YELLOW}Đang truy cập Zalo Web...")
            self.driver.get("https://chat.zalo.me/")
            
            print(f"{Fore.CYAN}Vui lòng đăng nhập vào Zalo trong trình duyệt...")
            print(f"{Fore.CYAN}Chương trình sẽ đợi 60 giây để bạn đăng nhập...")
            
            # Đợi người dùng đăng nhập thủ công
            time.sleep(60)
            
            # Kiểm tra xem đã đăng nhập thành công chưa
            try:
                # Tìm kiếm thanh tìm kiếm hoặc danh sách chat để xác nhận đã đăng nhập
                search_box = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[placeholder*='Tìm kiếm'], [placeholder*='Search']"))
                )
                print(f"{Fore.GREEN}✓ Đăng nhập thành công!")
                self.logger.info("Đăng nhập Zalo thành công")
                return True
                
            except TimeoutException:
                print(f"{Fore.RED}✗ Không thể xác nhận đăng nhập. Vui lòng thử lại.")
                self.logger.error("Không thể xác nhận đăng nhập Zalo")
                return False
                
        except Exception as e:
            print(f"{Fore.RED}✗ Lỗi khi đăng nhập: {e}")
            self.logger.error(f"Lỗi đăng nhập: {e}")
            return False
            
    def search_and_select_contact(self, contact_name):
        """
        Tìm kiếm và chọn liên hệ
        
        Args:
            contact_name (str): Tên liên hệ cần tìm
            
        Returns:
            bool: True nếu thành công, False nếu thất bại
        """
        try:
            print(f"{Fore.YELLOW}Đang tìm kiếm: {contact_name}")
            
            # Tìm thanh tìm kiếm
            search_selectors = [
                "[placeholder*='Tìm kiếm']",
                "[placeholder*='Search']",
                "input[type='text']",
                ".search-input",
                "#search-input"
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_box = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
                    
            if not search_box:
                print(f"{Fore.RED}✗ Không tìm thấy thanh tìm kiếm")
                return False
                
            # Xóa nội dung cũ và nhập tên liên hệ
            search_box.clear()
            search_box.send_keys(contact_name)
            time.sleep(2)
            
            # Tìm và click vào kết quả đầu tiên
            result_selectors = [
                ".conv-item",
                ".contact-item",
                ".search-result-item",
                "[role='button']",
                ".list-item"
            ]
            
            for selector in result_selectors:
                try:
                    results = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    if results:
                        results[0].click()
                        print(f"{Fore.GREEN}✓ Đã chọn liên hệ: {contact_name}")
                        time.sleep(2)
                        return True
                except Exception:
                    continue
                    
            print(f"{Fore.RED}✗ Không tìm thấy liên hệ: {contact_name}")
            return False
            
        except Exception as e:
            print(f"{Fore.RED}✗ Lỗi khi tìm kiếm liên hệ {contact_name}: {e}")
            self.logger.error(f"Lỗi tìm kiếm liên hệ {contact_name}: {e}")
            return False
            
    def send_message(self, message):
        """
        Gửi tin nhắn
        
        Args:
            message (str): Nội dung tin nhắn
            
        Returns:
            bool: True nếu thành công, False nếu thất bại
        """
        try:
            print(f"{Fore.YELLOW}Đang gửi tin nhắn...")
            
            # Tìm ô nhập tin nhắn
            message_selectors = [
                "[placeholder*='Nhập tin nhắn']",
                "[placeholder*='Type a message']",
                ".input-message",
                "[contenteditable='true']",
                "textarea",
                "input[type='text']"
            ]
            
            message_box = None
            for selector in message_selectors:
                try:
                    message_box = self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    break
                except TimeoutException:
                    continue
                    
            if not message_box:
                print(f"{Fore.RED}✗ Không tìm thấy ô nhập tin nhắn")
                return False
                
            # Nhập tin nhắn
            message_box.clear()
            message_box.send_keys(message)
            time.sleep(1)
            
            # Tìm và click nút gửi
            send_selectors = [
                "[title*='Gửi']",
                "[title*='Send']",
                ".send-button",
                "[type='submit']",
                ".btn-send"
            ]
            
            for selector in send_selectors:
                try:
                    send_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    send_button.click()
                    print(f"{Fore.GREEN}✓ Đã gửi tin nhắn thành công!")
                    time.sleep(2)
                    return True
                except Exception:
                    continue
                    
            # Nếu không tìm thấy nút gửi, thử nhấn Enter
            try:
                from selenium.webdriver.common.keys import Keys
                message_box.send_keys(Keys.RETURN)
                print(f"{Fore.GREEN}✓ Đã gửi tin nhắn thành công!")
                time.sleep(2)
                return True
            except Exception:
                pass
                
            print(f"{Fore.RED}✗ Không thể gửi tin nhắn")
            return False
            
        except Exception as e:
            print(f"{Fore.RED}✗ Lỗi khi gửi tin nhắn: {e}")
            self.logger.error(f"Lỗi gửi tin nhắn: {e}")
            return False
            
    def send_messages_to_contacts(self, contacts, message):
        """
        Gửi tin nhắn đến danh sách liên hệ
        
        Args:
            contacts (list): Danh sách tên liên hệ
            message (str): Nội dung tin nhắn
        """
        success_count = 0
        failed_contacts = []
        
        print(f"{Fore.CYAN}Bắt đầu gửi tin nhắn đến {len(contacts)} liên hệ...")
        print(f"{Fore.CYAN}Nội dung: {message}")
        print("-" * 50)
        
        for i, contact in enumerate(contacts, 1):
            print(f"{Fore.CYAN}[{i}/{len(contacts)}] Đang xử lý: {contact}")
            
            if self.search_and_select_contact(contact):
                if self.send_message(message):
                    success_count += 1
                    self.logger.info(f"Gửi tin nhắn thành công đến {contact}")
                else:
                    failed_contacts.append(contact)
                    self.logger.error(f"Gửi tin nhắn thất bại đến {contact}")
            else:
                failed_contacts.append(contact)
                self.logger.error(f"Không tìm thấy liên hệ {contact}")
                
            # Nghỉ giữa các lần gửi để tránh spam
            if i < len(contacts):
                print(f"{Fore.YELLOW}Đang nghỉ 3 giây...")
                time.sleep(3)
                
        # Báo cáo kết quả
        print("\n" + "="*50)
        print(f"{Fore.GREEN}✓ Đã gửi thành công: {success_count}/{len(contacts)} liên hệ")
        
        if failed_contacts:
            print(f"{Fore.RED}✗ Gửi thất bại: {len(failed_contacts)} liên hệ")
            print(f"{Fore.RED}Danh sách thất bại: {', '.join(failed_contacts)}")
            
        self.logger.info(f"Hoàn thành gửi tin nhắn: {success_count} thành công, {len(failed_contacts)} thất bại")
        
    def close(self):
        """Đóng trình duyệt"""
        if self.driver:
            self.driver.quit()
            print(f"{Fore.GREEN}✓ Đã đóng trình duyệt")


def load_config():
    """Load cấu hình từ file config.json"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"{Fore.RED}✗ Không tìm thấy file config.json")
        return None
    except json.JSONDecodeError as e:
        print(f"{Fore.RED}✗ Lỗi đọc file config.json: {e}")
        return None


def main():
    """Hàm chính"""
    print(f"{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}           CHƯƠNG TRÌNH TỰ ĐỘNG GỬI TIN NHẮN ZALO")
    print(f"{Fore.CYAN}{'='*60}")
    
    # Load cấu hình
    config = load_config()
    if not config:
        print(f"{Fore.RED}Vui lòng tạo file config.json trước khi chạy chương trình!")
        return
        
    contacts = config.get('contacts', [])
    message = config.get('message', '')
    headless = config.get('headless', False)
    
    if not contacts:
        print(f"{Fore.RED}Danh sách liên hệ trống!")
        return
        
    if not message:
        print(f"{Fore.RED}Tin nhắn trống!")
        return
        
    # Khởi tạo và chạy
    sender = ZaloAutoSender(headless=headless)
    
    try:
        sender.setup_driver()
        
        if sender.login_zalo():
            sender.send_messages_to_contacts(contacts, message)
        else:
            print(f"{Fore.RED}Không thể đăng nhập. Chương trình kết thúc.")
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Chương trình bị dừng bởi người dùng.")
        
    except Exception as e:
        print(f"{Fore.RED}Lỗi không mong muốn: {e}")
        
    finally:
        sender.close()
        print(f"{Fore.CYAN}Chương trình kết thúc.")


if __name__ == "__main__":
    main()