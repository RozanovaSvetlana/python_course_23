from fastapi import APIRouter, status, HTTPException

from app.tree_service import TreeService
from app.node_entity import NodeEntity

routers = APIRouter()
service = TreeService()


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
async def print_node(node: NodeEntity):
    """
    Print node and return node.parent_id
    :param node: Node
    :return: parent_id
    """
    print(node)
    return {node.parent_id}


@routers.post("/create")
async def create_node(node: NodeEntity):
    """
    Add new node to tree
    :param node: node entity fo add
    :return:
    """
    res, message = service.add_node(node)
    if res:
        code = status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    return {"status": code, "message": message}


@routers.get("/get_count")
async def get_count():
    """
    Get count node from tree
    """
    return {"status": status.HTTP_200_OK, "count_node": service.get_count()}


@routers.get("/print")
async def print_tree():
    """
    Print tree inorder
    """
    return {"status": status.HTTP_200_OK, "tree": service.get_inorder()}


@routers.get("/find")
async def contains(key: int):
    """
    Check is key contains
    :param key: key for check
    """
    return {"status": status.HTTP_200_OK, "contains": service.contains(key)}


@routers.get("/delete")
async def delete_node(key: int):
    """
    Delete node
    :param key: key for delete
    """
    res, message = service.delete(key)
    if res:
        code = status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
    return {"status": code, "message": message}
