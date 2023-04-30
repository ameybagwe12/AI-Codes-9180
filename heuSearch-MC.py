import heapq

class Node:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

def expand(node):
    children = []
    m = len(node.state[0])
    b = node.state[2][0]
    for i in range(m):
        if node.state[0][i] == b:
            for j in range(m):
                if node.state[0][j] == b:
                    continue
                if node.state[0][i] == 'M' and node.state[0][j] == 'C':
                    new_state = ([x if x != i and x != j else ' ' for x in node.state[0]], node.state[1], ('C' if b == 'M' else 'M', node.state[2][1]))
                    children.append(Node(new_state, parent=node, move=(i, j), depth=node.depth+1, cost=node.cost+1))
                elif node.state[0][i] == 'C' and node.state[0][j] == 'M':
                    new_state = ([x if x != i and x != j else ' ' for x in node.state[0]], node.state[1], ('M' if b == 'C' else 'C', node.state[2][1]))
                    children.append(Node(new_state, parent=node, move=(i, j), depth=node.depth+1, cost=node.cost+1))
    for i in range(2):
        if node.state[1][i]:
            new_state = (node.state[0], [not node.state[1][0], not node.state[1][1]], (node.state[2][0], not node.state[2][1]))
            children.append(Node(new_state, parent=node, move=None, depth=node.depth+1, cost=node.cost+1))
    return children

def solve(start):
    start_node = Node(start)
    heap = []
    heapq.heappush(heap, start_node)
    visited = set()
    while heap:
        node = heapq.heappop(heap)
        if node.state[0] == [' ', ' ', 'M', 'M', 'M', 'C', 'C', 'C', 'C']:
            return node
        visited.add(node)
        for child in expand(node):
            if child not in visited:
                heapq.heappush(heap, child)

start_state = (['M', 'M', 'M', 'C', 'C', 'C'], [True, True], ('L', False))
solution_node = solve(start_state)

path = []
node = solution_node
while node:
    path.append(node)
    node = node.parent
path.reverse()

for i, node in enumerate(path):
    print('Step', i)
    print('Move:', node.move)
    print('State:', node.state)
    print()
