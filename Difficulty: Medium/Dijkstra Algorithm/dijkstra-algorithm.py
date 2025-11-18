from collections import defaultdict
import heapq

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        graph = defaultdict(list)
        
        for u,v,w in edges:   #adjacency list
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        dist = [float('inf')] * V
        
        dist[src] = 0
        
        heap = [(0,src)]
        
        while heap:
            curr_dist,node = heapq.heappop(heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbor,weight in graph[node]:
                new_dist = curr_dist  + weight
                
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    
                    heapq.heappush(heap,(new_dist,neighbor))
                    
        return dist
                    
                    
                
                 