# nodes = 5
# num_edges = 3
# edges = [(0, 1), (1, 4), (0, 4)]
# storages = [1, 2, 3, 4, 5]
# threshold = 4

nodes,num_edges  = map(int,input().split())
edges = []
for i in range(num_edges):
    edges.append(tuple(map(int, input().split(" "))))
str=int(input())
storages = []
for i in range(nodes):
    storages.append(int(input()))
    
threshold = int(input())

class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
        
# Driver Code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(nodes)
    for edge in edges:
        from_node, to_node = edge
        g.addEdge(from_node, to_node)

        cc = g.connectedComponents()

        #print("\nFollowing are connected components")
        #print(cc)

        new_storages = []

        for connected_component in cc:
            if len(connected_component) == 1:
                new_storages.append(storages[connected_component[0]])
            else:
                storage = 0
                for i in connected_component:
                    storage = storage + storages[i]
                new_storages.append(storage)

        count = 0
        for storage in new_storages:
            if storage <= threshold:
                count = count + 1
        #print("Set of Computer having storage less than of equal to threshold:")
        print(count)