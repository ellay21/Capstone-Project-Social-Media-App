# 🌟 Django Social Media App

## 🚀 Description
The **Django Social Media App** is a **scalable, secure, and user-friendly** web platform designed to help users **connect, share posts, and engage** with others through likes, comments, and follows. Built with **Django** and **Django REST Framework (DRF)**, this app ensures a **robust backend** for seamless social networking experiences.

---

## 🎯 Features
✅ **User Authentication** - Secure registration & JWT-based login/logout.

✅ **User Profiles** - Create, edit, and view user profiles.

✅ **Posting System** - Share, update, and delete text & image-based posts.

✅ **Engagements** - Like/unlike posts and comment on them.

✅ **Follow System** - Follow/unfollow users and track followers/following.

✅ **API Documentation** - Interactive API documentation via Swagger/Postman.

---
# 🛠 Project Setup & Configuration

**Branch:** `setup/config`

This branch handles the foundational setup for the Django Social Media App.

---

## 🔧 What's Configured

- ✅ Django project initialized.
- ✅ SQLite database integrated.
- ✅ Django REST Framework (DRF) configured.
- ✅ JWT authentication set up.
- ✅ Static & media file handling added.
- ✅ Swagger (drf-yasg) included for API documentation.

---

## 📁 Environment Variables (.env)

Create a `.env` file at the root of your project with the following variables:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost



## 📥 Installation
### 🔹 Clone the Repository
```bash
git clone https://github.com/ellay21/Capstone-Project-Social-Media-App.git
cd Capstone-Project-Social-Media-App
```

### 🔹 Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 🔹 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 Run Migrations & Start the Server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🤝 Contributing
Contributions are **welcome**! Follow these steps:
1. **Fork** the repository.
2. **Create a feature branch** and make changes.
3. **Push** to your branch.
4. **Submit a Pull Request** for review.

---

## 📜 License
This project is licensed under the **MIT License**.

💡 **Star the repo** ⭐ if you like the project!

