import random
import copy


class Node:
    def __init__(self, val, isRoot):
        self.val = val
        self.isRoot = isRoot

    def __eq__(self, other):
        if(self.val == other.val and self.isRoot == other.isRoot):
            return True
        return False

class Solution:
    def __init__(self, n):
        self.a = []
        for i in range(n):
            self.a.append(Node(random.randint(0,n), i==0))
    def toString(self):
        for i in self.a:
            print(i.val, i.isRoot)
        print()
    def __eq__(self, other):
        for i, j in zip(self.a, other.a):
            if(i != j):
                return False
        return True
    def op(self):
        while(True):
            #q = set()
            #for i in self.a:
            #    q.add(i.val)
            #if len(q) == len(self.a):
            #                    self.toString()
             #                   return "Equal Length"
            b = copy.deepcopy(self)
            for i in range(len(self.a)):
                
                if self.a[i].isRoot:
                    self.a[i].val = (self.a[len(self.a)-1].val + (len(self.a)-1))%len(self.a)
                    #self.a[i].val = (self.a[len(self.a)-1].val + 2)%len(self.a)
                else:
                    self.a[i].val = (self.a[i-1].val + (len(self.a)-2))%(len(self.a)-1)
                    #self.a[i].val = (self.a[i-1].val + 1)%(len(self.a)-1)
            if b == a:
                self.toString()
                return "Stablilized\n"
                

if __name__ == "__main__":
    for i in range(10):
        a = Solution(5)
    
    #a.a = [Node(0,True),Node(2,False),Node(1,False)]
    
        print(a.op())


#prove that x0 will eventually become n-1
