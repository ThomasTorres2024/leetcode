#Template for Solutions
import time

def romanToInt(s):
    h={"I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000}
    sum = 0
    if len(s) == 1:
        return h[s]
    i = 0
    while i < len(s):
        if i != len(s)-1 and h[s[i]]<h[s[i+1]]:
            sum+=h[s[i+1]]-h[s[i]]
            i+=2
        else:
            sum+=h[s[i]]
            i+=1
    return sum
        
    

def timer():
    start = time.time()
    function()
    end = time.time()
    print("Time: " + str(end-start))

test_vals = ["III","LVIII","MCMXCIV"]
results = []
expected_vals = []

for x in test_vals: 
    print(romanToInt(x))