# IdeaApp---API-Automation-Testing
This repository contains API test cases, automation tests, and test management files for the IdeaApp project.

Project Overview

IdeaApp is an idea-sharing and management platform that allows users to create, update, and delete ideas. This repository includes:
✅ Test Management & Bug Tracker (.xlsx) for manual testing.
✅ Postman API Collection (.json) for automated API testing.
✅ Automation Tests (Pytest) for validating app functionality.

📦 IdeaApp-Test-Repository  
 ┣ 📂 automation_tests/  
 ┃ ┣ 📜 __init__.py  
 ┃ ┣ 📜 test_email_format_validation.py   # Email validation tests  
 ┃ ┣ 📜 test_field_length.py              # Field length validation  
 ┃ ┣ 📜 test_login_functionality.py       # Login functionality tests  
 ┃ ┣ 📜 test_password_strength.py         # Password security tests  
 ┃ ┣ 📜 test_session_expiry.py            # Session timeout tests  
 ┃ ┣ 📜 test_sql_injection.py             # SQL injection prevention tests  
 ┣ 📜 IdeaApp.xlsx                         # Test cases & bug tracking  
 ┣ 📜 ideaApp2024.postman_collection.json  # API testing collection  
 ┣ 📜 README.md                            # Project documentation  

 📝 Test Management & Bug Tracking

The IdeaApp.xlsx file contains structured test cases for IdeaApp, including:

Test Case ID
Test Description
Steps to Reproduce
Expected Result
Actual Result
Bug Status
📌 How to Use:
Open the .xlsx file using Microsoft Excel or Google Sheets.
Log test cases and update results as needed.
Track bug reports efficiently.

🔥 API Testing with Postman

The ideaApp2024.postman_collection.json file includes API test cases for:

User Authentication (/api/User/Authentication)
Create Idea (/api/Idea/Create)
Get All Ideas (/api/Idea/All)
Edit Idea (/api/Idea/Edit?ideaId={id})
Delete Idea (/api/Idea/Delete?ideaId={id})
🚀 How to Use Postman Collection:
Import the Collection:
Open Postman.
Click File > Import and select ideaApp2024.postman_collection.json.
Set Up Authentication:
Update Bearer Token in the request headers.
Run API Tests:
Click Send to test each endpoint.
View responses and debug issues.

🤖 Automation Testing with Pytest

The automation_tests/ folder contains automated test scripts using Pytest.

🧪 Implemented Tests:
✅ Email Format Validation (test_email_format_validation.py)
✅ Field Length Validation (test_field_length.py)
✅ Login Functionality (test_login_functionality.py)
✅ Password Strength Validation (test_password_strength.py)
✅ Session Expiry Handling (test_session_expiry.py)
✅ SQL Injection Prevention (test_sql_injection.py)
