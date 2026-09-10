"""API tests: authentication (POST /auth)."""
import pytest


@pytest.mark.api
@pytest.mark.auth
def test_valid_credentials_return_token(api_client):
    """Valid admin credentials return a usable session token."""
    response = api_client.create_token("admin", "password123")

    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert len(body["token"]) > 0


@pytest.mark.api
@pytest.mark.auth
def test_invalid_credentials_return_no_token(api_client):
    """Bad credentials get a 200 with a reason, not a token (restful-booker quirk)."""
    response = api_client.create_token("admin", "wrong_password")

    assert response.status_code == 200
    body = response.json()
    assert "token" not in body
    assert body.get("reason") == "Bad credentials"
