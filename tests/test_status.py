from fastapi.testclient import TestClient
from evrone_fastapi.main import app
from evrone_fastapi.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
