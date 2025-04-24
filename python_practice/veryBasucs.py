def salary_check():
    gross_salary = float(input("Please enter your gross salary: "))
    tax_rate = 0.27
    net_income = gross_salary * (1 - tax_rate)
    rent = 8500
    savings_goal = 5000

    if net_income >= rent + savings_goal:
        print("Rent and save!")
    elif net_income >= rent:
        print("Just rent.")
    else:
        print("Not enough.")

def shopping_calc():
    item_price = float(input("Enter the price of a single item: "))
    quantity = int(input("Enter the quantity: "))
    total_price = item_price * quantity
    shipping_fee = 0 if total_price > 200 else 20
    discount_applied = False
    if total_price > 500:
        total_price *= 0.9 # 10% discount
        discount_applied = True
    final_price = total_price + shipping_fee

    print("Total cost:", round(final_price, 2))
    print("Discount applied:", "Yes" if discount_applied else "No")
    print("Free shipping:", "Yes" if shipping_fee == 0 else "No")

    def ask_yes_no(question):
        while True:
            answer = input(question).strip().lower()
            if answer == "yes":
                return True
            elif answer == "no":
                return False
            else:
                print("Please enter only 'yes' or 'no'.")

def allow_entrance():
    age = int(input("Enter your age: "))
    gold_pass = ask_yes_no("Do you owm a gold pass? (yes/no): ")
    is_royal = ask_yes_no("Are you a part of a royal family? (yes/no): ")
    is_blacklisted = ask_yes_no("Are you blacklisted? (yes/no): ")

    allowed_in = (age >=18 and (gold_pass) and (is_royal) and not (is_blacklisted)) 

    if allowed_in:
        print("You are allowed to enter the club.")
    else:
        print("You are not allowed to enter the club.")

def car_insurance():
    driver_age = int(input("What is the driver's age? "))
    accident_count = int(input("How many accidents have you had in your life? "))

    if driver_age < 25:
        premium = 3000
    else:
        premium = 2000

    premium += accident_count * 500

    print("Total premium:", premium)
    if premium > 5000:
        print("Risk level: High Risk")
    else:
        print("Risk level: Standard")


def lab_sefety():
    temp = float(input("Enter the temperature in Celsius: "))
    pressure = float(input("Enter the pressure in bar: ")) 
    voltage = float(input("Enter the voltage in volts: "))
    if 20 < temp < 80 and pressure < 50 and 200 < voltage < 250:
        print("Safe to proceed")
    else:
        print("Unsafe conditions")



def final_exam():
    spell = int(input("Enter the spell evaluation (0-100): "))
    accracy = int(input("Enter the accuracy evaluation (0-100): "))
    control = int(input("Enter the control evaluation (0-100): "))
    
    if spell < 40 or accracy < 40 or control < 40:
        print("You have failed the exam.")
        return
    
    av = (spell + accracy + control) / 3
    if av <= 60: 
        print("You have failed the exam.")
    elif 60 < av < 75:
        print("You are Apprentice")
    elif 75 <= av < 89:
        print("You are a Mage")
    elif av > 90:
        print("You are a Archmage")
    



while True:
    print("\n=== Main Menu ===")
    print("1. Check if you can pay rent and save")
    print("2. Calculate shopping total with shipping and discount")
    print("3. Castle entry check")
    print("4. Car insurance premium calculation")
    print("5. Lab safety check")
    print("6. Final Wizard's exam evaluation")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
       salary_check()
    elif choice == "2":
        shopping_calc()
    elif choice == "3":
        allow_entrance()
    elif choice == "4":
        car_insurance()
    elif choice == "5":
        lab_sefety()
    elif choice == "6":
        final_exam()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")