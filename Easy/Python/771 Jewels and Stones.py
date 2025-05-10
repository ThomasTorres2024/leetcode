#771 Jewels and Stones

#Naive Solution
def naiveNumJewelsInStones(jewels, stones):
    in_common = 0

    for s in stones:
        if s in jewels: in_common +=1 
    return in_common

#O(n+m) solution
def numJewelsInStones(jewels, stones):
    in_common = 0

    #Convert jewels to a hashmap in n time 
    jewels = set(jewels)
    for s in stones:
        #Looks up in hashmap instead of traversing a list
        if s in jewels: in_common +=1 
    return in_common

print(numJewelsInStones("Z","ZZ"))