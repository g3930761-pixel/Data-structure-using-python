class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        return node

    if node.name < root.name:
        root.left = insert(root.left, node)
    else:
        root.right = insert(root.right, node)

    return root


def search(root, name):
    if root is None:
        return None

    if root.name == name:
        return root
    elif name < root.name:
        return search(root.left, name)
    else:
        return search(root.right, name)


def search_time(root, time):
    if root is None:
        return None

    if root.time == time:
        return root

    result = search_time(root.left, time)

    if result is not None:
        return result

    return search_time(root.right, time)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.name, root.time, root.purpose)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.name, root.time, root.purpose)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.name, root.time, root.purpose)


def delete(root, name):
    if root is None:
        return None

    if name < root.name:
        root.left = delete(root.left, name)

    elif name > root.name:
        root.right = delete(root.right, name)

    else:
        # No left child
        if root.left is None:
            return root.right

        # No right child
        if root.right is None:
            return root.left

        # Two children
        temp = root.right

        while temp.left:
            temp = temp.left

        root.name = temp.name
        root.time = temp.time
        root.purpose = temp.purpose

        root.right = delete(root.right, temp.name)

    return root


def count(root):
    if root is None:
        return 0

    return 1 + count(root.left) + count(root.right)


# Main program
root = None

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Count")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Visitor name: ")
        time = input("Entry time: ")
        purpose = input("Purpose: ")

        root = insert(root, Node(name, time, purpose))

        print("Entry inserted")

    elif choice == 2:
        name = input("Enter visitor name to delete: ")

        if search(root, name):
            root = delete(root, name)
            print("Entry deleted")
        else:
            print("Entry not found")

    elif choice == 3:
        print("1. Search by name")
        print("2. Search by time")

        s = int(input("Enter choice: "))

        if s == 1:
            name = input("Enter visitor name: ")
            result = search(root, name)

        elif s == 2:
            time = input("Enter entry time: ")
            result = search_time(root, time)

        else:
            print("Invalid choice")
            continue

        if result:
            print("Found:", result.name, result.time, result.purpose)
        else:
            print("Entry not found")

    elif choice == 4:
        print("Inorder:")
        inorder(root)

    elif choice == 5:
        print("Preorder:")
        preorder(root)

    elif choice == 6:
        print("Postorder:")
        postorder(root)

    elif choice == 7:
        print("Total entries:", count(root))

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")
