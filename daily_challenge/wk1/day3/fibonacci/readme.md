# Fibonacci Sequence

### In mathematics, the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.

In this code, 
```
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

```

the ```fibonacci``` function generates Fibonacci numbers from a range of numbers (0 - n).

Initialize the fibonacci list from 0 so that the sequence can start from 0. 

Use a while loop to append the numbers to the list. (The loop will terminate once the the value in the ```b``` variable exceeds ```n```)

We add and ```int``` to the ```input``` because the values in the input are strings, the ```int``` converts the string to an integer.