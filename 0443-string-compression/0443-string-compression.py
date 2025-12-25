class Solution:
    def compress(self, chars: List[str]) -> int:
        write_i = 0
        res = 0
        prev = chars[0]
        prev_count = 1
        for i in range(1, len(chars)):
            if chars[i] != prev:
                # Add the result once identify one repeating characters sequence
                res += 1
                chars[write_i] = prev
                write_i += 1
                # Make it into a string and add it
                if prev_count > 1:
                    prev_count = str(prev_count)
                    n = len(prev_count)
                    for j in range(n):
                        chars[write_i +j] = prev_count[j]
                        res += 1
                    write_i += n

                    prev_count = 1
                
                prev = chars[i]
            else:
                prev_count += 1
        
        chars[write_i] = prev
        res += 1
        write_i += 1
        if prev_count > 1:
            prev_count = str(prev_count)
            n = len(prev_count)
            for j in range(n):
                chars[write_i +j] = prev_count[j]
                res += 1

        return res
        



        