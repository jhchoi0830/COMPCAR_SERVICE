from fastapi.testclient import TestClient
from .car_routes import router


client = TestClient(router)


def test_read_root() -> object:
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}