class Solution:
    def reverseVowels(self, s: str) -> str:
        # Using two pointer approach ,to save time, especially string concatenation, I will put the back of the pointer into a string and add from the back
        if len(s) == 1:
            return s
        front = 0
        back = len(s) - 1
        res = ""
        reverse = []
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        while front < back:
            # The following 2 loops helps us to find the first vowel to exchange going from the back and the front
            while front < len(s) and s[front] not in vowels:
                res += s[front]
                front += 1

            # If no vowel, it will go all the way to the back

            # IF there's one vowel, front will be at that index, the following will not going into that index regardless
            
            while s[back] not in vowels and back > front:
                reverse.append(s[back])
                back -= 1

            # There might be a time there's no vowel at all, the later condition on the loop above ensure that

            # The edge cases where there's only one vowel and both of them stop at that indexes and it wasn't being added?
            
            if front < back:
                res += s[back]
                reverse.append(s[front])
                front += 1 
                back -= 1
        
        # If both vowels are next to each other, then front will now bigger than back and the case where both pointer stops at the middle vowels will make it a character that have yet to add in
        if front == back:
            res += s[front]
        for i in range(len(reverse) - 1, -1, -1):
            res += reverse[i]
        
        return res

        