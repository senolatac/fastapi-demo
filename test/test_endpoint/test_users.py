import json

from requests.auth import HTTPBasicAuth


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


def test_read_user(client):
    auth = HTTPBasicAuth(username="user11", password="secret")

    response = client.get("/users/1", auth=auth)

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["full_name"] == "Danny Manny"
