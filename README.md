# 🏆 SportsSphere — Dynamic Sports Blogging Platform

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square\&logo=flask\&logoColor=white)
![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat-square\&logo=sqlite\&logoColor=white)
![HTML](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square\&logo=html5\&logoColor=white)
![CSS](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square\&logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square\&logo=javascript\&logoColor=black)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-7952B3?style=flat-square\&logo=bootstrap\&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

⚽ **SportsSphere** is a vibrant, modern web application designed for sports enthusiasts to **read, write, and share** blogs about their favorite sports, players, and events — all in one interactive platform.

> 💬 Share your passion for sports. Read insights, write stories, and engage with the community.

---

## 🚀 Table of Contents

* [Overview](#-overview)
* [✨ Features](#-features)
* [🧠 Tech Stack](#-tech-stack)
* [⚙️ Setup Instructions](#️-setup-instructions)
* [📂 Project Structure](#-project-structure)
* [🌐 Usage Guide](#-usage-guide)
* [💾 Database Schema](#-database-schema)
* [🧩 Development Notes](#-development-notes)
* [🗺️ Roadmap](#️-roadmap)
* [🤝 Contributing](#-contributing)
* [📜 License](#-license)
* [👨‍💻 Authors & Acknowledgements](#-authors--acknowledgements)

---

## 🧩 Overview

**SportsSphere** is a dynamic blogging platform focused on sports content. Built with **Flask (Python)** on the backend and a stylish **Bootstrap + JavaScript** frontend, it enables users to **create posts, comment on articles,** and explore trending sports news.

Perfect for fans, journalists, or teams looking to showcase sports insights in a simple, elegant interface.

---

## ✨ Features

✅ User authentication (register/login/logout)
✅ Create, edit, and delete blog posts
✅ Comment system for user engagement
✅ Admin dashboard for content moderation
✅ SQLite database integration
✅ Responsive UI built with **Bootstrap**
✅ Search and filter blogs by category or author
✅ Timestamped posts for latest updates

---

## 🧠 Tech Stack

| Layer           | Technologies                     |
| --------------- | -------------------------------- |
| **Backend**     | Python (Flask Framework)         |
| **Frontend**    | HTML, CSS, JavaScript, Bootstrap |
| **Database**    | SQLite                           |
| **Templating**  | Jinja2                           |
| **Auth System** | Flask Sessions                   |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/SportsSphere.git
cd SportsSphere
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize Database

```bash
python init_db.py
```

### 5️⃣ Run the Application

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) 🌐

---

## 📂 Project Structure

```
SportsSphere/
├── app.py               # Main Flask application
├── init_db.py           # Script to initialize database
├── static/              # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
├── templates/           # Jinja2 templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── post_detail.html
│   ├── create_post.html
│   ├── edit_post.html
│   └── dashboard.html
├── database/            # SQLite database
│   └── blog.db
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🌐 Usage Guide

👤 **For Users:**

* Register and log in
* Browse the latest sports articles
* Like, comment, or share posts
* Write your own blog articles

🛠️ **For Admins:**

* Approve or remove inappropriate posts
* Manage users and comments
* View overall blog statistics

---

## 💾 Database Schema

**Users Table:**

| id | username | email | password |
| -- | -------- | ----- | -------- |

**Posts Table:**

| id | title | content | author_id | date_posted |
| -- | ----- | ------- | --------- | ----------- |

**Comments Table:**

| id | post_id | user_id | content | date_posted |
| -- | ------- | ------- | ------- | ----------- |

---

## 🧩 Development Notes

🧱 **Recommended Improvements:**

* Add user profile pages and avatars
* Enable image uploads for blog posts
* Implement tags/categories for posts
* Add likes/bookmarks functionality
* Add pagination for better UX
* Migrate to PostgreSQL or MySQL for scaling
* Implement JWT-based authentication for APIs

---

## 🗺️ Roadmap

🚧 Future Enhancements:

* ✅ Admin analytics dashboard
* ✅ Trending blog algorithm
* 🧩 Notification system for new comments
* 📱 Full mobile responsiveness
* 🎨 Dark/light mode toggle

---

## 🤝 Contributing

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request 🎉

---

## 📜 License

🪪 Distributed under the **MIT License**. See `LICENSE` for more information.

---

## 👨‍💻 Authors & Acknowledgements

👨‍💻 **Astro** — Lead Developer & Designer
⚽ **Inspiration:** Sports journalism platforms, fan communities, and interactive blogs
📚 **Frameworks Used:** Flask, SQLite, HTML, CSS, JavaScript, Bootstrap

---

✨ *Write passionately. Read widely. Live the game with SportsSphere!* 🏅
