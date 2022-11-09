class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and int(c) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        # remove the leading zeros
        while stack and int(stack[0]) == 0:
                stack.pop(0)
            
        return "".join(stack) if stack else "0"
                
        
        
        