# Check for prime numbers from 0 - 100

for num in range(0, 101):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")
