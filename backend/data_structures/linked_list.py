class Node:
    def __init__(self, data,next, w):
        self.vertex = data
        self.next = next
        self.w = w


class Graph:
    def __init__(self, vertices):
        self.nodes=[]
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest, w):
        if src not in self.nodes:
            self.nodes.append(src)

        index = self.nodes.index(src)
        if self.graph[index] is None:
            head = Node(dest,None,w)
            self.graph[index]=head
        else:
            curr_node=None
            curr_list = self.graph[index]
            while curr_list:
                if(curr_list.next==None):
                    curr_node=curr_list
                    break
                else:
                    curr_list=curr_list.next
            curr_node.next=Node(dest,None,w)

    def print_graph(self):
        for i in range(len(self.graph)):
            print(self.nodes[i]+"->")
            temp = self.graph[i]
            while temp:
                print(str(temp.vertex)+":"+str(temp.w))
                temp = temp.next
            print(" \n")

    def get(self,key):
        #{'B': 2, 'C': 4}
        if key is not None:
            index= self.nodes.index(key)
            if index is not None:
                vertex_list=[]
                node_list=self.graph[index]
                while node_list:
                    if(node_list.next==None):
                        break
                    else:
                        vertex_list.insert(0,{node_list.vertex:node_list.w})
                        node_list=node_list.next
                return vertex_list
        else:
            return None

    def pop(self,key):
        index = self.nodes.index(key)
        if index is not None:
            self.V=self.V-1
            self.graph.pop(index)
            self.nodes.pop(index)

