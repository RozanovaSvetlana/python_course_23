from fastapi import APIRouter
from hw_1.node import Node

routers = APIRouter()


@routers.get("/")
def my_app():
    """
    Default rout
    :return: Hello world
    """
    return {"message": "Hello World"}


@routers.get("/nodes/{item_id}")
async def get_node_id(item_id: int):
    """
    Get write item_id
    :param item_id: id
    :return: item_id
    """
    return {"Node id ": item_id}


@routers.get("/user/{id}")
async def get_user_info(id: int, query: str):
    """
    Get user id and query
    :param id: id is int
    :param query: something query
    :return:
    """
    return {"User id: ": id, "info: ": query}


@routers.post("/node/")
async def print_node(node: Node):
    """
    Print node and return node.parent_id
    :param node: Node
    :return: parent_id
    """
    print(node)
    return {node.parent_id}
