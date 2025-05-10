#20 Valid Parentheses 
def isValid(s):
    hashmap = {
        "(":")",
        ")":"(",
        "{":"}",
        "}":"{",
        "[":"]",
        "]":"[",
    }
    if len(s)%2 != 0:
        return False
    else:
        for i in range(len(s)-1):
            print(i)
            if s[i] == hashmap[s[len(s)-1-i]]:
                continue
            elif s[i+1] == hashmap[s[i]]:
                print("S[i] :" + s[i])
                print("S[i+1] :" + hashmap[s[i+1]])
                i=2
                print(i)
            else:
                print("S[i] :" + s[i])
                print("S[i+1] :" + hashmap[s[i+1]])
                return False
        if s[len(s)-2] != hashmap[s[len(s)-1]] and hashmap[s[len(s)-1]] != s[0]:
                return False
    return True

print(isValid("()[]{}"))