from array_stack import ArrayStack


class Infix2Postfix:
    def __init__(self, expr):
        self._stack = ArrayStack(100)
        self._expr = expr

    def precedence(self, op):
        if op in ("(", ")"):
            return 0
        if op in ("+", "-"):
            return 1
        if op in ("*", "/"):
            return 2
        return -1

    def infix_2_postfix(self):
        output = []

        for term in self._expr:
            if term == "(":
                self._stack.push(term)
            elif term == ")":
                while not self._stack.is_empty():
                    op = self._stack.pop()
                    if op == "(":
                        break
                    output.append(op)
            elif term in ("+", "-", "*", "/"):
                while not self._stack.is_empty():
                    op = self._stack.peek()
                    if self.precedence(term) <= self.precedence(op):
                        output.append(self._stack.pop())
                    else:
                        break
                self._stack.push(term)
            else:
                output.append(term)

        while not self._stack.is_empty():
            output.append(self._stack.pop())

        return output
