def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            # add num to total
            total += num
    return total

numbers = [1, 2, 3, 4]

total = sum_even_numbers(numbers)
print(total)