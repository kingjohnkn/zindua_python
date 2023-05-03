def fibonacci(n):
    """
    Generate Fibonacci numbers up to n starting from 0.
    """
    fib_list = [0]
    a, b = 0, 1
    while b <= n:
        fib_list.append(b)
        a, b = b, a + b
    return fib_list


print("Find Fibonacci numbers between 0 and n")
n = int(input("Enter a number (n): "))
fib_seq = fibonacci(n)

print(f"\nFibonacci numbers between 0 - {n} are: \n{fib_seq}")
