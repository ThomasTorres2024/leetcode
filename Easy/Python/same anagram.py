#retard brute force solu
def groupAnagrams(strs):
        containersHash = []

        array_container = []

        for j in range(len(strs)):
            s = strs[j]
            char_dict = {}
            for char in s:
                if char not in char_dict:
                    char_dict[char] = 1
                else:
                    char_dict[char] +=1

            dicts_unequal = True
            for i in range(len(containersHash)):
                if char_dict ==  containersHash[i]:
                    dicts_unequal = False 
                    array_container[i].append(s)
                    break

            if dicts_unequal:
                array_container.append([s])
                containersHash.append(char_dict)

        return array_container

#solu i thought of
def sortedSolu(strs):
        #main idea, every str has a fundamental sort, so we can sort them, and then make an array container where the sorted str corresponds to the 
        sorted_hash  = {}

        #container corresponding to each unique array, there are n arrays inside for eaach unique anagram
        array_container = []

        #go through strs 
        for j in range(len(strs)):

            #sort str and conver sorted to str 
            s = strs[j]
            sorted_str = ' '.join(sorted(s))

            #if sorted str is not in sorted, then add it and add it to the container
            if sorted_str not in sorted_hash:
                sorted_hash[sorted_str] = len(array_container)
                array_container.append([s])

            #add last array
            else:
                array_container[sorted_hash[sorted_str]].append(s)

        return array_container

#neet code optimal o(n*m*26) solu:
import collections
def optimal_solu(strs):
    ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
            
        ans[tuple(count)].append(s)
    return ans.values()

print(optimal_solu(["eat","tea","tan","ate","nat","bat"]))