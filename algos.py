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
# def tickets(people):
    

# 4. binary_search
def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    # print(is_correct('foo(bar);'))
    # print(tickets([25, 25, 25, 25, 50, 100, 50]))
    print(binary_search([1, 3, 5, 7, 9], 3))
