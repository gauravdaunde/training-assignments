'''
Determine whether a given integer number is prime.
    Example:
    * (is-prime 7)
    T
'''

#checking number is prime or not
def isPrime(number):

	#checking given number is divisible by any number from 2 to number itself
	for num in range(2,number):	
		if number == 1 or number % num ==0 and number != num:		#if so then number is not prime
			return(f'{number} is not prime')
	return(f'{number} is prime.')			


num = int(input('Enter any number: '))
print(isPrime(num))
