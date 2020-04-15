from typing import DefaultDict
from queue import Queue


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class UndirectedGraph:
    def __init__(self, n: int, edges: DefaultDict[str, ListNode]):
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

    def get_shortest_path(self, A: str, B: str) -> int:
        """Returns the length of the shortest path between nodes `A` and `B`.

        Uses a Bidirectional BFS"""
        # distance from a node to itself is 0
        if A == B:
            return 0
        # if one of the nodes is isolated, return -1
        if A not in self.edges or B not in self.edges or self.edges[A] is None or self.edges[B] is None:
            return -1

        # the BFS queue
        q1 = Queue()
        q2 = Queue()
        q1.put(A)
        q2.put(B)
        # the graph can have cycles, so keep track of nodes I've already visited
        # I'll also use this mapping to tell the distance I did to other nodes
        visited1 = {}
        visited2 = {}
        visited1[A] = 0
        visited2[B] = 0

        while q1.empty() is False or q2.empty() is False:
            if q1.empty() is False:
                current_node = q1.get()
                current_dist = visited1[current_node]
                # if both A and B got to the "meeting" node, stop
                # the distance if how much I've done from A to this point (the "center")
                # and how much B has done to this point
                if current_node in visited2:
                    return current_dist + visited2[current_node]
                # go through this user's friends
                friend = self.edges[current_node]
                while friend is not None:
                    if friend.value not in visited1:
                        # save this node to process it in the future
                        q1.put(friend.value)
                        visited1[friend.value] = current_dist + 1
                    friend = friend.next

            # same thing, from the other end
            if q2.empty() is False:
                current_node = q2.get()
                current_dist = visited2[current_node]
                if current_node in visited1:
                    return current_dist + visited1[current_node]
                friend = self.edges[current_node]
                while friend is not None:
                    if friend.value not in visited2:
                        q2.put(friend.value)
                        visited2[friend.value] = current_dist + 1
                    friend = friend.next

        return -1

    def get_shortest_path_simple_bfs(self, A: str, B: str) -> int:
        """Returns the length of the shortest path between nodes `A` and `B`.

        Uses a simple BFS"""
        # distance from a node to itself is 0
        if A == B:
            return 0
        # if one of the nodes is isolated, return -1
        if A not in self.edges or B not in self.edges or self.edges[A] is None or self.edges[B] is None:
            return -1

        # the BFS queue
        # the queue must have the node and the distance I had to that node
        q = Queue()
        q.put((A, 0))
        # the graph can have cycles, so keep track of nodes I've already visited
        visited = set()
        visited.add(A)

        while q.empty() is False:
            current_node, dist = q.get()
            # if I got to B, stop
            if current_node == B:
                return dist
            # go through this user's friends
            friend = self.edges[current_node]
            while friend is not None:
                if friend.value not in visited:
                    q.put((friend.value, dist + 1))
                    visited.add(friend.value)
                friend = friend.next

        return -1
