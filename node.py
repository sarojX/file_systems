class Node:
    def __init__(self, value, is_file=False, parent=None):
        self.value = value
        self.is_file = is_file
        self.parent = parent
        self.children = []

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
            child_node.parent = None

    def total_descendants(self):
        count = len(self.children)
        for child in self.children:
            count += child.total_descendants()
        return count

    def __repr__(self):
        type_str = 'File' if self.is_file else 'Folder'
        return f"<Node {self.value} ({type_str})>"
