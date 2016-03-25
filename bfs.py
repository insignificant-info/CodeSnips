# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from Queue import Queue
def bfs(n,m,s,edges):
    
    nodes = range(1,n+1)
    nodes.pop(s-1) 
    distances = []
    for i in nodes:
        if i not in edges:
            distances.append(-1)
            continue
        if i in edges[s]:
            distances.append(6)
            continue
        fringe = Queue()
        found = 0
        visited = set()
        visited.add(s)
        #print "start node" + str(i)
        
        for found_edge in edges[s]:
            #print "add " + str(found_edge)                
            fringe.put((found_edge,6))
        while fringe.empty() == False:
            if found == 1:
                break
            current_node, distance = fringe.get()
            #print "current node = " + str(current_node)
            if current_node not in visited:
                visited.add(current_node)
                if current_node == i:
                    distances.append(distance)
                    found = 1
                    break
                else:
                    for found_edge in edges[current_node]:
                        if found_edge not in visited:
                            if found_edge == i:
                                distances.append(distance + 6)
                                found = 1
                                break
                            fringe.put((found_edge,6+distance))
        if found == 0:
            distances.append(-1)
    print " ".join([str(x) for x in distances])
                
            
            
    

t = int(raw_input())
while t > 0:
    n,m = [int(x) for x in raw_input().strip().split(' ')]
    edges = defaultdict(list)
    while m > 0:
        x,y = [int(x) for x in raw_input().strip().split(' ')]
        if y not in edges[x]:
            edges[x].append(y)
        if x not in edges[y]:
            edges[y].append(x)
        m -= 1
    s = int(raw_input())
    bfs(n,m,s,edges)
    t -= 1
