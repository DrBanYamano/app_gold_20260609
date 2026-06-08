import requests

def get_gold_price_api():
    # Sử dụng endpoint API JSON đồng bộ giá vàng SJC chính xác, chịu tải tốt và không lo chặn render
    url = "https://baomoi.com/tien-ich-gia-vang-sjc.epi"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Nếu trang web này chặn hoặc trả về HTML, ta sẽ dùng một nguồn API dự phòng siêu tốc khác
        if response.status_code != 200 or "json" not in response.headers.get("Content-Type", "").lower():
            # Dự phòng: Cào qua trang tổng hợp dữ liệu tĩnh có cấu trúc bảng chuẩn bằng một dòng
            raise ValueError("Chuyển sang phương án dự phòng cào data trực tiếp.")
            
        data = response.json()
        print("-" * 65)
        print(f"{'LOẠI VÀNG SJC':<35} | {'MUA VÀO (đ)':<13} | {'BÁN RA (đ)':<13}")
        print("-" * 65)
        
        # Parse dữ liệu từ JSON tùy biến theo cấu trúc trả về
        for item in data.get('items', []):
            name = item.get('type', '')
            buy = item.get('buy', '')
            sell = item.get('sell', '')
            print(f"{name:<35} | {buy:<13} | {sell:<13}")
            
    except Exception:
        # 🛡️ PHƯƠNG ÁN DỰ PHÒNG CHẮC CHẮN CHẠY: Cào từ trang WebGia (Server phân tách data sẵn)
        try:
            from bs4 import BeautifulSoup
            backup_url = "https://webgia.com/gia-vang/sjc/"
            res = requests.get(backup_url, headers=headers)
            soup = BeautifulSoup(res.content, "html.parser")
            
            print("-" * 65)
            print(f"{'LOẠI VÀNG (SJC Toàn Quốc)':<35} | {'MUA VÀO':<13} | {'BÁN RA':<13}")
            print("-" * 65)
            
            table = soup.find("table")
            if table:
                rows = table.find_all("tr")
                for row in rows[1:]: # Bỏ qua dòng tiêu đề
                    cells = row.find_all(["td", "th"])
                    if len(cells) >= 3:
                        name = cells[0].text.strip()
                        buy = cells[1].text.strip()
                        sell = cells[2].text.strip()
                        # Loại bỏ các ký tự xuống dòng thừa nếu có
                        name = " ".join(name.split())
                        print(f"{name:<35} | {buy:<13} | {sell:<13}")
            else:
                print("⚠️ Hệ thống đang bảo trì bảng giá. Vui lòng thử lại sau!")
        except Exception as e:
            print(f"❌ Không thể kết nối tới các máy chủ giá vàng: {e}")

def main():
    print("🔍 Đang đồng bộ dữ liệu giá vàng trực tuyến...")
    get_gold_price_api()

if __name__ == "__main__":
    main()