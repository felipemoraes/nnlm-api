from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_rerank():
    response = client.post(
        "/api/rerank",
        headers={"X-Token": "coneofsilence"},
        json={"query": "foobar", 
            "docs": [ {"docid": "Foo Bar",  "content" : "Foo Bar Foo Bar Foo Foo Bar"}]},
    )
    res = response.json()
    assert res["query"] == "foobar"
    assert res["docs"][0]["docid"] == "Foo Bar"
    assert res["docs"][0]["score"] != 0.0