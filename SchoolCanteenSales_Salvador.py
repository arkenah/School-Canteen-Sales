target = 0
target_not_reached = 0
total_sales = 0

number_of_items = int(input("Enter number of food items: "))

for i in range(1, number_of_items + 1):
    sales = int(input(f"Enter sales for item {i}: "))
    total_sales += sales

    if sales >= 500:
        target += 1
    else:
        target_not_reached += 1

def calculate_average(total_sales, number_of_items):
    average = total_sales / number_of_items
    return average

def sales_report():
    print("CANTEEN SALES REPORT")
    print(f"Average Sales: PHP {calculate_average(total_sales, number_of_items):.2f} | Meeting Target: {target} | Below Target: {target_not_reached}")

sales_report()