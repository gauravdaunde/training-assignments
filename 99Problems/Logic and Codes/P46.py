'''
Truth tables for logical expressions.
    Define predicates and/2, or/2, nand/2, nor/2, xor/2, impl/2 and equ/2 (for logical equivalence) which succeed or fail according to the result of their respective operations; e.g. and(A,B) will succeed, if and only if both A and B succeed. Note that A and B can be Prolog goals (not only the constants true and fail).

    A logical expression in two variables can then be written in prefix notation, as in the following example: and(or(A,B),nand(A,B)).

    Now, write a predicate table/3 which prints the truth table of a given logical expression in two variables.

    Example:
    * table(A,B,and(A,or(A,B))).
    true true true
    true fail true
    fail true fail
    fail fail fail
'''


# predicate funtion return true if any one is true or both A and B are true, oterwise return false
def predicateOr(A, B):
    if A or B:
        return True
    else:
        return False


# predicate function returns true if both A and B are False or one of them is False
def predicateNand(A, B):
    if not(A and B):
        return True
    else:
        return False


# predicate function return true only if both A and B are true,otherwise returns false
def predicateAnd(A, B):
    if A and B:
        return True
    else:
        return False


# for two input A and B inputs to predicate functions are
A = [True, True, False, False]
B = [True, False, True, False]

print('Result for: and(A,or(A,B))')

# finding output of given expression with  all possible values of A and B
for i in range(len(A)):
    print(f"{A[i]}\t{B[i]}\t{predicateAnd(A[i],predicateOr(A[i],B[i]))}")


print('\nResult for: and( or (A, B), nand(A, B))')

for i in range(len(A)):
    output = predicateAnd(predicateOr(A[i], B[i]), predicateNand(A[i], B[i]))
    print(f"{A[i]}\t{B[i]}\t{output}")
