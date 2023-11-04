from hw_1.logic.node import Node


class Tree:
    def __init__(self):
        self.__root = None
        self.__count = 0

    def print(self):
        return self.__dfs(self.__root).strip()

    def add(self, key: int):
        try:
            self.__root = self.__insert_new_node(self.__root, Node(key))
            self.__count += 1
        except Exception as ex:
            raise ex

    def __insert_new_node(self, root: Node, node: Node):
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
        if node:
            answer = self.__dfs(node.left)
            answer += str(node.key) + " "
            answer += self.__dfs(node.right)
            return answer
        return ""

    def get_count(self):
        return self.__count

    def contains(self, key: int):
        return self.__find_node(self.__root, key)

    def __find_node(self, root: Node, key: int):
        if root:
            if root.key == key:
                return True
            elif root.key < key:
                return self.__find_node(root.right, key)
            else:
                return self.__find_node(root.left, key)
        return False
