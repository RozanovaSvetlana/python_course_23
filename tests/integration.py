import pytest
from fastapi.testclient import TestClient
from app import main


@pytest.mark.parametrize(
    "keys, key_delete, expected_status, expected_message",
    [([], 665, 400, "Tree is empty"), ([669, 665, 664], 660, 400, "Node not found!")],
)
def test_delete_fail_node(
    keys: list[int], key_delete: int, expected_status: int, expected_message: str
):
    client = TestClient(main.app)
    add_node(client, keys)
    res = client.get("/delete", params={"key": key_delete})
    assert res.status_code == expected_status
    assert res.json()["detail"] == expected_message


@pytest.mark.parametrize(
    "keys, expected_status",
    [
        ([-2], [200]),
        ([5, 6, 8], [200, 200, 200]),
        ([7, 1, 3], [200, 200, 200]),
        ([9, 15, 11, 2], [200, 200, 200, 200]),
        ([0, 0], [200, 400]),
        ([20, 21, 25, 27, 19, 21, 22], [200, 200, 200, 200, 200, 400, 200]),
    ],
)
def test_added_nodes(keys: list[int], expected_status: list[int]):
    client = TestClient(main.app)
    for key, status in zip(keys, expected_status):
        res = client.post("/create", json={"key": key})
        assert res.status_code == status


def test_count():
    client = TestClient(main.app)
    res = client.get("/get_count")
    assert res.status_code == 200
    count = client.get("/get_count").json()["count_node"]
    add_node(client, [3330])
    res = client.get("/get_count")
    assert res.status_code == 200
    assert client.get("/get_count").json()["count_node"] == count + 1


@pytest.mark.parametrize(
    "keys, search_keys, expected_status, is_find",
    [
        ([], 4420, 200, False),
        ([448, 449, 441, 444], 441, 200, True),
        ([4435, 4437, 4419, 4410, 442], 442, 200, True),
        ([4434, 4498, 4415], 443, 200, False),
    ],
)
def test_find_node(
    keys: list[int], search_keys: int, expected_status: int, is_find: bool
):
    client = TestClient(main.app)
    add_node(client, keys)
    res = client.get("/find", params={"key": search_keys})
    assert res.status_code == expected_status
    assert res.json()["contains"] == is_find


def test_delete_successfully_node():
    client = TestClient(main.app)
    add_node(client, [556, 551, 553, 5514, 5513, 5530])
    res = client.get("/delete", params={"key": 5513})
    assert res.status_code == 200
    assert res.json()["message"] == "Node has been successfully delete!"


def add_node(client, keys: list[int]):
    for key in keys:
        res = client.post("/create", json={"key": key})
