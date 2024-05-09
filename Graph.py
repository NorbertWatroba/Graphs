from collections import deque


class Graph:
    def __init__(self, number: int):
        self.nodes: dict[str, list] = dict()
        for i in range(1, number+1):
            self.nodes[str(i)] = input(f'  {i:>3}> ').split()

    def print_list(self):
        for node in self.nodes.keys():
            connections = ' '.join(self.nodes[node])
            print(f'{node:>3}> {connections}')

    def print_matrix(self):
        # header
        print(f'  | {" ".join(list(self.nodes.keys()))}')
        print(f'--+{"--" * len(self.nodes.keys())}')
        # body
        for node in self.nodes.keys():
            row = ['1' if i in self.nodes[node] else '0' for i in self.nodes.keys()]
            print(f'{node} | {" ".join(row)}')

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










