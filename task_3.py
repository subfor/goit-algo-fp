import heapq

import matplotlib.pyplot as plt
import networkx as nx


# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0
    previous = {node: None for node in graph.nodes}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous


# Відновлення шляху
def reconstruct_path(previous, node):
    path = []
    while node is not None:
        path.append(node)
        node = previous[node]
    return path[::-1]


if __name__ == "__main__":

    # Створення графа
    G = nx.Graph()
    G.add_edge("A", "B", weight=5)
    G.add_edge("A", "C", weight=10)
    G.add_edge("B", "D", weight=3)
    G.add_edge("C", "D", weight=2)
    G.add_edge("D", "E", weight=4)

    start_node = "A"
    distances, previous = dijkstra(G, start_node)

    # Вивід результатів
    for node in G.nodes:
        path = reconstruct_path(previous, node)
        print(f"Найкоротший шлях до {node}: {path}, відстань: {distances[node]}")

    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        node_color="skyblue",
        font_size=15,
        width=2,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()
