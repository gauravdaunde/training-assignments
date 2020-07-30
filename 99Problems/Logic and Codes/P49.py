'''
Gray code.
    An n-bit Gray code is a sequence of n-bit strings constructed
    according to certain rules. For example,
    n = 1: C(1) = ['0','1'].
    n = 2: C(2) = ['00','01','11','10'].
    n = 3: C(3) = ['000','001','011','010',´110´,´111´,´101´,´100´].

    Find out the construction rules and write a predicate with the
    following specification:

    % gray(N,C) :- C is the N-bit Gray code

    Can you apply the method of "result caching" in order to make
    the predicate more efficient, when it is to be used repeatedly?
'''


# function finds gray code of N bits with given gray codes of N-1 bits and N-2 bits(for 2 bit it calculates from 1 bit only)
def findGrayCode(N, gray_code, gray_code_2):
    result_gray_code = []
    for code in gray_code:
        if code == '0':
            i = 0
            while i < len(gray_code_2):
                result_gray_code.append(code+gray_code_2[i])
                i += 1
        else:
            i = len(gray_code_2)-1
            while i >= 0:
                result_gray_code.append(code+gray_code_2[i])
                i -= 1
    return result_gray_code


data = ['0', '1']
N = int(input('Enter how many bit gray code to generate: '))
i = 2
code = data
gray_code = data

# finding gray code
while i <= N:
    gray_code = findGrayCode(i, code[:], gray_code[:])
    i += 1

print(gray_code)
