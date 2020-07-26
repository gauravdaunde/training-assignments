'''
 (*) Compare the two methods of calculating Euler's totient function.
    Use the solutions of problems P34 and P37 to compare the algorithms.
     Take the number of logical inferences as a measure for efficiency. 
     Try to calculate phi(10090) as an example.
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


def getCustomFactorsList(prime_factors_list):
    custom_prime_factors_list = list()
    for factor in prime_factors_list:
        temp_list = list()
        # creating sublist of factor and its count in list
        temp_list.append(factor)
        temp_list.append(prime_factors_list.count(factor))

        # checking created sublist is alreay present or not
        if temp_list not in custom_prime_factors_list:
            custom_prime_factors_list.append(
                temp_list)  # if not then appending it
    return custom_prime_factors_list


def calc_phi_new(number):
    factors_list = calcPrimeFactorsList(number)
    custom_factors_list = getCustomFactorsList(factors_list)
    calculated_phi = 0

    '''
	applying formula to calculate phi with factors
	phi(m) = (p1 - 1) * p1 ** (m1 - 1) + (p2 - 1) * p2 ** (m2 - 1) + (p3 - 1) * p3 ** (m3 - 1) + ...
	'''
    for element in custom_factors_list:
        calculated_phi += ((element[0] - 1) * (element[0] ** (element[1] - 1)))

    return calculated_phi


def gcd(a, b):
    if b == 0:
        return a  # after some iteration b beacomes zero, and a is the gcd of a and b
    return gcd(b, a % b)  # Euclid's algoritms states that gcd(a,b)=gcd(b,a%b)


def calc_phi(number):
    count = 0

    for i in range(1, number):
        if gcd(i, number) == 1:  # checking if i and number are coprime
            count += 1  # incrementing counter on every coprime
    return count


number = int(input('Enter the number: '))


phi = calc_phi(number)
phi_by_formula = calc_phi_new(number)


print(f'factors method, phi({number}) is: {phi}')
print(f'Formula method, phi({number}) is: {phi_by_formula}')
