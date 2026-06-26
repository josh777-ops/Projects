# Capstone project - Task Manager

# 📋 Task Manager System

A Python-based task management application developed as part of the HyperionDev Software Engineering Bootcamp Capstone Project.

This application allows teams to manage users, assign tasks, track task completion, generate reports, and display statistics through a command-line interface.

---

## 🚀 Features

### User Authentication
- Secure login system
- Username and password validation
- User credentials stored in `user.txt`

### User Management
- Register new users (Admin only)
- Prevent duplicate usernames
- Password confirmation validation

### Task Management
- Add new tasks
- Assign tasks to users
- View all tasks
- View personal tasks
- Edit assigned tasks
- Mark tasks as complete

### Administrator Functions
- View completed tasks
- Delete tasks
- Generate reports
- Display system statistics

### Reporting System

The application automatically generates:

#### task_overview.txt
Contains:
- Total number of tasks
- Completed tasks
- Incomplete tasks
- Overdue tasks
- Percentage incomplete
- Percentage overdue

#### user_overview.txt
Contains:
- Total users
- Total tasks
- User-specific task statistics
- Completion percentages
- Overdue task percentages

---

## 🛠 Technologies Used

- Python 3
- File Handling
- Functions
- Lists and Dictionaries
- Exception Handling
- Date and Time Module
- Defensive Programming
- Modular Programming Principles

---

## 📂 Project Structure

task-manager/

├── task_manager.py

├── user.txt

├── tasks.txt

├── task_overview.txt

├── user_overview.txt

└── README.md

---

## 🔐 Login Credentials

Default administrator account:

Username: admin

Password: adm1n

---

## 📖 How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/task-manager.git
```

### Navigate to the Project Folder

```bash
cd task-manager
```

### Run the Application

```bash
python task_manager.py
```

---

## 🖥 Menu Options

### Administrator Menu

```text
r   - Register User
a   - Add Task
va  - View All Tasks
vm  - View My Tasks
vc  - View Completed Tasks
del - Delete Task
gr  - Generate Reports
ds  - Display Statistics
e   - Exit
```

### Standard User Menu

```text
a   - Add Task
va  - View All Tasks
vm  - View My Tasks
e   - Exit
```

---

## 📊 Example Task Output

```text
Task: Complete README

Assigned To: Joshua

Date Assigned: 25 June 2026

Due Date: 30 June 2026

Task Complete?: No

Description:
Create professional GitHub documentation.
```

---

## 🎯 Learning Outcomes

This project demonstrates proficiency in:

- Python fundamentals
- Working with files
- Data validation
- Functions and modular programming
- Lists and dictionaries
- Error handling
- User authentication systems
- Report generation
- Software design principles
- PEP 8 coding standards

---

## 🔮 Future Improvements

Potential future enhancements include:

- Password encryption
- SQLite database integration
- GUI implementation with Tkinter
- Email notifications
- Task priorities
- Task categories
- Web application version using Flask or Django
- Cloud deployment

---

## 👨‍💻 Author

**Joshua Kotze**

Aspiring Data Analyst | AI Enthusiast 

GitHub: https://github.com/josh777-ops

LinkedIn: https://www.linkedin.com/in/joshua-kotze-sa/

---

## 📜 License

This project was developed for educational purposes as part of the HyperionDev Data Science Bootcamp Capstone Project.

---

⭐ If you found this project useful, consider giving it a star!
