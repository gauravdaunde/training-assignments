'''
Truth tables for logical expressions (3).
    Generalize problem P47 in such a way that the logical expression 
    may contain any number of logical variables. Define table/2 in a 
    way that table(List,Expr) prints the truth table for the expression 
    Expr, which contains the logical variables enumerated in List.

    Example:
    * table([A,B,C], A and (B or C) equ A and B or A and C).
    true true true true
    true true fail true
    true fail true true
    true fail fail true
    fail true true true
    fail true fail true
    fail fail true true
    fail fail fail true

'''


def evaluate(expr, input_data):
    # checking if expression contains any brackets, to solve bracket first
    if '(' in expr:
        # if found then solve that nested expression present in bracket first
        new_expr = expr[:expr.find(')')+1]  # taking that equation
        # removing brackets
        new_expr = new_expr.replace(
            '(', '').replace(')', '')
        # calling evaluate again with new expression
        result = evaluate(new_expr, input_data)
        # adding got result at its place from where expression is grabbed
        expr = expr[:expr.find('(')]+str(result)+expr[expr.find(')')+1:]
        # returing result after solving expression
        return evaluate(expr, input_data)

    else:
        # converting string to list with seperated by space
        new_list = list(expr.split(' '))

        # if list contains only one element, element itself the result of whole expression
        while len(new_list) > 1:

            # if expression contains not operation then performing here
            if 'not' in new_list:
                i = new_list.index('not')
                new_list[i+1] = str(not input_data[new_list[i+1]])
                new_list.remove('not')

            # if expression contains and operation then performing here
            if 'and' in new_list:
                i = new_list.index('and')
                res = new_list[i-1] and new_list[i+1]
                new_list.pop(i-1)
                new_list.insert(i-1, str(res))
                new_list.remove('and')
                new_list.pop(i)

            # if expression contains or operation then performing here
            elif new_list[1] == 'or':
                res = input_data[new_list[0]] or input_data[new_list[2]]
                new_list = new_list[3:]
                new_list.insert(0, str(res))

        return new_list[0]  # returning result


# logical expression to be evaluated
expr = 'A and (B or C) equ A and B or A and C'


# inputs
A = [True, True, True, True, False, False, False, False]
B = [True, True, False, False, True, True, False, False]
C = [True, False, True, False, True, False, True, False]

print(f"A\tB\tC\tOutput")

for i in range(len(A)):
    data = {'A': A[i], 'B': B[i], 'C': C[i], 'True': True, 'False': False}

    # splitting equation in two parts with equ operator
    expr_1, expr_2 = expr.split('equ')
    expr_1, expr_2 = expr_1.strip(), expr_2.strip()  # removing white spaces

    # calling evaluate functions for both functions
    res_1 = evaluate(expr_1, data)
    res_2 = evaluate(expr_2, data)

    # checking equality as i expression
    output = res_1 == res_2

    # printing outputs
    print(f"{A[i]}\t{B[i]}\t{C[i]}\t{output}")
