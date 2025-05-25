
# Chatbot Project

Dự án chatbot gồm **Frontend** sử dụng React và **Backend** sử dụng Flask. Mục tiêu của dự án là xây dựng một chatbot với giao diện người dùng thân thiện và backend xử lý logic, mô hình AI.

---

## Mô tả

- **Frontend:** React app cung cấp giao diện chat.
- **Backend:** Flask API cung cấp các endpoint để xử lý yêu cầu chat, gọi mô hình AI.
- **Kết nối:** Frontend gửi request tới backend để nhận phản hồi chatbot.

---

## Yêu cầu

- Python 3.8+
- Node.js 14+
- npm hoặc yarn

---

## Hướng dẫn cài đặt và chạy

### 1. Backend (Flask)

#### Tạo môi trường ảo và cài đặt thư viện

```bash
# Tạo môi trường ảo (nên dùng python3 hoặc python nếu có nhiều phiên bản)
python -m venv venv

# Kích hoạt môi trường ảo
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Cài đặt các thư viện trong requirements.txt
pip install -r requirements.txt
```

#### Tải mô hình AI (`model.safetensors`)

Do GitHub giới hạn dung lượng file (<100MB), bạn cần tải model từ Google Drive và đặt đúng vị trí:

**👉 Link tải model:**  
[📥 Tải từ Google Drive](https://drive.google.com/file/d/1AbcDEfGhijKlmNOpqrStUVwxYZ/view?usp=sharing](https://drive.google.com/drive/u/0/folders/1Uz06kBuGJ3ZEl1lQPuTPv-D3erl4flu2))

**Đặt file vào:**
```
backend/trained_model/model.safetensors
```

#### (Tùy chọn) Tải tự động bằng script Python

```bash
pip install gdown
```

```python
# download_model.py
import gdown
import os

url = "https://drive.google.com/uc?id=1AbcDEfGhijKlmNOpqrStUVwxYZ"
output = "backend/trained_model/model.safetensors"

if not os.path.exists(output):
    print("Downloading model...")
    gdown.download(url, output, quiet=False)
else:
    print("Model already exists.")
```

Sau đó chạy:

```bash
python download_model.py
```

#### Chạy backend Flask

```bash
python app.py
```

Backend mặc định chạy ở `http://127.0.0.1:5000`

---

### 2. Frontend (React)

#### Cài đặt thư viện

```bash
cd frontend

# Cài đặt dependencies
npm install
# hoặc
yarn install
```

#### Chạy frontend React

```bash
npm start
# hoặc
yarn start
```

Frontend mặc định chạy ở `http://localhost:3000`

---

## Cấu hình kết nối frontend - backend

- Trong mã nguồn frontend, bạn cần đảm bảo URL API backend đúng. Ví dụ:

```js
const API_URL = 'http://127.0.0.1:5000';
```

- Khi gửi request (fetch hoặc axios) từ frontend, dùng `API_URL` làm base URL.

---

## Cấu trúc thư mục gợi ý

```
root/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── trained_model/
│       └── model.safetensors
├── frontend/
│   ├── package.json
│   ├── src/
│   └── ...
└── README.md
```

---

## Lưu ý

- Khi deploy, cần cấu hình CORS để frontend gọi được backend (ví dụ dùng `flask-cors` trong Flask).
- Luôn kích hoạt môi trường ảo khi làm việc với backend để đảm bảo đúng phiên bản thư viện.
- Có thể cần cấu hình proxy trong React để gọi API backend khi deploy.

---

## Hình ảnh demo
![demo](image.png)
