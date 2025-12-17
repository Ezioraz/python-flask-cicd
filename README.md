# Python Flask CI/CD Pipeline

This project demonstrates a **Python Flask web application** integrated with a **CI/CD pipeline using GitHub Actions**. It showcases how to automate application testing and build workflows using modern DevOps practices.

---

## 📌 Project Overview

The repository contains a simple Flask application along with an automated CI/CD pipeline that runs on every push or pull request. The pipeline installs dependencies, runs unit tests, and validates the application code.

This project is designed to demonstrate **CI/CD fundamentals**, not business logic complexity.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Testing:** Pytest  
- **CI/CD:** GitHub Actions  
- **Dependency Management:** pip, virtualenv  
- **Runtime:** Python 3.x  

---

## 📁 Project Structure

```
python-flask-cicd/
├── app.py
├── requirements.txt
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
```

---

## 🚀 Application Functionality

- Runs a basic Flask web application
- Exposes simple HTTP endpoints
- Includes unit tests to validate application behavior
- Automatically triggers CI pipeline on code changes

---

## ⚙️ Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Ezioraz/python-flask-cicd.git
cd python-flask-cicd
```

### 2. Create and activate virtual environment
**Linux / macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask application
```bash
python app.py
```

Access the app at:  
`http://localhost:5000`

---

## 🧪 Running Tests

Tests are written using **pytest**.

```bash
pytest
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

The CI/CD workflow is defined in:

```
.github/workflows/ci-cd.yml
```

### Pipeline Actions:
- Triggered on push and pull request events
- Sets up Python environment
- Installs dependencies
- Runs automated unit tests

---

## 🔮 Possible Enhancements

- Add Dockerfile for containerization
- Integrate deployment (AWS / Azure / GCP)
- Add code coverage reporting
- Use Terraform for infrastructure provisioning

---

## 📜 License

MIT License
