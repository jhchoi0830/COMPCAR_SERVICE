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

def test_get_car_by_maker():
  response = requests.get("http://127.0.0.1:8000/api/car/makers/toyota")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert car['maker'] == 'toyota'
  pass

def test_get_car_by_model():
  response = requests.get("http://127.0.0.1:8000/api/car/models/forte")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert 'forte' in car['model']
  pass

def test_get_car_by_color():
  response = requests.get("http://127.0.0.1:8000/api/car/colors/blue")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert car['color'] == 'blue'
  pass

def test_get_car_by_year():
  response = requests.get("http://127.0.0.1:8000/api/car/years/2019")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert car['madeYear'] == 2019
  pass

def test_get_car_by_mileage():
  response = requests.get("http://127.0.0.1:8000/api/car/mileage/1")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert car['mileage'] > 0
    assert car['mileage'] < 50000
  pass

def test_get_car_by_price():
  response = requests.get("http://127.0.0.1:8000/api/car/price/1")
  response_body = response.json()
  assert response.status_code == 200
  assert response.headers["Content-Type"] == "application/json"
  for car in response_body:
    assert car['price'][0]['price'] > 0
    assert car['price'][0]['price'] < 10000
  pass