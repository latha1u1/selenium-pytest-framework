📌 Selenium Pytest Automation Framework

A scalable and maintainable Selenium + Pytest automation framework built using Page Object Model (POM) design pattern.

🚀 Tech Stack

Python

Selenium WebDriver

Pytest

Page Object Model (POM)

HTML Test Reports

📂 Project Structure
selenium-pytest-framework/
│
├── config/           # Configuration files
├── pages/            # Page Object classes
├── tests/            # Test cases
├── utils/            # Utility/helper functions
├── reports/          # Test reports
├── conftest.py       # Pytest fixtures
├── pytest.ini        # Pytest configuration
└── requirements.txt  # Dependencies

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone git@github-personal:latha1u1/selenium-pytest-framework.git
cd selenium-pytest-framework

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run Tests
pytest -v


For HTML report:

pytest --html=reports/report.html

📊 Features

✔ Page Object Model (POM) structure
✔ Reusable fixtures using conftest.py
✔ Configurable test execution
✔ HTML report generation
✔ Clean modular architecture

💡 Future Improvements

Add CI/CD using GitHub Actions

Integrate Allure reporting

Docker support

Parallel execution


