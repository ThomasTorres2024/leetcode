#2544. Alternating Digit Sum
def alternateDigitSum(n):
    sum = 0
    for i in range(len(str(n))):
        if i%2 == 0:
            sum+=int(str(n)[i])
        else: 
            sum-=int(str(n)[i])
    return sum 


print(alternateDigitSum(111))