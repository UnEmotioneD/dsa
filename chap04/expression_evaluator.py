from array_stack import ArrayStack


class ExpressionEvaluator:
    def __init__(self):
        self.stack = ArrayStack(100)

    def precedence(self, op):
        if op in ('(', ')'):
            return 0
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return -1

    def infix_2_postfix(self, expr):
        self.stack = ArrayStack(100)
        output = []

        for term in expr:
            if term == '(':
                self.stack.push(term)
            elif term == ')':
                while not self.stack.is_empty():
                    op = self.stack.pop()
                    if op == '(':
                        break
                    output.append(op)
            elif term in ('+', '-', '*', '/'):
                while not self.stack.is_empty():
                    op = self.stack.peek()
                    if self.precedence(term) <= self.precedence(op):
                        output.append(self.stack.pop())
                    else:
                        break
                self.stack.push(term)
            else:
                output.append(term)

        while not self.stack.is_empty():
            output.append(self.stack.pop())

        return output

    def eval_post_fix(self, expr):
        self.stack = ArrayStack(100)

        for token in expr:
            if token in '+-*/':
                val2 = self.stack.pop()
                val1 = self.stack.pop()
                if token == '+':
                    self.stack.push(val1 + val2)
                elif token == '-':
                    self.stack.push(val1 - val2)
                elif token == '*':
                    self.stack.push(val1 * val2)
                elif token == '/':
                    self.stack.push(val1 / val2)
            else:
                self.stack.push(float(token))

        return self.stack.pop()
