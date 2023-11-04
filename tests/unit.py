import pytest
from app.logic.tree import Tree


@pytest.mark.parametrize(
    "keys, expected_print",
    [
        ([], ""),
        ([9, 5, 1, 3, 12, 6, 17], "1 3 5 6 9 12 17"),
        ([5, 4, 3, 2, 1], "1 2 3 4 5"),
    ],
)
def test_print(keys: list[int], expected_print: str):
    tree = Tree()
    add_node(tree, keys)
    assert tree.print() == expected_print


@pytest.mark.parametrize("keys", [([5, 6, 8]), ([7, 5, 1, 3]), ([9, 7, 11, 2])])
def test_successfully_added_nodes(keys: list[int]):
    tree = Tree()
    count = 0
    for key in keys:
        tree.add(key)
        count += 1
        assert count == tree.get_count()
        assert tree.contains(key)


@pytest.mark.parametrize(
    "keys, expected_count",
    [
        ([2, 1, 4, 2], 3),
        ([5, 5], 1),
        ([3, 2, 1, 1, 7, 9], 3),
        ([6, 5, 8, 5], 3),
        ([9, 4, 3, 6, 15, 12, 18, 15], 7),
    ],
)
def test_fail_added(keys: list[int], expected_count: int):
    is_ex = False
    tree = Tree()
    try:
        add_node(tree, keys)
    except:
        is_ex = True
    assert is_ex == True
    assert tree.get_count() == expected_count


@pytest.mark.parametrize(
    "keys, key_search, expected_result",
    [
        ([], 7, False),
        ([6, 4, 2, 1], 6, True),
        ([7, 34, 0, 45, 8, 9, 37], 0, True),
        ([25, 31, -6, 19], 100, False),
        ([6, 19, 38], 0, False),
    ],
)
def test_contains(keys: list[int], key_search: int, expected_result: bool):
    tree = Tree()
    add_node(tree, keys)
    assert tree.contains(key_search) == expected_result


@pytest.mark.parametrize(
    "keys, delete_key, expected_message",
    [
        ([], 5, "Tree is empty"),
        ([4, 5, 7, 9, 12], 6, "Node not found!"),
        ([5, 15, 1, 42, 65, 39, 4, 0], 43, "Node not found!"),
    ],
)
def test_delete_node_exception(keys: list[int], delete_key: int, expected_message: str):
    tree = Tree()
    add_node(tree, keys)
    is_ex = False
    try:
        tree.delete_node(delete_key)
    except Exception as ex:
        is_ex = True
        assert ex.args[0] == expected_message
    assert is_ex == True


@pytest.mark.parametrize(
    "keys, delete_keys, result_count",
    [
        ([5, 7, 9, 15, 19, 34, 90], [19, 5], 5),
        ([9, 6, 1, 8, 10, 15, 12, 11, 13, 19], [15], 9),
        ([1, 2, 3], [3, 2, 1], 0),
    ],
)
def test_delete_node(keys: list[int], delete_keys: list[int], result_count: int):
    tree = Tree()
    add_node(tree, keys)
    for key in delete_keys:
        assert tree.delete_node(key) == True
    assert tree.get_count() == result_count


def add_node(tree: Tree, keys: list[int]):
    for key in keys:
        tree.add(key)
