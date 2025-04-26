age = int(input("Age? "))
if age < 0:
    print("Invalid age")
    exit()

day = input("Day (weekday/weekend)? ").lower()
if day != "weekday" and day != "weekend":
    print("Invalid day")
    exit()

loyalty = input("Loyalty member (y/n)? ").lower()

price = 20

if age < 13:
    price = price * 0.5
elif age >= 60:
    price = price * 0.7

if day == "weekend":
    price = price + 5

if loyalty == "y":
    price = price - 2

print("Total: $" + str(int(price)))
