# Django

---

## Project

- **User:**  Untuk melakukan kontrol terhadap data user
- **Payment:** Untuk menampilkan jumlah amount atas payment user
- **Notification:** Untuk menampilkan data notifikasi per user

---


## Features

- **gRPC:**  Komunikasi antar project menggunakan gRPC
- **SSO Login:** Mampu melakukan login dari ketiga service sekaligus memvalidasi token-nya disetiap project
- **Custom Hasher:** Membuat custom hasher

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)


### Steps to Install

1. **Clone Repository**  
   ```bash
   git clone https://github.com/adindak/interview-be-vpn.git
   cd visiprima-grpc
   
2. Install env :

```shell
python -m venv devEnv
```

3. Aktifkan env :

```shell
cd visiprima-grpc/myproject
```

```shell
source devEnv/bin/activate
```

4. Install Pip requirement :

```shell
pip install -r requirement.txt
```


How To Run
------------
1. **Jalankan Project**  
- Ketik `python manage.py runserver`

2. **Jalankan data seeder**
- Untuk menambahkan user baru, hit pada endpoint `[GET] {{LOCAL-URL}}/api/users/register/`
- Untuk menambahkan data payment baru, hit pada endpoint `[GET] {{LOCAL-URL}}/api/payments/register/`
- Untuk menambahkan data notification baru, hit pada endpoint `[GET] {{LOCAL-URL}}/api/notifications/register/`

3. **Option 1: Run gRPC**  
- cd visiprima-grpc/myproject
- Jalankan satu persatu project yang terdapat grpc server nya : 
```shell
python users/grpc_server.py  
```
```shell
python payments/grpc_server.py  
```
```shell
python notifications/grpc_server.py  
```
- Jalankan grpc client nya untuk pengetesan : 
```shell
python users/grpc_client.py  
```

4. **Option 2: Pengecekan Token** 
- Login bisa dilakukan pada 3 project yaitu users, payments dan notifications (asumsi ketiga project ini berada di project yang berbeda)
- Untuk login bisa di lakukan HIT pada `[POST] {{LOCAL-URL}}/api/users/login/` atau `[POST] {{LOCAL-URL}}/api/payments/login/` atau `[POST] {{LOCAL-URL}}/api/notifications/login/` dengan parameter body `username` dan `password` (untuk `username` dan `password` dapat dicek pada file `visiprima-grpc/myproject/users/views.py` )
- Kemudian bisa dicek Ketika hit endpoint `[GET] {{LOCAL-URL}}/api/users/list/` atau `[GET] {{LOCAL-URL}}/api/notifications/list/` atau `[GET] {{LOCAL-URL}}/api/payments/list/`
