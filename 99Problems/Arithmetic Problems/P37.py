'''
Calculate Euler's totient function phi(m) (improved).
    See problem P34 for the definition of Euler's totient function. 
    If the list of the prime factors of a number m is known in the form 
    of problem P36 then the function phi(m) can be efficiently calculated 
    as follows: Let ((p1 m1) (p2 m2) (p3 m3) ...) be the list of prime 
    factors (and their multiplicities) of a given number m. Then phi(m) 
    can be calculated with the following formula:

    phi(m) = (p1 - 1) * p1 ** (m1 - 1) + (p2 - 1) * p2 ** (m2 - 1) + (p3 - 1) * p3 ** (m3 - 1) + ...

    Note that a ** b stands for the b'th power of a.
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


def calc_phi(factors_list):
    calculated_phi = 0
    '''applying formula to calculate phi with factors
            phi(m) = (p1 - 1) * p1 ** (m1 - 1) + (p2 - 1) * p2 ** (m2 - 1) + (p3 - 1) * p3 ** (m3 - 1) + ...
        '''
    for element in factors_list:
        calculated_phi += ((element[0] - 1) * element[0] ** (element[1] - 1))
    return calculated_phi


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
print(f'phi({number}) is: {calc_phi(custom_prime_factors_list)}')
