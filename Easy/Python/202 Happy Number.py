#202. Happy Number 
def isHappy(n):
    for i in range(10):
        sum = 0 
        while n != 0:
            sum += (n%10)*(n%10)
            n = n//10
            print("Updated N: " + str(n))
            print("Updated Sum: " + str(sum))
        n = sum 
        if sum == 1:
            return True 
        print("Updated N: " + str(n))
    return False
        
#Expected True
print(isHappy(2))
#Expected False
print(isHappy(2))