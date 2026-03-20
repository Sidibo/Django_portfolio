
---

# 🌐 Django Portfolio Website----

A personal portfolio website built using **Django** to showcase projects, skills, and achievements.

---

## 📌 Overview

This is a dynamic portfolio web application where users can:-

- View projects
- Explore skills
- Contact the developer
- Manage content via admin panel

----

## 🎯 Features

- 🧑‍💻 Personal portfolio homepage  
- 📂 Project showcase section  
- 🛠 Skills & technologies section  
- 📬 Contact form  
- 🔐 Django admin panel for content managements
- 🌐 Fully dynamic backend  

----

## 🧠 Tech Stack

### 🔹 Backend
- Django (Python)

### 🔹 Frontend
- HTML, CSS, JavaScript  
- (Optional: Bootstrap / Tailwind)

### 🔹 Database
- SQLite (default)  
- (Can be upgraded to PostgreSQL)

----

## 📂 Project Structure

portfolio_project/ │ ├── portfolio_project/ │   ├── settings.py │   ├── urls.py │ ├── portfolio/ │   ├── views.py │   ├── models.py │   ├── urls.py │   ├── templates/ │   └── static/ │ ├── manage.py ├── db.sqlite3 └── README.md

----

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/portfolio-django.git
cd portfolio-django


---

2️⃣ Create virtual environment

python -m venv myenv
myenv\Scripts\activate   # Windows


---

3️⃣ Install dependencies

pip install django


---

4️⃣ Run migrations

python manage.py migrate


---

5️⃣ Run the server

python manage.py runserver


---

🌐 Open in browser

http://127.0.0.1:8000/


---

🔐 Admin Panel

Create superuser:

python manage.py createsuperuser

Then access:

http://127.0.0.1:8000/admin/


---

📈 Future Improvements

Add blog section

Add authentication system

Deploy on cloud (Render / AWS)

Add animations and modern UI



---

👨‍💻 Author

Srijit Bhattacharya 



---

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

---

