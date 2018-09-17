graph = {'1': set(['2', '3']),
         '2': set(['1', '4', '5']),
         '3': set(['1', '6']),
         '4': set(['2']),
         '5': set(['2', '6']),
         '6': set(['3', '5'])}

print(graph)

print(graph.keys())

print(graph.values())

from collections import deque
def bfs(graph,start): #Normal BFS for components
    visited, queue = set(), deque([start]) #Use Deque for popleft
    while queue:
        vertex = queue.popleft() #for O(1) pop
        
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
            if(len(queue) == 1):
                print(vertex)
            else:
                print(vertex,end=" --> ")
    return visited


from collections import deque
def bfs_paths(graph,start,goal):
    queue = deque([(start,[start])]) # Queue = [(start vertex,[path to goal from start vertex])]
    paths = [] #Contains all paths from start vertex to end vertex
    while(queue):
        (vertex,path) = queue.popleft()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                paths.append(path+[nxt])
            else:
                queue.append((nxt,path+[nxt]))
    return paths


"""
Graph implemented with lists instead of sets
"""
graph = {'1': ['2', '3'],
         '2': ['1', '4', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}


from collections import deque
def bfs(graph,start): #Normal Bfs for components
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend([i for i in graph[vertex] if i not in visited])
    return visited



dfs(graph,'1')

from collections import deque
def bfs_paths(graph,start,goal):
    queue = deque([(start,[start])]) # Queue contains a set (current vertex (initially start), [path to end vertex from start vertex])
    paths = []
    while(queue):
        (vertex,path) = queue.popleft()
        for nextvertex in graph[vertex]:
            if(nextvertex not in path):
                if nextvertex == goal:
                    paths.append(path + [nextvertex])
                else:
                    queue.append([nextvertex, path + [nextvertex]])
    return paths

dfs_paths(graph,'1','6')

