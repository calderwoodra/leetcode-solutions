class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set()
        q = []
        islands = 0
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if (m,n) in seen:
                    continue
                
                if grid[m][n] == "0":
                    seen.add((m,n))
                    continue
                
                islands += 1
                q.append((m,n))
                while q:
                    curr = q.pop()
                    seen.add(curr)
                    
                    j,k = curr
                    if grid[j][k] == "0":
                        continue
                    else:
                        if j - 1 >= 0 and (j - 1, k) not in seen:
                            q.append((j - 1, k))
                        if j + 1 < len(grid) and (j + 1, k) not in seen:
                            q.append((j + 1, k))
                        if k - 1 >= 0 and (j, k - 1) not in seen:
                            q.append((j, k - 1))
                        if k + 1 < len(grid[0]) and (j, k + 1) not in seen:
                            q.append((j, k + 1))
        
        return islands