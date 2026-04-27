🚀 Exam Portal – Enterprise RBAC System
production-ready Django web application** featuring a modern UI and a Role-Based Access Control (RBAC) system designed like real-world SaaS platforms.


 ✨ Overview

This project demonstrates how to build a (secure, scalable, and maintainable admin system) where different staff users have different responsibilities.

It follows **industry practices** like:

* Separation of concerns
* Permission-based access control
* Audit logging
* Clean UI/UX


🔥 Key Features
🔐 Authentication System

* Secure login & signup
* Unique email validation
* Session-based authentication

📝 Exam Form Management

* Users can submit form **only once**
* Data stored with timestamps
* Clean form validation

🛡️ Enterprise RBAC (Role-Based Access Control)

Different roles with controlled permissions:

✔ Built using Django Groups + Permissions
✔ Fully scalable (add roles without code changes)

📊 Dashboard

* Total forms count
* Approved / Pending stats
* Interactive data table
* Action buttons based on role

📜 Audit Logging (Enterprise Feature)

Tracks critical actions:

* Approve
* Reject
* Delete

Includes:

* User who performed action
* Timestamp
* Related record


🧱 Tech Stack

| Layer    | Technology                             |
| -------- | -------------------------------------- |
| Backend  | Django                                 |
| Database | SQLite (dev) / PostgreSQL (prod ready) |
| Frontend | HTML, CSS, Bootstrap                   |
| Auth     | Django Authentication System           |

⚙️ Installation Guide

Clone repository
git clone https://github.com/YOUR_USERNAME/exam-portal.git

 Navigate to project
cd exam-portal

Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makemigrations
python manage.py migrate

Create admin user
python manage.py createsuperuser

Run server
python manage.py runserver

🔐 Admin Setup (RBAC)

1. Open:
   👉 http://127.0.0.1:8000/admin/

2. Create Groups:

   * Admin
   * User

3. Assign permissions:

   * view_examform
   * change_examform
   * delete_examform
   * can_approve
   * can_reject

4. Assign users to groups

📁 Project Struct

<img width="583" height="1150" alt="image" src="https://github.com/user-attachments/assets/3359c027-fa8f-4876-8757-e1862b6ec729" />

💡 Design Decisions

* Used **Django permissions instead of hardcoded roles**
* Added **AuditLog model** for accountability
* Ensured **backend-level security checks**
* UI adapts dynamically using `perms`

🚀 Future Enhancements

* 🔍 Search & filtering system
* 📊 Analytics dashboard (charts)
* ⚡ AJAX for no-reload UI
* 🌐 Deployment (Render / AWS)
* 🔔 Notification system


👨‍💻 Author

Aryan Kumar

⭐ Support

