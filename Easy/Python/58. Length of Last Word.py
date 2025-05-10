#Solution Going from the Last Word 
def lengthOfLastWord(s):
    pointer = len(s)-1
    for i in range(len(s)):
        if s[pointer] != " ":
            for j in range(len(s)):
                if s[pointer-j] == " ":
                    return j 
        pointer-=1
    return len(s)

#Solution with Python 
def lengthPython(s):
    return len(s.split()[len(s.split())-1])

print(lengthPython("Hello World"))
