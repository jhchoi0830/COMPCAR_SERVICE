from fastapi.testclient import TestClient
import requests


def test_get_root():
  response = requests.get("http://127.0.0.1:8000/")
  assert response.status_code == 200
  assert response.json() == {"message": "Hello World"}
  pass


def test_get_cars():
  response = requests.get("http://127.0.0.1:8000/api/car")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  assert len(response_body) == 500
  pass


def test_get_kijiji_cars():
  response = requests.get("http://127.0.0.1:8000/api/kijijiCar")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  assert len(response_body) == 40
  pass