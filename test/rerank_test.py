from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_rerank():
    response = client.post(
        "/api/rerank",
        headers={"X-Token": "coneofsilence"},
        json={"query": "foobar", 
            "docs": [ {"doc_id": "Foo Bar", 
            "score": 1.4}]},
    )
    assert response.status_code == 200
    assert response.json() == {"query": "foobar", 
            "docs": [ {"doc_id": "Foo Bar", "score" : 1.4} ]}