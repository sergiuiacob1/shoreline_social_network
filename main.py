import os
from graph import UndirectedGraph

# run the algorithm on every defined test
for test in os.listdir('./tests'):
    # tests are files that have the 'in' extension
    if test.endswith('.in') is False:
        continue

    print(f'\nSolving test {test}')

    # read the file
    with open(f'./tests/{test}', 'r') as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        # make sure the test is valid
        assert n > 0, 'Number of nodes is invalid'
        # I can have a maximum number of edges of n*(n-1)/2
        assert m <= n * (n - 1) / 2, 'Number of edges is too big'
        # create our graph
        g = UndirectedGraph(n)
        for _ in range(m):
            line = f.readline().strip()
            a, b = [int(x) for x in line.split(' ')]
            g.add_edge(a, b)

        # print(g)

        # answer the questions
        f_out = open(test.replace('.in', '.out'), 'w')
        no_queries = int(f.readline().strip())
        for _ in range(no_queries):
            line = f.readline().strip()
            a, b = [int(x) for x in line.split(' ')]
            res = g.get_shortest_path(a, b)
            s = f'Distance between {a} and {b}: {res}'
            f_out.write(s)
            print(s)

        f_out.close()
