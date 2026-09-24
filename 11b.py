graph = {}
n = int(input("Enter number of vertices: "))
for i in range(n):
    vertex = int(input("Enter vertex: "))
    graph[vertex] = []
e = int(input("Enter number of edges: "))
for i in range(e):
    u = int(input("Enter starting vertex of edge: "))
    v = int(input("Enter ending vertex of edge: "))
    graph[u].append(v)
print("\nGraph: ")
for vertex in graph:
    print(vertex, "->", graph[vertex])
def bfs(start):
    visited = []
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return visited
def dfs(start):
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)

            for neighbour in reversed(graph[vertex]):
                if neighbour not in visited:
                    stack.append(neighbour)
    return visited
start = int(input("\nEnter starting vertex: "))
print("\nBFS traversal: ")
print("->".join(map(str, bfs(start))))
print("\nDFS traversal: ")
print("->".join(map(str, dfs(start))))
