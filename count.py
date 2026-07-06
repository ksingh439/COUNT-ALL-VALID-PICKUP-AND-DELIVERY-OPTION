import heapq

def reachableNodes(edges, maxMoves, n):
    # Step 1: Build the adjacency list
    adj = {i: [] for i in range(n)}
    edge_dict = {}
    for u, v, cnt in edges:
        adj[u].append((v, cnt + 1))
        adj[v].append((u, cnt + 1))
        edge_dict[(u, v)] = cnt

    # Step 2: Dijkstra's Algorithm to find shortest paths
    dist = {i: float('inf') for i in range(n)}
    dist[0] = 0
    pq = [(0, 0)] # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    # Step 3: Count reachable major nodes
    ans = 0
    for i in range(n):
        if dist[i] <= maxMoves:
            ans += 1
            
    # Step 4: Count reachable subdivision nodes along the edges
    for u, v, cnt in edges:
        # Moves remaining when standing at u and v respectively
        moves_from_u = max(0, maxMoves - dist[u]) if dist[u] <= maxMoves else 0
        moves_from_v = max(0, maxMoves - dist[v]) if dist[v] <= maxMoves else 0
        
        # The sum of sub-nodes taken from both ends cannot exceed total sub-nodes (cnt)
        ans += min(cnt, moves_from_u + moves_from_v)
        
    return ans