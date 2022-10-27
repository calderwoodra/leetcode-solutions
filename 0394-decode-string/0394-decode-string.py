class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # "3[a2[c]]2[a]"
        result = []         # ["accaccacc", "aa"]
        multipliers = []    # []
        chunks = []         # []
        prev = None
        for i, c in enumerate(s):
            if c.isnumeric():
                if prev and prev.isnumeric():
                    multipliers[len(multipliers) - 1] *= 10
                    multipliers[len(multipliers) - 1] += int(c)
                else:
                    multipliers.append(int(c))
            
            elif c.isalpha():
                if not chunks:
                    multipliers.append(1)
                    chunks.append("")
                chunks[len(chunks) - 1] += c
            
            elif c == '[':
                chunks.append("")
            
            elif c == ']':
                res = chunks.pop() * multipliers.pop()
                if multipliers:
                    chunks[len(chunks) - 1] += res
                else:
                    result += res
            prev = c
        
        if chunks:
            result.append(chunks.pop() * multipliers.pop())
        return "".join(result)
