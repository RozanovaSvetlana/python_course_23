from app.logic.node import Node


class Tree:
    """
    BST with unique keys
    """

    def __init__(self):
        self.__root = None
        self.__count = 0

    def print(self):
        """
        Print all tree
        :return: String for print
        """
        return self.__dfs(self.__root).strip()

    def add(self, key: int):
        """
        Add new node in tree
        :param key: key for add
        :exception: if node already exist
        """
        try:
            self.__root = self.__insert_new_node(self.__root, Node(key))
            self.__count += 1
        except Exception as ex:
            raise ex

    def __insert_new_node(self, root: Node, node: Node):
        """
        Insert new node in tree
        :param root: node
        :param node: new node
        """
        if root is None:
            return node
        if root.key == node.key:
            raise Exception("Such node already exists")
        elif root.key < node.key:
            root.right = self.__insert_new_node(root.right, node)
        else:
            root.left = self.__insert_new_node(root.left, node)
        return root

    def __dfs(self, node: Node):
        """
        Do inorder for print
        :param node: node
        :return: String for print
        """
        if node:
            answer = self.__dfs(node.left)
            answer += str(node.key) + " "
            answer += self.__dfs(node.right)
            return answer
        return ""

    def get_count(self):
        """
        Get count node in tree
        :return: count node
        """
        return self.__count

    def contains(self, key: int):
        """
        Check is key contains in tree
        :param key: key for check
        :return: True if key in tree, False -- otherwise
        """
        return self.__find_node(self.__root, key)

    def __find_node(self, root: Node, key: int):
        """
        Find node in tree
        :param root: node
        :param key: key for found
        :return: True if node in tree, False -- otherwise
        """
        if root:
            if root.key == key:
                return True
            elif root.key < key:
                return self.__find_node(root.right, key)
            else:
                return self.__find_node(root.left, key)
        return False

    def delete_node(self, key: int):
        """
        Delete node from tree
        :param key: key for delete
        """
        if self.__root is None:
            raise Exception("Tree is empty")
        try:
            self.__root = self.__delete(self.__root, key)
            self.__count -= 1
        except Exception as ex:
            raise ex
        return True

    def __delete(self, root: Node, key: int):
        """
        Search and delete node
        :param root: node
        :param key: key for delete
        :return: node
        """
        if root is None:
            raise Exception("Node not found!")
        if root.key > key:
            root.left = self.__delete(root.left, key)
            return root
        elif root.key < key:
            root.right = self.__delete(root.right, key)
            return root
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            succ_parent = root
            succ = root.right
            while succ.left is not None:
                succ_parent = succ
                succ = succ.left
            if succ_parent != root:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
            root.key = succ.key
            del succ
            return root
