#258 Add Digits
def addDigits(num): 
    if num == 0:
        return 0
    elif num%10 == num:
        return num
    sum = 0
    while num%10 != num:
        sum = 0
        while num !=0:
            sum+=num%10
            num=num//10
        num = sum

    return sum

print(addDigits(1))
        
