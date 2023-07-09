import os
import requests
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ.get("API_ENDPOINT")

HEADER_JWT_KEY = os.environ.get("HEADER_JWT_KEY")

# LOGIN
def test_login_successful():
    response = requests.post(ENDPOINT + "/user/login", json={
        "email": "elon@email.com",
        "password": "test123"
    })
    assert response.status_code == 200

def test_login_invalid_credentials():
    response = requests.post(ENDPOINT + "/user/login", json={
        "email": "elon@email.com",
        "password": "cdslkcnsdkmc"
    })
    assert response.status_code == 401

def test_login_user_not_found():
    response = requests.post(ENDPOINT + "/user/login", json={
        "email": "test@email.com",
        "password": "test123"
    })
    assert response.status_code == 404

# SIGN UP
def test_signup_successful():
    response = requests.post(ENDPOINT + "/user/signup", json={
        "name": "Guest",
        "email": "guest@email.com",
        "password": "test123"
    })
    assert response.status_code == 201

def test_signup_user_already_exists_error():
    response = requests.post(ENDPOINT + "/user/signup", json={
        "name": "Elon",
        "email": "elon@email.com",
        "password": "test123"
    })
    assert response.status_code == 409

# GET USER INFORMATION
def test_get_user_info():
    userId = "64a690a5f4a5f5eb51f305a3"
    response = requests.get(ENDPOINT + "/user/" + userId , headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    })
    assert response.status_code == 200

def test_get_user_info_not_found():
    userId = "64a690a5f4a5f5eb53c305a3"
    response = requests.get(ENDPOINT + "/user/" + userId , headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    })
    assert response.status_code == 404