"""API tests: booking CRUD lifecycle (create, read, update, delete)."""
import pytest


@pytest.mark.api
@pytest.mark.booking
@pytest.mark.smoke
def test_create_booking_returns_id_and_matching_data(api_client, booking_payload_factory):
    """Creating a booking returns a new id and echoes back the submitted data."""
    payload = booking_payload_factory()
    response = api_client.create_booking(payload)

    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"] == payload


@pytest.mark.api
@pytest.mark.booking
def test_get_booking_returns_created_data(api_client, created_booking):
    """A booking fetched by id matches the data it was created with."""
    booking_id, payload = created_booking
    response = api_client.get_booking(booking_id)

    assert response.status_code == 200
    assert response.json() == payload


@pytest.mark.api
@pytest.mark.booking
def test_get_nonexistent_booking_returns_404(api_client):
    """Fetching a booking id that doesn't exist returns 404."""
    response = api_client.get_booking(999999999)
    assert response.status_code == 404


@pytest.mark.api
@pytest.mark.booking
def test_update_booking_with_valid_token(api_client, created_booking, auth_token, booking_payload_factory):
    """A fully-authenticated PUT replaces the booking's data."""
    booking_id, _ = created_booking
    updated_payload = booking_payload_factory(firstname="Updated", lastname="Name", totalprice=222)

    response = api_client.update_booking(booking_id, updated_payload, auth_token)
    assert response.status_code == 200
    assert response.json() == updated_payload

    fetched = api_client.get_booking(booking_id)
    assert fetched.json() == updated_payload


@pytest.mark.api
@pytest.mark.booking
def test_update_booking_without_valid_token_is_rejected(api_client, created_booking, booking_payload_factory):
    """PUT with a bogus token is rejected rather than silently applied."""
    booking_id, _ = created_booking
    response = api_client.update_booking(booking_id, booking_payload_factory(), token="not-a-real-token")
    assert response.status_code in (401, 403)


@pytest.mark.api
@pytest.mark.booking
def test_partial_update_changes_only_given_fields(api_client, created_booking, auth_token):
    """PATCH updates only the fields provided, leaving the rest untouched."""
    booking_id, original_payload = created_booking
    response = api_client.partial_update_booking(booking_id, {"firstname": "Patched"}, auth_token)

    assert response.status_code == 200
    body = response.json()
    assert body["firstname"] == "Patched"
    assert body["lastname"] == original_payload["lastname"]


@pytest.mark.api
@pytest.mark.booking
def test_delete_booking_removes_it(api_client, auth_token, booking_payload_factory):
    """A deleted booking can no longer be fetched."""
    created = api_client.create_booking(booking_payload_factory())
    booking_id = created.json()["bookingid"]

    delete_response = api_client.delete_booking(booking_id, auth_token)
    assert delete_response.status_code in (200, 201)

    fetch_response = api_client.get_booking(booking_id)
    assert fetch_response.status_code == 404
