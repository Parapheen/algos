# Algrorithms 

# 1. Brackets
def is_correct(s):
    stack = []
    index_stack = []
    i = 1
    for char in s:
        if char in ('(', '[', '{'):
            stack += char
            index_stack.append(i)
        else:
            if char not in (')', ']', '}'):
                i += 1
                continue
            elif stack:
                top = stack[-1]
                if top == '(' and char == ')' or top == '[' and char == ']' or top == '{' and char == '}':
                    stack.pop(-1)
                    index_stack.pop(-1)
                else:
                    return i
            else:
                return i
        i += 1
    if len(stack) == 0:
        return 'Success'
    else:
        return index_stack[-1]

# 2. Tree heights
# def tree_height(n, st):


# 3. https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python
def tickets(people):
    bank = [] # clerks money
    """ if there is change with 25$ we return YES starting our sales """
    for cash in people:
        if cash > 25 and len(bank) == 0:
            return 'NO'
        elif cash == 25:
            bank.append(cash)
        else:
            if sum(bank) >= cash - 25:
                while bank:
                    change = cash - bank[-1]
                    bank.pop()
                    if change == 25:
                        bank.append(cash)
                        break
                    
            else:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    # print(is_correct('foo(bar);'))
    print(tickets([25, 25, 50, 100]))
