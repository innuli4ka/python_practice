def rectangle_area(length, width):
    return length * width

while True:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))

    area = rectangle_area(length, width)
    print("The area of the rectangle is:", area)

    again = input("Do you want to calculate another rectangle? (yes/no): ").lower()

    if "y" in again or "טקד" in again:
        continue
    else:
        print("Goodbye!")
        break
