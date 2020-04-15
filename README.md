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
In real life, it will do much better, especially with our graph configuration.

## Question 3: Please enumerate the test cases you considered and explain their relevance.
These are some special cases I've identified
1. One of the nodes is isolated (somebody has no friends 😔). Will return `-1` for this case. (see test_1.in)
2. There are cycles in the graph (test_2.in)
3. There are no edges (test_3.in)
4. Graph is a degenerate tree (test_4.in)
5. Graph is complete (test_5.in)
6. Graph has multiple connected componentes (test_6.in)