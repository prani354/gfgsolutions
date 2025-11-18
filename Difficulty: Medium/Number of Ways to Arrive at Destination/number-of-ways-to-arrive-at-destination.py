from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, V, edges):
        # code here
        graph = defaultdict(list)
        
        #created adjacency list
        for u,v,time in edges:
            graph[u].append((v,time))
            graph[v].append((u,time))
            
        #dijkistra's algorithm
        dist = [float('inf')] * V
        ways = [0] * V
        
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0,0)]
        
        while heap:
            
            curr_dist,node = heapq.heappop(heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbor,time in graph[node]:
                new_dist = curr_dist + time
                
                if new_dist < dist[neighbor]:  #key insight 1 ---> Update the new_distance and update the ways
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    
                    heapq.heappush(heap,(new_dist,neighbor))
                    
                elif new_dist == dist[neighbor]: #key insight 2 ---> update the ways[neighbor]
                    ways[neighbor] += ways[node]
                    
        return ways[V-1]
            
        
        
        