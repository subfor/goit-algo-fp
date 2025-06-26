import heapq
import uuid
from typing import Optional

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key: int, color: str = "skyblue"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, color_map=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    if color_map:
        colors = [color_map.get(node[0], "skyblue") for node in tree.nodes(data=True)]
    else:
        colors = [node[1]["color"] for node in tree.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def generate_color(step, total_steps):
    base_color = [18, 150, 240]  # (#1296F0)

    # Кожен наступний крок — зменшуємо яскравість
    decrement = int(160 * (step / max(total_steps - 1, 1)))  # максимум 160 одиниць

    new_color = [
        max(0, base_color[0] - decrement),
        max(0, base_color[1] - decrement),
        max(0, base_color[2] - decrement),
    ]
    return f"#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}"


def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return colors


def bfs_visualize(root, total_steps):
    visited = set()
    queue = [root]
    colors = {}
    step = 0

    while queue:
        node = queue.pop(0)
        if node and node.id not in visited:
            visited.add(node.id)
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors


if __name__ == "__main__":
    heap_list = [10, 5, 2, 4, 6, 3, 1]
    heapq.heapify(heap_list)

    heap_tree_root = build_heap_tree(heap_list)

    total_steps = count_nodes(heap_tree_root)

    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)
