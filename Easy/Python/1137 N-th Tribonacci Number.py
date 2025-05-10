import time 
#1137 N-th Tribonacci Number 
#Using memoization
def meme_tribonacci(n,mem):
    if n in mem:
        return mem[n]
    else: 
        mem[n] = meme_tribonacci(n-1,mem)+meme_tribonacci(n-2,mem)+meme_tribonacci(n-3,mem)
        return mem[n]

#using recursion (Leetcode doesn't even accept this)
def tribonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    else:
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

#using brute force 
def tribonacci_brute(n):
    if n == 0: 
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1 
    t0 = 0
    t1 = 1
    t2 = 1
    for i in range(n-2):
        tn = t0+ t1 + t2
        t0 = t1 
        t1 = t2 
        t2 = tn
    return tn
#Testing
test_vals = [30]
for  x in test_vals:
    start = time.time()
    print(tribonacci(x))
    end = time.time()
    print("For non-mem: " + str(end-start))

    start1 = time.time()
    print(meme_tribonacci(x,{0:0, 1:1 , 2:1}))
    end2 = time.time()
    print("For mem: " + str(end2-start1))

    start = time.time()
    print(tribonacci_brute(x))
    end = time.time()
    print("For brute force: " + str(end-start))