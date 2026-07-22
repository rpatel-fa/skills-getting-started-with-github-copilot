from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore in-memory activities before each test for isolation."""
    activities.clear()
    activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
