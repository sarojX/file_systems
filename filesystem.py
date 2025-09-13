from file_systems.node import Node

class FileSystem:
    def __init__(self, root_value="root"):
        self.root = Node(root_value, is_file=False)
        self.current = self.root

    def add_node(self, parent_node, value, is_file=False):
        new_node = Node(value, is_file)
        parent_node.add_child(new_node)
        return new_node

    def remove_node(self, node):
        if node.parent:
            node.parent.remove_child(node)

    def total_nodes(self):
        # Includes root
        return 1 + self.root.total_descendants()

    def change_directory(self, folder_name):
        if folder_name == "..":
            if self.current.parent:
                self.current = self.current.parent
        else:
            for child in self.current.children:
                if not child.is_file and child.value == folder_name:
                    self.current = child
                    return
            raise ValueError(f"Folder '{folder_name}' not found in current directory.")

    def list_directory(self):
        return [(child.value, 'File' if child.is_file else 'Folder') for child in self.current.children]

    def open_all(self, node=None, indent=0):
        """
        Recursively print all files and folders from the given node (default: root).
        """
        if node is None:
            node = self.root
        prefix = "    " * indent
        print(f"{prefix}{node.value} ({'File' if node.is_file else 'Folder'})")
        for child in node.children:
            self.open_all(child, indent + 1)
