# Lap-3-Des-socket
Bai Tap lab 3 cua Trieu Duk Tay
DU AN MA HOA DES QUA SOCKET TCP
1. Gioi thieu chung
Day la do an trien khai viec truyen tin bao mat giua hai may tinh (Client-Server). Chuong trinh su dung thuat toan ma hoa doi xung DES (Data Encryption Standard) o che do CBC (Cipher Block Chaining) thong qua giao thuc Socket TCP trong ngon ngu Python.

2. Cau truc thu muc
src/: Chua ma nguon chinh (sender.py va receiver.py).

logs/: Chua hinh anh minh chung ket qua va cac kich ban loi.

docs/: Chua bao cao chi tiet va phan tich moi de doa (Threat Model).

3. Yeu cau he thong
Ngon ngu: Python 3.x.

Thu vien bat buoc: pycryptodome (Cai dat bang lenh: pip install pycryptodome).

4. Huong dan su dung
Buoc 1: Chay file receiver.py tren may nhan de bat dau lang nghe ket noi.

Buoc 2: Mo file sender.py, thay doi bien HOST thanh dia chi IP cua may nhan (vi du: 10.89.235.76 hoac 127.0.0.1).

Buoc 3: Chay file sender.py de thuc hien ma hoa va gui tin nhắn.

5. Cac kich ban kiem thu (Test Cases)
He thong da duoc kiem tra qua 5 truong hop de dam bao tinh on dinh:

Ca 1 (Thanh cong): Truyen tin thong suot qua mang LAN, giai ma chinh xac.

Ca 2 (Timeout): Xu ly khi sai dia chi IP hoac bi tuong lua (Firewall) chan.

Ca 3 (Truncated Data): Xu ly khi du lieu bi cat cut, khong du do dai de giai ma.

Ca 4 (Invalid Padding): Phat hien khi dung sai khoa (Key) dan den loi cau truc Padding.

Ca 5 (Connection Reset): Xu ly tinh huong doi tac ngat ket noi dot ngot khi dang truyen.

6. Phan tich bao mat (Threat Model)
Tai san bao ve: Noi dung tin nhan, Khoa DES, Vector khoi tao (IV).

Nguy co: Nghe len (Sniffing) tren mang LAN vi khoa va IV dang duoc truyen o dang ban ro.

Huong khac phuc: Su dung RSA de trao doi khoa hoac trien khai SSL/TLS cho Socket.
