import sys

def min_distance(dist, visited, V):
    # Initialize minimum distance for next node
    min_val = sys.maxsize
    min_index = -1

    # Search for the nearest unvisited vertex
    for v in range(V):
        if not visited[v] and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v

    return min_index

def dijkstra(graph, src, V):
    # Initialize distance values and visited set
    dist = [sys.maxsize] * V
    visited = [False] * V
    dist[src] = 0

    for _ in range(V - 1):
        # Find the nearest unvisited vertex
        u = min_distance(dist, visited, V)
        visited[u] = True

        # Update the distance value of the adjacent vertices
        for v in range(V):
            if not visited[v] and graph[u][v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    # Print the result
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t\t {dist[i]}")

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    graph = [[0] * V for _ in range(V)]

    E = int(input("Enter the number of edges: "))
    for _ in range(E):
        print("Enter the directed edges (source destination weight):",end=" ")
        src, dest, weight = map(int, input().split())
        graph[src][dest] = weight

    src = int(input("Enter the source vertex: "))
    dijkstra(graph, src, V)
