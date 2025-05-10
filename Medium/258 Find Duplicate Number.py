#258 Find Duplicaate Number 

#O(N) solution using a hashmap, but a higher space compltexiy than they wanted 
def findDuplicate(nums):
    hashmap = {}
    for i in range(len(nums)):
        if nums[i] not in hashmap:
            hashmap[nums[i]] =i
        else: 
            return nums[i] 
print(findDuplicate([3,1,3,4,2]))
