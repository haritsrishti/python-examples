# firstname, lastname, age, monthly_salary,
# and bonus_percentage. . also, calculate the annual bonus by applying the
# bonus percentage to the annual salary. The function should then return a
# concatenated string containing the full name (first name and last name),
# age, annual salary, and total compensation (annual salary + annual bonus)

def calculate_annual_salary(first_name, last_name,age, annual_salary, annual_bonus):
    annual_salary = annual_salary * annual_bonus
    annual_bonus = annual_salary * (annual_bonus / 100)
    total_compensation = annual_salary + annual_bonus
    response = (f"{first_name} , {last_name} , {annual_salary} , {annual_bonus}")
    print(response)
    return response

calculate_annual_salary("Vishakha", "Srivastava", 21, 10000, 1500 )

'''Write a Python function that accepts four arguments: item_name, quantity, price_per_unit,
and discount_percentage.The function should calculate
the total price before discount by multiplying the quantity by the price per unit.
Then, calculate the discount amount by applying the discount percentage to the total price.
Finally, calculate the final price after subtracting the discount from the total price.
The function should return a concatenated string containing the item name, quantity, total price'''


item_name=input("item name")
quantity=int(input("quantity"))
price_per_unit=float(input("price per unit"))
discount_percentage=float(input("discount percentage"))
def totalprice(item_name, quantity, price_per_unit, discount_percentage):
    total_price=quantity*price_per_unit
    discount_amount=total_price*(discount_percentage/100)
    final_price=total_price-discount_amount
    return f"item name: {item_name}, quantity: {quantity}, total price: {final_price}"
print(totalprice(item_name, quantity, price_per_unit, discount_percentage))






