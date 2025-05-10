#2553 Sepaarate the Digits in an Array

def separateDigits(nums):
    new = []
    for i in range(len(nums)):
        while nums[i] % 10 != nums[i]:
            new.append(nums[i]%10)
            nums[i] = nums[i]//10
        new.append(nums[i])
    return new

print(separateDigits([13,25,83,77]))
        