'''
A list of prime numbers.
    Given a range of integers by its lower and upper limit,
	construct a list of all prime numbers in that range.
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


min, max = map(int, input("Enter range seperating by space: ").split(' '))

# printing only prime numbers from min_number to max_number
for i in range(min, max+1):
    if isPrime(i):
        print(i)
