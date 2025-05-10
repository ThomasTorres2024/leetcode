import heapq 

#1046. Last Stone Weight
def lastStoneWeight(stones):
    #Solution using built in sort algorithm 
    while len(stones) > 1:
        stones = sorted(stones)
        if stones[len(stones)-1] - stones[len(stones)-2] > 0:
            stones.append(stones[len(stones)-1] - stones[len(stones)-2])
            stones.pop(len(stones)-2)
            stones.pop(len(stones)-2)
        else:
            stones.pop(len(stones)-1)
            stones.pop(len(stones)-1)
    if len(stones) == 0:
        return 0
    else: 
        return stones[0]

def lastStoneWeightQueue(stones):
    stones= [-x for x in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
    return -(stones[0])

def usingDefaultPythonMethods(stones):
        while len(stones)>1:
            new = max(stones)
            stones.remove(new)
            new -=max(stones)
            stones.remove(max(stones))
            if new > 0:
                stones.append(new)
        if len(stones) == 0:
            return 0
        else: 
            return stones[0]



print(usingDefaultPythonMethods([1]))