'''
Goldbach's conjecture.
    Goldbach's conjecture says that every positive even number greater than 2 is the sum of two prime numbers. Example: 28 = 5 + 23. It is one of the most famous facts in number theory that has not been proved to be correct in the general case. It has been numerically confirmed up to very large numbers (much larger than we can go with our Prolog system). Write a predicate to find the two prime numbers that sum up to a given even integer.

    Example:
    * (goldbach 28)
    (5 23)
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


number = int(input("Enter number: "))


for num in range(2, number-1):
    if isPrime(num) and isPrime(number-num):  # checking num and number-num are prime or not
        print(f"({num},{number-num})")
        break
