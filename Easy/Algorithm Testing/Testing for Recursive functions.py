import time 

#Testing for Recursive functions

def evenNums(num):
    print(num)
    if num == 2:
        return num 
    else: 
        evenNums(num-2)

def fibonacci(num):
    if num <= 1:
        return num
    else: 
        return fibonacci(num-1) + fibonacci(num-2)

def factorial(num):
    if num == 0:
        return 1
    else: 
        return (num)*factorial(num-1)

def factorialIt(num):
    result = 1
    while num > 0:
        result*num
        num-=1
    return result

a = 100
start = time.time()
print(factorial(a))
end = time.time()
time1 = end-start
print("Recursion: " + str(end - start))


start = time.time()
print(factorialIt(a))
end = time.time()
time2 = end-start
print("Iteration: " + str(end - start))
print("Runtime difference: " + str(time1-time2))

