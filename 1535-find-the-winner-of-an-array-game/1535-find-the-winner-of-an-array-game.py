class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        win_count = 0
        candidate = arr[0]
        for i in range(1, len(arr)):
            print(candidate, arr[i])
            if candidate > arr[i]:
                win_count += 1
                if win_count == k:
                    return candidate
            else:
                candidate = arr[i]
                win_count = 1
                if win_count == k:
                    return candidate
            
        return candidate
