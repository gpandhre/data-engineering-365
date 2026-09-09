customers = [
    {
        "id": 101,
        "name": "Amit Sharma",
        "city": "Pune",
        "purchase": 15000
    },
    {
        "id": 102,
        "name": "Priya Patil",
        "city": "Mumbai",
        "purchase": 22000
    },
    {
        "id": 103,
        "name": "Rohan Mehta",
        "city": "Pune",
        "purchase": 18000
    },
    {
        "id": 104,
        "name": "Sneha Kulkarni",
        "city": "Nashik",
        "purchase": 12000
    }
]

print("Customer Records")
print("----------------")


def calculate_total_and_count(customers):
    total = 0
    count = 0
    for customer in customers:
        total += customer["purchase"]
        count += 1
    return total, count

total, count = calculate_total_and_count(customers)

def get_high_value_customers(customers, threshold=15000):
    high_value_customers = []
    for customer in customers:
        if(customer["purchase"] > threshold):
            high_value_customers.append(customer)
    return high_value_customers

high_value_customers_list = get_high_value_customers(customers, threshold=15000)

for customer in high_value_customers_list:
    print(customer["name"], "-", "₹", customer["purchase"])


average = total / count

print("----------------")
print("Total Purchase Amount:", "₹", total)
print("Total Customers:", count)
print("Average Purchase Amount:", "₹", average) 
print("----------------")
print("High Value Customers (Purchase > ₹15000):")
print("----------------")
print("Total High Value Customers:", len(high_value_customers_list))
print("----------------")
print("High Value Customer Details:")
print("----------------")
print("ID\tName\t\tCity\tPurchase")
for customer in high_value_customers_list:
    print(f"{customer['id']}\t{customer['name']}\t{customer['city']}\t₹{customer['purchase']}")
