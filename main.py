from file_systems.filesystem import FileSystem

if __name__ == "__main__":
    fs = FileSystem("root")
    # Add folders and files
    folder1 = fs.add_node(fs.root, "folder1", is_file=False)
    folder2 = fs.add_node(fs.root, "folder2", is_file=False)
    file1 = fs.add_node(folder1, "file1.txt", is_file=True)
    file2 = fs.add_node(folder1, "file2.txt", is_file=True)
    file3 = fs.add_node(folder2, "file3.txt", is_file=True)

    # List files in a directory
    def list_files(node, indent=0):
        prefix = "    " * indent
        print(f"{prefix}{node.value} ({'File' if node.is_file else 'Folder'})")
        for child in node.children:
            list_files(child, indent + 1)

    print("\nFile System Structure:")
    list_files(fs.root)

    # Show total nodes below root
    print(f"\nTotal nodes below root: {fs.root.total_descendants()}")

    # Remove a file and show updated count
    folder1.remove_child(file1)
    print("\nAfter removing file1.txt:")
    list_files(fs.root)
    print(f"Total nodes below root: {fs.root.total_descendants()}")
