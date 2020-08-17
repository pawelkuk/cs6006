from typing import List
import heapq
from collections import defaultdict
import random
import math
from pprint import pprint


def from_adjmatrix(adjmat: List[List[int]]):
    adjlist = defaultdict(list)
    for source, row in enumerate(adjmatrix):
        for to, weight in enumerate(row):
            if source != to and weight != 0:
                adjlist[source].append((to, weight))
    return adjlist


v = 10
adjmatrix = [
    [
        random.choices(
            population=[0, 1, 2, 3, 4], weights=[0.6, 0.25, 0.05, 0.03, 0.02]
        )[0]
        for j in range(v)
    ]
    for _ in range(v)
]

adjlist = from_adjmatrix(adjmatrix)

s = random.randint(0, v - 1)
print(s)
end = random.randint(0, v - 1)
print(end)
assert s != end
d = [float("inf") for i in range(v)]
visited = [False for i in range(v)]

d[s] = 0


def dijkstra():
    while True:
        tmp_list = [
            (vertex, dist)
            for vertex, (visit, dist) in enumerate(zip(visited, d))
            if not visit
        ]
        if visited[end]:
            return 1  # found end vertex
        if not tmp_list:
            return 2  # traversed all
        curr_node, dist = min(tmp_list, key=lambda x: x[1],)
        if dist == float("inf"):
            return 3  # no path
        neighbors = adjlist[curr_node]
        for vertex, dist in neighbors:
            if d[vertex] > d[curr_node] + dist:
                d[vertex] = d[curr_node] + dist
        visited[curr_node] = True


return_code = dijkstra()
print("return code", return_code)
pprint(adjlist)
pprint(["Dists"] + d)

