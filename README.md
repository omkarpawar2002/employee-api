A simple Django REST Framework-based API for managing employee data using class-based views.

## 🚀 Features

- List all employees
- Create a new employee
- Retrieve a single employee by \`eid\`
- Update (PUT/PATCH) employee details
- Delete an employee

## 🛠️ Tech Stack

- Python 3
- Django
- Django REST Framework

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/omkarpawar2002/employee-api.git
   cd employee-api
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the server**
   ```bash
   python manage.py runserver
   ```

6. **Test Endpoints**
   - `GET /api/emp/` – List all employees
   - `POST /api/emp/` – Create a new employee
   - `GET /api/emp/<eid>/` – Retrieve a single employee
   - `PUT /api/emp/<eid>/` – Fully update an employee
   - `PATCH /api/emp/<eid>/` – Partially update an employee
   - `DELETE /api/emp/<eid>/` – Delete an employee

   

## 🧾 Example JSON Payload
```json
{
  "eid": 102,
  "name": "Omkar",
  "age": 23,
  "dept": "ADMIN",
  "sal": 18000.0
}
```


## 📤 Git Commands

```bash
# Step 2: Initialize Git & Set Remote
git init
git remote add origin https://github.com/omkarpawar2002/employee-api.git

# Step 3: Commit and push README
git add README.md
git commit -m "Add project README"
git branch -M main
git push -u origin main
```

