'''
Truth tables for logical expressions (2).
    Continue problem P46 by defining and/2, or/2, etc as being operators.
    This allows to write the logical expression in the more natural way,
    as in the example: A and (A or not B). Define operator precedence as
    usual; i.e. as in Java.

    Example:
    * table(A,B, A and (A or not B)).
    true true true
    true fail true
    fail true fail
    fail fail fail
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


# taking expression as input
expr = input('Enter input: ')


# defining inputs
A = [True, True, False, False]
B = [True, False, True, False]

print(f"A\tB\tOutput")
for i in range(len(A)):
    # creating dictionary for reference
    data = {'A': A[i], 'B': B[i], 'True': True, 'False': False}
    # calculating output by passing expression to evaluate along with data dictionary
    output = evaluate(expr, data)
    print(f"{A[i]}\t{B[i]}\t{output}")
