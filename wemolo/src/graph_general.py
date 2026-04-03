class GraphSolutions:
    # 1. Number of Islands
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        rows, cols, islands = len(grid), len(grid[0]), 0
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0" # Mark as visited
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands

    # 2. Course Schedule (Cycle Detection)
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites: preMap[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit: return False
            if preMap[crs] == []: return True
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
