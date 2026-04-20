import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Cấu hình trùng với Receiver
HOST = '127.0.0.1'
PORT = 65432

def start_sender():
    # Chuẩn bị dữ liệu [cite: 24]
    key = get_random_bytes(8) # Sinh khóa DES 8 byte(một chuỗi 8Byt
    iv = get_random_bytes(8)  # Sinh IV 8 byte cho CBC [cite: 48]
    message = "Chào Tài, bài Lab 3 đã chạy thành công!"
    
    # Mã hóa với PKCS#7 padding [cite: 49, 68]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_message = pad(message.encode('utf-8'), 8)
    ciphertext = cipher.encrypt(padded_message)

    # Gửi dữ liệu qua Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT)) # Chủ động kết nối [cite: 41]
            print("[+] Đã kết nối tới Receiver.")
            
            # Gửi theo đúng thứ tự quy định [cite: 34, 35, 36, 67]
            s.sendall(key)
            s.sendall(iv)
            # Gửi header 4 byte mô tả độ dài [cite: 35]
            s.sendall(len(ciphertext).to_bytes(4, byteorder='big'))
            s.sendall(ciphertext)
            
            print("[+] Đã gửi toàn bộ gói tin.")
        except ConnectionRefusedError:
            print("[-] Lỗi: Receiver chưa bật!")

if __name__ == "__main__":
    start_sender()