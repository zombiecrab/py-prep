#Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def addNode(self, data):
        new_node = Node(data)

        if self.next is None:
            self.next = new_node
        else:
            temp_next = self.next
            while temp_next.next:
                temp_next = temp_next.next
            temp_next.next = new_node

        return self

    def deleteNode (self, data, prev_node = None):
        root_node = self
        if self.data is data:
            if prev_node is None:
                root_node = self.next
            else:
                root_node = self
                prev_node.next = self.next


        elif self.next is not None:
            self.next.deleteNode(data, self)
        else:
            print("Node not found")
        
        return root_node

    def reverse(self):
        if self.next is None:
            return self

        prev_node = None
        current_node = self
        next_node = self.next

        while next_node is not None:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = current_node.next

        return current_node
        

    def __str__(self):
        temp_node = self
        aggr_output = self.data+"\n"

        while temp_node.next is not None:
            temp_node = temp_node.next
            aggr_output += temp_node.data+"\n"

        return aggr_output

    def __iter__(self):
        current_node = self

        while current_node is not None:
            yield current_node.data
            current_node = current_node.next


linked_list = Node("Hello")
linked_list.addNode("world")
linked_list.addNode("!")

print(linked_list)

linked_list = linked_list.deleteNode("22")
print(linked_list)

for data in linked_list:
    print(data)

reversed = linked_list.reverse()

for rev in reversed:
    print(rev)
#Binary Trees


class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def printTree(self):
        if self.left is not None:
            self.left.printTree()

        print(self.data)
        
        if self.right is not None:
            self.right.printTree()

    def contains (self, value):
        tmp = self.get(value)
        
        return True if tmp else False


    def get(self, value):
        if self.data is value:
            return self

        if value < self.data and self.left is not None:
            return self.left.get(value)
        
        if value > self.data and self.right is not None:
            return self.right.get(value)

        return None

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0

        return max(left_depth, right_depth) + 1

    def minDepth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0

        return min(left_depth, right_depth) + 1

    def depthOfnode(self, data):
        if self.data is data:
            return 1

        left_depth = self.left.depthOfnode(data) if self.left else 0
        right_depth = self.right.depthOfnode(data) if self.right else 0

        return max(left_depth, right_depth) + 1 if not left_depth or not right_depth else 0

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.contains(key)

        
            


root = BinaryTreeNode(10)
root.insert(4)
root.insert(8)
root.insert(9)
root.insert(7)
root.insert(56)
root.insert(2)

root.printTree()

print("Found: ", root.contains(10))
print("Found: ", root.contains(4))
print("Found: ", root.contains(8))
print("Found: ", root.contains(8))
print("Found: ", root.contains(56))
print("Found: ", root.contains(2))

print("Found: ", root.contains(3))
print(root.depth())
print(root.minDepth())
print(root.depthOfnode(8))

print(root[4].data)

test_string = "abbcd"

is_unique = True
for c1 in test_string:
    if not is_unique:
        break
        
    found = False
    for c2 in test_string:
        if c1 == c2:
            if found:
                is_unique = False
                break
            else:
                found = True

print ("Is unique: ", is_unique)           

            

#Tries
#Stacks

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        value = None
        if not self.isEmpty():
            value = self.items[-1]
            del self.items[-1]
        return value

    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(5)
stack.push(7)
stack.push(1)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.pop())
#Queues

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)


print("################ QUEUES ################")
queue = Queue()
queue.enqueue(4)
queue.enqueue(8)
queue.enqueue(22)
queue.enqueue(1)

print(queue)

while not queue.isEmpty():
    print(queue)
    print(queue.dequeue())



#Vectors / ArrayLists
#Hash Tables

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.stored_size = 0

    def put(self, key, data):
        hashvalue = self.hashFunction(key, self.size)
        entered = False
        
        while not entered:
            if self.slots[hashvalue] == None:
                self.slots[hashvalue] = key
                self.data[hashvalue] = data
                entered = True
            else:
                if self.slots[hashvalue] == key:
                    self.data[hashvalue] = data        
                    entered = True
                else:
                    hashvalue = self.rehash(hashvalue, self.size)

        self.stored_size += 1

    def get(self, key):
        starting_position = self.hashFunction(key, self.size)
 
        data = None
        done = False
        position = starting_position
        while not done and self.slots[position] is not None:
            if self.slots[position] == key:
                done = True
                data = self.data[position]
            else:
                position = self.rehash(position, self.size)
                if position == starting_position:
                    done = True
        
        return data

    def hashFunction(self, key, size):
        return key%size

    def rehash(self,oldhash, size):
        return (oldhash+1)%size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self):
        return "\t".join(str(e) for e in self.slots)+"\n"+"\t".join(str(e) for e in self.data)
        
print("################ HASH TABLES ################")

H = HashTable(11)

H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"

H[20]="duck"
print(H[20])


print(H)

#Graph
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def addNeighbour(self, neighbour, weight=0):
        self.connections[neighbour] = weight

    def __str__(self):
        return "ID:{}, connected to: {}".format(self.id, [e.id for e in self.connections])

    def getConnections(self):
        return self.connections.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, neighbour):
        return self.connections[neighbour]

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.vertices[key] = Vertex(key)

        return newVertex

    def getVertex(self, key):
        return self.vertices.get(key, None)

    def addEdge(self, vertexFrom, vertexTo, cost=0):
        if vertexFrom not in self.vertices:
            self.addVertex(vertexFrom)
        if vertexTo not in self.vertices:
            self.addVertex(vertexTo)

        self.vertices[vertexFrom].addNeighbour(self.vertices[vertexTo], cost)

    def getVertices(self):
        return self.vertices.keys()

    def __contains__(self, vertex):
        return vertex in self.vertices
    
    def __iter__(self):
        return iter(self.vertices.values())


g = Graph()

for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)


for vertex in g:
    for w in vertex.getConnections():
        print("(%d, %d)" % (vertex.getId(), w.getId()))


#Breadth First Search
#Depth First Search
#Binary Search
#Merge Sort
#Quick Sort
#Tree Insert / Find / etc


#Bit Manipulation
#Singleton Design Pattern
#Factory Design Pattern
#Memory (Stack vs Heap)
#Recursion
#Big-O Time