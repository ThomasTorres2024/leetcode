#Template for Solutions
import time

def timer(test_function : function):
    start = time.time()
    function()
    end = time.time()
    print("Time: " + str(end-start))

test_vals = []
results = []
expected_vals = []

for x in test_vals: 
    timer()