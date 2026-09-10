"""API tests: searching/filtering bookings (GET /booking)."""
import pytest


@pytest.mark.api
@pytest.mark.booking
def test_get_all_booking_ids_returns_a_list(api_client):
    """GET /booking with no filters returns a list of booking id objects."""
    response = api_client.get_booking_ids()

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert all("bookingid" in item for item in body)


@pytest.mark.api
@pytest.mark.booking
def test_filter_by_firstname_and_lastname(api_client, created_booking):
    """Filtering by firstname/lastname returns the matching booking's id."""
    booking_id, payload = created_booking
    response = api_client.get_booking_ids(firstname=payload["firstname"], lastname=payload["lastname"])

    assert response.status_code == 200
    ids = [item["bookingid"] for item in response.json()]
    assert booking_id in ids


@pytest.mark.api
@pytest.mark.booking
def test_filter_with_no_matches_returns_empty_list(api_client):
    """A filter that matches nothing returns an empty list, not an error."""
    response = api_client.get_booking_ids(firstname="Zzyzzyx", lastname="Nomatch")

    assert response.status_code == 200
    assert response.json() == []
