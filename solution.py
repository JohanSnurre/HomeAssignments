import random
import copy


class Node:
    def __init__(self, val, isRoot):
        self.val = val
        self.newVal = val
        self.isRoot = isRoot

    def __eq__(self, other):
        if(self.val == other.val and self.isRoot == other.isRoot):
            return True
        return False

class Solution:
    def __init__(self, n):
        self.a = []
        for i in range(n):
            #self.a.append(Node(random.randint(0,n), i==0))
            self.a.append(Node(random.randint(0,n-1), i==0))
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
        self.toString()
        n = len(self.a)
        while(True):
            #q = set()
            #for i in self.a:
            #    q.add(i.val)
            #if len(q) == len(self.a):
            #                    self.toString()
             #                   return "Equal Length"
            b = copy.deepcopy(self)
            for i in range(n):
                
                if self.a[i].isRoot:
                    self.a[i].newVal = (self.a[n-1].val + (n-1))%n
                    #self.a[i].val = (self.a[len(self.a)-1].val + 2)%len(self.a)
                else:
                    self.a[i].newVal = (self.a[i-1].val + (n-2))%(n-1)
                    #self.a[i].val = (self.a[i-1].val + 1)%(len(self.a)-1)
            for i in range(n):
                self.a[i].val = self.a[i].newVal 
                
            self.toString()
            if b == a:
                self.toString()
                return "Stablilized\n"
                

if __name__ == "__main__":
    for i in range(10):
        pass
    a = Solution(3)
    
    a.a = [Node(2,True),Node(2,False),Node(2,False),Node(2,False),Node(2,False)]
    
    print(a.op())


#prove that x0 will eventually become n-1
