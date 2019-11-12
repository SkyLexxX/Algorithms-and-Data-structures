from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, rec_stack, cycle):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.dfs(neighbour, visited, rec_stack, cycle):
                    cycle.append(neighbour)
                    return True
            elif visited[neighbour]:
                cycle.append(neighbour)
                return True
        rec_stack[v] = False
        return False

    def identify_cycle(self):
        visited = [False] * self.V
        rec_stack = [False] * self.V
        cycle = []
        for node in range(0, self.V):
            if not visited[node]:
                if self.dfs(node, visited, rec_stack, cycle):
                    return cycle
        return False


def create_graph(file_name):
    with open(file_name) as file:
        num = file.readline()
        graph = Graph(int(num))
        for line in file.readlines():
            edge = line.split(" ")
            u = int(edge[0])
            v = int(edge[1])
            graph.add_edge(u, v)
    return graph


def main():
    g = create_graph('test_output_3.txt')
    print(g.identify_cycle())


if __name__ == '__main__':
    main()
