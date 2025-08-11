class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    open_bracket = stack.pop(-1)
                    if c == ")":
                        if open_bracket != "(":
                            return False
                    if c == "]":
                        if open_bracket != "[":
                            return False
                    if c == "}":
                        if open_bracket != "{":
                            return False
        
        if len(stack) > 0:
            return False

        return True 
