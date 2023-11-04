from app.logic.tree import Tree
from app.node_entity import NodeEntity


class TreeService:
    """
    Class for manage tree
    """

    def __init__(self):
        self.__tree = Tree()

    def add_node(self, node: NodeEntity):
        """
        Add new node in tree
        :param node: node for add
        :return: True if node has been added, False -- otherwise
        """
        try:
            self.__tree.add(node.key)
            return True, "The node has been successfully added"
        except Exception as ex:
            return False, ex.args[0]

    def get_count(self):
        """
        Get count node in tree
        :return: count node
        """
        return self.__tree.get_count()

    def get_inorder(self):
        """
        Print tree
        :return: string for print
        """
        return self.__tree.print()

    def contains(self, key: int):
        """
        Check contains node in tree
        :param key: key for check
        """
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
