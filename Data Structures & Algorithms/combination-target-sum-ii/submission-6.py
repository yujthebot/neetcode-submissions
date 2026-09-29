class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(start, path,total):
            exist = set()
            if total == target:
                ans.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                if candidates[i] in exist:
                    continue
                if total + candidates[i]> target:
                    break
                exist.add(candidates[i])
                total+=candidates[i]
                path.append(candidates[i])
                backtrack(i+1,path,total)
                path.pop()
                total-=candidates[i]
        backtrack(0,[],0)
        return ans