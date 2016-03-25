def getDescendents(node,A):
    unexplored = deque([node])

    while unexplored:
        node = unexplored.popleft()
        yield node
        children = A.getrow(node).indicies
        for child in children:
            unexplored.append(child)




