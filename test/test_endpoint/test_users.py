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


def test_read_user_json_placeholder(client):
    response = client.get("/users/placeholder/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response is not None


def test_read_user(client):
    auth = HTTPBasicAuth(username="user11", password="secret")

    response = client.get("/users/dummy/1", auth=auth)

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["full_name"] == "Danny Manny"


def test_read_user_with_auth_client(authorized_client):
    response = authorized_client.get("/users/dummy/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["full_name"] == "Danny Manny"


def test_add_user_to_db(authorized_client):
    response = authorized_client.post(
        "/users/db/add",
        json={"email": "deadpool@example.com", "hashed_password": "chimichangas4life", "name": "test"},
    )

    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "deadpool@example.com"
    email = data["email"]

    response = authorized_client.get(f"/users/db/email/{email}")
    data = response.json()
    assert data["email"] == "deadpool@example.com"

    assert response.status_code == 200, response.text

    response = authorized_client.get("/users/all-users-from-db")

    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 1
