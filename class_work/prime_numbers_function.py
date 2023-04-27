# write a function that prints prime numbers from 0 - 100

def prime_numbers(numbers):
    for num in range(2, numbers + 1):
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num, end=" ")

prime_numbers(1000)