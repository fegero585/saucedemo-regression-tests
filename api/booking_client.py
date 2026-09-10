"""API client for restful-booker (https://restful-booker.herokuapp.com/apidoc/)."""
from api.base_client import BaseClient

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password123"


class BookingClient(BaseClient):
    """Wraps the ping/auth/booking endpoints exposed by restful-booker."""

    def health_check(self):
        """GET /ping - 201 Created when the API is up."""
        return self.get("/ping")

    def create_token(self, username: str = ADMIN_USERNAME, password: str = ADMIN_PASSWORD):
        """POST /auth - exchange credentials for a session token."""
        return self.post("/auth", json={"username": username, "password": password})

    def get_booking_ids(self, **filters):
        """GET /booking - list booking ids, optionally filtered (firstname, lastname, checkin, checkout)."""
        return self.get("/booking", params=filters)

    def get_booking(self, booking_id: int):
        """GET /booking/{id} - fetch a single booking's details."""
        return self.get(f"/booking/{booking_id}")

    def create_booking(self, payload: dict):
        """POST /booking - create a new booking."""
        return self.post("/booking", json=payload)

    def update_booking(self, booking_id: int, payload: dict, token: str):
        """PUT /booking/{id} - fully replace a booking. Requires an auth token."""
        return self.put(
            f"/booking/{booking_id}",
            json=payload,
            headers={"Cookie": f"token={token}"},
        )

    def partial_update_booking(self, booking_id: int, payload: dict, token: str):
        """PATCH /booking/{id} - update only the given fields. Requires an auth token."""
        return self.patch(
            f"/booking/{booking_id}",
            json=payload,
            headers={"Cookie": f"token={token}"},
        )

    def delete_booking(self, booking_id: int, token: str):
        """DELETE /booking/{id} - remove a booking. Requires an auth token."""
        return self.delete(
            f"/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
        )
