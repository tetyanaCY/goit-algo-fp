import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас для представлення вузлів бінарної купи
class Node:
    def __init__(self, key, color="#FFFFFF"):  # Білий колір за замовчуванням
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 8))
    nx.draw(tree, pos, with_labels=True, labels=labels, node_size=2500, node_color=colors, arrowstyle='->', arrowsize=20)
    plt.show()

# Допоміжна функція для додавання ребер
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            add_edges(graph, node.left, pos, x=x-1/(2**layer), y=y-1, layer=layer+1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            add_edges(graph, node.right, pos, x=x+1/(2**layer), y=y-1, layer=layer+1)

# Функція для DFS обходу з візуалізацією
def dfs_visualize(node, colors, current_color=0):
    if node is None:
        return current_color
    # Змінюємо колір вузла
    node.color = colors[current_color % len(colors)]
    current_color += 1
    current_color = dfs_visualize(node.left, colors, current_color)
    current_color = dfs_visualize(node.right, colors, current_color)
    return current_color

# Функція для BFS обходу з візуалізацією
def bfs_visualize(root, colors):
    queue = [root]
    current_color = 0
    while queue:
        node = queue.pop(0)
        if node:
            # Змінюємо колір вузла
            node.color = colors[current_color % len(colors)]
            current_color += 1
            queue.append(node.left)
            queue.append(node.right)

# Генерація послідовності кольорів від темного до світлого
def generate_colors(n):
    return [f"#{i:02x}{i:02x}{255:02x}" for i in range(0, 255, int(255/n))]

# Створення бінарної купи і візуалізація з DFS або BFS обходом
root = Node(1)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(5)
root.left.right = Node(9)

colors = generate_colors(5)  # Приклад генерації 5 кольорів
# Виберіть один з методів для візуалізації:
dfs_visualize(root, colors)  # Для DFS
# bfs_visualize(root, colors)  # Для BFS

draw_tree(root)
