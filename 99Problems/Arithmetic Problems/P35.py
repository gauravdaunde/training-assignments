'''
Determine the prime factors of a given positive integer.
    Construct a flat list containing the prime factors in ascending order.
    Example:
    * (prime-factors 315)
    (3 3 5 7)
'''


def calcPrimeFactorsList(number):
    divisor_number = 2
    prime_factors_list = list()
    while number > 1.0:  # checking division of number is further possible or not
        if number % divisor_number == 0:  # checking divisor_number is root or not
            temp = number
            temp %= divisor_number  # then dividing the number by divisor
            number /= divisor_number  # getting number after division
            # and adding to the list of roots
            prime_factors_list.append(divisor_number)
        else:
            divisor_number += 1  # increating divisor number to find next roots
    return prime_factors_list  # returning founded roots list


num = int(input('Enter the number: '))
print(calcPrimeFactorsList(num))
