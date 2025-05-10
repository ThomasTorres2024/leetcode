def strStr(haystack, needle):
    for i in range(len(haystack)):
        index = i
        if len(haystack) - index >= len(needle):
            for j in range(len(needle)):
                    if haystack[index+j] == needle[j]:
                        i+=1
                        if j == len(needle)-1:
                            return index 
                    else: 
                        break
        else:
            return -1
    return -1
   
        
#Expected 0            
print(strStr("sadbutsad","sad"))
#Expected -1
print(strStr("leetcode","leeto"))

