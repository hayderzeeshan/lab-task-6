#!/usr/bin/env python
# coding: utf-8

# In[10]:


def bfs_without(graph, start):
    visited = set()  
    queue = [start] 
    while queue:
        current = queue.pop(0) 
        if current not in visited:
            print(current) 
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)  

graph = {
    '0': ['1', '2'],
    '1': ['3', '4'],
    '2': ['5'],
    '3': [],
    '4': ['5'],
    '5': []
}
bfs_without(graph, '0')



# In[9]:


from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
    def neighbor(self, neighbor):
        self.neighbors.append(neighbor)
def bfs_with_stack(start_node):
    visited = set()  
    queue = deque([start_node]) 
    while queue:
        current_node = queue.popleft()  
        if current_node not in visited:
            print(current_node.value)  
            visited.add(current_node)
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.neighbor(b)
a.neighbor(c)
b.neighbor(d)
b.neighbor(e)
c.neighbor(e)

bfs_with_stack(a)

          


# In[ ]:




