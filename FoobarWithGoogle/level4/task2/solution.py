# sultion utlize BellmanFord shortest path algorithm
# the reason is that in graph exist negative cycles

import copy


class Graph:

    def __init__(self, square_matrix):
        self.graph = square_matrix
        self.size = len(square_matrix)  # No. of vertices
        self.INF = float("Inf")
        self.distances = [[self.INF for _ in range(
            self.size)] for _ in range(self.size)]

    def bellman_ford(self, src):
        self.distances[src][src] = 0

        for _ in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.distances[src][u] != self.INF and self.distances[src][u] + self.graph[u][v] < self.distances[src][v]:
                        self.distances[src][v] = self.distances[src][u] + \
                            self.graph[u][v]

        # Check for negative-weight cycles.
        for u in range(self.size):
            for v in range(self.size):
                if self.distances[src][u] != self.INF and self.distances[src][u] + self.graph[u][v] < self.distances[src][v]:
                    return False

        return True

    # The Bellman-Ford's complete sources algorithm.
    # Shortest path from all to all points

    def bellman_ford_complete_source(self):
        for v in range(self.size):
            if not self.bellman_ford(v):
                return False
        return True

    def get_paths(self, start, goal, time):
        stack = [(start, [start], time,
                  [[i] for i in range(self.size)])]
        childVertexes = set(range(self.size))
        while stack:
            (vertex, path, remainTime, cycleFactorVertexes) = stack.pop()
            for next in childVertexes - set(cycleFactorVertexes[vertex]):
                # calculate times to next and then bulkhead nodes
                timeToNext = self.distances[vertex][next]
                timeToGoalFromNext = self.distances[next][goal]
                timeToBackFromNext = self.distances[next][vertex]
                nextCycleFactorVertexes = copy.deepcopy(cycleFactorVertexes)

                # find zero cost cycle to blocking that:
                if timeToBackFromNext + timeToNext == 0:
                    nextCycleFactorVertexes[vertex].append(next)
                    nextCycleFactorVertexes[next].append(vertex)

                if (0 <= remainTime - timeToNext - timeToGoalFromNext):
                    nextPath = path + [next]  # update path
                    nextRemainTime = remainTime - timeToNext
                    stack.append((next, nextPath, nextRemainTime,
                                  nextCycleFactorVertexes))
                    if next == goal:
                        freedBunnies = set(nextPath)
                        yield freedBunnies
                        if len(freedBunnies) == self.size:  # all bunnies are released
                            return


def solution(times, time_limit):
    if len(times) < 3:
        return []

    g = Graph(times)

    maxFreedBunnies = set([])
    if g.bellman_ford_complete_source():
        for freedBunnies in g.get_paths(0, g.size-1, time_limit):
            maxLen = len(maxFreedBunnies)
            freedLen = len(freedBunnies)
            if maxLen < freedLen or (maxLen == freedLen and sum(maxFreedBunnies) > sum(freedBunnies)):
                maxFreedBunnies = freedBunnies
    else:
        return range(g.size-2)

    return map(lambda x: x-1, sorted(maxFreedBunnies - set([0, g.size-1])))
