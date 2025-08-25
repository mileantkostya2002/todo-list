# 📋 Django Todo List

<div align="center">

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

**A modern, responsive task management web application built with Django**

[🚀 Demo](#demo) • [📖 Features](#features) • [⚡ Quick Start](#quick-start) • [📱 Screenshots](#screenshots) • [🤝 Contributing](#contributing)

</div>

---

## 🌟 Overview

Django Todo List is a full-featured task management system that allows users to create, manage, and collaborate on tasks. Built with modern web technologies, it provides an intuitive interface for personal and team productivity.

## ✨ Features

### 🔐 **User Management**
- 📝 User registration and authentication
- 🔒 Secure login/logout system
- 👤 Personal dashboard for each user

### 📋 **Task Management**
- ➕ Create new tasks with detailed descriptions
- 📊 View all available tasks
- ✅ Mark tasks as completed
- 🎯 Take responsibility for specific tasks
- 🔍 Filter and search functionality

### 🎨 **Modern UI/UX**
- 📱 Fully responsive design
- 🌈 Clean, modern interface with Bootstrap 5
- ⚡ Fast and intuitive user experience
- 🖥️ Works on desktop, tablet, and mobile

### 🔄 **Real-time Updates**
- 🚀 Dynamic task status updates
- 👥 See which tasks are being worked on
- 📈 Track progress in real-time

## 🛠️ Tech Stack

<table>
<tr>
<td>

**Backend**
- ![Python](https://img.shields.io/badge/-Python_3.12-3776ab?style=flat-square&logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/-Django_5.2-092e20?style=flat-square&logo=django&logoColor=white)
- ![SQLite](https://img.shields.io/badge/-SQLite-003b57?style=flat-square&logo=sqlite&logoColor=white)

</td>
<td>

**Frontend**
- ![HTML5](https://img.shields.io/badge/-HTML5-e34f26?style=flat-square&logo=html5&logoColor=white)
- ![CSS3](https://img.shields.io/badge/-CSS3-1572b6?style=flat-square&logo=css3&logoColor=white)
- ![Bootstrap](https://img.shields.io/badge/-Bootstrap_5-7952b3?style=flat-square&logo=bootstrap&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/-JavaScript-f7df1e?style=flat-square&logo=javascript&logoColor=black)

</td>
</tr>
</table>

## ⚡ Quick Start

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Git

### 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mileantkostya2002/todo-list.git
   cd todo-list
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open your browser and visit:** `http://127.0.0.1:8000`


## 🚀 Deployment

### Deploy to Heroku
1. Create a `Procfile`:
   ```
   web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn todo_list.wsgi
   ```

2. Install gunicorn:
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Development Guidelines
- Follow PEP 8 coding standards
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Kostya Milean**
- GitHub: [@mileantkostya2002](https://github.com/mileantkostya2002)


## 🙏 Acknowledgments

- Django community for the amazing framework
- Bootstrap team for the UI components
- All contributors who help improve this project

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ and Django

</div>
