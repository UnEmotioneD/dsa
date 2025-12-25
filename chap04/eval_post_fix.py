from array_stack import ArrayStack


class EvalPostFix:
    def __init__(self, expr):
        self._stack = ArrayStack(100)
        self._expr = expr

    def eval_post_fix(self):
        for token in self._expr:
            if token in "+-*/":
                val2 = self._stack.pop()
                val1 = self._stack.pop()
                if token == "+":
                    self._stack.push(val1 + val2)
                elif token == "-":
                    self._stack.push(val1 - val2)
                elif token == "*":
                    self._stack.push(val1 * val2)
                elif token == "/":
                    self._stack.push(val1 / val2)
            else:
                self._stack.push(float(token))

        return self._stack.pop()
