class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # [73,74,75,71,69,72,76,73]
        
        temps = temperatures
        res = [0] * len(temps)
        
        stack = [] # (73, 0)
        for i, t in enumerate(temps):
            
            while stack and t > stack[-1][0]:
                last_temp, last_index = stack.pop()
                res[last_index] = i - last_index
            
            stack.append([t,i])
        return res
