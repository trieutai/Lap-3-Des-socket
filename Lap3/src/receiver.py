import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# Cấu hình kết nối nội bộ (localhost)
HOST = '0.0.0.0'
PORT = 3636

def start_receiver():
    # Tạo socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 3636)) # chiếm giữ cổng 
        s.listen() # đưa vào trạng thái chờ kết nối
        print(f"[*] Receiver đang lắng nghe tại {HOST}:{PORT}...")
        
        conn, addr = s.accept() # Chấp nhận kết nối
        with conn:
            print(f"[*] Kết nối thành công từ: {addr}")
            
            try:
                # 1. Nhận DES Key (8 byte)
                key = conn.recv(8)
                # 2. Nhận IV (8 byte)
                iv = conn.recv(8)
                # 3. Nhận Length Header (4 byte)
                length_bytes = conn.recv(4)
                if not length_bytes: return
                length = int.from_bytes(length_bytes, byteorder='big')
                
                # 4. Nhận Ciphertext
                ciphertext = conn.recv(length)
                print(f"[*] Đã nhận {len(ciphertext)} byte ciphertext.")
                ciphertext = conn.recv(length)
                print("Đã nhận xong dữ liệu, đang đợi thêm...") # Dòng này sẽ không bao giờ được in ra nếu Header sai 100 byte

                # Giải mã dữ liệu
                cipher = DES.new(key, DES.MODE_CBC, iv)
                # Gỡ bỏ PKCS#7 padding
                raw_data = cipher.decrypt(ciphertext)
                plaintext = unpad(raw_data, 8) 
                
                print(f"[+] Bản rõ sau giải mã: {plaintext.decode('utf-8')}")
                
            except Exception as e:
                print(f"[-] Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    start_receiver()