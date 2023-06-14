from datetime import datetime

def calculate_age(birth_date):
    current_date = datetime.now().date()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
    age = current_date.year - birth_date.year

    # Check if the birthday has occurred this year or not
    if current_date.month < birth_date.month:
        age -= 1
    elif current_date.month == birth_date.month and current_date.day < birth_date.day:
        age -= 1

    return age

# Example usage
birth_date = "1957-09-03"
age = calculate_age(birth_date)
print(f"The person is {age} years old.")
