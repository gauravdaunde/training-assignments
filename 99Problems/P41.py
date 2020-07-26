'''
A list of Goldbach compositions.
    Given a range of integers by its lower and upper limit, print a list of all even numbers and their Goldbach composition.

    Example:
    * (goldbach-list 9 20)
    10 = 3 + 7
    12 = 5 + 7
    14 = 3 + 11
    16 = 3 + 13
    18 = 5 + 13
    20 = 3 + 17
'''


# checking number is prime or not
def isPrime(number):
    if number == 1:
        return False
    # checking given number is divisible by any number from 2 to number itself
    for num in range(2, number):
        if number % num == 0 and number != num:  # if so then number is not prime
            return False
    return True


min_number, max_number = map(int, input(
    "Enter range seperating by space: ").split(' '))


for num in range(min_number, max_number+1):
    if num % 2 != 0:  # eliminating odd numbers
        continue
    for i in range(2, num-1):
        if isPrime(i) and isPrime(num-i):  # checking num and number-num are prime or not
            print(f"{num} = {i} + {num-i}")
            break
