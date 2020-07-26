'''
Determine whether two positive integer numbers are coprime.
    Two numbers are coprime if their greatest common divisor equals 1.
    Example:
    * (coprime 35 64)
    T
'''


def gcd(a, b):
    if b == 0:
        return a  		# after some iteration b beacomes zero, and a is the gcd of a and b
    return gcd(b, a % b)  # Euclid's algoritms states that gcd(a,b)=gcd(b,a%b)


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if gcd(num1, num2) == 1:  # using euclid's gcd algorithm to check coprime number
    print("Coprime")  # if two numbers are coprime gcd of numbers is 1
else:
    print("non coprime")
