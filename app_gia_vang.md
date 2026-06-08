# 🪙 Ứng dụng Cào Giá Vàng Trực Tuyến (app_cao_gia_vang)

Một ứng dụng Python nhỏ gọn, mạnh mẽ sử dụng kỹ thuật **Web Scraping** để tự động thu thập, chuẩn hóa và hiển thị bảng giá vàng SJC cũng như vàng nhẫn 9999 từ các nguồn uy tín tại Việt Nam theo thời gian thực.

---

## 📌 Các Tính Năng Nổi Bật

* **Cập nhật thời gian thực:** Dữ liệu được tải trực tiếp từ máy chủ tại thời điểm chạy ứng dụng (yêu cầu kết nối Internet).
* **Chuẩn hóa dữ liệu thông minh:** Tự động phát hiện cấu trúc bảng phức tạp (lệch dòng, gộp ô do phân chia vùng miền Hồ Chí Minh, Miền Bắc, Miền Tây...) để đưa giá tiền về đúng cột.
* **Bộ lọc sạch sẽ:** Loại bỏ hoàn toàn các ký tự xuống dòng thừa, khoảng trắng và các đoạn chữ rác quảng cáo của website nguồn.
* **Giao diện dòng lệnh (CLI) trực quan:** Bảng giá được căn lề đều đặn, thẳng hàng, giúp người dùng dễ dàng theo dõi ngay trên Terminal/CMD.

---

## 🛠️ Yêu Cầu Hệ Thống & Cài Đặt

### 1. Yêu cầu tiên quyết
* Máy tính đã cài đặt **Python 3.x** (Đã được cấu hình biến môi trường `PATH`).
* Có kết nối mạng **Internet** ổn định khi vận hành.

### 2. Cài đặt các thư viện bổ trợ
Mở Terminal hoặc Command Prompt (CMD) và chạy lệnh sau để cài đặt các thư viện cần thiết:
```bash
pip install requests beautifulsoup4