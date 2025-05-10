import math
def containsNearbyDuplicate(nums, k):
    hashmap = {}
    for i in range(len(nums)):
          if nums[i] not in hashmap:
                hashmap[nums[i]] = i
          else: 
               print(hashmap[nums[i]])
               print(i)
               if abs(hashmap[nums[i]] - i ) <= k:
                return True
               else: 
                hashmap[nums[i]] = i
    return False 

print(containsNearbyDuplicate([1,2,3,1,2,3],2))