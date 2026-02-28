# ☁️ Cloud File Storage System

### Secure RESTful File Management API with Flask

A production-ready cloud file storage backend built using **Python**, **Flask**, and **RESTful API architecture**, featuring secure authentication with **Flask-Login**, structured modular design, and scalable deployment configuration.

> Designed as a backend system demonstrating authentication, file handling, REST principles, and production deployment practices.

---

## 🚀 Live Features

- 🔐 Secure user authentication (Flask-Login)
- 🗂️ User-isolated file storage
- 📤 File upload (multipart/form-data)
- 📥 Secure file download
- 🧾 RESTful API structure
- 🛡️ Password hashing & session protection
- ⚙️ Production-ready configuration
- 📄 Swagger (OpenAPI) documentation support

---

## 🏗 System Architecture

Client → Flask REST API → Authentication Layer → Database → File Storage  

### Key Design Principles:

- Separation of concerns (auth & file routes separated)
- Session-based authentication
- User-file ownership enforcement
- Environment-based configuration
- Production WSGI support (Gunicorn)

---

## 🧠 Technical Highlights

| Feature | Implementation |
|----------|----------------|
| Authentication | Flask-Login |
| Password Security | Werkzeug hash |
| Database | MongoDB |
| File Handling | Secure filename + size limit |
| API Design | RESTful JSON responses |
| Deployment | Gunicorn compatible |

---

## 📁 Project Structure

```text
cloud-file-storage/
│
├── app/
│   ├── models.py
│   ├── auth_routes.py
│   ├── file_routes.py
│   └── __init__.py
│
├── uploads/
├── config.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/cloud-file-storage.git
cd cloud-file-storage
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Development Server

```bash
python run.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🔐 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/register | Register user |
| POST | /api/login | Login user |
| POST | /api/logout | Logout user |

### File Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/upload | Upload file |
| GET | /api/files | List user files |
| GET | /api/files/<id> | Download file |
| DELETE | /api/files/<id> | Delete file |

---

## 🛡 Security Implementation

- Password hashing with `generate_password_hash`
- `@login_required` route protection
- User-based file isolation
- Secure filename sanitization
- File size limits
- Session protection
- Environment secrets management

---

## 📦 Example API Usage

### Register

```bash
curl -X POST http://127.0.0.1:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"john","password":"password123"}'
```

### Upload File

```bash
curl -X POST http://127.0.0.1:5000/api/upload \
  -F "file=@example.pdf"
```

---

## 📈 Scalability Considerations

To scale this system:

- Replace local storage with AWS S3
- Switch to PostgreSQL
- Add Redis for session caching
- Deploy behind Nginx reverse proxy
- Containerize with Docker
- Add CI/CD pipeline

---

## 🎯 Why This Project Matters

This project demonstrates:

- Backend system design
- Authentication workflows
- REST API architecture
- Secure file handling
- Production deployment awareness
- Clean project organization

It reflects practical backend engineering skills beyond basic CRUD apps.

---

## 🔮 Future Improvements

- JWT-based stateless authentication
- Role-based access control
- Public file share links
- Expiring download URLs
- File encryption at rest
- Rate limiting
- API versioning

---

## 👨‍💻 Author

prajjwal kumar 
GitHub: https://github.com/prajjwal-coder15
