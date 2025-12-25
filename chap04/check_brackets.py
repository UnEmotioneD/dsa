from array_stack import ArrayStack


class CheckBrackets:
    def __init__(self, statement):
        self._stack = ArrayStack(100)
        self._statement = statement

    def check_brackets(self):
        for char in self._statement:
            if char in ("(", "{", "["):
                self._stack.push(char)
            elif char in (")", "}", "]"):
                if self._stack.is_empty():
                    return False
                if not self._stack.is_empty():
                    left = self._stack.pop()
                    if char == ")" and left != "(":
                        return False
                    if char == "}" and left != "{":
                        return False
                    if char == "]" and left != "[":
                        return False
            return self._stack.is_empty()
