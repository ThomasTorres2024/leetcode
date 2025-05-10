#217 Contains Duplicate

def containsDuplicate(nums):
    d={}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]]=i
        else:
            return True
    return False
        
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]
))