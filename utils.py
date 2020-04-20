class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            print("ERROR ADDING EDGE: Vertex not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a q and enqueue starting vertex
        qq = Queue()
        qq.enqueue([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # visited = []
        # While queue is not empty:
        while qq.size() > 0:
            # dequeue/pop the first vertex
            path = qq.dequeue()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # visited.append(path[-1])
                # enqueue all neightbors
                if path[-1] == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    # print(new_path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)
                # print(visited)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a s and push starting vertex
        ll = []
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # While stack is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # print(path)
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                # mark as visited
                visited.add(path[-1])
                ll.append(path[-1])
                # enqueue all neightbors
                for next_vert in self.get_neighbors(path[-1]):
                    # print(path[-1],next_vert)
                    new_path = list(path)
                    # print(new_path)
                    new_path.append(next_vert)
                    ss.push(new_path)
            else: 
                # ll.append(path[-1])
                # print(path[-1],"was already in visited")
                pass
        return(ll)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a q and enqueue starting vertex
        ss = Stack()
        ss.push([starting_vertex])
        # Create a set of traversed vertices
        visited = set()
        # visited = []
        # While queue is not empty:
        while ss.size() > 0:
            # dequeue/pop the first vertex
            path = ss.pop()
            # if not visited
            if path[-1] not in visited:
                # DO THE THING!!!!!!!
                # print(path[-1])
                # mark as visited
                visited.add(path[-1])
                # visited.append(path[-1])
                # enqueue all neightbors
                if path[-1] == destination_vertex:
                    return path
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    # print(new_path)
                    new_path.append(next_vert)
                    ss.push(new_path)
                # print(visited)
    def get_direction(self,start,end,room_graph):
        pass






class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)