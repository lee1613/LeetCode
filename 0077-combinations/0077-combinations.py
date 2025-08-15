class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        

        combi = [i for i in range(1, k + 1)]

        if n == k:
            return [combi]
        
        res = []
        res.append([i for i in range(1, k + 1)])
        while True:
            
            next_combi = combi.pop(-1) + 1
            
            while len(combi) < k:
                # Curr index (len(combi))
                if next_combi > len(combi) + n - k + 1:
                    if len(combi) == 0:
                        return res
                    next_combi = combi.pop(-1) + 1
                else:
                    combi.append(next_combi)
                    next_combi += 1
            
            res.append([i for i in combi])

        return res

            
