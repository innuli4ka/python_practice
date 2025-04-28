def fibonacci_recursive(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

# Testing
print(fibonacci_recursive(5))   # [0, 1, 1, 2, 3]
print(fibonacci_recursive(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
