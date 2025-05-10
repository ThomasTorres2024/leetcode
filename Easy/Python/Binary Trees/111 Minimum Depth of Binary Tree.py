#DFS Solution
class Solution(object):
    
    #DFS Solution
    def minDepthTesterDFS(self,root,depth):

        if not root: return 10e5+1

        if not root.left and not root.right:
            return depth +1

        return min(self.minDepthTesterDFS(root.left,depth+1),self.minDepthTesterDFS(root.right,depth+1))

    #BFS Solution
    def minDepthTesterBFS(self, root):
    
        if not root:
            return 0

        old_q = queue.Queue() 
        new_q = queue.Queue()

        old_q.put(root)
        depth = 0 
        while(not old_q.empty()):

            #empty old_q 
            while(not old_q.empty()):
                curr = old_q.get()

                #only do something if curr isn't null 
                if curr:
                    if curr and (not curr.right and not curr.left):
                        return depth + 1 
                    else: 
                        new_q.put(curr.left)
                        new_q.put(curr.right)
            new_q = old_q
            depth+=1 

        return self.minDepthTester(root,0)
        

    def minDepth(self, root):

        if not root:
            return 0

        
        return self.minDepthTesterDFS(root,0)
        