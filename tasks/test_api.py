import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from tasks.models import Task


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def alice(db):
    return User.objects.create_user("alice", password="pass12345")


@pytest.fixture
def bob(db):
    return User.objects.create_user("bob", password="pass12345")


def test_requires_authentication(client):
    response = client.get("/api/v1/tasks/")
    assert response.status_code == 401


def test_create_task_sets_owner(client, alice):
    client.force_authenticate(alice)
    response = client.post("/api/v1/tasks/", {"title": "Learn DRF"})
    assert response.status_code == 201
    assert Task.objects.get().owner == alice


def test_user_cannot_see_others_task(client, alice, bob):
    task = Task.objects.create(owner=alice, title="Private")
    client.force_authenticate(bob)
    response = client.get(f"/api/v1/tasks/{task.id}/")
    assert response.status_code == 404