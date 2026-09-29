class Solution:
    def isValid(self, s: str) -> bool:
        pos = {"(","[","{"}
        neg = {")","]","}"}
        stack = []
        if len(s)<2:
            return False
        for char in s:
            if char in pos:
                stack.append(char)
            else:
                x = stack.pop() if stack != [] else None
                if char == ")" and x == "(":
                    continue
                elif char == "]" and x == "[":
                    continue
                elif char == "}" and x == "{":
                    continue
                else:
                    return False
        if stack != []:
            return False
        return True