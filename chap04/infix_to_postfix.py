"""
19102467 김찬희

Page 150
---
example)
input: 8/2-3+(3*2)
output: 82/3-32*+
"""

def check_brackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch == '(' or ch == '{' or ch == '[':


def infix_2_postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term in '(':
            s.push('()')


def main() -> None:
    print('Hello, world')


if __name__ == '__main__':
    main()
