from hw_1.logic.tree import Tree
from hw_1.node_entity import NodeEntity


class TreeService:
    def __init__(self):
        self.__tree = Tree()

    def add_node(self, node: NodeEntity):
        try:
            self.__tree.add(node.key)
            return True, "The node has been successfully added"
        except Exception as ex:
            return False, ex.args[0]

    def get_count(self):
        return self.__tree.get_count()

    def get_inorder(self):
        return self.__tree.print()

    def contains(self, key: int):
        return self.__tree.contains(key)

    def delete(self, key: int):
        """
        Delete node from tree
        :param key: key for delete
        :return: True if delete successfully, False -- otherwise
        """
        try:
            self.__tree.delete_node(key)
            return True, "Node has been successfully delete!"
        except Exception as ex:
            return False, ex.args[0]
