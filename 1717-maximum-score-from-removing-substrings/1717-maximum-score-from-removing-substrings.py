class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        out = 0
        buffer = 0
        
        if x > y:
            priority = "a"
            second = "b"
            higher = x
            lower = y
        else:
            priority = "b"
            second = "a"
            higher = y
            lower = x
        
        prior_count = 0



        for c in s:
            if c == priority:
                prior_count += 1

            elif c == second:
                if prior_count > 0:
                    out += higher
                    prior_count -= 1
                else:
                    buffer += 1
            
            else:
                out += min(prior_count, buffer) * lower
                prior_count = 0
                buffer = 0

        out += min(prior_count, buffer) * lower

        return out

                
