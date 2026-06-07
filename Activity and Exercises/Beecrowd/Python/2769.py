import heapq
from collections import deque
from dataclasses import dataclass
from typing import TypeVar, Generic, Dict, List, Set, Optional, Tuple

T = TypeVar('T')

@dataclass(frozen=True)
class Node(Generic[T]):
    id: str
    payload: T
    
    def __repr__(self) -> str:
        return f"Node({self.id})"


@dataclass(frozen=True)
class Edge(Generic[T]):
    destination: Node[T]
    weight: float = 1.0

class Graph(Generic[T]):
    def __init__(self):
        self._adjacency_list: Dict[Node[T], List[Edge[T]]] = {}

    def add_node(self, node: Node[T]) -> None:
        if node not in self._adjacency_list:
            self._adjacency_list[node] = []

    def add_edge(self, src: Node[T], dest: Node[T], weight: float = 1.0, bidirectional: bool = True) -> None:
        self.add_node(src)
        self.add_node(dest)
        
        self._adjacency_list[src].append(Edge(dest, weight))
        if bidirectional:
            self._adjacency_list[dest].append(Edge(src, weight))

    def _reconstruct_path(self, parent_map: Dict[Node[T], Node[T]], current: Node[T]) -> List[Node[T]]:
        path = [current]
        while current in parent_map:
            current = parent_map[current]
            path.append(current)
        path.reverse()
        return path

    def dijkstra_shortest_path(self, start: Node[T], target: Node[T]) -> Tuple[Optional[List[Node[T]]], float]:
        if start not in self._adjacency_list or target not in self._adjacency_list:
            return None, float('inf')

        distances: Dict[Node[T], float] = {node: float('inf') for node in self._adjacency_list}
        distances[start] = 0.0
        
        parent_map: Dict[Node[T], Node[T]] = {}
        
        pq: List[Tuple[float, int, Node[T]]] = [(0.0, 0, start)]
        tie_breaker = 0

        while pq:
            current_cost, _, current_node = heapq.heappop(pq)

            if current_node == target:
                return self._reconstruct_path(parent_map, current_node), current_cost

            if current_cost > distances[current_node]:
                continue

            for edge in self._adjacency_list[current_node]:
                new_cost = current_cost + edge.weight

                if new_cost < distances[edge.destination]:
                    distances[edge.destination] = new_cost
                    parent_map[edge.destination] = current_node
                    
                    tie_breaker += 1
                    heapq.heappush(pq, (new_cost, tie_breaker, edge.destination))

        return None, float('inf')


while True:
    try:
        N = int(input()) # etapas de produção
        e1, e2 = list(map(int, input().split(" "))) # tempo entrada em cada linha de produção

        A_1n = list(map(int, input().split(" "))) # tempo de cada etapa na linha 1
        A_2n = list(map(int, input().split(" "))) # tempo de cada etapa na linha 2

        T_1n2 = list(map(int, input().split(" "))) # tempo de transferência da linha 1 para a 2
        T_2n1 = list(map(int, input().split(" "))) # tempo de transferência da linha 2 para a 1

        x1, x2 = list(map(int, input().split(" "))) # tempo de saída da linha 1 e 2

        new_graph = Graph[int]()

        node_e1 = Node("e1", e1)
        node_e2 = Node("e2", e2)

        node_x1 = Node("x1", x1)
        node_x2 = Node("x2", x2)

        node_a1n = [node_e1]
        node_a2n = [node_e2]

        for i in range(N): 
            node_a1n.append(Node(f"a1_{i}", A_1n[i]))
            node_a2n.append(Node(f"a2_{i}", A_2n[i]))

            new_graph.add_edge(node_a1n[i], node_a1n[i + 1], node_a1n[i + 1].payload)
            new_graph.add_edge(node_a2n[i], node_a2n[i + 1], node_a2n[i + 1].payload)


    except EOFError:
        break