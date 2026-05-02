# 📊 GlobalTech Solutions - Customer Management System

## 📌 Overview
This project is a **Python-based Customer Management System** developed for Module 8. It demonstrates the use of:

- Dictionaries for structured data storage
- Nested data handling
- Data lookup and updates
- Aggregation and analysis
- Dictionary comprehensions
- Functions for validation and reporting

The system simulates how a company manages customers, services, and project data.

---

## 🚀 Features

### 👥 Customer Management
- Store and manage customer details (company, contact, email, phone)
- Lookup customers by ID
- Update customer information dynamically
- Validate customer records

### 🛠️ Service Management
- Maintain a catalog of services and hourly rates
- Categorize services into pricing tiers
- Apply rate adjustments (e.g., 10% increase)

### 📁 Project Tracking
- Assign multiple projects to customers
- Track:
  - Project name
  - Service type
  - Hours worked
  - Budget
  - Status (active, completed, pending)

### 💰 Financial Analysis
- Calculate:
  - Project costs (rate × hours)
  - Total hours and budgets
  - Average project budget
  - Highest and lowest project budgets

### 📈 Data Insights
- Service usage analysis
- Customer statistics
- Active customer filtering
- Budget summaries per customer

### 🤖 Smart Features
- Service recommendation system
- Budget analysis per customer
- Project status tracking

---

## 🧱 Data Structures Used

### Services Dictionary
```python
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 95
}
````

### Customers Dictionary

```python
customers = {
    "C001": {...},
    "C002": {...},
    ...
}
```

### Projects Dictionary

```python
projects = {
    "C001": [project1, project2],
    "C002": [project3],
    ...
}
```

---

## ⚙️ Key Functions

### ✅ `validate_customer(customer_dict)`

Checks if a customer contains all required fields:

* `company_name`
* `contact_person`
* `email`
* `phone`

---

### 📊 `analyze_customer_budgets(projects_dict)`

Returns budget statistics per customer:

```python
{
    "C001": {
        "total": 35600,
        "average": 17800,
        "count": 2
    }
}
```

---

### 💡 `recommend_services(customer_id, customers, projects, services)`

* Identifies unused services for a customer
* Returns recommended services

---

## 📊 Example Outputs

### Customer Statistics

* Total customers
* List of customer IDs
* Company names

### Financial Summary

* Total hours worked
* Total budget
* Average project budget
* Highest & lowest project budgets

### Service Usage

* Frequency of each service used across projects

---

## 🧠 Concepts Demonstrated

* Dictionary creation and manipulation
* Nested data structures
* Looping through complex data
* Aggregation using `sum()`, `len()`, `max()`, `min()`
* Dictionary comprehensions
* Defensive programming with `.get()`
* Function design and reuse

---

## ▶️ How to Run

1. Make sure you have Python installed (3.x recommended)
2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/customer-management-system.git
   ```
3. Navigate to the project folder:

   ```bash
   cd customer-management-system
   ```
4. Run the script:

   ```bash
   python main.py
   ```

---

## 📌 Future Improvements

* Add user input for dynamic data entry
* Store data in files (JSON/CSV)
* Build a simple GUI or web interface
* Add error handling for invalid inputs

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

Developed as part of a programming assignment on dictionaries and data aggregation.

