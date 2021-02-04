class Solution:
    def isValid(self, s: str) -> bool:
        close = {}
        close['('] = ')'
        close['{'] = '}'
        close['['] = ']'
        op3n = ['(', '[', '{']
        stack = []
        
        for ch in s:
            if ch in op3n:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            elif ch == close[stack[-1]]:
                stack = stack[:-1]
            else:
                return False
        
        if len(stack) > 0:
            return False
        return True
