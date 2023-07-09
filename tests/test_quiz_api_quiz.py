import os
import requests
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.environ.get("API_ENDPOINT")

HEADER_JWT_KEY = os.environ.get("HEADER_JWT_KEY")

def test_get_all_quizzes():
    response = requests.get(ENDPOINT + "/quiz/", headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    })
    assert response.status_code == 200

def test_get_quiz_by_id():
    quizId = "64aa88b74cb058da0f6dd88a"
    response = requests.get(ENDPOINT + "/quiz/" + quizId , headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    })
    assert response.status_code == 200

def test_get_quiz_by_id_not_found():
    quizId = "64aa88b74cb058da1c6dd88a"
    response = requests.get(ENDPOINT + "/quiz/" + quizId , headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    })
    assert response.status_code == 404

def test_create_quiz():
    userId = "64a690a5f4a5f5eb53c305a3"
    response = requests.post(ENDPOINT + "/quiz/create" , headers={
        "Authorization": "Bearer " + HEADER_JWT_KEY
    }, json={      
        "quizTitle": "Test Quiz",
        "quizDescription": "This is a test quiz",
        "ownerId": userId
    })
    assert response.status_code == 201