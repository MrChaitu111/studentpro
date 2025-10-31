# 🎓 Student Management System (Django + MySQL)

The **Student Management System** is a fully functional web-based CRUD application built using **Django** and **MySQL**, designed to manage and organize student data efficiently.  
It provides an intuitive interface for administrators to **add**, **view**, **update**, and **delete** student records seamlessly.  
This project demonstrates how to integrate **Django with MySQL**, handle **forms and models**, and **deploy a Django web app on PythonAnywhere**.

---

## 🧩 Project Description

This project is developed to simplify the process of maintaining student information for educational institutions.  
It can be used by schools, colleges, and coaching centers to keep track of their students’ details like name, email, address, and contact number.

The web application includes **user-friendly forms**, **database connectivity**, and **Bootstrap-based responsive design**.  
All CRUD operations are implemented using Django’s **Model-View-Template (MVT)** architecture, ensuring clean separation of logic, data, and UI.

---

## 🎯 Objectives

- ✅ To build a web-based system that replaces manual student record-keeping.
- ✅ To provide a clean dashboard for managing students efficiently.
- ✅ To demonstrate CRUD operations using Django ORM.
- ✅ To integrate Django with MySQL for production-level applications.
- ✅ To deploy the project live on PythonAnywhere.

---

## 💡 Key Features

- **Add Student:** Add new student details using a form.
- **View Students:** Display all students in a tabular format with pagination.
- **Edit Student:** Update existing student data quickly.
- **Delete Student:** Remove any student record from the database.
- **Responsive Design:** Works well on desktop and mobile devices.
- **User Feedback:** Success messages after each operation.
- **MySQL Integration:** Persistent database for all records.
- **PythonAnywhere Hosting:** Live production deployment.

---

## 🧠 How It Works

The project follows Django’s **MVT (Model-View-Template)** structure:

- **Model:** Defines the structure of student data (fields like name, email, age, etc.).
- **View:** Handles business logic and database operations.
- **Template:** HTML pages with embedded Django template tags for dynamic content.

Whenever a user submits a form (for adding, editing, or deleting a student), the data is processed by the corresponding view and saved to the MySQL database using Django’s ORM.

---

## 🗄️ Database Design

### Database Name

### Table: `studentapp_student`
| Field | Type | Description |
|--------|------|-------------|
| id | Integer (Primary Key) | Unique identifier |
| name | CharField | Student’s full name |
| email | EmailField | Contact email |
| age | IntegerField | Student’s age |
| address | TextField | Student’s address |
| created_at | DateTimeField | Record creation timestamp |

---

## 🌐 Deployment on PythonAnywhere

The project is deployed using the **free tier of PythonAnywhere**.  
It uses:
- **Django as the backend framework**
- **MySQL as the production database**
- **Gunicorn** as the WSGI HTTP server

The live app can be accessed at:  
👉 https://chaitanya511.pythonanywhere.com/

---

## 🧰 Tools & Technologies

| Category | Technology |
|-----------|-------------|
| Language | Python 3 |
| Framework | Django 4.x |
| Database | MySQL |
| Frontend | HTML, CSS, Bootstrap |
| Version Control | Git & GitHub |
| Hosting | PythonAnywhere |
| Editor | VS Code |

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone Repository

git clone https://github.com/MrChaitu111/studentpro.git
#####

🧑‍💻 Developer

👤 Name: Chaitanya D

💼 Role: Django Developer | Python Full-Stack Enthusiast

🌍 Location: India

📧 Email: your-email@example.com

🏷️ Tags

django python mysql crud student-management-system fullstack pythonanywhere bootstrap webapp

📜 License

This project is released under the MIT License.
You’re free to modify, distribute, or use it for educational purposes.



