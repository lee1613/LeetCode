class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        # Have to check if there's any whitespaces after splitting
        words = words[:: -1]
        print(words)
        res = ""
        for word in words:
            if len(word) > 0:
                res += word + " "
        

        return res[:-1]
            
        # # Assuming no whitespaces:

        # res = " ".join(words[len(words) - 1: -1 : -1])
        # print(words)
        # return res
        