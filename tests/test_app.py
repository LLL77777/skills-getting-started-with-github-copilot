import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    # Sign up
    resp_signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp_signup.status_code == 200 or resp_signup.status_code == 400
    # Unregister
    resp_unreg = client.post(f"/activities/{activity}/unregister?email={email}")
    assert resp_unreg.status_code == 200 or resp_unreg.status_code == 404

def test_signup_duplicate():
    activity = list(client.get("/activities").json().keys())[0]
    email = "dupuser@mergington.edu"
    client.post(f"/activities/{activity}/signup?email={email}")
    resp_dup = client.post(f"/activities/{activity}/signup?email={email}")
    assert resp_dup.status_code == 400
