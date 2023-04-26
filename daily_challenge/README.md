# Prime Numbers

#### A prime number is a positive integer greater than 1 that has no positive integer divisors other than 1 and itself. 

However, 0 and 1 do not satisfy this definition.

- 0 is not a prime number because it is not a positive integer.
- 1 is not a prime number because it only has one positive integer divisor (which is itself), and prime numbers by definition must have at least two different positive integer divisors.

Here is the Python code to print all prime numbers from 0 to 100:
```
for num in range(2, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")
```

In this code, we iterate over the numbers from *2 to 100* using a for loop. For each number, we check if it is divisible by any number between 2 and the number itself (excluding the number itself). If it is not divisible by any of these numbers, then it is a prime number and we print it.

The else statement is used with the for loop to print the prime number if the for loop completes without encountering a break statement, which indicates that the number is prime. The ```end=" "``` argument is used to print the numbers on the same line with a space in between them.