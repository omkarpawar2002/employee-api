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
   \`\`\`bash
   git clone https://github.com/omkarpawar2002/employee-api.git
   cd employee-api
   \`\`\`

2. **Create and activate a virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run migrations**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Start the server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. **Test Endpoints**
   - \`GET /employees/\` – List all employees
   - \`POST /employees/\` – Create employee
   - \`GET /employees/<eid>/\` – Retrieve employee
   - \`PUT/PATCH /employees/<eid>/\` – Update employee
   - \`DELETE /employees/<eid>/\` – Delete employee

## 🧾 Example JSON Payload

\`\`\`json
{
  \"eid\": \"EMP001\",
  \"name\": \"John Doe\",
  \"department\": \"Engineering\",
  \"salary\": 60000
}
\`\`\`

## 🧰 Notes

- Make sure the \`eid\` field is unique if you're using it as a lookup field.
- You can improve this API later with ViewSets and Routers for cleaner routing.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
" > README.md

# Step 2: Initialize Git & Set Remote
git init
git remote add origin https://github.com/omkarpawar2002/employee-api.git

# Step 3: Commit and push README
git add README.md
git commit -m "Add project README"
git branch -M main
git push -u origin main
