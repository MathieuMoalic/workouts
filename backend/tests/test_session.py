import datetime

from backend.models import SessionCreate


def test_read_sessions(client):
    response = client.get(
        "/api/sessions",
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_session(client, test_user):
    data = SessionCreate(
        date=datetime.date(2025, 1, 24),
        notes="Morning session",
    ).model_dump()
    data["date"] = data["date"].isoformat()
    response = client.post(
        "/api/sessions",
        json=data,
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == test_user.id
    assert response.json()["notes"] == "Morning session"


def test_update_session(client, test_user):
    data = SessionCreate(
        date=datetime.date(2025, 1, 24),
        notes="Morning session",
    ).model_dump()
    data["date"] = data["date"].isoformat()
    session = client.post(
        "/api/sessions",
        json=data,
    )
    session_id = session.json()["id"]

    response = client.put(
        f"/api/sessions/{session_id}",
        json={"notes": "Updated session notes"},
    )
    assert response.status_code == 200
    assert response.json()["id"] == session_id
    assert response.json()["notes"] == "Updated session notes"


def test_delete_session(client, test_user):
    session = client.post(
        "/api/sessions",
        json={
            "user_id": test_user.id,
            "date": "2025-01-24",
            "notes": "Workout to be deleted",
        },
    )
    session_id = session.json()["id"]

    response = client.delete(
        f"/api/sessions/{session_id}",
    )
    assert response.status_code == 200
    assert response.json()["id"] == session_id
    assert response.json()["notes"] == "Workout to be deleted"
