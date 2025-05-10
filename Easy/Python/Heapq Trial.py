import heapq 

data =[2,7,4,1,8,1]
data = [-x for x in data]
heapq.heapify(data)
new = heapq.heappop(data) - heapq.heappop(data)
data.append(new)
print(data)