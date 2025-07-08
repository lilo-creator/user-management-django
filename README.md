# 🧑‍💼 User Management System - Django Project

A simple and powerful *Django-based User Management System* that supports registration, login/logout, profile management, password change, and an admin panel. It was built as part of a personal learning challenge.

---

## 🚀 Features

- ✅ User Registration
- ✅ Login & Logout
- ✅ Profile View & Edit
- ✅ Password Change
- ✅ Admin Panel for User Management
- ✅ Custom User Types (Staff & Community Members)
- ✅ Authentication-protected profile page
- ✅ Unit Tests for Models and Views

---

## 🛠 Tech Stack

- Python 3.10+
- Django 4.x
- SQLite (for development)
- Bootstrap 5 (for styling)
- Crispy Forms
- Git & GitHub for version control

---

## 📸 Screenshots

> 🖼 Add screenshots of:
- Register Page
- ![Register]("./Register-page.png)
- Login Page
- Profile Page
- Admin Panel

---

## ⚙ Setup Instructions

### 1. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows

### 2.  Install dependencies
pip install -r requirements.txt

 ### 3. Run migrations
python manage.py migrate

 ### 4. Create superuser
python manage.py createsuperuser

 ### 5. Run the server
python manage.py runserver
Now visit http://127.0.0.1:8000 in your browser
