graph = {'1': set(['2', '3']),
         '2': set(['1', '4', '5']),
         '3': set(['1', '6']),
         '4': set(['2']),
         '5': set(['2', '6']),
         '6': set(['3', '5'])}

print(graph)

print(graph.keys())

print(graph.values())

def dfs(graph, start): #Normal DFS for components
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
            if(len(stack) == 1):
                print(vertex)
            else:
                print(vertex,end=" --> ")
    return visited

dfs(graph,'1')


def dfs_paths(graph, start, end): #To find and return all paths from start vertex to end vertex
    stack = [(start, [start])]
    paths = []
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == end:
                paths.append(path + [nxt])
            else:
                stack.append((nxt, path + [nxt]))
    return paths

dfs_paths(graph,'1','6')


"""
Graph implemented with lists instead of sets
"""
graph = {'1': ['2', '3'],
         '2': ['1', '4', '5'],
         '3': ['1', '6'],
         '4': ['2'],
         '5': ['2', '6'],
         '6': ['3', '5']}


def dfs(graph, start): #Normal DFS for components
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend([i for i in graph[vertex] if i not in visited])
			if(len(stack) == 1):
				print(vertex)
			else:
				print(vertex,end=" --> ")
    return visited



dfs(graph,'1')


def dfs_paths(graph, start, goal): #DFS TO FIND ALL PATHS TO ENDGOAl
    stack = [(start,[start])] # Stack contains a set (current vertex (initially start), [path to end vertex from start vertex])
    paths = []
    while(stack):
        (vertex,path) = stack.pop()
        for nextvertex in graph[vertex]:
            if(nextvertex not in path):
                if nextvertex == goal:
                    paths.append(path + [nextvertex])
                else:
                    stack.append([nextvertex, path + [nextvertex]])
    return paths

dfs_paths(graph,'1','6')

