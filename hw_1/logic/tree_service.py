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
