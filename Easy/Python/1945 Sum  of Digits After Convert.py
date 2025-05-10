#1945 Sum of Digits String After Convert

def getLucky(s,k):
    converted = ""
    sum = 0
    for i in range(len(s)):
        converted += str(ord(s[i])-96)
    for n in range(k):
        for j in range(len(converted)):
            sum+=int(converted[j])
        converted = str(sum)
        sum = 0
    return converted

print(getLucky("iiii",1))