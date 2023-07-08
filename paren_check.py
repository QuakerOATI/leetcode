class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        try:
            for c in s:
                if c in brackets:
                    stack.append(c)
                elif brackets.get(stack.pop()) != c:
                    return False
            return len(stack) == 0
        except IndexError:
            return False
