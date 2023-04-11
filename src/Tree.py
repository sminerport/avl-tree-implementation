from Node import Node
from TreePrint import pretty_tree
from collections import OrderedDict


class Tree():

    def __init__(self, initialList):
        #self.size = 0
        self.root = self.build_tree(initialList)
        self.current_node = None

    def build_tree(self, initialList):
        initialList = list(OrderedDict.fromkeys(initialList))
        for _ in range(len(initialList)):
            node_to_insert = Node(initialList[_])
            # Special case: if the tree is empty, just set the root
            # the new node
            if _ == 0:
                self.root = node_to_insert
                node_to_insert.parent = None
            else:
                current_node = self.root
                # Step 1 - do a regular binary search tree insert.
                while (current_node is not None):
                    if node_to_insert < current_node:
                        if current_node.left is None:
                            current_node.left = node_to_insert
                            node_to_insert.parent = current_node
                            current_node = None
                            continue
                        else:
                            current_node = current_node.left

                    else:
                        # If there is no right child, add the new
                        # node here; otherwise repeat from the
                        # right child.
                        if current_node.right is None:
                            current_node.right = node_to_insert
                            node_to_insert.parent = current_node
                            current_node = None
                            continue
                        else:
                            current_node = current_node.right

                # Step 2 - Reblanace along a path from the
                # new node's parent up to the root
                node_to_insert = node_to_insert.parent
                while node_to_insert is not None:
                    self.rebalance(node_to_insert)
                    node_to_insert = node_to_insert.parent

        return(self.root)

    def rotate_left(self, node):
        # Define a convenience pointer to the right child of the
        # left child
        right_left_child = node.right.left

        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later
        if node.parent is not None:
            node.parent.replace_child(node, node.right)

        else:  # node is root
            self.root = node.right
            self.root.parent = None

        # Step 2 - the node becomes the left child of what used
        # to be its right child, but is now its parent.  This will
        # detach right_left_child from the tree.
        node.right.set_child('left', node)

        # Step 3 - reattach right_left_child as the right child of node.
        node.set_child('right', right_left_child)

        return node.parent

    # Performs a right rotation at the given node.  Returns the
    # subtree's new root.
    def rotate_right(self, node):
        # Define a convenience pointer to the left child of the
        # right child.
        left_right_child = node.left.right

        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:  # node is root
            self.root = node.left
            self.root.parent = None

        # Step 2 - the node becomes the right child of what sued
        # to be its left child, but is now its parent.  This will
        # detach left_right_child from the tree.
        node.left.set_child('right', node)

        # Step 3 - reattach left_right_child as the left child of node.
        node.set_child('left', left_right_child)

        return node.parent

    def rebalance(self, node):

        # First update the height of this node.
        node.update_height()

        # Check for an imbalance.
        if node.get_balance() == -2:

            # The subtree is too big to the right.
            if node.right.get_balance() == 1:
                # Double rotation case. First do a right rotation
                # on the right child.
                self.rotate_right(node.right)

            # a left rotation will now make the subtree balanced.
            return self.rotate_left(node)

        elif node.get_balance() == 2:

            # The subtree is too big to the left
            if node.left.get_balance() == -1:
                # Double rotation case. First do a left rotation
                # on the left child.
                self.rotate_left(node.left)

            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)

        # No imbalance, so just return the original node.

        return node

    def insert(self, node_to_insert):
        search_node = self.search(node_to_insert)
        if search_node is not None:
            print(
                f"Node {search_node.key} already exists, remove {search_node.key} before inserting.")
        else:
            node_to_insert = Node(node_to_insert)
            # Special case: if the tree is empty, just set the root
            # the new node
            if self.root is None:
                self.root = node_to_insert
                node_to_insert.parent = None
            else:
                current_node = self.root
                # Step 1 - do a regular binary search tree insert.
                while (current_node is not None):
                    if node_to_insert < current_node:
                        if current_node.left is None:
                            current_node.left = node_to_insert
                            node_to_insert.parent = current_node
                            current_node = None
                            continue
                        else:
                            current_node = current_node.left

                    else:
                        # If there is no right child, add the new
                        # node here; otherwise repeat from the
                        # right child.
                        if current_node.right is None:
                            current_node.right = node_to_insert
                            node_to_insert.parent = current_node
                            current_node = None
                            continue
                        else:
                            current_node = current_node.right

                # Step 2 - Reblanace along a path from the new node's parent up
                # to the root
                node_to_insert = node_to_insert.parent
                while node_to_insert is not None:
                    self.rebalance(node_to_insert)
                    node_to_insert = node_to_insert.parent

    def search(self, key):
        key_node = Node(key)
        current_node = self.root
        while current_node is not None:
            if current_node == key_node:
                return current_node
            elif current_node < key_node:
                current_node = current_node.right
            else:
                current_node = current_node.left

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.delete_node(node)

    def make_list(self, aNode, a=[]):
        if aNode != None:
            self.make_list(aNode.left, a)
            a += [aNode.key]
            self.make_list(aNode.right, a)
        return a

    def delete_node(self, node):

        if node is None:
            return False

        # Parent needed for rebalancing.
        parent = node.parent

        # Case 1: Internal node with 2 children
        if node.left is not None and node.right is not None:
            # Find successor
            successor_node = node.right
            while successor_node.left != None:
                successor_node = successor_node.left

            # Copy the value from the node
            node.key = successor_node.key

            # Recursively remove successor
            self.delete_node(successor_node)

            # Nothing left to do since the recursive call will have rebalanced
            return True

        # Case 2: Root node (with 1 or 0 children)
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

        # Case 3: Internal with left child only
        elif node.left is not None:
            parent.replace_child(node, node.left)

        # Case 4: Internal with right child only OR leaf
        else:
            parent.replace_child(node, node.right)

        # node is gone. Anything that was below node that has persisted is already correctly
        # balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True

    def __str__(self):
        return pretty_tree(self)
