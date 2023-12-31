import math

import pygame
from queue import Queue
from queue import LifoQueue

WIDTH = 700
WINDOW = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Path Finder Visualization")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (102, 102, 255)
YELLOW = (255, 255, 0)
DARKYELLOW = (204, 204, 0)
PINK = (255, 192, 203)
GRAY = (128, 128, 128)
PURPLE = (102, 0, 102)


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i].get_distance() < self.queue[max_val].get_distance():
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


class Node():
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self. col = col
        self. width = width
        self.color = WHITE
        self.neighbors = []
        self.x = row * width
        self.y = col * width
        self.total_rows = total_rows
        self.visited = False
        self.prev = None
        self.distance = math.inf

    def get_position(self):
        return self.row, self.col

    def get_distance(self):
        return self.distance

    def set_distance(self, distance):
        self.distance = distance

    def is_barrier(self):
        return self.color == BLACK

    def is_closed(self):
        return  self.color == RED

    def is_start(self):
        return self.color == DARKYELLOW

    def is_end(self):
        return self.color == PURPLE

    def reset(self):
        self.color = WHITE

    def set_to_close(self):
        self.color = RED

    def set_to_open(self):
        self.color = GREEN

    def set_to_barrier(self):
        self.color = BLACK

    def set_to_start(self):
        self.color = DARKYELLOW

    def set_to_end(self):
        self.color = PURPLE

    def set_path(self):
        self.color = BLUE

    def set_visited(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def set_prev(self, node):
        self.prev = node

    def get_prev(self):
        return self.prev

    def draw(self, window):
        pygame.draw.rect(window, self.color,(self.x, self.y, self.width, self.width))

    def set_neighbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows -1 and not grid[self.row +1][self.col].is_barrier(): # DOWN Neighbor
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #UP
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col +1].is_barrier(): #RIGHT
            self.neighbors.append((grid[self.row][self.col +1]))


def set_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

#This function is meant to draw straight lines to make the appearance look better

def draw_grid(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(window, GRAY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(window, GRAY, (j * gap, 0), (j * gap, width))


def draw(window, grid, rows, width):
    window.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(window)

    draw_grid(window, rows, width)
    pygame.display.update()

def get_clicked_pos(pos,rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def bfs(draw, grid, start_node, end_node):
    start_node.set_visited()
    q = Queue(maxsize = 500)
    q.put(start_node)
    while not q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        node = q.get()
        if node == end_node:
            reconstruct_path(node, draw)
            end_node.set_to_end()
            start_node.set_to_start()
            return True
        for neighbor in node.neighbors:
            if (not neighbor.get_visited()) and (not neighbor.is_barrier()):
                q.put(neighbor)
                neighbor.set_visited()
                neighbor.set_prev(node)
                neighbor.set_to_open()
        draw()
        if node != start_node:
            node.set_to_close()
    return False


def dfs(draw, start_node, end_node):
    start_node.set_visited()
    stack = LifoQueue()
    stack.put(start_node)
    while not stack.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        node = stack.get()
        if node == end_node:
            reconstruct_path(node, draw)
            end_node.set_to_end()
            start_node.set_to_start()
            return True
        for neighbor in node.neighbors:
            if (not neighbor.get_visited()) and (not neighbor.is_barrier()):
                stack.put(neighbor)
                neighbor.set_visited()
                neighbor.set_prev(node)
                neighbor.set_to_open()
        draw()
        if node != start_node:
            node.set_to_close()
    return False


def dijkstra(draw, grid, start_node, end_node):
    q = PriorityQueue()
    for row in grid:
        for node in row:
            q.insert(node)
    start_node.set_distance(0)
    while not q.isEmpty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        u = q.delete()
        for v in u.neighbors:
            if v.get_visited() == False and not v.is_barrier():
                v.set_to_open()
                v.set_visited()
                tempDist = u.get_distance() + 1
                if tempDist < v.get_distance():
                    v.set_distance(tempDist)
                    v.set_prev(u)
        draw()
        if u != start_node and u != end_node and not u.is_barrier():
            u.set_to_close()
    reconstruct_path(end_node, draw)
    start_node.set_to_start()
    end_node.set_to_end()




    """
        for each vertex V in G:
            distances[V] = inf
            prev[V] = None
            if V != Start_node:
                add V to priority Q(according to distance)
        distances[Start_node] = 0

        while Q is not empty:
            u = min(Q)
            for each unvisited neighbor V of u:
                tempDist = distance(u) + 1
                if tempDist < distance[V]:
                    distance[V] = tempDist
                    prev[V] = u
            


    """

    """
    short_path = []
    unvisited = []
    distance = 0
    min_node = start_node
    for row in grid:
        for node in row:
            if node != start_node:
                node.set_distance(math.inf)
                unvisited.append(node)
    start_node.set_distance(distance)
    while node != end_node:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        min_node = find_min_distance(grid)
        min_node.set_distance(distance)
        min_node.set_visited()
        short_path.append(min_node)
        for neighbor in min_node.neighbors:
            if neighbor == end_node:
                break
            elif (not neighbor.get_visited()) and (not neighbor.is_barrier()):
                if min_node.get_distance() + 1 < neighbor.get_distance():
                    neighbor.set_distance(min_node.get_distance() + 1)
                    neighbor.set_prev(min_node)
                    neighbor.set_visited()
                    neighbor.set_to_open()
        draw()
        if min_node != start_node:
            node.set_to_close()

        distance += 1

    for node in short_path:
        node.set_path()
"""

def reconstruct_path(current,draw):
    while current != None:
        current.set_path()
        current = current.get_prev()
        draw()

def find_min_distance(grid):
    min = math.inf
    min_node = Node
    for row in grid:
        for node in row:
            if(node.get_distance() < min and node.visited == False):
                min = node.get_distance()
                min_node = node
    return min_node


def main(window, width):
    ROWS = 50
    grid = set_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(window,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if pygame.mouse.get_pressed()[0]: #LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.set_to_start()
                elif not end and node != start:
                    end = node
                    end.set_to_end()
                elif node != end and node != start:
                    node.set_to_barrier()
            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for node in row:
                            node.set_neighbors(grid)
                    #bfs(lambda: draw(window, grid, ROWS, width), grid, start, end)
                    #dfs(lambda :draw(window,grid,ROWS,width), start, end)
                    dijkstra(lambda :draw(window, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = set_grid(ROWS,width)
    pygame.quit()

main(WINDOW,WIDTH)