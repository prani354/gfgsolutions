from collections import deque,defaultdict
class Solution:
    def shortCycle(self, V, edges):
        # code here
        g = defaultdict(list)
        
        #build grap adj list
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            
        #initialize result
        res = float('inf')
        
        for start in range(V):
            dist = [-1] * V  #distance vector
            parent = [-1] * V  #parent node
            
            q = deque()
            q.append(start)
            dist[start] = 0
            
            while q:
                curr = q.popleft()
                
                for neighbor in g[curr]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        parent[neighbor] = curr
                        q.append(neighbor)
                    elif parent[curr] != neighbor:
                        #cycle found
                        cycle_length = dist[curr] + dist[neighbor] + 1
                        res = min(res,cycle_length)
                        
        return -1 if res == float('inf') else res
                        