#101 Symmetric Tree
import math

#Access every element of Perfect Compelte Binary Tree
def printTree(root):
    print("Children of the root: " +str(root[0]) +" , index 0.")
    print(root[0])
    for i in range(int(math.log(len(root)+1)/math.log(2)-1)):
        try: 
            print("Children of " + str(root[i]) + ", index " + str(i))
            print(root[i*2+1])
            print(root[i*2+2])
            print("-----------------------")
        except IndexError:
            break
    return True 

def isSymmetric(root):
    for i in range(1,int(math.log(len(root)+1)/math.log(2)-1)):
        #print("Comparisons 1: " + str(root[(i+1)*2+1]) + " and " + str((root[i*2+1])))
        #print("Comparisons 2: " + str(root[i*2+1]) + " and " + str(root[(i+1)*2+2]))
        if not ((root[i*2+2]) == (root[(i+1)*2+1]) and (root[i*2+1]) == (root[(i+1)*2+2])):
            return False
    return True 


printTree([1,2,2,"null",3,"null",3])
print("The binary tree is Symmetric: " + str(isSymmetric([1,2,2,"null",3,"null",3])))
    
        