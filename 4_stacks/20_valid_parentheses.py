class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            
            if (not stack) or (stack[-1] != Map[c]):
                return False
            
            stack.pop()
        
        return not stack
    
sol = Solution()

case_1 = "()"
case_2 = "()[]{}"
case_3 = "(]"
case_4 = "({[]})"
case_5 = "([)]"
case_6 = "["
case_7 = "]"

print(sol.isValid(case_1))
print(sol.isValid(case_2))
print(sol.isValid(case_3))
print(sol.isValid(case_4))
print(sol.isValid(case_5))
print(sol.isValid(case_6))
print(sol.isValid(case_7))