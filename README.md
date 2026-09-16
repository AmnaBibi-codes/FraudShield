<div align="center">

# 🛡️ FraudShield

**Report. Search. Stay Safe.**

FraudShield lets users report and search scam phone numbers to warn others.
It builds a shared database that helps people recognize and avoid scams early.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

<sub>Built by <a href="https://github.com/AmnaBibi-codes">@AmnaBibi-codes</a></sub>

</div>

---

## 📑 Table of Contents

<details open>
<summary>Click to expand / collapse</summary>

- [About](#-about)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Routes](#-routes)
- [Risk Scoring](#-risk-scoring)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

</details>

---

## 🧠 About

FraudShield is a community-driven platform for fighting phone scams. Instead of every person discovering a scam number the hard way, FraudShield turns individual reports into a **shared, searchable database** — so the next person who gets a suspicious call can check the number first.

---

## ✨ Features

- 🔐 **User accounts** | signup/login with hashed passwords (Flask-Bcrypt)
- 📝 **Report scam numbers** | tag a number with a scam category and description
- 🔎 **Search by number** | instantly see how many times a number has been reported, broken down by category
- 🚦 **Automatic risk rating** | numbers are labeled `NO REPORTS`, `LOW RISK`, `MODERATE RISK`, or `HIGH RISK` based on report volume
- 📊 **Analytics dashboard** | platform-wide stats across all scam categories
- 🚫 **Duplicate protection** | the same user can't spam-report the same number/category twice

---

## 🛠 Tech Stack

<div align="center">

| Category | Tools |
|---|---|
| Language | Python 3 |
| Web Framework | Flask |
| Database | MongoDB (via PyMongo) |
| Auth | Flask-Bcrypt (password hashing) + Flask sessions |
| Templating | Jinja2 (Flask `templates/`) |

</div>

---

## 📂 Project Structure

```
FraudShield/
├── app.py              # Flask app — routes, auth, MongoDB logic
├── templates/           # Jinja2 HTML templates
│   ├── index.html        # Home page — recent reports & stats
│   ├── signup.html        # User signup
│   ├── login.html          # User login
│   ├── report.html          # Submit a scam report
│   ├── search.html           # Search a number & view its risk
│   └── analytics.html         # Platform-wide analytics
└── README.md
```

---

## 🚀 Getting Started

<details open>
<summary><b>1️⃣ Clone the repository</b></summary>

```bash
git clone https://github.com/AmnaBibi-codes/FraudShield.git
cd FraudShield
```

</details>

<details open>
<summary><b>2️⃣ Set up your environment</b></summary>

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install flask pymongo flask-bcrypt
```

</details>

<details open>
<summary><b>3️⃣ Start MongoDB</b></summary>

FraudShield expects a local MongoDB instance at `mongodb://localhost:27017/` (database name: `fraudshield`). Make sure MongoDB is installed and running:

```bash
mongod
```

</details>

<details open>
<summary><b>4️⃣ Run the app</b></summary>

```bash
python app.py
```

The app runs at **http://127.0.0.1:5000** 🎉

</details>


---

## 🧭 Routes

| Route | Method(s) | Description |
|---|---|---|
| `/` | GET | Home page — recent reports, total reports & users |
| `/signup` | GET, POST | Create a new account |
| `/login` | GET, POST | Log into an existing account |
| `/logout` | GET | End the current session |
| `/report` | GET, POST | Submit a scam report (login required) |
| `/reports?search=<number>` | GET | Search a phone number and view its report breakdown |
| `/analytics` | GET | Platform-wide scam category stats |

---

## 🚦 Risk Scoring

When a number is searched, FraudShield tallies reports across four categories — **OTP Scam**, **Prize Scam**, **Investment Scam**, and **Job Scam** — and assigns a risk level:

| Total Reports | Risk Level |
|---|---|
| 0 | NO REPORTS |
| 1–2 | LOW RISK |
| 3–5 | MODERATE RISK |
| 6+ | HIGH RISK |

---

## 🗺 Roadmap

- [ ] Move `secret_key` and MongoDB URI to environment variables
- [ ] Add a `requirements.txt`
- [ ] Add input validation for phone numbers
- [ ] Add pagination for search results and analytics
- [ ] Deploy to a live environment (e.g. Render, Railway)
- [ ] Add rate limiting to prevent report spam

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and adapt it.
_(Add a `LICENSE` file to the repo to make this official.)_

---

## 📬 Contact

**Amna** — [GitHub @AmnaBibi-codes](https://github.com/AmnaBibi-codes)

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
