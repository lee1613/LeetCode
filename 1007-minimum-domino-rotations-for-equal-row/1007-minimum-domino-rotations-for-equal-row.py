class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        first = tops[0]
        second = bottoms[0]
        first_top = 1
        second_bottom = 1
        if first == second:
            for i in range(1, len(tops)):
                if tops[i] != first and bottoms[i] != first:
                    return -1
            return len(tops) - max(Counter(tops)[first], Counter(bottoms)[first])
                    

                
                
        else:
            
            first_bottom = 0
            second_top = 0
            first_valid = True
            second_valid = True
            for i in range(1, len(tops)):
                if first_valid:
                    if bottoms[i] != first and tops[i] != first:
                        first_valid = False
                    if tops[i] == first:
                        first_top += 1
                    if bottoms[i] == first:
                        first_bottom += 1
                    
                    
                    
                    
                if second_valid:
                    if bottoms[i] != second and tops[i] != second:
                        second_valid = False
                    if tops[i] == second:
                        second_top += 1
                    if bottoms[i] == second:
                        second_bottom += 1
                
                if not first_valid and not second_valid:
                    return -1
            
            if first_valid and second_valid:
                return len(tops) - max(first_top, first_bottom, second_top, second_bottom)
            elif first_valid: 
                return len(tops) - max(first_top, first_bottom)
            else:
                return len(tops) - max(second_top, second_bottom)
