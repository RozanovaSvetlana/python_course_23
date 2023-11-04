import pytest
from fastapi.testclient import TestClient
from app import main


@pytest.mark.parametrize(
    "keys, expected_inorder, expected_status",
    [([], "", 200), ([119, 116, 117, 118, 115, 114], "114 115 116 117 118 119", 200)],
)
def test_print_tree(keys: list[int], expected_inorder: str, expected_status: int):
    client = TestClient(main.app)
    for key in keys:
        res = client.post("/create", json={"key": key})
    res = client.get("/print")
    assert res.status_code == expected_status
    assert res.json()["tree"] == expected_inorder
