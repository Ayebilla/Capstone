# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 19:56:18 2020
@author: avoka
"""
# original sourcecode: https://www.geeksforgeeks.org/ 

# A Python program for Dijkstra's shortest  
# path algorithm for adjacency 
# list representation of graph 
  
from collections import defaultdict 
import sys 
paths = []
class Heap():
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
    # A utility function to swap two nodes  
    # of min heap. Needed for min heapify 
    def swapMinHeapNode(self,a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped.Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2*idx + 1
        right = 2*idx + 2
  
        if left < self.size and self.array[left][1]  < self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1]< self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min  
        # heap if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum  
    # node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is  
        # not hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1)//2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
  
    # A utility function to check if a given  
    # vertex 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(dist, n): 
    print ("Vertex\tDistance from source \t Path")
    for i in range(n): 
        print ("%d\t\t%d" % (i,dist[i]) )

   


class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
    def printId(self, path):
        for g in path:
            print("\t\t\t\t\t \t",self.graph[g][2][1])
        
   
        
    def printPath(self, parent, j): 
        #Base Case : If j is source 
        if parent[j] == -1 :  
            print ("\t\t\t\t\t", j) 
            if parent[j] != -1:
                print ("\t\t\t\t\t\t", parent[j][1])
            return 
        self.printPath(parent , parent[j][0])
        print ("\t\t\t\t\t", j)
        if parent[j] != -1:
                print ("\t\t\t\t\t\t", parent[j][1])
        paths.append(j)
           # print(j[2])
             # Function to print shortest path from source to on node
   
# A function to print out path.
    def printSolution(self, dist, parent):
        src = 0
        destinations = ["A", "B","C", "D","E","F","G","H", "I"]
        destination = input("Enter destination:" )
        if destination in destinations:
            target = destinations.index(destination)
            print("Vertex \t\tDistance from Source\t Path \t ID ") 
            print("\n%d --> %d \t\t%d" % (src, target, dist[target])), 
            self.printPath(parent,target)
            #self.printId(paths)
        else: print("destination not found")
  
    
    # Adds an edge to an undirected graph 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node  
        # is added to the adjacency list of src. The  
        # node is added at the beginning. The first  
        # element of the node has the destination  
        # and the second elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge  
        # from dest to src also 
        
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode)
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode)
    
  
    # The main function that calulates distances  
    # of shortest paths from src to all vertices.  
    # It is a O(ELogV) function 
    def dijkstra(self, src): 
  
        V = self.V  # Get the number of vertices in graph 
        dist = []   # dist values used to pick minimum  
                    # weight edge in cut 
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        #  Initialize min heap with all vertices.  
        # dist value of all vertices 
        for v in range(V): 
            dist.append(sys.maxsize) 
            minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
            minHeap.pos.append(v) 
  
        # Make dist value of src vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[src] = src 
        dist[src] = 0
        minHeap.decreaseKey(src, dist[src]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
        parent = [-1] * V
               
       
        
    
  
        # In the following loop, min heap contains all nodes 
        # whose shortest distance is not yet finalized. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
        
  
            # Traverse through all adjacent vertices of  
            # u (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
                  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less  
                # than its previously calculated distance 
                if minHeap.isInMinHeap(v) and dist[u] != sys.maxsize:
                   if pCrawl[1] + dist[u] < dist[v]: 
                        dist[v] = pCrawl[1] + dist[u] 
                        parent[v] = (u, pCrawl[1])
                       
  
                        # update distance value  
                        # in min heap also 
                        minHeap.decreaseKey(v, dist[v])  
        self.printSolution(dist, parent)
# Driver program to test the above functions 
graph = Graph(4) 
graph.addEdge(0, 1, 120) 
graph.addEdge(0, 3, 80) 
graph.addEdge(1, 2, 65) 
graph.addEdge(1, 3, 110) 
graph.addEdge(2, 3, 60) 
graph.addEdge(3, 2, 60) 
graph.dijkstra(0) 
