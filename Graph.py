from collections import deque


class Graph:
    def __init__(self, number: int):
        self.nodes: dict[str, list] = dict()
        for i in range(1, number+1):
            self.nodes[str(i)] = [v for v in input(f'    {i}> ').split() if int(v) in range(1, number+1)]

    def print_list(self):
        for node in self.nodes.keys():
            connections = ' '.join(self.nodes[node])
            print(f'{node}> {connections}')

    def print_matrix(self):
        # header
        print(f'  | {" ".join(list(self.nodes.keys()))}')
        print(f'--+{"--" * len(self.nodes)}')
        # body
        for node in self.nodes.keys():
            row = ['1' if i in self.nodes[node] else '0' for i in self.nodes.keys()]
            print(f'{node} | {" ".join(row)}')

    def print_table(self):
        for node in self.nodes.keys():
            for edge in self.nodes[node]:
                print(f'({node},{edge})')

    def find_edge(self, frm: str, to: str):
        if self.nodes.get(frm) and to in self.nodes.get(frm):
            print(f'True: edge({frm},{to}) exists in the Graph!')
        else:
            print(f'False: edge({frm},{to}) does not exist in the Graph!')

    def bfs(self):
        visited = {'1'}
        que = deque(['1'])
        while que:
            current = que.popleft()
            print(current, end=' ')
            for edge in self.nodes[current]:
                if edge not in visited:
                    que.append(edge)
                    visited.add(edge)
        print('')

    def dfs(self):
        self._dfs(set())
        print('')

    def _dfs(self, visited: set[str], current: str = '1'):
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            for neighbour in self.nodes[current]:
                self._dfs(visited, neighbour)

    def kahn_sort(self):
        incoming_edges = {k: 0 for k in self.nodes.keys()}
        for node in self.nodes.keys():
            for edge in self.nodes[node]:
                incoming_edges[edge] += 1

        que = deque([k for k, v in incoming_edges.items() if v == 0])
        order = []

        while que:
            node = que.popleft()
            order.append(node)
            for edge in self.nodes[node]:
                incoming_edges[edge] -= 1
                if incoming_edges[edge] == 0:
                    que.append(edge)

        if len(order) == len(self.nodes):
            print(f'Topologically sorted graph: {" ".join(order)}')
        else:
            print('Cycles found in the graph!')

    def tarjan_sort(self):
        def dfs(node):
            if node in perm:
                return
            perm.add(node)
            temp.add(node)
            for neighbor in self.nodes[node]:
                if neighbor not in perm:
                    dfs(neighbor)
                elif neighbor in temp:
                    raise ValueError('Cycles found in the graph!')
            temp.remove(node)
            sorted_nodes.append(node)

        perm = set()
        temp = set()
        sorted_nodes = []

        for key in self.nodes.keys():
            try:
                dfs(key)
            except ValueError as e:
                print(e)
                return
        print(f'Topologically sorted graph: {" ".join(sorted_nodes[::-1])}')
