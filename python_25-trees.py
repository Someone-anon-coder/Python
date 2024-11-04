class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data: any) -> None:
        if not self.root:
            self.root = Node(data)
            return
        else:
            self._insert_recursive(data, self.root)
    
    def _insert_recursive(self, data: any, current_node: Node) -> None:
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(data, current_node.left)
        
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(data, current_node.right)
    
    def in_order_traversal(self, node: Node) -> None:
        if node:
            self.in_order_traversal(node.left)
            print(node.data, end=" ")
            self.in_order_traversal(node.right)
    
    def pre_order_traversal(self, node: Node) -> None:
        if node:
            print(node.data, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def post_order_traversal(self, node: Node) -> None:
        if node:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end=" ")

binaryTree = BinaryTree()

binaryTree.insert(5)
binaryTree.insert(3)
binaryTree.insert(2)
binaryTree.insert(15)
binaryTree.insert(10)
binaryTree.insert(12)
binaryTree.insert(18)

print("In Order Traversal:", end=" ")
binaryTree.in_order_traversal(binaryTree.root)

print("\nPre Order Traversal:", end=" ")
binaryTree.pre_order_traversal(binaryTree.root)

print("\nPost Order Traversal:", end=" ")
binaryTree.post_order_traversal(binaryTree.root)