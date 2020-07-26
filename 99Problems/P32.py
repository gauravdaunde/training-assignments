'''
Determine the greatest common divisor of two positive integer numbers.
    Use Euclid's algorithm.
    Example:
    * (gcd 36 63)
 '''


def gcd(a, b):
    if b == 0:
        return a  # after some iteration b beacomes zero, and a is the gcd of a and b
    return gcd(b, a % b)  # Euclid's algoritms states that gcd(a,b)=gcd(b,a%b)


num1 = int(input('Enter first numbers: '))
num2 = int(input('Enter second numbers: '))
print(f'gcd of {num1} and {num2} is {gcd(num1,num2)}')
