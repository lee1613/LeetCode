class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        # start indicating the start of the substring
        start = 0
        coll =  {s[0]: 1}
        curr_length = 1
        for i in range(1, len(s)):
            print(start)
            c = s[i]
            curr_length += 1
            if coll.get(c, 0) == 0:
                if curr_length > res:
                    res = curr_length
                coll[c] = 1
                
            else:
                while start < i:
                    curr_length -= 1
                    start_c = s[start]
                    
                    start += 1
                    if start_c == c:
                        break
                    
                    coll[start_c] -= 1

                    

                    
                    

        return res


                        
                    

                

