from collections import deque


class GraphTable:
    def __init__(self, size: int, mode: str = 'input', **kwargs):
        if mode == 'generate':
            self.size = size
            self.edges = []
            self._generate(size, **kwargs)
        else:
            self.size = size
            self.edges = []
            for i in range(1, size + 1):
                edges = [int(v) for v in set(input(f'{i}> ').split()) if int(v) in range(1, size + 1)]
                for edge in edges:
                    self.edges.append((i, edge))

    def _generate(self, size: int, saturation: int = 100) -> None:
        max_edges = size * (size - 1) // 2
        num_edges = saturation * max_edges // 100
        for i in range(1, size + 1):
            for j in range(i + 1, min(size + 1, i + num_edges + 1)):
                self.edges.append((i, j))

    def print_table(self):
        for edge in self.edges:
            print(edge)

    @staticmethod
    def print_list():
        print('Only available in List representation!')

    @staticmethod
    def print_matrix():
        print('Only available in List and Matrix representation!')

    def find_edge(self, frm: str, to: str):
        try:
            frm = int(frm)
            to = int(to)
        except ValueError as e:
            print(e)
            return
        if (frm, to) in self.edges:
            print(f'True: edge({frm},{to}) exists in the Graph!')
        else:
            print(f'False: edge({frm},{to}) does not exist in the Graph!')

    def bfs(self):
        def _bfs(start: int = 1) -> list[str]:
            visited.add(start)
            queue = deque([start])
            result = []

            while queue:
                current = queue.popleft()
                result.append(str(current))

                for edge in self.edges:
                    if edge[0] == current and edge[1] not in visited:
                        queue.append(edge[1])
                        visited.add(edge[1])
            return result

        visited = set()
        order: list[str] = _bfs()
        while len(order) != self.size:
            to_go = [node for node in range(1, self.size) if str(node) not in order]
            order.extend(list(set(_bfs(to_go.pop())) - set(order)))
        print(' '.join(order))

    def dfs(self):
        def _dfs(current=1) -> list[str]:
            result = [str(current)]
            visited.add(current)
            for edge in self.edges:
                if edge[0] == current and edge[1] not in visited:
                    result.extend(_dfs(edge[1]))
            return result

        visited = set()
        order: list[str] = _dfs()
        to_go = [node for node in range(1, self.size + 1) if str(node) not in order]
        while len(order) != self.size:
            order.extend(_dfs(to_go.pop()))
        print(' '.join(order))

    def kahn_sort(self):
        incoming_edges = [0] * (self.size + 1)
        graph = [[] for _ in range(self.size + 1)]

        for edge in self.edges:
            incoming_edges[edge[1]] += 1
            graph[edge[0]].append(edge[1])

        queue = deque([node for node in range(1, len(incoming_edges)) if incoming_edges[node] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(str(node))

            for adj_node in graph[node]:
                incoming_edges[adj_node] -= 1
                if incoming_edges[adj_node] == 0:
                    queue.append(adj_node)

        if len(order) == self.size:
            print(f'Topologically sorted graph: {" ".join(order)}')
        else:
            print('Cycles found in the graph!')

    def tarjan_sort(self):
        def dfs(node):
            if node in perm:
                return
            perm.add(node)
            temp.add(node)
            for neighbor in graph[node]:
                if neighbor not in perm:
                    dfs(neighbor)
                elif neighbor in temp:
                    raise ValueError("The graph contains a cycle.")
            temp.remove(node)
            sorted_nodes.append(str(node))

        graph = {k: [] for k in range(1, self.size + 1)}
        for k, v in self.edges:
            graph[k].append(v)

        perm = set()
        temp = set()
        sorted_nodes = []

        for key in graph.keys():
            try:
                dfs(key)
            except ValueError as e:
                print(e)
                return
        print(f'Topologically sorted graph: {" ".join(sorted_nodes[::-1])}')
