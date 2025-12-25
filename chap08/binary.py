"""
Binary Search Tree Implementation

This module provides a simple implementation of a Binary Search Tree (BST)
with basic operations including insertion, search, deletion, and inorder
traversal. The BST is built from a shuffled list of numbers, and the module
demonstrates its usage through a command-line interface where users can
search for and delete nodes.

Usage:
    Run the module directly. The program will:
    - Generate a shuffled list of numbers from 0 to 9.
    - Build a BST from the list.
    - Prompt the user to search for a number.
    - Display an inorder traversal of the BST.
    - Allow the user to delete nodes repeatedly until termination.

Author: UnEmotioned
Date: 2023-11
"""

import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    """
    Represents a node in a binary search tree.

    Attributes:
        data (int): The value stored in the node.
        left (Optional[Node]): Reference to the left child.
        right (Optional[Node]): Reference to the right child.
    """

    data: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __str__(self) -> str:
        """Return a string representation of the node."""
        return f"Node({self.data})"


class BinarySearchTree:
    """
    A binary search tree (BST) implementation that supports insertion,
    searching, deletion, and inorder traversal.
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, data: int) -> None:
        """Insert a new node with the specified data into the BST."""
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data)
                    return
                current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = Node(data)
                    return
                current = current.right
            else:
                # Duplicate value; do nothing.
                return

    def search(self, data: int) -> bool:
        """
        Search for a node with the specified data in the BST.

        Returns:
            bool: True if found, False otherwise.
        """
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self) -> None:
        """Perform an inorder traversal of the BST and print node values."""

        def _inorder(node: Optional[Node]) -> None:
            if node is None:
                return
            _inorder(node.left)
            print(node.data, end=" -> ")
            _inorder(node.right)

        _inorder(self.root)
        print("End")

    def delete(self, data: int) -> None:
        """Delete the node with the specified data from the BST, if it exists."""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node: Optional[Node], data: int) -> Optional[Node]:
        """
        Recursively delete the node with the given data.

        Returns:
            Optional[Node]: The new subtree after deletion.
        """
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
            return node
        if data > node.data:
            node.right = self._delete_recursive(node.right, data)
            return node

        # Node found (node.data == data):
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        # Node with two children: Find the inorder successor.
        successor = self._min_value_node(node.right)
        node.data = successor.data
        node.right = self._delete_recursive(node.right, successor.data)
        return node

    def _min_value_node(self, node: Node) -> Node:
        """
        Find the node with the minimum data in the subtree.

        Returns:
            Node: The node with the smallest data.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current


def main() -> None:
    """
    Main function demonstrating BST operations: insertion, search,
    inorder traversal, and deletion.
    """
    # Create a shuffled list of numbers from 0 to 9.
    numbers = list(range(10))
    random.shuffle(numbers)
    print("Numbers:", numbers)

    # Build the BST from the shuffled numbers.
    bst = BinarySearchTree()
    for number in numbers:
        bst.insert(number)

    # Search for a user-specified number.
    try:
        find_number = int(input("Type a number you want to search -> "))
    except ValueError:
        print("Invalid input. Exiting.")
        return

    if bst.search(find_number):
        print(f"{find_number} found in the BST.")
    else:
        print(f"{find_number} not found in the BST.")

    print("Inorder traversal:")
    bst.inorder_traversal()

    # Repeatedly prompt the user for a number to delete.
    while True:
        try:
            delete_number = int(input("Type in a number you want to delete -> "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        bst.delete(delete_number)
        print(f"{delete_number} deleted (if it existed).")
        print("Inorder traversal after deletion:")
        bst.inorder_traversal()

        repeat = input("Do you want to delete another number? (y/n): ")
        if repeat.lower() == "n":
            print("Terminated")
            break


if __name__ == "__main__":
    main()
