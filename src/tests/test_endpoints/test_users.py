import json


def test_create_user(client):
    data = {
        "username": "testuser",
        "email": "testuser@nofoobar.com",
        "password": "testing",
    }
    response = client.post("/users/add", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["user"] == "testuser"
    assert response.json()["is_active"] == True
