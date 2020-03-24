# "-(a+b) + c - (d-e)" 
#in_bracket = 0
def convert(equation):
    eqn = []
    sign = []
    neg_counter = 0
    sign_set = set()
    sign_set.add('+')
    sign_set.add('-')
    equation = "".join(equation.split())  # in case there are spaces in the equation
    equation = list(equation)
    for i in range(len(equation)):
        if equation[i] == '(' and i > 0:
            equation[i] = ''
            s = equation[i-1]
            if s == '-':
                neg_counter += 1
            sign.append(s)
            
        elif equation[i] == ')':
            equation[i] = ''
            s = sign.pop()
            if s == '-':
                neg_counter -= 1
        elif equation[i] == '+':
            if len(sign) > 0 and sign[-1] == '-':
                equation[i] = '-'
        elif equation[i] == '-':
            if len(sign) > 0 and sign[-1] == '-':
                equation[i] = '+'
    
    equation = ''.join(equation)
    equation = list(equation)
    for i in range(len(equation)):
        if i > 0 and equation[i] in sign_set and equation[i-1] in sign_set:
                equation[i-1] = ''
    for i in range(len(equation)):
        if equation[i] == '':
            continue
        if equation[i] == '+':
            equation[i] = ''
            break
    
    return ''.join(equation)
    
print(convert("-(-(-(-(-a))))"))               
    
