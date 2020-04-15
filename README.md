# Social network
We are building a social network. In this social network, each user has friends.

A chain of friends between two users, user `A` and user `B`, is a sequence of users starting with `A` and ending with `B`, such that for each user in the chain, u<sub>a</sub>, the subsequent user, u<sub>a+1</sub>, are friends.

Given a social network and two users, user `A` and user `B`, please write a function that computes the length of the shortest chain of friends between `A` and `B`.

## Question 1: How did you represent the social network? Why did you choose this representation?
A social network is mostly defined by its users and the connections between these users.
In our case, a "connection" is actually a "friendship", so we can assume that if user `A` is friends with user `B`, then `B` is also friends with `A`, since a friendship is a symmetrical relationship.
If we were to model something else, like Twitter (where we have "follows" instead of friendships), then we wouldn't have had symmetrical relationships by default.

I've chosen to represent the network using an **undirected** graph, since it would cover our basic needs.
Each user represents a vertex and a friendship is defined by an **undirected** edge between two vertices.
So, the number of users equals to the graph's number of nodes (`n`), and the number of friendships equals to the number of the edges in the graph (`m`).
Also, we're assuming a user can't be a friend with himself.

We'll make another assumption and say that each user is defined by a string id, such as `sn:user-123`.

Up next, we'll look into how we can actually save the edges in our code.
Here are some viable options:

1. Matrix of incidence
2. List of edges per user

Social networks tend to have many users. Facebook, for example, has an estimated number of users of over 2.4 billions.
The first method would require `O(n`<sup>`2`</sup>`)` space, which is out of discussion, so we'll go with the second.

In our case, we'll not be interested to know if user `A` is friends with user `B`, we'll not make this type of queries.
We're more interested in knowing who are user's `X` friends, in no particular order (the reasoning behind this is due to the algorithm chosen, explained at question 2).

I decided to implement the edges as a **mapping between the users id's and linked lists**, a linked list consisting of that user's friends (other user id's).
If we were to use simple lists instead of linked lists, when adding a new item in that list, it would have been possible that the list would have to be repositioned in memory (due to it not having enough space where it was), which would cost `O(n)` time.
With linked lists, that operation is done in `O(1)` time.
Also, people tend to make friends throughout the time, so we can assume we'll keep adding connections to our edges list.


## Question 2: What algorithm did you use to compute the shortest chain of friends? What alternatives did you consider? Why did you choose this algorithm over the alternatives?
A brute approach could have consisted in a backtracking.
We start in node `A` and we try to go through all of the nodes (based on our edges) until we reach `B`.
However, we don't stop the first time we reach `B`, as that wouldn't necessarily be the shortest path.
This approach is also known as DFS (Depth First Search).

However, this is a classical graph problem, able to be solved with **BFS** (Breadth First Search).
The advantage BFS has over DFS is that the first time it reaches it's goal node (`B`), it does so with the least number of steps taken.
In the worst case it does the same thing as DFS, going through all of the edges, so it has a time complexity of `O(n + m)`.
However, that's only on certain type of graphs, for example on a binary tree.
In real life, however, it will do better most of the times.

Another solutions could have consisted in Bellman-Ford, which isn't difficult to implement, or Dijkstra with a min-heap, to keep track of the closest node at all times.

We can extend the BFS to a **Bidirectional BFS**, in which we start the search from both ends, `A` and `B`.
It's a easy-to-implement extension if one knows BFS, so I'll go with this option.
The advantage this has over a simple BFS is that it will cut the search time in half.

## Question 3: Please enumerate the test cases you considered and explain their relevance.
I have created multiple tests in the [tests](./tests) directory. The structure is as follows:

```
n
m
a_1 b_1
a_2 b_2
...
a_m b_m
q
a_1 b_1
...
a_q b_q
```

- first line: n = number of nodes
- second line: m = number of edges
- following m lines: the edges
- next line: q = number of queries
- next q lines: the nodes for which we want to find the shortest path between

These are some special cases I've identified:
1. One of the nodes is isolated (somebody has no friends 😔). Will return `-1` for this case: [tests/test_1.in](./tests/test_1.in)
2. Distance from a node to itself. Will return `0` for this case: [tests/test_2.in](./tests/test_2.in)
3. There are cycles in the graph: [tests/test_3.in](./tests/test_3.in)
4. There are no edges: [tests/test_4.in](./tests/test_4.in)
5. Graph is a degenerate tree: [tests/test_5.in](./tests/test_5.in)
6. Graph is complete: [tests/test_6.in](./tests/test_6.in)
7. Graph has multiple connected componentes: [tests/test_7.in](./tests/test_7.in)