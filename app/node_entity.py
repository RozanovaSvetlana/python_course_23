from pydantic import BaseModel


class NodeEntity(BaseModel):
    """
    Entity for node
    """

    key: int
