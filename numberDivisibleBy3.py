start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor: "))

count = 0
current = start

while current <= end:
    if current % divisor == 0:
        print(current)
        count += 1
    current += 1

print("Total numbers divisible by", divisor, ":", count)
