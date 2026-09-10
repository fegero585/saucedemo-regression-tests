"""API tests: health check."""
import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_ping_returns_201(api_client):
    """The health check endpoint responds when the service is up."""
    response = api_client.health_check()
    assert response.status_code == 201
