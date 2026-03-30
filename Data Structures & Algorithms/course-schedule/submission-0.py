class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i:[] for i in range(numCourses)}
        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if preqMap[crs] == []:
                return True

            visit.add(crs)
            for preq in preqMap[crs]:
                if not dfs(preq):
                    return False
            visit.remove(crs)
            preqMap[crs] = []
            return True
        
        # loop through all course in number of courses, because graph can be not connected
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True                





