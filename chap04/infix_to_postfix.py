"""
19102467 김찬희

chapter 04
Page 150
"""

from ArrayStack import ArrayStack


def precedence(op):
    if op in ('(', ')'):
        return 0
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return -1


def infix_2_postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push(term)
        elif term == ')':
            while not s.is_empty():
                op = s.pop()
                if op == '(':
                    break
                output.append(op)
        elif term in ('+', '-', '*', '/'):
            while not s.is_empty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(s.pop())
                else:
                    break
            s.push(term)
        else:
            output.append(term)

    while not s.is_empty():
        output.append(s.pop())

    return output


def eval_post_fix(expr):
    s = ArrayStack(100)

    for token in expr:
        if token in '+-*/':
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1 + val2)
            elif token == '-':
                s.push(val1 - val2)
            elif token == '*':
                s.push(val1 * val2)
            elif token == '/':
                s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()


def main() -> None:
    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    postfix1 = infix_2_postfix(infix1)
    postfix2 = infix_2_postfix(infix2)

    result1 = eval_post_fix(postfix1)
    result2 = eval_post_fix(postfix2)

    print(f'중위표기: {infix1}')
    print(f'후위표기: {postfix1}')
    print(f'계산 결과: {result1}')
    print()
    print(f'중위표기: {" ".join(infix2)}')
    print(f'후위표기: {" ".join(postfix2)}')
    print(f'계산 결과: {result2}')


if __name__ == '__main__':
    main()
