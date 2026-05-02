# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services

services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}

customer1 = {
    "company_name": "Alpha Corp",
    "contact_person": "John Smith",
    "email": "john@alphacorp.com",
    "phone": "813-555-1001"
}

customer2 = {
    "company_name": "Beta Industries",
    "contact_person": "Maria Lopez",
    "email": "maria@betaind.com",
    "phone": "813-555-1002"
}

customer3 = {
    "company_name": "Gamma LLC",
    "contact_person": "David Chen",
    "email": "david@gammallc.com",
    "phone": "813-555-1003"
}

customer4 = {
    "company_name": "Delta Solutions",
    "contact_person": "Sara Patel",
    "email": "sara@deltasolutions.com",
    "phone": "813-555-1004"
}


# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}

customers = {"C001": customer1, "C002": customer2, "C003": customer3, "C004": customer4} 

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information

for cid, info in customers.items():
    print(f"{cid}: {info}")

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here

c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"] #access nested dictionary value
c999_info = customers.get("C999","Customer not found") #safe lookup with default value if key doesn't exsist

print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Info:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here

customers["C001"]["phone"] = "813-555-9999" # update exsisting value
customers["C002"]["industry"] = "Technology" #add new field to dictionary

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here

project1 = {"name": "Website Redesign", "service": "Web Development", "hours": 120, "budget": 18000}
project2 = {"name": "Security Audit", "service": "Cybersecurity", "hours": 80, "budget": 17600}
project3 = {"name": "Data Dashboard", "service": "Data Analysis", "hours": 60, "budget": 10500}
project4 = {"name": "Cloud Migration", "service": "Cloud Consulting", "hours": 90, "budget": 18000}
project5 = {"name": "Helpdesk Setup", "service": "IT Support", "hours": 40, "budget": 3800}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4],
    "C004": [project5]
}

for cid, plist in projects.items():
    print(cid, plist)

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
# nested loop through customers and their projects
for cid, plist in projects.items():
    for p in plist:
        rate = services[p["service"]]
        cost = rate * p["hours"]
        print(f"{cid} - {p['name']} | Cost: ${cost}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here

print("Customer IDs:", list(customers.keys()))

companies = [c["company_name"] for c in customers.values()] # extract company names
print("Customer Companies:", companies)

print("Total Customers:", len(customers)) # total number of customers

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here

service_counts = {}
#count occurences of each service across projects
for plist in projects.values():
    for p in plist:
        service = p["service"]
        service_counts[service] = service_counts.get(service,0) +1
        
print(service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here

all_hours = []
all_budgets = []
#collect hours and budget from all projects
for plist in projects.values():
    for p in plist:
        all_hours.append(p["hours"])
        all_budgets.append(p["budget"])
        
total_hours = sum(all_hours)
total_budget = sum(all_budgets)
avg_budget = total_budget/len(all_budgets)
max_budget = max(all_budgets)
min_budget = min(all_budgets)

print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Highest Budget:", max_budget)
print("Lowest Budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here

for cid, cust in customers.items():
    plist = projects.get(cid, []) # get customers' projects if they exsist
    hours = sum(p["hours"] for p in plist)
    budget = sum(p["budget"] for p in plist)
    
    print(cid, cust["company_name"])
    print("Projects:", len(plist))
    print("Total Hours:", hours)
    print("Total Budget:", budget)
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here

#apply 10% discount
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here

active_customers = {cid: customers[cid] for cid in customers if cid in projects}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here

customer_budgets = {cid: sum(p["budget"] for p in plist) for cid, plist in projects.items()}

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here

service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
# validate required fields in customer dictionaries 
def validate_customer(customer_dict):
    required = ["company_name", "contact_person", "email", "phone"]
    for field in required:
        if field not in customer_dict:
            return False
    return True

for cid, cust in customers.items():
    print(cid, validate_customer(cust))
    

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here

statuses= ["active", "completed", "pending"]
i=0
# assign project status
for plist in projects.values():
    for p in plist:
        p["status"] = statuses[i % 3]
        i += 1

status_counts = {}
# count projects by status
for plist in projects.values():
    for p in plist:
        s = p["status"]
        status_counts[s] = status_counts.get(s, 0) + 1
        
print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
# calculate budget statistics per customer
def analyze_customer_budgets(projects_dict):
    
    results = {}
    
    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        average = total / count if count > 0 else 0
        
        results[cid] = {
            "total": total,
            "average": average,
            "count": count
        }
    
    return results

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
# recommend services not previously used by customer
def recommend_services(customer_id, customers, projects, services):
    
    used_services = []
    
    for p in projects.get(customer_id, []):
        used_services.append(p["service"])
        
    recommendations = []
    
    for service in services:
        if service not in used_services:
            recommendations.append(service)
            
    return recommendations

for cid in customers:
    recs = recommend_services(cid, customers, projects, services)
    print(cid,recs)



