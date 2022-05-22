from unittest.mock import Mock, patch

from app.service.user_service import get_user


@patch('app.service.user_service.requests.get')
def test_get_user(mock_get):
    user1 = {
        "id": 2,
        "username": "test-user",
        "email": "testuser@nofoobar.com",
        "password": "testing",
    }
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = user1

    response = get_user(1)

    assert response is not None
    assert response["id"] == 2

