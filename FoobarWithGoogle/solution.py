from collections import deque


class Node:
    def __init__(self, x, y, remove, maze):
        self.x = x
        self.y = y
        self.remove = remove
        self.maze = maze

    def __hash__(self):
        return self.x ^ self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.remove == other.remove

    def get_neighbors(self):
        neighbors = []
        x = self.x
        y = self.y
        remove = self.remove
        maze = self.maze
        rows = len(maze)
        columns = len(maze[0])

        if x > 0:
            wall = maze[y][x - 1] == 1
            if wall:
                if remove and ((x > 1 and maze[y][x-2] == 0) or (y < columns - 1 and maze[y+1][x-1] == 0) or (y > 1 and maze[y-1][x-1] == 0)):
                    neighbors.append(Node(x-1, y, False, maze))
            else:
                neighbors.append(Node(x-1, y, remove, maze))

        if x < columns - 1:
            wall = maze[y][x + 1] == 1
            if wall:
                if remove and ((x < columns - 2 and maze[y][x+2] == 0) or (y < rows - 1 and maze[y+1][x+1] == 0) or (y > 1 and maze[y-1][x+1] == 0)):
                    neighbors.append(Node(x+1, y, False, maze))
            else:
                neighbors.append(Node(x+1, y, remove, maze))

        if y > 0:
            wall = maze[y - 1][x] == 1
            if wall:
                if remove and ((x < columns - 1 and maze[y-1][x+1] == 0) or (y > 2 and maze[y-2][x] == 0) or (x > 0 and maze[y-1][x-1] == 0)):
                    neighbors.append(Node(x, y-1, False, maze))
            else:
                neighbors.append(Node(x, y-1, remove, maze))

        if y < rows - 1:
            wall = maze[y + 1][x]
            if wall:
                if remove and ((x < columns - 1 and maze[y+1][x+1] == 0) or (y < rows - 2 and maze[y+2][x] == 0) or (x > 0 and maze[y + 1][x-1] == 0)):
                    neighbors.append(Node(x, y+1, False, maze))
            else:
                neighbors.append(Node(x, y+1, remove, maze))

        return neighbors


def solution(maze):
    rows = len(maze)
    columns = len(maze[0])
    source = Node(0, 0, True, maze)
    queue = deque([source])
    distance_map = {source: 1}

    while queue:
        current_node = queue.popleft()

        if current_node.x == columns - 1 and current_node.y == rows - 1:
            return distance_map[current_node]

        for child_node in current_node.get_neighbors():
            if child_node not in distance_map.keys():
                distance_map[child_node] = distance_map[current_node] + 1
                queue.append(child_node)
