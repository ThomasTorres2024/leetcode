#347 Top K Frequent Elements 

def brute_force_solu(nums, k):
        
    count_hash  = {}
    for i in range(len(nums)):
        count_hash[nums[i]] = 1+ count_hash.get(nums[i],0)

    matching_k_occurrences = sorted(count_hash.values())

    return matching_k_occurrences[0:k]


print(brute_force_solu([-1,-1],1))

