from typing import DefaultDict
from queue import Queue


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class UndirectedGraph:
    def __init__(self, n: int, edges: DefaultDict[str, ListNode] = {}):
        """Creates a graph where `n` represends the number of nodes and `edges` is an adjacency list implemented with simple linked lists."""
        self.n = n
        self.edges = edges

    def add_edge(self, A, B):
        node_A = ListNode(A)
        node_B = ListNode(B)

        for node in [A, B]:
            if node not in self.edges:
                self.edges[node] = None

        # insert nodes at the beginning of the linked list
        # O(1) time

        # A is friends with B
        node_B.next = self.edges[A]
        self.edges[A] = node_B
        # B is friends with A
        node_A.next = self.edges[B]
        self.edges[B] = node_A

    def __str__(self):
        s = f'Graph has {self.n} nodes.\n'
        for node in self.edges:
            s += f'{node}: '
            friend = self.edges[node]
            while friend is not None:
                s += f'{friend.value}, '
                friend = friend.next
            s = s[:-2]
            s += '\n'
        return s

    def get_shortest_path(self, A: int, B: int) -> int:
        """Returns the length of the shortest path between nodes `A` and `B`."""
        # distance from a node to itself is 0
        if A == B:
            return 0
        # if one of the nodes is isolated, return -1
        if A not in self.edges or B not in self.edges or self.edges[A] is None or self.edges[B] is None:
            return -1

        # the BFS queue
        q = Queue()
        q.put(A)
        # distance from A to B
        dist = 0
        # the graph can have cycles, so keep track of nodes I've already visited
        visited = set()
        visited.add(A)

        while q.empty() is False:
            current_node = q.get()
            # go through this guy's friends
            friend = self.edges[current_node]
            while friend is not None:
                # when I reach B, I stop
                if friend.value == B:
                    return dist + 1
                if friend.value not in visited:
                    q.put(friend.value)
                    visited.add(friend.value)
                friend = friend.next
            dist += 1

        return -1
