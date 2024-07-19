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

calculate_annual_salary("Vishkaha", "Srivastava", 21, 10000, 1500 )




