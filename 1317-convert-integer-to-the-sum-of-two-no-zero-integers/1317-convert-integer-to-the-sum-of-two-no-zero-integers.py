class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        str_n = str(n)
        deduct = False
        a = 0
        b = 0
        for i in range(len(str_n) - 1, 0, -1):
            curr = int(str_n[i])
            if deduct:
                curr -= 1
            
            a +=  10** (len(str_n) -1 - i)
            if curr == -1:
                deduct = True
                b += 8 * (10 ** (len(str_n) - 1 - i))
                
            elif curr == 0:
                deduct = True
                b += 9 * (10 ** (len(str_n) - 1 - i))

            elif curr == 1:
                deduct = True
                b += 9 * (10 ** (len(str_n) - 1 - i))
                a += 10** (len(str_n) -1 - i)
            else:
                deduct = False
                b += (curr - a) * (10** (len(str_n) - i - 1))

        
        curr = int(str_n[0])
        if deduct:
            curr -= 1
        if curr != 0:
            a += 10 ** (len(str_n) - 1)
            b += (curr - a) * (10** (len(str_n) - 1))

        return [a, b]

            