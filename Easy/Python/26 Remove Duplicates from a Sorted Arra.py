#I decided to give up on this problem, when I print nums it seems fine in this code, but when I
#put it into leetcode it gives me an error for some reason 
#26 Remove Duplicates from a Sorted Array

def removeDuplicates(nums):
    nums2 = []
    for i in range(len(nums)):
        if nums[i] not in nums2:
            nums2.append(nums[i])
    nums = nums2

    #Remove 
    print(nums)

    return len(nums)

def main():
    print(removeDuplicates([1,1,2]))

main()