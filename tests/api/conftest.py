"""Shared pytest fixtures for restful-booker API tests.

These tests hit a real hosted API (https://restful-booker.herokuapp.com),
so they need no browser fixtures - just an HTTP client per test session.
"""
import pytest
from api.booking_client import BookingClient

BASE_URL = "https://restful-booker.herokuapp.com"


def sample_booking(**overrides):
    """Build a valid booking payload, with optional field overrides."""
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05",
        },
        "additionalneeds": "Breakfast",
    }
    payload.update(overrides)
    return payload


@pytest.fixture(scope="session")
def api_client():
    """A BookingClient shared across the whole test session."""
    return BookingClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api_client):
    """A valid session token for endpoints that require write access."""
    response = api_client.create_token()
    return response.json()["token"]


@pytest.fixture
def booking_payload_factory():
    """Returns a factory for building booking payloads with optional overrides."""
    return sample_booking


@pytest.fixture
def created_booking(api_client, booking_payload_factory):
    """Create a booking, hand back (booking_id, payload), then clean it up."""
    payload = booking_payload_factory()
    response = api_client.create_booking(payload)
    booking_id = response.json()["bookingid"]

    yield booking_id, payload

    token = api_client.create_token().json()["token"]
    api_client.delete_booking(booking_id, token)
