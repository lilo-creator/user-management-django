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
![register page](https://github.com/user-attachments/assets/379c298d-1ba8-4b1e-99b8-aa3d7bc67414)

- Edit profile page
  ![Edit profile page](https://github.com/user-attachments/assets/43fbfd3e-b1d1-40c9-b841-8168fd169ffb)

  -user page
  ![User page](https://github.com/user-attachments/assets/2d5d66c4-4ebe-406d-af1f-477cae7e4b91)




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
