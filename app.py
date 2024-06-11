from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome, to numbers guessing game!!!!!!!!!'

secret_number = random.randint(1, 80)
secret_numbers = []


def guess_number_list(guess: int, secret_numbers: list[int]) -> str:
    """
    Check if the guessed number is in the list of secret numbers.

    Args:
    guess (int): The guessed number.
    secret_numbers (list of int): The list of secret numbers.

    Returns:
    str: A message indicating whether the guess is correct or not.
    """
    for number in secret_numbers:
        if number == guess:
            return f'{guess} is a secret number, you win :) !!!!!!'
    return f'{guess} is not a secret number, you lose :('


def create_secret_numbers():
    """
    Generate a new list of 6 random secret numbers between 1 and 80.
    """
    global secret_numbers
    secret_numbers = []
    for i in range (6):
        secret_numbers. append(random.randint(1,80))

create_secret_numbers()
@app.route('/')
def welcome():
    """
    Display a welcome message.

    Returns:
    str: A welcome message.
    """
    return 'Welcome to the number-guessing game!'


@app.route('/reset')
def reset():
    """
    Generate a new secret number.

    Returns:
    str: A message indicating a new secret number has been generated.
    """
    global secret_number
    secret_number = random.randint(1, 80)
    return 'A new secret number has been generated.'


@app.route('/guess', methods=['GET', 'POST'])
def number_guessing_game():
    """
    Handle the guessing game for a single secret number.

    Returns:
    Response: The guess form or the result of the guess.
    """
    
    if request.method == 'GET':
        print('Secret number:', secret_number)
        return render_template('guess.html', response='')

    if request.method == 'POST':
        guess = int(request.form['text'])

        if guess == secret_number:
            return render_template('guess.html', response='Congratulations!!! You guessed the correct number :)')

        response = 'Your guess is too low, Please try again :(' if guess < secret_number else 'Your guess is too high, Please try again :('
        return render_template('guess.html', response=response)


@app.route('/secret_numbers', methods=['GET', 'POST'])
def guess_secret_numbers():
    """
    Handle the guessing game for the list of secret numbers.

    Returns:
    Response: The guess form or the result of the guess.
    """
    
    if request.method == 'GET':
        print('Secret numbers:', secret_numbers)
        return render_template('guess.html', response='')

    if request.method == 'POST':
        guess = int(request.form['text'])
        return guess_number_list(guess, secret_numbers)

if __name__ == '__main__':
    app.run(host='localhost', port=1724)