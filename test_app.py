import pytest
from app import app, create_secret_numbers, secret_number, secret_numbers
from http import HTTPStatus

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

def test_welcome(client):
    """Test the welcome route"""
    rv = client.get('/')
    assert rv.status_code == HTTPStatus.OK
    assert b'Welcome to the number-guessing game!' in rv.data

def test_reset(client):
    """Test the reset route"""
    old_secret_number = secret_number
    rv = client.get('/reset')
    assert rv.status_code == HTTPStatus.OK
    assert b'A new secret number has been generated.' in rv.data
    assert secret_number != old_secret_number  

def test_number_guessing_game_get(client):
    """Test the GET method of the guess route"""
    rv = client.get('/guess')
    assert rv.status_code == HTTPStatus.OK
    assert b'' in rv.data  

def test_number_guessing_game_post(client):
    """Test the POST method of the guess route"""
    with client:
        with app.app_context():
            response = client.post('/guess', data=dict(text=secret_number))
            assert response.status_code == HTTPStatus.OK
            assert b'Congratulations!!! You guessed the correct number :)' in response.data

            response = client.post('/guess', data=dict(text=secret_number - 1))
            assert response.status_code == HTTPStatus.OK
            assert b'Your guess is too low, Please try again :(' in response.data

            response = client.post('/guess', data=dict(text=secret_number + 1))
            assert response.status_code == HTTPStatus.OK
            assert b'Your guess is too high, Please try again :(' in response.data

def test_guess_secret_numbers_get(client):
    """Test the GET method of the secret_numbers route"""
    rv = client.get('/secret_numbers')
    assert rv.status_code == HTTPStatus.OK
    assert b'' in rv.data  

def test_guess_secret_numbers_post(client):
    """Test the POST method of the secret_numbers route"""
    create_secret_numbers()  

    with client:
        with app.app_context():
            guess = secret_numbers[0]
            response = client.post('/secret_numbers', data=dict(text=guess))
            assert response.status_code == HTTPStatus.OK
            assert f'{guess} is a secret number, you win :) !!!!!!' in response.data.decode('utf-8')

            guess = 81  
            response = client.post('/secret_numbers', data=dict(text=guess))
            assert response.status_code == HTTPStatus.OK
            assert f'{guess} is not a secret number, you lose :(' in response.data.decode('utf-8')
