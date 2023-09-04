class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        for i in s:
            if (i == "(") or (i == "{") or (i == "["):
                brackets.append(i)
            elif (i == ")" ) and (len(brackets) == 0):
                brackets.append(i)
            elif (i == "}" ) and (len(brackets) == 0):
                brackets.append(i)
            elif (i == "]" ) and (len(brackets) == 0):
                brackets.append(i)
            elif (i == ")") and (brackets[-1] == "{"):
                brackets.append(i)
            elif (i == ")") and (brackets[-1] == "("):
                brackets.pop()
            elif (i == ")") and (brackets[-1] == "["):
                brackets.append(i)
            elif (i == "}") and (brackets[-1] == "("):
                brackets.append(i)
            elif (i == "}") and (brackets[-1] == "{"):
                brackets.pop()
            elif (i == "}") and (brackets[-1] == "["):
                brackets.append(i)
            elif (i == "]") and (brackets[-1] == "("):
                brackets.append(i)
            elif (i == "]") and (brackets[-1] == "{"):
                brackets.append(i)
            elif (i == "]") and (brackets[-1] == "["):
                brackets.pop()
            else:
                brackets.append(i)
                

        if (len(brackets) == 0):
            return 1
        else:
            return 0


        
