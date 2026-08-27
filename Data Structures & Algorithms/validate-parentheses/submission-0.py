class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]":"[",
            "}":"{"
        }
        for i in s:
            if i in "({[":
                stack.append(i)
            elif i in ")}]":
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop()
        return len(stack) == 0
            
            


        