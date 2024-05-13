from collections import deque


class Graph:
    def __init__(self, size: int, mode: str = 'input', **kwargs):
        if mode == 'generate':
            self.nodes = self._generate(size, **kwargs)
        else:
            self.nodes: dict[str, list[str]] = dict()
            for i in range(1, size+1):
                self.nodes[str(i)] = [v for v in set(input(f'    {i}> ').split()) if int(v) in range(1, size+1)]

    @staticmethod
    def _generate(size: int, saturation: int = 100) -> dict[str, list[str]]:
        max_edges = size * (size - 1) // 2
        num_edges = saturation * max_edges // 100
        graph: dict[str, list[str]] = {str(k): [] for k in range(1, size+1)}
        current = 1
        edge = 2
        for _ in range(num_edges):
            if edge > size:
                current += 1
                edge = current + 1
            graph[str(current)].append(str(edge))
            edge += 1
        return graph

    def print_list(self):
        for node, edges in self.nodes.items():
            connections = ' '.join(edges)
            print(f'{node}> {connections}')

    def print_matrix(self):
        # header
        print(f'  | {" ".join(list(self.nodes.keys()))}')
        print(f'--+{"--" * len(self.nodes)}')
        # body
        for node, edges in self.nodes.items():
            row = ['1' if i in edges else '0' for i in self.nodes]
            print(f'{node} | {" ".join(row)}')

    def print_table(self):
        for node, edges in self.nodes.items():
            for edge in edges:
                print(f'({node},{edge})')

    def find_edge(self, frm: str, to: str):
        if self.nodes.get(frm) and to in self.nodes.get(frm):
            print(f'True: edge({frm},{to}) exists in the Graph!')
        else:
            print(f'False: edge({frm},{to}) does not exist in the Graph!')

    def bfs(self):
        def _bfs(start: str = '1') -> list[str]:
            visited.add(start)
            queue = deque([start])
            result = []

            while queue:
                current = queue.popleft()
                result.append(current)

                for edge in self.nodes[current]:
                    if edge not in visited:
                        queue.append(edge)
                        visited.add(edge)
            return result

        visited = set()
        order: list[str] = _bfs()
        while len(order) != len(self.nodes):
            to_go = [node for node in self.nodes if node not in order]
            order.extend(list(set(_bfs(to_go.pop())) - set(order)))
        print(' '.join(order))

    def dfs(self):
        def _dfs(current: str = '1'):
            result = [current]
            visited.add(current)
            for neighbour in self.nodes[current]:
                if neighbour not in visited:
                    result.extend(_dfs(neighbour))
            return result

        visited = set()
        order: list[str] = _dfs()
        to_go = [node for node in self.nodes if node not in order]
        while len(order) != len(self.nodes):
            order.extend(_dfs(to_go.pop()))
        print(' '.join(order))

    def kahn_sort(self):
        incoming_edges = {k: 0 for k in self.nodes}
        for node, edges in self.nodes.items():
            for edge in edges:
                incoming_edges[edge] += 1

        queue = deque([k for k, v in incoming_edges.items() if v == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for edge in self.nodes[node]:
                incoming_edges[edge] -= 1
                if incoming_edges[edge] == 0:
                    queue.append(edge)

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

        for key in self.nodes:
            try:
                dfs(key)
            except ValueError as e:
                print(e)
                return
        print(f'Topologically sorted graph: {" ".join(sorted_nodes[::-1])}')
