'''
Determine the prime factors of a given positive integer (2).
    Construct a list containing the prime factors and their multiplicity.
    Example:
    * (prime-factors-mult 315)
    ((3 2) (5 1) (7 1))
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


number = int(input('Enter the number: '))

prime_factors_list = calcPrimeFactorsList(number)

custom_prime_factors_list = list()


for factor in prime_factors_list:
    temp_list = list()
    # creating sublist of factor and its count in list
    temp_list.append(factor)
    temp_list.append(prime_factors_list.count(factor))

    # checking created sublist is alreay present or not
    if temp_list not in custom_prime_factors_list:
        custom_prime_factors_list.append(temp_list)  # if not then appending it

print(custom_prime_factors_list)
