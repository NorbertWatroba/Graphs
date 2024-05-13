from collections import deque


class GraphMatrix:
    def __init__(self, size: int, mode: str = 'input', **kwargs):
        if mode == 'generate':
            self.size = size
            self.matrix = [[0] * size for _ in range(size)]
            self._generate(size, **kwargs)
        else:
            self.size = size
            self.matrix = [[0] * size for _ in range(size)]
            for i in range(size):
                edges = [int(v) - 1 for v in set(input(f'{i + 1}> ').split()) if int(v) in range(1, size + 1)]
                for edge in edges:
                    self.matrix[i][edge] = 1

    def _generate(self, size: int, saturation: int = 100):
        max_edges = size * (size - 1) // 2
        num_edges = saturation * max_edges // 100
        current = 1
        edge = 2
        for _ in range(num_edges):
            if edge > size:
                current += 1
                edge = current + 1
            self.matrix[current - 1][edge - 1] = 1
            edge += 1

    def print_matrix(self):
        size = len(self.matrix)
        # header
        print(f'  | {" ".join(str(i) for i in range(1, size + 1))}')
        print(f'--+{"--" * size}')
        # body
        for i in range(size):
            row = [str(cell) for cell in self.matrix[i]]
            print(f"{i + 1} | {' '.join(row)}")

    @staticmethod
    def print_list():
        print('Only available in List representation!')

    @staticmethod
    def print_table():
        print('Only available in List and Table representation!')

    def find_edge(self, frm: str, to: str):
        try:
            frm = int(frm)
            to = int(to)
        except ValueError as e:
            print(e)
            return
        if self.matrix[frm-1][to-1]:
            print(f'True: edge({frm},{to}) exists in the Graph!')
        else:
            print(f'False: edge({frm},{to}) does not exist in the Graph!')

    def bfs(self):
        def _bfs(start: int = 1) -> list[str]:
            visited[start-1] = True
            queue = deque([start])
            result = []

            while queue:
                current = queue.popleft()
                result.append(str(current))

                for i in range(self.size):
                    if self.matrix[current-1][i] == 1 and not visited[i]:
                        queue.append(i+1)
                        visited[i] = True
            return result

        visited = [True] + [False] * (self.size - 1)
        order: list[str] = _bfs()
        while len(order) != len(self.matrix):
            to_go = [node for node in range(1, self.size + 1) if str(node) not in order]
            order.extend(list(set(_bfs(to_go.pop())) - set(order)))
        print(' '.join(order))

    def dfs(self):
        def _dfs(current=0) -> list[str]:
            result = [str(current+1)]
            visited[current] = True
            for i in range(self.size):
                if self.matrix[current][i] == 1 and not visited[i]:
                    result.extend(_dfs(i))
            return result

        visited = [False] * self.size
        order: list[str] = _dfs()
        to_go = [node for node in range(1, self.size + 1) if str(node) not in order]
        while len(order) != self.size:
            order.extend(_dfs(to_go.pop()))
        print(' '.join(order))

    def kahn_sort(self):
        size = len(self.matrix)
        incoming_edges = [0] * size
        for i in range(size):
            for j in range(size):
                incoming_edges[j] += self.matrix[i][j]

        queue = [i for i in range(size) if incoming_edges[i] == 0]
        order = []

        while queue:
            node = queue.pop(0)
            order.append(node)
            for j in range(size):
                if self.matrix[node][j] == 1:
                    incoming_edges[j] -= 1
                    if incoming_edges[j] == 0:
                        queue.append(j)

        if len(order) == size:
            print(f'Topologically sorted graph: {" ".join(str(node + 1) for node in order)}')
        else:
            print('Cycles found in the graph!')

    def tarjan_sort(self):
        def dfs(node):
            if node in perm:
                return
            perm.add(node)
            temp.add(node)
            for j in range(len(self.matrix[node])):
                if self.matrix[node][j] == 1:
                    if j not in perm:
                        dfs(j)
                    elif j in temp:
                        raise ValueError('Cycles found in the graph!')
            temp.remove(node)
            sorted_nodes.append(node)

        perm = set()
        temp = set()
        sorted_nodes = []

        for i in range(len(self.matrix)):
            try:
                dfs(i)
            except ValueError as e:
                print(e)
                return
        sorted_nodes.reverse()
        print(f'Topologically sorted graph: {" ".join(str(node + 1) for node in sorted_nodes)}')

