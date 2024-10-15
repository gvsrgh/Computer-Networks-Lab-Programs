import sys

INF = float('inf')

def print_routing_table(dist, next_hop, n, src):
    print(f"\nRouting table for router {chr(ord('A') + src)}:")
    print("Destination\tDistance\tNext Hop")
    for i in range(n):
        destination = chr(ord('A') + i)
        hop = destination if next_hop[i] == -1 else chr(ord('A') + next_hop[i])
        if dist[i] == INF:
            print(f"{destination}\t\tinf\t\t-")
        else:
            print(f"{destination}\t\t{dist[i]}\t\t{hop}")

def distance_vector_routing(graph, n):
    dist = [[INF] * n for _ in range(n)]
    next_hop = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if graph[i][j] != INF:
                dist[i][j] = graph[i][j]
                next_hop[i][j] = j
    
    updated = True
    while updated:
        updated = False
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if dist[i][j] < INF and dist[j][k] < INF and dist[i][k] > dist[i][j] + dist[j][k]:
                        dist[i][k] = dist[i][j] + dist[j][k]
                        next_hop[i][k] = next_hop[i][j]
                        updated = True
    
    for i in range(n):
        print_routing_table(dist[i], next_hop[i], n, i)

if __name__ == "__main__":
    n = int(input("Enter the number of routers: "))
    graph = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
    
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        srcChar, destChar, weight = input("Enter edge (source destination weight): ").split()
        weight = int(weight)
        src = ord(srcChar) - ord('A')
        dest = ord(destChar) - ord('A')
        graph[src][dest] = weight
        graph[dest][src] = weight
    
    distance_vector_routing(graph, n)
