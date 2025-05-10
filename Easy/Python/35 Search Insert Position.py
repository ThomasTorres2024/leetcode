#35 Search Insert Position 
import math 
def searchInsert(nums, target):
    i1 = len(nums)-1
    for i in range (len(nums)):
        i2 = math.ceil(i1/2)
        print(i1)
        print(i2)
        if nums[i2] > target: 
            i1 -= math.ceil((i1+i2)/2)

        #if nums[i] == target:
        #    return i

#Expected 2 
#print(searchInsert([1,3,5,6],5))
#Expected 1 
print(searchInsert([1,3,5,6],2))
#Expected 4
#print(searchInsert([1,3,5,6],7))