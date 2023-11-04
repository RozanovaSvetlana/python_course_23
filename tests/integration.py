import pytest
from fastapi.testclient import TestClient
from app import main


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
    add_node(client, [30])
    res = client.get("/get_count")
    assert res.status_code == 200
    assert client.get("/get_count").json()["count_node"] == count + 1


@pytest.mark.parametrize(
    "keys, expected_inorder, expected_status",
    [([], "", 200), ([9, 6, 7, 8, 5, 4], "4 5 6 7 8 9", 200)],
)
def test_print_tree(keys: list[int], expected_inorder: str, expected_status: int):
    client = TestClient(main.app)
    add_node(client, keys)
    res = client.get("/print")
    assert res.status_code == expected_status
    assert res.json()["tree"] == expected_inorder


@pytest.mark.parametrize(
    "keys, search_keys, expected_status, is_find",
    [
        ([], 20, 200, False),
        ([8, 9, 1, 4], 1, 200, True),
        ([35, 37, 19, 10, 2], 2, 200, True),
        ([34, 98, 15], 3, 200, False),
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
    add_node(client, [6, 1, 3, 14, 13, 30])
    res = client.get("/delete", params={"key": 13})
    assert res.status_code == 200
    assert res.json()["message"] == "Node has been successfully delete!"


@pytest.mark.parametrize(
    "keys, key_delete, expected_status, expected_message",
    [([], 5, 400, "Tree is empty"), ([9, 5, 4], 0, 400, "Node not found!")],
)
def test_delete_fail_node(
    keys: list[int], key_delete: int, expected_status: int, expected_message: str
):
    client = TestClient(main.app)
    add_node(client, keys)
    res = client.get("/delete", params={"key": key_delete})
    assert res.status_code == expected_status
    assert res.json()["detail"] == expected_message


def add_node(client, keys: list[int]):
    for key in keys:
        res = client.post("/create", json={"key": key})
