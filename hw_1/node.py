from pydantic import BaseModel
from typing import Union


class Node(BaseModel):
    """
    Entity for node
    """

    id: int
    key: str
    parent_id: Union[int, None] = None
